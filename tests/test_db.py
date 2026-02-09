"""Unit tests for deduplication database."""

import pytest
from datetime import date, datetime, timedelta
from agentpaper_reporter.db import DeduplicationDB
from agentpaper_reporter.models import Paper


def _make_paper(id="1", title="Test", source="arxiv"):
    """Helper to create a Paper with defaults."""
    return Paper(
        id=id,
        title=title,
        authors=[],
        abstract="Abstract text",
        published_date=date(2024, 1, 1),
        source=source,
        url="http://x.com",
    )


@pytest.fixture
def db(tmp_path):
    """Fixture providing a temporary database."""
    db_path = str(tmp_path / "test.db")
    with DeduplicationDB(db_path) as d:
        yield d


class TestDeduplicationDB:
    """Tests for DeduplicationDB class."""

    def test_init_creates_database(self, tmp_path):
        """Database file is created on initialization."""
        db_path = str(tmp_path / "test.db")
        db = DeduplicationDB(db_path)
        assert tmp_path.joinpath("test.db").exists()
        db.close()

    def test_init_creates_parent_dirs(self, tmp_path):
        """Parent directories are created if they don't exist."""
        db_path = str(tmp_path / "subdir" / "nested" / "test.db")
        db = DeduplicationDB(db_path)
        assert tmp_path.joinpath("subdir", "nested", "test.db").exists()
        db.close()

    def test_is_seen_new_paper(self, db):
        """New paper returns False for is_seen."""
        assert db.is_seen("paper1") is False

    def test_mark_seen_and_check(self, db):
        """Paper marked as seen returns True for is_seen."""
        db.mark_seen("paper1", "Title", "arxiv")
        assert db.is_seen("paper1") is True

    def test_mark_seen_multiple(self, db):
        """Multiple papers can be marked as seen."""
        db.mark_seen("paper1", "Title 1", "arxiv")
        db.mark_seen("paper2", "Title 2", "biorxiv")
        db.mark_seen("paper3", "Title 3", "medrxiv")
        assert db.is_seen("paper1") is True
        assert db.is_seen("paper2") is True
        assert db.is_seen("paper3") is True

    def test_mark_seen_updates_last_seen(self, db):
        """Marking seen paper again updates last_seen_date."""
        db.mark_seen("paper1", "Title", "arxiv")
        # Mark again
        db.mark_seen("paper1", "Title", "arxiv")
        # Should still be seen (no error)
        assert db.is_seen("paper1") is True

    def test_get_new_papers_all_new(self, db):
        """All papers are new returns all papers."""
        p1 = _make_paper(id="1")
        p2 = _make_paper(id="2")
        new = db.get_new_papers([p1, p2])
        assert len(new) == 2
        assert p1 in new
        assert p2 in new

    def test_get_new_papers_marks_seen(self, db):
        """get_new_papers marks papers as seen."""
        p1 = _make_paper(id="1")
        p2 = _make_paper(id="2")
        db.get_new_papers([p1, p2])
        # Second call - both should be seen
        new2 = db.get_new_papers([p1, p2])
        assert len(new2) == 0

    def test_get_new_papers_mixed(self, db):
        """Mixed new and seen papers returns only new."""
        p1 = _make_paper(id="1")
        p2 = _make_paper(id="2")
        p3 = _make_paper(id="3")
        # Mark p1 as seen
        db.mark_seen("1", "Test", "arxiv")
        # Get new papers
        new = db.get_new_papers([p1, p2, p3])
        assert len(new) == 2
        assert p2 in new
        assert p3 in new
        assert p1 not in new

    def test_get_new_papers_empty_input(self, db):
        """Empty input list returns empty list."""
        new = db.get_new_papers([])
        assert len(new) == 0

    def test_get_new_papers_all_seen(self, db):
        """All papers already seen returns empty list."""
        p1 = _make_paper(id="1")
        p2 = _make_paper(id="2")
        # First call marks all as seen
        db.get_new_papers([p1, p2])
        # Second call should return empty
        new = db.get_new_papers([p1, p2])
        assert len(new) == 0

    def test_cleanup_removes_old_records(self, db):
        """Cleanup removes records older than specified days."""
        db.mark_seen("old", "Old Paper", "arxiv")
        # Manually set old date
        db.conn.execute(
            "UPDATE seen_papers SET last_seen_date = ? WHERE paper_id = ?",
            ("2020-01-01", "old"),
        )
        db.conn.commit()
        deleted = db.cleanup(older_than_days=90)
        assert deleted == 1
        assert db.is_seen("old") is False

    def test_cleanup_keeps_recent_records(self, db):
        """Cleanup keeps recent records."""
        db.mark_seen("recent", "Recent Paper", "arxiv")
        deleted = db.cleanup(older_than_days=90)
        assert deleted == 0
        assert db.is_seen("recent") is True

    def test_cleanup_mixed_records(self, db):
        """Cleanup removes old but keeps recent records."""
        # Add old record
        db.mark_seen("old", "Old Paper", "arxiv")
        db.conn.execute(
            "UPDATE seen_papers SET last_seen_date = ? WHERE paper_id = ?",
            ("2020-01-01", "old"),
        )
        db.conn.commit()
        # Add recent record
        db.mark_seen("recent", "Recent Paper", "biorxiv")
        # Cleanup
        deleted = db.cleanup(older_than_days=90)
        assert deleted == 1
        assert db.is_seen("old") is False
        assert db.is_seen("recent") is True

    def test_cleanup_custom_threshold(self, db):
        """Cleanup respects custom days threshold."""
        db.mark_seen("paper1", "Paper 1", "arxiv")
        # Set date to 40 days ago
        old_date = (datetime.now().date() - timedelta(days=40)).isoformat()
        db.conn.execute(
            "UPDATE seen_papers SET last_seen_date = ? WHERE paper_id = ?",
            (old_date, "paper1"),
        )
        db.conn.commit()
        # Cleanup with 30 days threshold should remove it
        deleted = db.cleanup(older_than_days=30)
        assert deleted == 1
        # Cleanup with 50 days threshold should not remove it (if we had kept it)
        db.mark_seen("paper2", "Paper 2", "arxiv")
        db.conn.execute(
            "UPDATE seen_papers SET last_seen_date = ? WHERE paper_id = ?",
            (old_date, "paper2"),
        )
        db.conn.commit()
        deleted = db.cleanup(older_than_days=50)
        assert deleted == 0

    def test_context_manager(self, tmp_path):
        """Database works as context manager."""
        db_path = str(tmp_path / "ctx.db")
        with DeduplicationDB(db_path) as db:
            db.mark_seen("paper1", "Title", "arxiv")
            assert db.is_seen("paper1") is True
        # Connection should be closed after context

    def test_close(self, tmp_path):
        """Close method closes connection."""
        db_path = str(tmp_path / "close.db")
        db = DeduplicationDB(db_path)
        db.mark_seen("paper1", "Title", "arxiv")
        db.close()
        # Connection should be closed

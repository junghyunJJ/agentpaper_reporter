"""Unit tests for keyword filtering and deduplication."""

import pytest
from datetime import date
from unittest.mock import MagicMock
from agentpaper_reporter.models import Paper
from agentpaper_reporter.filter import matches_keywords, filter_and_deduplicate


def _make_paper(title="Test", abstract="Abstract", **kwargs):
    """Helper to create a Paper with defaults."""
    defaults = dict(
        id="1",
        authors=[],
        published_date=date(2024, 1, 1),
        source="arxiv",
        url="http://x.com",
    )
    defaults.update(kwargs)
    return Paper(title=title, abstract=abstract, **defaults)


class TestMatchesKeywords:
    """Tests for matches_keywords function."""

    def test_matches_exact_in_title(self):
        """Exact keyword match in title returns True."""
        p = _make_paper(title="Agentic AI system")
        assert matches_keywords(p, ["agentic AI"]) is True

    def test_matches_case_insensitive_title(self):
        """Case-insensitive match in title returns True."""
        p = _make_paper(title="MULTI-AGENT SYSTEM")
        assert matches_keywords(p, ["multi-agent"]) is True

    def test_matches_in_abstract(self):
        """Keyword match in abstract returns True."""
        p = _make_paper(title="Something", abstract="Uses LLM agent framework")
        assert matches_keywords(p, ["agent framework"]) is True

    def test_matches_partial_in_title(self):
        """Partial keyword match in title returns True."""
        p = _make_paper(title="The agents are working")
        assert matches_keywords(p, ["agent"]) is True

    def test_matches_partial_in_abstract(self):
        """Partial keyword match in abstract returns True."""
        p = _make_paper(title="Title", abstract="Multi-agent systems are complex")
        assert matches_keywords(p, ["multi-agent"]) is True

    def test_no_match(self):
        """No keyword match returns False."""
        p = _make_paper(title="Unrelated paper", abstract="About cooking")
        assert matches_keywords(p, ["AI agent"]) is False

    def test_matches_any_keyword(self):
        """Matching any keyword returns True."""
        p = _make_paper(title="AI paper")
        assert matches_keywords(p, ["robotics", "AI", "quantum"]) is True

    def test_matches_multiple_keywords(self):
        """Paper matches if any keyword is present."""
        p = _make_paper(title="Machine learning", abstract="Deep neural networks")
        assert matches_keywords(p, ["machine learning", "robotics"]) is True

    def test_no_match_multiple_keywords(self):
        """Paper doesn't match any keyword returns False."""
        p = _make_paper(title="Biology study", abstract="Cell structure")
        assert matches_keywords(p, ["AI", "agent", "robotics"]) is False

    def test_empty_keywords_list(self):
        """Empty keywords list returns False."""
        p = _make_paper(title="Any paper")
        assert matches_keywords(p, []) is False

    def test_empty_title_and_abstract(self):
        """Paper with empty title and abstract doesn't match."""
        p = _make_paper(title="", abstract="")
        assert matches_keywords(p, ["keyword"]) is False

    def test_none_title_abstract(self):
        """Paper with None title handled gracefully."""
        # This shouldn't happen with Pydantic validation, but test defensively
        p = _make_paper(title="Title", abstract="Abstract")
        # Modify internals for test
        p.title = None  # type: ignore
        p.abstract = None  # type: ignore
        # Should not crash
        result = matches_keywords(p, ["keyword"])
        assert result is False


class TestFilterAndDeduplicate:
    """Tests for filter_and_deduplicate function."""

    def test_filter_and_deduplicate_basic(self):
        """Filter papers by keywords and deduplicate."""
        papers = [
            _make_paper(id="1", title="AI agent paper", published_date=date(2024, 1, 3)),
            _make_paper(id="2", title="Unrelated paper", abstract="cooking"),
            _make_paper(id="3", title="Multi-agent system", published_date=date(2024, 1, 5)),
        ]
        db = MagicMock()
        db.get_new_papers.side_effect = lambda ps: ps  # All are new
        result = filter_and_deduplicate(papers, ["AI agent", "multi-agent"], db)
        assert len(result) == 2
        # Should be sorted by date descending
        assert result[0].id == "3"  # More recent first
        assert result[1].id == "1"

    def test_filter_and_deduplicate_none_match(self):
        """No papers match keywords returns empty list."""
        papers = [
            _make_paper(id="1", title="Biology paper"),
            _make_paper(id="2", title="Chemistry study"),
        ]
        db = MagicMock()
        db.get_new_papers.side_effect = lambda ps: ps
        result = filter_and_deduplicate(papers, ["AI agent"], db)
        assert len(result) == 0

    def test_filter_and_deduplicate_all_duplicates(self):
        """All papers are duplicates returns empty list."""
        papers = [
            _make_paper(id="1", title="AI agent paper"),
            _make_paper(id="2", title="Multi-agent system"),
        ]
        db = MagicMock()
        db.get_new_papers.return_value = []  # All are duplicates
        result = filter_and_deduplicate(papers, ["agent"], db)
        assert len(result) == 0

    def test_filter_and_deduplicate_some_duplicates(self):
        """Some papers are duplicates, only new ones returned."""
        papers = [
            _make_paper(id="1", title="AI agent paper", published_date=date(2024, 1, 1)),
            _make_paper(id="2", title="Multi-agent system", published_date=date(2024, 1, 2)),
            _make_paper(id="3", title="Agent framework", published_date=date(2024, 1, 3)),
        ]
        db = MagicMock()
        # Only paper 2 and 3 are new
        db.get_new_papers.return_value = [papers[1], papers[2]]
        result = filter_and_deduplicate(papers, ["agent"], db)
        assert len(result) == 2
        assert result[0].id == "3"  # Most recent first
        assert result[1].id == "2"

    def test_filter_and_deduplicate_date_sorting(self):
        """Papers are sorted by published_date descending."""
        papers = [
            _make_paper(id="1", title="agent paper", published_date=date(2024, 1, 10)),
            _make_paper(id="2", title="agent paper", published_date=date(2024, 1, 5)),
            _make_paper(id="3", title="agent paper", published_date=date(2024, 1, 15)),
            _make_paper(id="4", title="agent paper", published_date=date(2024, 1, 1)),
        ]
        db = MagicMock()
        db.get_new_papers.side_effect = lambda ps: ps
        result = filter_and_deduplicate(papers, ["agent"], db)
        assert len(result) == 4
        assert result[0].id == "3"  # 2024-01-15
        assert result[1].id == "1"  # 2024-01-10
        assert result[2].id == "2"  # 2024-01-05
        assert result[3].id == "4"  # 2024-01-01

    def test_filter_and_deduplicate_empty_input(self):
        """Empty input list returns empty list."""
        db = MagicMock()
        db.get_new_papers.side_effect = lambda ps: ps
        result = filter_and_deduplicate([], ["agent"], db)
        assert len(result) == 0

    def test_filter_and_deduplicate_calls_db(self):
        """Function calls db.get_new_papers with matched papers."""
        papers = [
            _make_paper(id="1", title="AI agent"),
            _make_paper(id="2", title="unrelated"),
        ]
        db = MagicMock()
        db.get_new_papers.return_value = []
        filter_and_deduplicate(papers, ["agent"], db)
        # Should be called with only the matched paper
        db.get_new_papers.assert_called_once()
        called_papers = db.get_new_papers.call_args[0][0]
        assert len(called_papers) == 1
        assert called_papers[0].id == "1"

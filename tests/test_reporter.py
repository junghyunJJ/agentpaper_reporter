"""Unit tests for report generation."""

import pytest
from datetime import date, datetime
from pathlib import Path
from agentpaper_reporter.models import Paper, ReportData
from agentpaper_reporter.reporter import ReportGenerator


def _make_report_data(papers_by_source=None, **kwargs):
    """Helper to create ReportData with defaults."""
    if papers_by_source is None:
        papers_by_source = {}
    defaults = {
        "date_range_start": date(2024, 1, 1),
        "date_range_end": date(2024, 1, 7),
        "total_papers_fetched": 10,
        "total_papers_matched": 5,
        "papers_by_source": papers_by_source,
        "search_keywords": ["AI agent"],
    }
    defaults.update(kwargs)
    return ReportData(**defaults)


def _make_paper(id="1", title="Test Paper", **kwargs):
    """Helper to create Paper with defaults."""
    defaults = {
        "id": id,
        "title": title,
        "authors": ["Author A"],
        "abstract": "Test abstract",
        "published_date": date(2024, 1, 1),
        "source": "arxiv",
        "url": "http://example.com",
    }
    defaults.update(kwargs)
    return Paper(**defaults)


class TestReportGenerator:
    """Tests for ReportGenerator class."""

    def test_init_default_template_dir(self):
        """ReportGenerator initializes with default template directory."""
        gen = ReportGenerator()
        # Should find templates/ relative to project root
        assert gen.template_dir is not None
        assert "templates" in gen.template_dir

    def test_init_custom_template_dir(self, tmp_path):
        """ReportGenerator initializes with custom template directory."""
        template_dir = str(tmp_path / "custom_templates")
        Path(template_dir).mkdir()
        # Create dummy template
        (Path(template_dir) / "report.md.j2").write_text("# Test Template")
        gen = ReportGenerator(template_dir=template_dir)
        assert gen.template_dir == template_dir

    def test_generate_empty_papers(self):
        """Generate report with no papers."""
        gen = ReportGenerator()
        data = _make_report_data()
        content = gen.generate(data)
        assert isinstance(content, str)
        assert len(content) > 0
        # Should contain some report structure
        assert "Weekly AI Agent Paper Report" in content or "Report" in content

    def test_generate_with_papers(self):
        """Generate report with papers."""
        paper = _make_paper(
            id="1",
            title="Test Paper Title",
            authors=["Author A", "Author B"],
            abstract="This is a test abstract.",
            summary="This is a test summary.",
        )
        data = _make_report_data(papers_by_source={"arxiv": [paper]})
        gen = ReportGenerator()
        content = gen.generate(data)

        assert "Test Paper Title" in content
        assert "Author A" in content
        assert "This is a test summary" in content or "This is a test abstract" in content

    def test_generate_multiple_sources(self):
        """Generate report with papers from multiple sources."""
        arxiv_paper = _make_paper(id="1", title="arXiv Paper", source="arxiv")
        biorxiv_paper = _make_paper(id="2", title="bioRxiv Paper", source="biorxiv")
        data = _make_report_data(
            papers_by_source={"arxiv": [arxiv_paper], "biorxiv": [biorxiv_paper]}
        )
        gen = ReportGenerator()
        content = gen.generate(data)

        assert "arXiv Paper" in content
        assert "bioRxiv Paper" in content

    def test_generate_multiple_papers_same_source(self):
        """Generate report with multiple papers from same source."""
        papers = [
            _make_paper(id="1", title="Paper 1"),
            _make_paper(id="2", title="Paper 2"),
            _make_paper(id="3", title="Paper 3"),
        ]
        data = _make_report_data(
            papers_by_source={"arxiv": papers}, total_papers_matched=3
        )
        gen = ReportGenerator()
        content = gen.generate(data)

        assert "Paper 1" in content
        assert "Paper 2" in content
        assert "Paper 3" in content

    def test_save_creates_directory(self, tmp_path):
        """Save creates output directory if it doesn't exist."""
        gen = ReportGenerator()
        content = "# Test Report"
        output_dir = str(tmp_path / "new_dir")
        path = gen.save(content, output_dir, "report.md")

        assert path.exists()
        assert path.parent.name == "new_dir"

    def test_save_with_date_pattern(self, tmp_path):
        """Save substitutes date in filename pattern."""
        gen = ReportGenerator()
        content = "# Test Report"
        path = gen.save(
            content, str(tmp_path), "report_{date}.md", date=date(2024, 1, 1)
        )

        assert path.exists()
        assert path.name == "report_2024-01-01.md"
        assert path.read_text() == "# Test Report"

    def test_save_default_date(self, tmp_path):
        """Save uses today's date if not provided."""
        gen = ReportGenerator()
        content = "# Test Report"
        path = gen.save(content, str(tmp_path), "report_{date}.md")

        assert path.exists()
        today = datetime.now().date()
        assert path.name == f"report_{today}.md"

    def test_save_no_date_pattern(self, tmp_path):
        """Save works with filename without date pattern."""
        gen = ReportGenerator()
        content = "# Test Report"
        path = gen.save(content, str(tmp_path), "weekly_report.md")

        assert path.exists()
        assert path.name == "weekly_report.md"

    def test_save_content_written(self, tmp_path):
        """Save writes correct content to file."""
        gen = ReportGenerator()
        content = "# Test Report\n\nThis is test content.\n\n## Section 1\n\nMore content."
        path = gen.save(content, str(tmp_path), "report.md")

        written_content = path.read_text(encoding="utf-8")
        assert written_content == content

    def test_save_returns_path_object(self, tmp_path):
        """Save returns Path object."""
        gen = ReportGenerator()
        content = "# Test"
        path = gen.save(content, str(tmp_path), "report.md")

        assert isinstance(path, Path)
        assert path.is_file()

    def test_generate_with_paper_no_summary(self):
        """Generate report with paper that has no summary."""
        paper = _make_paper(
            title="Paper Without Summary",
            abstract="This is the abstract",
            summary=None,
        )
        data = _make_report_data(papers_by_source={"arxiv": [paper]})
        gen = ReportGenerator()
        content = gen.generate(data)

        assert "Paper Without Summary" in content
        # Should handle missing summary gracefully

    def test_generate_includes_metadata(self):
        """Generate report includes metadata like date range and counts."""
        data = _make_report_data(
            date_range_start=date(2024, 1, 1),
            date_range_end=date(2024, 1, 7),
            total_papers_fetched=100,
            total_papers_matched=25,
        )
        gen = ReportGenerator()
        content = gen.generate(data)

        # Should include date information
        assert "2024" in content
        # Should include some count information (format may vary)
        assert "100" in content or "25" in content

    def test_generate_includes_keywords(self):
        """Generate report includes search keywords."""
        data = _make_report_data(search_keywords=["AI agent", "multi-agent", "LLM"])
        gen = ReportGenerator()
        content = gen.generate(data)

        # Should mention keywords somewhere
        assert "AI agent" in content or "multi-agent" in content or "keyword" in content.lower()

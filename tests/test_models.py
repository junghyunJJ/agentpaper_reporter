"""Unit tests for data models."""

import pytest
from datetime import date, datetime
from agentpaper_reporter.models import Paper, ReportData


class TestPaper:
    """Tests for Paper model validation."""

    def test_paper_valid_all_fields(self):
        """Paper with all required fields validates successfully."""
        p = Paper(
            id="arxiv:2301.12345",
            title="Test Paper",
            authors=["Author A"],
            abstract="This is an abstract.",
            published_date=date(2024, 1, 1),
            source="arxiv",
            url="http://example.com",
        )
        assert p.id == "arxiv:2301.12345"
        assert p.title == "Test Paper"
        assert p.authors == ["Author A"]
        assert p.abstract == "This is an abstract."
        assert p.published_date == date(2024, 1, 1)
        assert p.source == "arxiv"
        assert p.url == "http://example.com"

    def test_paper_optional_fields_none(self):
        """Paper with optional fields set to None validates successfully."""
        p = Paper(
            id="1",
            title="Test Title",
            authors=[],
            abstract="Abstract text",
            published_date=date(2024, 1, 1),
            source="biorxiv",
            url="http://x.com",
        )
        assert p.pdf_url is None
        assert p.summary is None
        assert p.categories == []

    def test_paper_with_optional_fields(self):
        """Paper with optional fields provided validates successfully."""
        p = Paper(
            id="2",
            title="Paper with extras",
            authors=["A", "B"],
            abstract="Abstract",
            published_date=date(2024, 2, 1),
            source="medrxiv",
            url="http://example.com",
            pdf_url="http://example.com/paper.pdf",
            categories=["cs.AI", "cs.MA"],
            summary="This is a summary.",
        )
        assert p.pdf_url == "http://example.com/paper.pdf"
        assert p.summary == "This is a summary."
        assert p.categories == ["cs.AI", "cs.MA"]

    def test_paper_source_arxiv(self):
        """Paper source 'arxiv' is valid."""
        p = Paper(
            id="1",
            title="T",
            authors=[],
            abstract="A",
            published_date=date(2024, 1, 1),
            source="arxiv",
            url="http://x.com",
        )
        assert p.source == "arxiv"

    def test_paper_source_biorxiv(self):
        """Paper source 'biorxiv' is valid."""
        p = Paper(
            id="1",
            title="T",
            authors=[],
            abstract="A",
            published_date=date(2024, 1, 1),
            source="biorxiv",
            url="http://x.com",
        )
        assert p.source == "biorxiv"

    def test_paper_source_medrxiv(self):
        """Paper source 'medrxiv' is valid."""
        p = Paper(
            id="1",
            title="T",
            authors=[],
            abstract="A",
            published_date=date(2024, 1, 1),
            source="medrxiv",
            url="http://x.com",
        )
        assert p.source == "medrxiv"

    def test_paper_invalid_source(self):
        """Paper with invalid source raises validation error."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Paper(
                id="1",
                title="T",
                authors=[],
                abstract="A",
                published_date=date(2024, 1, 1),
                source="invalid",  # type: ignore
                url="http://x.com",
            )

    def test_paper_missing_required_field(self):
        """Paper missing required field raises validation error."""
        with pytest.raises(Exception):  # Pydantic ValidationError
            Paper(
                id="1",
                title="T",
                # authors missing
                abstract="A",
                published_date=date(2024, 1, 1),
                source="arxiv",
                url="http://x.com",
            )


class TestReportData:
    """Tests for ReportData model validation."""

    def test_report_data_valid(self):
        """ReportData with all required fields validates successfully."""
        rd = ReportData(
            date_range_start=date(2024, 1, 1),
            date_range_end=date(2024, 1, 7),
            total_papers_fetched=10,
            total_papers_matched=5,
            papers_by_source={},
            search_keywords=["AI"],
        )
        assert rd.date_range_start == date(2024, 1, 1)
        assert rd.date_range_end == date(2024, 1, 7)
        assert rd.total_papers_fetched == 10
        assert rd.total_papers_matched == 5
        assert rd.papers_by_source == {}
        assert rd.search_keywords == ["AI"]

    def test_report_data_generated_at_default(self):
        """ReportData generated_at has default datetime."""
        before = datetime.now()
        rd = ReportData(
            date_range_start=date(2024, 1, 1),
            date_range_end=date(2024, 1, 7),
            total_papers_fetched=10,
            total_papers_matched=5,
            papers_by_source={},
            search_keywords=["AI"],
        )
        after = datetime.now()
        assert isinstance(rd.generated_at, datetime)
        assert before <= rd.generated_at <= after

    def test_report_data_with_papers(self):
        """ReportData with papers_by_source validates successfully."""
        paper = Paper(
            id="1",
            title="Test",
            authors=["A"],
            abstract="Abstract",
            published_date=date(2024, 1, 1),
            source="arxiv",
            url="http://x.com",
        )
        rd = ReportData(
            date_range_start=date(2024, 1, 1),
            date_range_end=date(2024, 1, 7),
            total_papers_fetched=1,
            total_papers_matched=1,
            papers_by_source={"arxiv": [paper]},
            search_keywords=["test"],
        )
        assert len(rd.papers_by_source["arxiv"]) == 1
        assert rd.papers_by_source["arxiv"][0].title == "Test"

    def test_report_data_multiple_keywords(self):
        """ReportData with multiple search keywords validates successfully."""
        rd = ReportData(
            date_range_start=date(2024, 1, 1),
            date_range_end=date(2024, 1, 7),
            total_papers_fetched=0,
            total_papers_matched=0,
            papers_by_source={},
            search_keywords=["AI agent", "multi-agent", "LLM"],
        )
        assert len(rd.search_keywords) == 3
        assert "AI agent" in rd.search_keywords

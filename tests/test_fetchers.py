"""Unit tests for paper fetchers."""

import pytest
from datetime import date
from unittest.mock import patch, MagicMock
from agentpaper_reporter.fetchers.arxiv_fetcher import ArxivFetcher
from agentpaper_reporter.fetchers.biorxiv_fetcher import BiorxivFetcher


class TestArxivFetcher:
    """Tests for ArxivFetcher class."""

    def test_init(self):
        """ArxivFetcher initializes with keywords and categories."""
        fetcher = ArxivFetcher(
            keywords=["AI agent", "multi-agent"],
            categories=["cs.AI", "cs.MA"],
            max_results=100,
        )
        assert fetcher.keywords == ["AI agent", "multi-agent"]
        assert fetcher.categories == ["cs.AI", "cs.MA"]
        assert fetcher.max_results == 100

    def test_build_query_keywords_and_categories(self):
        """Query built with both keywords and categories."""
        fetcher = ArxivFetcher(
            keywords=["AI agent", "multi-agent"], categories=["cs.AI", "cs.MA"]
        )
        query = fetcher._build_query()
        assert 'ti:"AI agent"' in query
        assert 'abs:"AI agent"' in query
        assert 'ti:"multi-agent"' in query
        assert 'abs:"multi-agent"' in query
        assert "cat:cs.AI" in query
        assert "cat:cs.MA" in query
        assert "AND" in query

    def test_build_query_keywords_only(self):
        """Query built with only keywords."""
        fetcher = ArxivFetcher(keywords=["AI agent"], categories=[])
        query = fetcher._build_query()
        assert 'ti:"AI agent"' in query
        assert 'abs:"AI agent"' in query
        assert "cat:" not in query

    def test_build_query_categories_only(self):
        """Query built with only categories."""
        fetcher = ArxivFetcher(keywords=[], categories=["cs.AI"])
        query = fetcher._build_query()
        assert "cat:cs.AI" in query
        assert 'ti:"' not in query
        assert 'abs:"' not in query

    def test_build_query_empty(self):
        """Query built with no keywords or categories."""
        fetcher = ArxivFetcher(keywords=[], categories=[])
        query = fetcher._build_query()
        assert query == "all"

    def test_extract_arxiv_id(self):
        """Extract arXiv ID from entry_id URL."""
        fetcher = ArxivFetcher(keywords=[], categories=[])
        assert (
            fetcher._extract_arxiv_id("http://arxiv.org/abs/2301.12345v1")
            == "arxiv:2301.12345"
        )
        assert (
            fetcher._extract_arxiv_id("http://arxiv.org/abs/2401.00001v2")
            == "arxiv:2401.00001"
        )

    def test_extract_arxiv_id_no_match(self):
        """Extract arXiv ID with no match returns full URL."""
        fetcher = ArxivFetcher(keywords=[], categories=[])
        url = "http://example.com/paper"
        assert fetcher._extract_arxiv_id(url) == url

    @patch("agentpaper_reporter.fetchers.arxiv_fetcher.arxiv")
    def test_fetch_success(self, mock_arxiv):
        """Fetch papers successfully."""
        # Create mock result
        mock_result = MagicMock()
        mock_result.entry_id = "http://arxiv.org/abs/2401.00001v1"
        mock_result.title = "Test Paper"
        mock_author = MagicMock()
        mock_author.name = "Author A"
        mock_result.authors = [mock_author]
        mock_result.summary = "Test abstract"
        mock_result.published.date.return_value = date(2024, 1, 15)
        mock_result.pdf_url = "http://arxiv.org/pdf/2401.00001v1"
        mock_result.categories = ["cs.AI"]

        # Setup client mock
        mock_client = MagicMock()
        mock_client.results.return_value = [mock_result]
        mock_arxiv.Client.return_value = mock_client
        mock_arxiv.SortCriterion.SubmittedDate = "submittedDate"
        mock_arxiv.SortOrder.Descending = "descending"
        mock_arxiv.Search.return_value = MagicMock()

        fetcher = ArxivFetcher(keywords=["AI"], categories=["cs.AI"])
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 1
        assert papers[0].id == "arxiv:2401.00001"
        assert papers[0].title == "Test Paper"
        assert papers[0].authors == ["Author A"]
        assert papers[0].abstract == "Test abstract"
        assert papers[0].source == "arxiv"
        assert papers[0].published_date == date(2024, 1, 15)

    @patch("agentpaper_reporter.fetchers.arxiv_fetcher.arxiv")
    def test_fetch_filters_by_date(self, mock_arxiv):
        """Fetch filters papers outside date range."""
        # Create mock results with different dates
        mock_result1 = MagicMock()
        mock_result1.entry_id = "http://arxiv.org/abs/2401.00001v1"
        mock_result1.title = "Paper 1"
        mock_result1.authors = []
        mock_result1.summary = "Abstract 1"
        mock_result1.published.date.return_value = date(2024, 1, 5)  # Inside range
        mock_result1.pdf_url = "http://arxiv.org/pdf/2401.00001v1"
        mock_result1.categories = []

        mock_result2 = MagicMock()
        mock_result2.entry_id = "http://arxiv.org/abs/2401.00002v1"
        mock_result2.title = "Paper 2"
        mock_result2.authors = []
        mock_result2.summary = "Abstract 2"
        mock_result2.published.date.return_value = date(2023, 12, 15)  # Outside range
        mock_result2.pdf_url = "http://arxiv.org/pdf/2401.00002v1"
        mock_result2.categories = []

        mock_client = MagicMock()
        mock_client.results.return_value = [mock_result1, mock_result2]
        mock_arxiv.Client.return_value = mock_client
        mock_arxiv.SortCriterion.SubmittedDate = "submittedDate"
        mock_arxiv.SortOrder.Descending = "descending"
        mock_arxiv.Search.return_value = MagicMock()

        fetcher = ArxivFetcher(keywords=["AI"], categories=[])
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 1
        assert papers[0].title == "Paper 1"

    @patch("agentpaper_reporter.fetchers.arxiv_fetcher.arxiv")
    def test_fetch_handles_error(self, mock_arxiv):
        """Fetch handles exceptions gracefully."""
        mock_arxiv.Client.side_effect = Exception("API error")

        fetcher = ArxivFetcher(keywords=["AI"], categories=[])
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 0


class TestBiorxivFetcher:
    """Tests for BiorxivFetcher class."""

    def test_init_biorxiv(self):
        """BiorxivFetcher initializes with biorxiv server."""
        fetcher = BiorxivFetcher(server="biorxiv", max_results=500)
        assert fetcher.server == "biorxiv"
        assert fetcher.max_results == 500

    def test_init_medrxiv(self):
        """BiorxivFetcher initializes with medrxiv server."""
        fetcher = BiorxivFetcher(server="medrxiv", max_results=300)
        assert fetcher.server == "medrxiv"
        assert fetcher.max_results == 300

    def test_init_invalid_server(self):
        """BiorxivFetcher raises error for invalid server."""
        with pytest.raises(ValueError):
            BiorxivFetcher(server="invalid")

    @patch("agentpaper_reporter.fetchers.biorxiv_fetcher.requests")
    def test_fetch_success(self, mock_requests):
        """Fetch papers successfully from bioRxiv."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "messages": [{"total": "1"}],
            "collection": [
                {
                    "doi": "10.1101/2024.01.01.000001",
                    "title": "Test Paper",
                    "authors": "Author A; Author B",
                    "abstract": "Test abstract",
                    "date": "2024-01-15",
                    "category": "bioinformatics",
                }
            ],
        }
        mock_response.raise_for_status = MagicMock()
        mock_requests.get.return_value = mock_response
        mock_requests.exceptions = __import__("requests").exceptions

        fetcher = BiorxivFetcher(server="biorxiv")
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 1
        assert papers[0].id == "biorxiv:10.1101/2024.01.01.000001"
        assert papers[0].title == "Test Paper"
        assert papers[0].authors == ["Author A", "Author B"]
        assert papers[0].abstract == "Test abstract"
        assert papers[0].source == "biorxiv"
        assert papers[0].published_date == date(2024, 1, 15)
        assert papers[0].categories == ["bioinformatics"]

    @patch("agentpaper_reporter.fetchers.biorxiv_fetcher.requests")
    def test_fetch_empty_response(self, mock_requests):
        """Fetch handles empty response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"messages": []}
        mock_response.raise_for_status = MagicMock()
        mock_requests.get.return_value = mock_response
        mock_requests.exceptions = __import__("requests").exceptions

        fetcher = BiorxivFetcher(server="biorxiv")
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 0

    @patch("agentpaper_reporter.fetchers.biorxiv_fetcher.requests")
    def test_fetch_pagination(self, mock_requests):
        """Fetch handles pagination correctly."""
        # First page
        first_response = MagicMock()
        first_response.json.return_value = {
            "messages": [{"total": "150"}],
            "collection": [
                {
                    "doi": f"10.1101/2024.01.01.{i:06d}",
                    "title": f"Paper {i}",
                    "authors": "Author A",
                    "abstract": "Abstract",
                    "date": "2024-01-15",
                    "category": "bioinformatics",
                }
                for i in range(100)
            ],
        }
        first_response.raise_for_status = MagicMock()

        # Second page
        second_response = MagicMock()
        second_response.json.return_value = {
            "messages": [{"total": "150"}],
            "collection": [
                {
                    "doi": f"10.1101/2024.01.01.{i:06d}",
                    "title": f"Paper {i}",
                    "authors": "Author A",
                    "abstract": "Abstract",
                    "date": "2024-01-15",
                    "category": "bioinformatics",
                }
                for i in range(100, 150)
            ],
        }
        second_response.raise_for_status = MagicMock()

        mock_requests.get.side_effect = [first_response, second_response]
        mock_requests.exceptions = __import__("requests").exceptions

        fetcher = BiorxivFetcher(server="biorxiv", max_results=500)
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 150

    @patch("agentpaper_reporter.fetchers.biorxiv_fetcher.requests")
    def test_fetch_handles_network_error(self, mock_requests):
        """Fetch handles network errors gracefully."""
        mock_requests.get.side_effect = __import__("requests").exceptions.RequestException(
            "Network error"
        )
        mock_requests.exceptions = __import__("requests").exceptions

        fetcher = BiorxivFetcher(server="biorxiv")
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 0

    @patch("agentpaper_reporter.fetchers.biorxiv_fetcher.requests")
    def test_fetch_respects_max_results(self, mock_requests):
        """Fetch respects max_results limit."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "messages": [{"total": "200"}],
            "collection": [
                {
                    "doi": f"10.1101/2024.01.01.{i:06d}",
                    "title": f"Paper {i}",
                    "authors": "Author A",
                    "abstract": "Abstract",
                    "date": "2024-01-15",
                    "category": "bioinformatics",
                }
                for i in range(100)
            ],
        }
        mock_response.raise_for_status = MagicMock()
        mock_requests.get.return_value = mock_response
        mock_requests.exceptions = __import__("requests").exceptions

        fetcher = BiorxivFetcher(server="biorxiv", max_results=50)
        papers = fetcher.fetch(date(2024, 1, 1), date(2024, 1, 31))

        assert len(papers) == 50

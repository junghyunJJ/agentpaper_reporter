"""Tests for source fetch failure handling."""

from datetime import date
from unittest.mock import MagicMock, patch

import pytest

from agentpaper_reporter import __main__ as cli_main
from agentpaper_reporter.config import (
    AppConfig,
    DatabaseConfig,
    EmailConfig,
    LLMConfig,
    ReportConfig,
    ScheduleConfig,
    SearchConfig,
    SourceConfig,
    SourcesConfig,
)
from agentpaper_reporter.fetchers.arxiv_fetcher import ArxivFetcher


def _make_config(db_path: str) -> AppConfig:
    """Build a minimal config for CLI failure tests."""
    return AppConfig(
        search=SearchConfig(keywords=["AI agent"], categories=["cs.AI"]),
        sources=SourcesConfig(
            arxiv=SourceConfig(enabled=True, max_results=10),
            biorxiv=SourceConfig(enabled=False, max_results=10),
            medrxiv=SourceConfig(enabled=False, max_results=10),
        ),
        llm=LLMConfig(
            provider="openai",
            claude_model="claude-sonnet-4-20250514",
            openai_model="gpt-4.1-mini",
            openrouter_model="openai/gpt-oss-120b:free",
            max_tokens=300,
            openai_api_key="test-key",
        ),
        report=ReportConfig(output_dir="reports", filename_pattern="weekly_report_{date}.md"),
        database=DatabaseConfig(path=db_path),
        schedule=ScheduleConfig(lookback_days=7),
        email=EmailConfig(enabled=False, recipients=[]),
    )


@patch("agentpaper_reporter.fetchers.arxiv_fetcher.arxiv")
def test_arxiv_fetch_propagates_api_request_failures(mock_arxiv):
    """arXiv API failures are not silently converted to an empty result set."""
    mock_client = MagicMock()
    mock_client.results.side_effect = RuntimeError("HTTP 429")
    mock_arxiv.Client.return_value = mock_client
    mock_arxiv.SortCriterion.SubmittedDate = "submittedDate"
    mock_arxiv.SortOrder.Descending = "descending"
    mock_arxiv.Search.return_value = MagicMock()

    fetcher = ArxivFetcher(keywords=["AI agent"], categories=["cs.AI"])

    with pytest.raises(RuntimeError, match="HTTP 429"):
        fetcher.fetch(date(2026, 5, 25), date(2026, 5, 31))


def test_main_fails_when_enabled_source_fetch_fails(tmp_path, monkeypatch):
    """CLI returns non-zero when an enabled source cannot be fetched."""
    monkeypatch.setattr(
        "sys.argv",
        [
            "agentpaper_reporter",
            "--start-date",
            "2026-05-25",
            "--end-date",
            "2026-05-31",
        ],
    )
    monkeypatch.setattr(cli_main, "load_config", lambda: _make_config(str(tmp_path / "db.sqlite")))
    monkeypatch.setattr(
        cli_main.ArxivFetcher,
        "fetch",
        lambda self, start_date, end_date: (_ for _ in ()).throw(RuntimeError("HTTP 429")),
    )

    assert cli_main.main() == 1

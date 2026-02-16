# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Weekly AI Paper Monitor — an automated pipeline that fetches papers from arXiv, bioRxiv, and medRxiv, filters by agentic AI keywords, deduplicates via SQLite, generates LLM summaries (Claude or OpenAI), and produces a weekly Markdown report. Runs on GitHub Actions (Monday 9:00 UTC) or locally via CLI.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the full pipeline (fetches papers for the previous Mon–Sun week)
python -m agentpaper_reporter

# Run with custom date range
python -m agentpaper_reporter --start-date 2026-02-03 --end-date 2026-02-09

# Run tests
pytest tests/
pytest tests/ -v
pytest tests/test_fetchers.py::TestArxivFetcher::test_fetch_success  # single test

# Coverage
pytest tests/ --cov=agentpaper_reporter
```

## Configuration

- `config.yaml` — primary config (keywords, sources, LLM provider, output paths, lookback days)
- `.env` — API keys (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`); loaded via python-dotenv, never committed
- Env vars `LLM_PROVIDER` and `LOOKBACK_DAYS` override their config.yaml counterparts

The LLM provider is set to `"openai"` by default in config.yaml. Switch to `"claude"` by changing `llm.provider` or setting `LLM_PROVIDER=claude`.

Email notifications are **disabled by default**. To enable: set `email.enabled: true` in `config.yaml` (or `EMAIL_ENABLED=true`), configure `SMTP_USER`/`SMTP_PASSWORD` in `.env`, and set recipients via `email.recipients` in config or `EMAIL_RECIPIENTS` env var (comma-separated).

## Architecture

Linear pipeline orchestrated in `__main__.py:main()`:

```
config.yaml + .env → load_config() → Fetch → Filter → Deduplicate → Summarize → Report → Email (optional) → Cleanup
```

### Key modules (all under `agentpaper_reporter/`)

| Module | Responsibility |
|---|---|
| `__main__.py` | CLI entry point, pipeline orchestration, date range calculation |
| `config.py` | Pydantic-validated config loading with env var overrides |
| `models.py` | `Paper`, `ReportData`, `WeekComparison` — Pydantic data models |
| `fetchers/arxiv_fetcher.py` | arXiv API queries (keywords + categories, date-filtered client-side) |
| `fetchers/biorxiv_fetcher.py` | bioRxiv/medRxiv REST API with cursor pagination (shared class, `server` param distinguishes) |
| `filter.py` | Case-insensitive keyword matching on title+abstract, delegates dedup to DB |
| `db.py` | `DeduplicationDB` — SQLite context manager; `get_new_papers()` atomically filters and marks seen |
| `summarizer.py` | LLM calls (Claude/OpenAI) with tenacity retry; per-paper summaries, biomedical overview, week-over-week comparison |
| `comparison.py` | Weekly stats JSON persistence in `data/`; loads previous week's stats and builds `WeekComparison` |
| `reporter.py` | Jinja2 rendering of `templates/report.md.j2` into Markdown |
| `email_sender.py` | Optional HTML email delivery of reports via SMTP (disabled by default) |

### Data flow details

- **Date range**: defaults to previous Mon–Sun. Report filename uses Mon (day after end_date). CLI `--start-date`/`--end-date` override this.
- **bioRxiv fetcher** handles both bioRxiv and medRxiv (same API, different `server` param). Pagination is cursor-based in increments of 100. The API returns `total` as a string.
- **Deduplication**: `get_new_papers()` checks + marks papers in a single transaction. Papers older than 90 days are cleaned up after each run.
- **Week-over-week comparison**: stats saved as `data/weekly_stats_{date}.json`; if a previous week's file exists, an LLM-generated trend summary is added to the report.
- **Report template** (`templates/report.md.j2`) renders collapsible abstracts, biomedical highlights section, and week-over-week comparison table.

### Test conventions

Tests use `unittest.mock` (patch/MagicMock) to mock external APIs (arxiv client, requests, LLM clients). Tests are organized per-module in `tests/test_*.py`. No fixtures file — mocks are created inline per test method.

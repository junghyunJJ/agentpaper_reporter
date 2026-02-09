# Weekly AI Paper Monitor

An automated system that fetches, filters, summarizes, and reports on agentic AI papers from multiple academic sources. The system intelligently monitors arXiv, bioRxiv, and medRxiv for papers related to agentic AI systems, deduplicates findings, generates AI-powered summaries, and publishes comprehensive weekly reports.

## Features

- **Multi-source paper fetching**: Automatically retrieves papers from arXiv, bioRxiv, and medRxiv
- **Keyword-based filtering**: Configurable search keywords and arXiv category filters to find relevant papers
- **SQLite deduplication**: Maintains a database of seen papers to prevent duplicate reports
- **LLM summarization**: Uses Claude or OpenAI to generate concise, relevant summaries of paper abstracts
- **Markdown report generation**: Creates beautifully formatted reports with collapsible abstracts and structured metadata
- **GitHub Actions automation**: Runs automatically every Monday at 9:00 UTC (configurable)
- **Environment-based configuration**: Override settings via environment variables for flexible deployment

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Copy the example `.env` file and set your API key:

```bash
cp .env.example .env
# Edit .env with your API key
```

Or set environment variables directly:

```bash
# For Claude
export ANTHROPIC_API_KEY=your-anthropic-api-key

# OR for OpenAI
export OPENAI_API_KEY=your-openai-api-key
```

### Run

```bash
python -m agentpaper_reporter
```

The first run will create the database and output directory. Subsequent runs will only report new papers.

## Configuration

The system reads configuration from `config.yaml`. You can override any setting using environment variables.

### config.yaml Structure

```yaml
search:
  keywords:
    - "agentic AI"
    - "multi-agent system"
    - "AI agent"
    - "tool-use"
    - "function calling"
  categories:
    - "cs.AI"
    - "cs.MA"
    - "cs.CL"
    - "cs.LG"

sources:
  arxiv:
    enabled: true
    max_results: 200
  biorxiv:
    enabled: true
    max_results: 500
  medrxiv:
    enabled: true
    max_results: 500

llm:
  provider: "claude"  # "claude" or "openai"
  claude_model: "claude-sonnet-4-20250514"
  openai_model: "gpt-4o-mini"
  max_tokens: 300

report:
  output_dir: "reports"
  filename_pattern: "weekly_report_{date}.md"

database:
  path: "data/papers.db"

schedule:
  lookback_days: 7
```

### Configuration Sections

**search**: Defines keywords and arXiv categories to filter papers
- `keywords`: List of keywords to match in paper titles and abstracts
- `categories`: arXiv category codes (e.g., cs.AI for artificial intelligence)

**sources**: Enable/disable paper sources and set result limits
- `arxiv`, `biorxiv`, `medrxiv`: Each has `enabled` flag and `max_results` limit

**llm**: Language model configuration
- `provider`: Choose "claude" or "openai"
- `claude_model`: Claude model name (e.g., claude-sonnet-4-20250514)
- `openai_model`: OpenAI model name (e.g., gpt-4o-mini)
- `max_tokens`: Maximum tokens for each summary (typically 300)

**report**: Output settings
- `output_dir`: Directory to save markdown reports
- `filename_pattern`: Filename format (use {date} placeholder for date substitution)

**database**: SQLite database location
- `path`: Path to the deduplication database file

**schedule**: Fetch settings
- `lookback_days`: Number of days to look back when fetching papers (default 7 for weekly reports)

## Environment Variables

Override config.yaml settings using environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| ANTHROPIC_API_KEY | Required for Claude summarization | sk-ant-xxx |
| OPENAI_API_KEY | Required for OpenAI summarization | sk-xxx |
| LLM_PROVIDER | Override LLM provider | claude or openai |
| LOOKBACK_DAYS | Override lookback period | 14 |

### Priority

Environment variables override config.yaml settings. This allows flexible deployment across different environments.

## GitHub Actions Setup

The system includes GitHub Actions workflow for automated weekly report generation and publishing.

### 1. Add Secrets

In your GitHub repository, add one of the following as a secret:

- Go to Settings → Secrets and variables → Actions → New repository secret
- Add either `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` with your API key value

### 2. Optional: Set LLM Provider Variable

If you want to use OpenAI instead of the default Claude:

- Go to Settings → Secrets and variables → Actions → Variables → New repository variable
- Add variable `LLM_PROVIDER` with value `openai`

### 3. Workflow Configuration

The workflow file (`.github/workflows/weekly_report.yml`) is pre-configured to:

- Run every Monday at 9:00 UTC
- Support manual triggering via `workflow_dispatch`
- Automatically commit and push generated reports and database updates

To modify the schedule, edit the `cron` expression in `.github/workflows/weekly_report.yml`:

```yaml
on:
  schedule:
    - cron: '0 9 * * 1'  # Monday 9:00 UTC
```

Common cron patterns:
- `0 9 * * 1` = Monday 9:00 UTC
- `0 9 * * *` = Daily at 9:00 UTC
- `0 0 * * 0` = Sunday midnight UTC

## Architecture

The system follows a linear pipeline architecture:

```
config.yaml
    ↓
Load Configuration
    ↓
Fetch Papers (arXiv/bioRxiv/medRxiv)
    ↓
Filter by Keywords
    ↓
Deduplicate (SQLite)
    ↓
Summarize (LLM)
    ↓
Generate Report (Markdown)
    ↓
Save Report
    ↓
Cleanup Database
```

### Core Components

**Fetchers**: Specialized modules for each paper source
- `arxiv_fetcher.py`: Queries arXiv API with keywords and categories
- `biorxiv_fetcher.py`: Fetches from bioRxiv and medRxiv servers

**Filter**: Keyword-based filtering and deduplication
- `filter.py`: Matches papers against keywords (case-insensitive)
- `db.py`: Maintains SQLite database of seen papers

**Summarizer**: LLM-powered paper summarization
- `summarizer.py`: Interfaces with Claude or OpenAI APIs with retry logic

**Reporter**: Markdown report generation
- `reporter.py`: Renders Jinja2 templates into markdown reports

**Models**: Data structures
- `models.py`: Pydantic models for Paper and ReportData

## Project Structure

```
agentpaper_reporter/
├── agentpaper_reporter/              # Main package
│   ├── __main__.py                   # CLI entry point
│   ├── __init__.py
│   ├── config.py                     # Configuration management
│   ├── models.py                     # Data models
│   ├── db.py                         # SQLite deduplication database
│   ├── filter.py                     # Keyword filtering
│   ├── summarizer.py                 # LLM summarization
│   ├── reporter.py                   # Report generation
│   └── fetchers/                     # Paper source fetchers
│       ├── arxiv_fetcher.py
│       └── biorxiv_fetcher.py
├── templates/                        # Jinja2 templates
│   └── report.md.j2                  # Markdown report template
├── tests/                            # Test suite
├── data/                             # Runtime data
│   └── papers.db                     # SQLite database (created at runtime)
├── reports/                          # Generated reports (created at runtime)
├── config.yaml                       # Configuration file
├── requirements.txt                  # Python dependencies
├── .github/workflows/                # GitHub Actions
│   └── weekly_report.yml
└── README.md                         # This file
```

## Running Tests

Run the test suite using pytest:

```bash
pytest tests/
```

For verbose output:

```bash
pytest tests/ -v
```

For coverage report:

```bash
pytest tests/ --cov=agentpaper_reporter
```

## How It Works

### Workflow

1. **Load Configuration**: Reads config.yaml and applies environment variable overrides
2. **Calculate Date Range**: Uses lookback_days to determine fetch window
3. **Fetch Papers**: Queries each enabled source (arXiv, bioRxiv, medRxiv) with configured limits
4. **Filter**: Matches papers against keywords (case-insensitive search in title and abstract)
5. **Deduplicate**: Uses SQLite database to identify and exclude previously seen papers
6. **Summarize**: Sends new papers to configured LLM for summarization with retry logic
7. **Generate Report**: Renders filtered and summarized papers into markdown
8. **Save**: Writes report to output_dir with timestamped filename
9. **Cleanup**: Removes database entries older than 90 days

### Deduplication

The SQLite database stores:
- Paper ID (unique identifier from source)
- Title
- Source (arxiv, biorxiv, or medrxiv)
- First seen date
- Last seen date

Papers are considered duplicates if they have the same ID across multiple fetches. When a paper is seen again, only its last_seen_date is updated. This ensures each paper appears in exactly one report.

### Summarization

Each new paper receives an AI-generated summary via:

- **Claude**: Uses anthropic-sdk with configured model and max_tokens
- **OpenAI**: Uses openai-sdk with configured model and max_tokens

Summaries focus on:
- Main contribution
- Methodology
- Key findings relevant to agentic AI

Failed summaries gracefully degrade to "Summary unavailable." Retry logic with exponential backoff handles transient API errors.

## Dependencies

See `requirements.txt`:

- **arxiv** >= 2.1.0: arXiv API client
- **requests** >= 2.31.0: HTTP library for bioRxiv/medRxiv
- **pydantic** >= 2.5.0: Data validation
- **pyyaml** >= 6.0.1: YAML configuration parsing
- **jinja2** >= 3.1.3: Template rendering for reports
- **anthropic** >= 0.40.0: Claude API client
- **openai** >= 1.50.0: OpenAI API client
- **tenacity** >= 8.2.0: Retry logic with backoff

## Troubleshooting

### No papers found

Check:
1. Keywords in config.yaml match your research area
2. Date range is correct (lookback_days setting)
3. Check logs for API errors during fetch

### "API key not found" error

Ensure the required API key environment variable is set:

```bash
# For Claude
echo $ANTHROPIC_API_KEY

# For OpenAI
echo $OPENAI_API_KEY
```

### Database locked error

If you see sqlite3 database locked errors, ensure:
1. Only one instance of the tool is running
2. Database file has write permissions
3. Disk space is available

### Report not generated

Check:
1. Template file exists at `templates/report.md.j2`
2. Output directory exists or can be created
3. Disk space and write permissions available

## License

MIT

## Contributing

Contributions are welcome. Please ensure:

1. Tests pass: `pytest tests/`
2. Code follows project conventions
3. Configuration changes are backward compatible
4. Environment variables are documented in this README

"""Weekly stats persistence and week-over-week comparison."""

from __future__ import annotations

import json
import logging
import pathlib
from datetime import date

from agentpaper_reporter.models import ReportData, WeekComparison

logger = logging.getLogger(__name__)


def save_weekly_stats(
    report_data: ReportData,
    stats_dir: str,
    report_date: date,
) -> pathlib.Path:
    """Save weekly statistics as a JSON sidecar file.

    Args:
        report_data: The completed report data.
        stats_dir: Directory to store stats files.
        report_date: The report generation date (used in filename).

    Returns:
        Path to the saved stats file.
    """
    stats_path = pathlib.Path(stats_dir)
    stats_path.mkdir(parents=True, exist_ok=True)

    by_source = {
        source: len(papers)
        for source, papers in report_data.papers_by_source.items()
    }

    top_papers = [
        paper.title
        for papers in report_data.papers_by_source.values()
        for paper in papers[:5]
    ]

    stats = {
        "report_date": str(report_date),
        "date_range_start": str(report_data.date_range_start),
        "date_range_end": str(report_data.date_range_end),
        "total_fetched": report_data.total_papers_fetched,
        "total_matched": report_data.total_papers_matched,
        "by_source": by_source,
        "top_papers": top_papers,
        "keywords_used": report_data.search_keywords,
    }

    file_path = stats_path / f"weekly_stats_{report_date}.json"
    file_path.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    logger.info(f"Weekly stats saved to {file_path}")
    return file_path


def load_previous_stats(
    stats_dir: str,
    current_report_date: date,
) -> dict | None:
    """Load the most recent stats JSON before the current report date.

    Args:
        stats_dir: Directory containing stats files.
        current_report_date: Current report date to look before.

    Returns:
        Parsed stats dict, or None if no previous stats found.
    """
    stats_path = pathlib.Path(stats_dir)
    if not stats_path.exists():
        return None

    candidates = sorted(stats_path.glob("weekly_stats_*.json"), reverse=True)
    for candidate in candidates:
        # Extract date from filename: weekly_stats_YYYY-MM-DD.json
        try:
            date_str = candidate.stem.replace("weekly_stats_", "")
            file_date = date.fromisoformat(date_str)
        except ValueError:
            continue

        if file_date < current_report_date:
            logger.info(f"Found previous stats: {candidate}")
            return json.loads(candidate.read_text(encoding="utf-8"))

    logger.info("No previous weekly stats found")
    return None


def build_comparison(
    current_data: ReportData,
    prev_stats: dict,
    summary: str,
) -> WeekComparison:
    """Build a WeekComparison from current report data and previous stats.

    Args:
        current_data: Current week's report data.
        prev_stats: Previous week's stats dict.
        summary: LLM-generated comparison summary.

    Returns:
        WeekComparison object with diffs computed.
    """
    prev_by_source = prev_stats.get("by_source", {})
    current_by_source = {
        source: len(papers)
        for source, papers in current_data.papers_by_source.items()
    }

    change_by_source = {}
    all_sources = set(current_by_source.keys()) | set(prev_by_source.keys())
    for source in all_sources:
        curr = current_by_source.get(source, 0)
        prev = prev_by_source.get(source, 0)
        change_by_source[source] = curr - prev

    prev_total = prev_stats.get("total_matched", 0)

    return WeekComparison(
        prev_report_date=date.fromisoformat(prev_stats["report_date"]),
        prev_total_matched=prev_total,
        change_total=current_data.total_papers_matched - prev_total,
        prev_by_source=prev_by_source,
        change_by_source=change_by_source,
        summary=summary,
    )

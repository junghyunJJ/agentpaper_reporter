"""Main entry point for agentpaper_reporter CLI."""

import argparse
import logging
import sys
from datetime import date, timedelta

from agentpaper_reporter.config import load_config
from agentpaper_reporter.db import DeduplicationDB
from agentpaper_reporter.fetchers.arxiv_fetcher import ArxivFetcher
from agentpaper_reporter.fetchers.biorxiv_fetcher import BiorxivFetcher
from agentpaper_reporter.filter import filter_and_deduplicate
from agentpaper_reporter.models import ReportData
from agentpaper_reporter.reporter import ReportGenerator
from agentpaper_reporter.summarizer import Summarizer

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Weekly AI Paper Monitor")
    parser.add_argument(
        "--start-date", type=date.fromisoformat,
        help="Start date (YYYY-MM-DD). Overrides lookback_days.",
    )
    parser.add_argument(
        "--end-date", type=date.fromisoformat,
        help="End date (YYYY-MM-DD). Defaults to today.",
    )
    return parser.parse_args()


def main() -> int:
    """
    Main entry point for the agentpaper_reporter application.

    Returns:
        0 on success, 1 on fatal error
    """
    args = parse_args()

    try:
        # Load configuration
        config = load_config()
    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        return 1

    # Calculate date range
    end_date = args.end_date or date.today()
    start_date = args.start_date or (end_date - timedelta(days=config.schedule.lookback_days))

    logger.info(f"Starting paper collection for {start_date} to {end_date}")

    # Initialize database
    with DeduplicationDB(config.database.path) as db:
        all_papers = []

        # Fetch from arXiv
        if config.sources.arxiv.enabled:
            try:
                logger.info("Fetching papers from arXiv...")
                fetcher = ArxivFetcher(
                    keywords=config.search.keywords,
                    categories=config.search.categories,
                    max_results=config.sources.arxiv.max_results
                )
                arxiv_papers = fetcher.fetch(start_date, end_date)
                all_papers.extend(arxiv_papers)
                logger.info(f"Fetched {len(arxiv_papers)} papers from arXiv")
            except Exception as e:
                logger.error(f"Failed to fetch from arXiv: {e}", exc_info=True)

        # Fetch from bioRxiv
        if config.sources.biorxiv.enabled:
            try:
                logger.info("Fetching papers from bioRxiv...")
                fetcher = BiorxivFetcher(
                    server="biorxiv",
                    max_results=config.sources.biorxiv.max_results
                )
                biorxiv_papers = fetcher.fetch(start_date, end_date)
                all_papers.extend(biorxiv_papers)
                logger.info(f"Fetched {len(biorxiv_papers)} papers from bioRxiv")
            except Exception as e:
                logger.error(f"Failed to fetch from bioRxiv: {e}", exc_info=True)

        # Fetch from medRxiv
        if config.sources.medrxiv.enabled:
            try:
                logger.info("Fetching papers from medRxiv...")
                fetcher = BiorxivFetcher(
                    server="medrxiv",
                    max_results=config.sources.medrxiv.max_results
                )
                medrxiv_papers = fetcher.fetch(start_date, end_date)
                all_papers.extend(medrxiv_papers)
                logger.info(f"Fetched {len(medrxiv_papers)} papers from medRxiv")
            except Exception as e:
                logger.error(f"Failed to fetch from medRxiv: {e}", exc_info=True)

        total_fetched = len(all_papers)
        logger.info(f"Total papers fetched: {total_fetched}")

        if total_fetched == 0:
            logger.warning("No papers fetched from any source")
            return 0

        # Filter and deduplicate
        logger.info("Filtering and deduplicating papers...")
        filtered_papers = filter_and_deduplicate(all_papers, config.search.keywords, db)
        logger.info(f"Papers after filtering: {len(filtered_papers)}")

        if len(filtered_papers) == 0:
            logger.warning("No papers matched filtering criteria")
            return 0

        # Summarize papers
        logger.info("Generating AI summaries...")
        summarizer = Summarizer(config)
        summarizer.summarize_papers(filtered_papers)
        logger.info("Summarization complete")

        # Group papers by source
        papers_by_source = {}
        for paper in filtered_papers:
            if paper.source not in papers_by_source:
                papers_by_source[paper.source] = []
            papers_by_source[paper.source].append(paper)

        # Build report data
        report_data = ReportData(
            date_range_start=start_date,
            date_range_end=end_date,
            total_papers_fetched=total_fetched,
            total_papers_matched=len(filtered_papers),
            papers_by_source=papers_by_source,
            search_keywords=config.search.keywords
        )

        # Generate and save report
        logger.info("Generating report...")
        reporter = ReportGenerator()
        content = reporter.generate(report_data)
        report_path = reporter.save(
            content,
            config.report.output_dir,
            config.report.filename_pattern,
            date=end_date,
        )

        # Cleanup old database entries
        deleted = db.cleanup()
        logger.info(f"Database cleanup: removed {deleted} old entries")

        # Log summary
        logger.info(f"Report generated successfully: {report_path}")
        logger.info("=" * 60)
        logger.info("Summary Statistics:")
        logger.info(f"  Date range: {start_date} to {end_date}")
        logger.info(f"  Total papers fetched: {total_fetched}")
        logger.info(f"  Papers after filtering: {len(filtered_papers)}")
        logger.info(f"  Papers by source:")
        for source, papers in sorted(papers_by_source.items()):
            logger.info(f"    {source}: {len(papers)}")
        logger.info(f"  Output: {report_path}")
        logger.info("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())

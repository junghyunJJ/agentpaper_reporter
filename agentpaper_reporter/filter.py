"""Keyword filtering and deduplication pipeline."""

import logging

from agentpaper_reporter.models import Paper
from agentpaper_reporter.db import DeduplicationDB

logger = logging.getLogger(__name__)


def matches_keywords(paper: Paper, keywords: list[str]) -> bool:
    """Case-insensitive check if ANY keyword appears in title OR abstract."""
    title_lower = paper.title.lower() if paper.title else ""
    abstract_lower = paper.abstract.lower() if paper.abstract else ""

    for keyword in keywords:
        keyword_lower = keyword.lower()
        if keyword_lower in title_lower or keyword_lower in abstract_lower:
            return True

    return False


def filter_and_deduplicate(
    papers: list[Paper],
    keywords: list[str],
    db: DeduplicationDB,
) -> list[Paper]:
    """Filter papers by keywords, deduplicate, and sort by date descending."""
    matched_papers = [p for p in papers if matches_keywords(p, keywords)]
    matched_count = len(matched_papers)

    new_papers = db.get_new_papers(matched_papers)
    new_count = len(new_papers)

    sorted_papers = sorted(
        new_papers,
        key=lambda p: p.published_date,
        reverse=True,
    )

    logger.info(f"{matched_count} papers matched keywords, {new_count} are new")

    return sorted_papers

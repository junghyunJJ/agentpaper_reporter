"""Fetcher for arXiv papers using the arxiv Python package."""

import logging
import re
from datetime import date

import arxiv

from agentpaper_reporter.models import Paper

logger = logging.getLogger(__name__)


class ArxivFetcher:
    """Fetcher for arXiv papers using the arxiv Python package."""

    def __init__(
        self, keywords: list[str], categories: list[str], max_results: int = 200
    ):
        self.keywords = keywords
        self.categories = categories
        self.max_results = max_results
        logger.info(
            f"Initialized ArxivFetcher with {len(keywords)} keywords, "
            f"{len(categories)} categories, max_results={max_results}"
        )

    def _build_query(self) -> str:
        """Build arXiv query string combining keywords and categories."""
        keyword_parts = []
        for kw in self.keywords:
            keyword_parts.append(f'ti:"{kw}"')
            keyword_parts.append(f'abs:"{kw}"')
        keyword_query = " OR ".join(keyword_parts)

        category_parts = [f"cat:{cat}" for cat in self.categories]
        category_query = " OR ".join(category_parts)

        if keyword_parts and category_parts:
            query = f"({keyword_query}) AND ({category_query})"
        elif keyword_parts:
            query = f"({keyword_query})"
        elif category_parts:
            query = f"({category_query})"
        else:
            query = "all"

        logger.debug(f"Built query: {query}")
        return query

    def fetch(self, start_date: date, end_date: date) -> list[Paper]:
        """Fetch papers from arXiv within the specified date range."""
        try:
            query = self._build_query()
            logger.info(
                f"Fetching arXiv papers from {start_date} to {end_date} "
                f"with max_results={self.max_results}"
            )

            search = arxiv.Search(
                query=query,
                max_results=self.max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )

            client = arxiv.Client()
            results = client.results(search)

            papers = []
            for result in results:
                try:
                    published = result.published.date()

                    if not (start_date <= published <= end_date):
                        continue

                    arxiv_id = self._extract_arxiv_id(result.entry_id)

                    paper = Paper(
                        id=arxiv_id,
                        title=result.title.strip(),
                        authors=[author.name for author in result.authors],
                        abstract=result.summary.strip(),
                        published_date=published,
                        source="arxiv",
                        url=result.entry_id,
                        pdf_url=result.pdf_url,
                        categories=result.categories,
                    )
                    papers.append(paper)

                except Exception as e:
                    logger.error(
                        f"Error processing arXiv result {result.entry_id}: {e}",
                        exc_info=True,
                    )
                    continue

            logger.info(
                f"Successfully fetched {len(papers)} papers from arXiv "
                f"in date range {start_date} to {end_date}"
            )
            return papers

        except Exception as e:
            logger.error(f"Error fetching papers from arXiv: {e}", exc_info=True)
            return []

    def _extract_arxiv_id(self, entry_id: str) -> str:
        """Extract arXiv ID from entry_id URL.

        e.g., http://arxiv.org/abs/2301.12345v1 -> arxiv:2301.12345
        """
        match = re.search(r"arxiv\.org/abs/(\d+\.\d+)", entry_id)
        if match:
            return f"arxiv:{match.group(1)}"
        logger.warning(f"Could not extract arXiv ID from {entry_id}, using full URL")
        return entry_id

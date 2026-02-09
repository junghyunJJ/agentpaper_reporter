"""Fetcher for bioRxiv and medRxiv papers via REST API."""

from __future__ import annotations

import logging
from datetime import date

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from agentpaper_reporter.models import Paper

logger = logging.getLogger(__name__)


class BiorxivFetcher:
    """Fetches papers from bioRxiv or medRxiv using their REST API."""

    def __init__(self, server: str = "biorxiv", max_results: int = 500):
        """
        Initialize the BiorxivFetcher.

        Args:
            server: Either "biorxiv" or "medrxiv"
            max_results: Maximum number of papers to fetch

        Raises:
            ValueError: If server is not "biorxiv" or "medrxiv"
        """
        if server not in ("biorxiv", "medrxiv"):
            raise ValueError(f"server must be 'biorxiv' or 'medrxiv', got '{server}'")

        self.server = server
        self.max_results = max_results
        self.base_url = "https://api.biorxiv.org/details"
        logger.info(f"Initialized {server} fetcher with max_results={max_results}")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=8),
        retry=retry_if_exception_type(requests.exceptions.RequestException),
    )
    def _fetch_page(self, start_date: str, end_date: str, cursor: int = 0) -> dict:
        """
        Fetch a single page of results from the API.

        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            cursor: Pagination cursor (increments by 100)

        Returns:
            JSON response as dictionary

        Raises:
            requests.exceptions.RequestException: On network/HTTP errors
        """
        url = f"{self.base_url}/{self.server}/{start_date}/{end_date}/{cursor}/json"
        logger.info(f"Fetching {url}")

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()

    def fetch(self, start_date: date, end_date: date) -> list[Paper]:
        """
        Fetch papers from the specified date range.

        Args:
            start_date: Start date for paper search
            end_date: End date for paper search

        Returns:
            List of Paper objects
        """
        start_str = start_date.strftime("%Y-%m-%d")
        end_str = end_date.strftime("%Y-%m-%d")

        logger.info(f"Fetching {self.server} papers from {start_str} to {end_str}")

        papers = []
        cursor = 0

        try:
            # Fetch first page to get total count
            first_page = self._fetch_page(start_str, end_str, cursor=0)

            # Handle empty response
            if "messages" not in first_page or not first_page["messages"]:
                logger.warning("No messages in API response")
                return []

            # Get total count (IMPORTANT: API returns this as a STRING)
            total_str = first_page["messages"][0].get("total", "0")
            total = int(total_str)
            logger.info(f"Total papers available: {total}")

            # Process first page
            if "collection" in first_page:
                papers.extend(self._parse_papers(first_page["collection"]))

            # Fetch remaining pages
            cursor = 100
            while cursor < total and len(papers) < self.max_results:
                page = self._fetch_page(start_str, end_str, cursor=cursor)

                if "collection" in page and page["collection"]:
                    papers.extend(self._parse_papers(page["collection"]))
                    logger.info(f"Fetched {len(papers)} papers so far (cursor={cursor})")
                else:
                    logger.warning(f"No collection in page at cursor={cursor}")
                    break

                cursor += 100

            # Trim to max_results
            papers = papers[:self.max_results]
            logger.info(f"Successfully fetched {len(papers)} papers from {self.server}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error fetching {self.server} papers: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error fetching {self.server} papers: {e}")
            return []

        return papers

    def _parse_papers(self, collection: list[dict]) -> list[Paper]:
        """
        Parse API response collection into Paper objects.

        Args:
            collection: List of paper dictionaries from API

        Returns:
            List of Paper objects
        """
        papers = []

        for item in collection:
            try:
                # Parse authors (semicolon-separated)
                authors_str = item.get("authors", "")
                authors = [a.strip() for a in authors_str.split(";") if a.strip()]

                # Parse date
                date_str = item.get("date", "")
                published_date = date.fromisoformat(date_str)

                # Get DOI and category
                doi = item.get("doi", "")
                category = item.get("category", "")

                paper = Paper(
                    id=f"{self.server}:{doi}",
                    title=item.get("title", ""),
                    authors=authors,
                    abstract=item.get("abstract", ""),
                    published_date=published_date,
                    source=self.server,  # type: ignore
                    url=f"https://doi.org/{doi}",
                    categories=[category] if category else [],
                )
                papers.append(paper)

            except Exception as e:
                logger.warning(f"Failed to parse paper: {e}")
                continue

        return papers

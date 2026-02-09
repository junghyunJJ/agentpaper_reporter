"""SQLite-based deduplication store for paper tracking."""

from __future__ import annotations

import logging
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agentpaper_reporter.models import Paper

logger = logging.getLogger(__name__)


class DeduplicationDB:
    """SQLite database for tracking seen papers and preventing duplicates."""

    def __init__(self, db_path: str):
        """
        Initialize the deduplication database.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = Path(db_path)

        # Create parent directories if they don't exist
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        # Connect to database
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row

        # Create table if not exists
        self._create_table()

        logger.info(f"Initialized deduplication database at {self.db_path}")

    def _create_table(self) -> None:
        """Create the seen_papers table if it doesn't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seen_papers (
                paper_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                source TEXT NOT NULL,
                first_seen_date TEXT NOT NULL,
                last_seen_date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def is_seen(self, paper_id: str) -> bool:
        """
        Check if a paper has been seen before.

        Args:
            paper_id: Unique identifier for the paper

        Returns:
            True if paper exists in database, False otherwise
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM seen_papers WHERE paper_id = ?",
            (paper_id,)
        )
        result = cursor.fetchone()
        return result is not None

    def mark_seen(self, paper_id: str, title: str, source: str) -> None:
        """
        Mark a paper as seen, inserting or updating the record.

        Args:
            paper_id: Unique identifier for the paper
            title: Paper title
            source: Source of the paper (arxiv, biorxiv, medrxiv)
        """
        cursor = self.conn.cursor()
        today = datetime.now().date().isoformat()

        # Try to insert, or update last_seen_date if exists
        cursor.execute("""
            INSERT INTO seen_papers (paper_id, title, source, first_seen_date, last_seen_date)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(paper_id) DO UPDATE SET
                last_seen_date = excluded.last_seen_date
        """, (paper_id, title, source, today, today))

        self.conn.commit()
        logger.debug(f"Marked paper as seen: {paper_id}")

    def get_new_papers(self, papers: list[Paper]) -> list[Paper]:
        """
        Filter papers to return only new (unseen) ones, then mark all as seen atomically.

        Args:
            papers: List of Paper objects to check

        Returns:
            List of Paper objects that haven't been seen before
        """
        if not papers:
            return []

        # Start transaction
        cursor = self.conn.cursor()

        # Check which papers are new
        new_papers = []
        today = datetime.now().date().isoformat()

        for paper in papers:
            cursor.execute(
                "SELECT 1 FROM seen_papers WHERE paper_id = ?",
                (paper.id,)
            )

            if cursor.fetchone() is None:
                new_papers.append(paper)

        # Mark all papers as seen (both new and existing)
        for paper in papers:
            cursor.execute("""
                INSERT INTO seen_papers (paper_id, title, source, first_seen_date, last_seen_date)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(paper_id) DO UPDATE SET
                    last_seen_date = excluded.last_seen_date
            """, (paper.id, paper.title, paper.source, today, today))

        self.conn.commit()

        logger.info(f"Filtered {len(papers)} papers: {len(new_papers)} new, {len(papers) - len(new_papers)} duplicates")
        return new_papers

    def cleanup(self, older_than_days: int = 90) -> int:
        """
        Delete records older than the specified number of days.

        Args:
            older_than_days: Delete records where last_seen_date is older than this many days

        Returns:
            Number of records deleted
        """
        cutoff_date = (datetime.now().date() - timedelta(days=older_than_days)).isoformat()

        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM seen_papers WHERE last_seen_date < ?",
            (cutoff_date,)
        )
        deleted_count = cursor.rowcount
        self.conn.commit()

        logger.info(f"Cleaned up {deleted_count} records older than {older_than_days} days")
        return deleted_count

    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            logger.debug("Database connection closed")

    def __enter__(self) -> DeduplicationDB:
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close()

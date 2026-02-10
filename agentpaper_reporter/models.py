from __future__ import annotations

from datetime import datetime, date
from typing import Literal

from pydantic import BaseModel, Field


class Paper(BaseModel):
    """Represents a research paper from various sources."""

    id: str
    title: str
    authors: list[str]
    abstract: str
    published_date: date
    source: Literal["arxiv", "biorxiv", "medrxiv"]
    url: str
    pdf_url: str | None = None
    categories: list[str] = Field(default_factory=list)
    summary: str | None = None


class WeekComparison(BaseModel):
    """Week-over-week comparison data."""

    prev_report_date: date
    prev_total_matched: int
    change_total: int
    prev_by_source: dict[str, int]
    change_by_source: dict[str, int]
    summary: str


class ReportData(BaseModel):
    """Data structure for the generated report."""

    generated_at: datetime = Field(default_factory=datetime.now)
    date_range_start: date
    date_range_end: date
    total_papers_fetched: int
    total_papers_matched: int
    papers_by_source: dict[str, list[Paper]]
    search_keywords: list[str]
    biomedical_papers: list[Paper] = Field(default_factory=list)
    biomedical_summary: str | None = None
    comparison: WeekComparison | None = None

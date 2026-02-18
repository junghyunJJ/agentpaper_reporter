"""LLM summarization with Claude and OpenAI support."""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING

import anthropic
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

from agentpaper_reporter.models import Paper, ReportData

if TYPE_CHECKING:
    from agentpaper_reporter.config import AppConfig

logger = logging.getLogger(__name__)


class Summarizer:
    """Generates concise summaries of research papers using LLMs."""

    SYSTEM_PROMPT = (
        "You are a scientific paper summarizer specializing in AI and agent systems research."
    )

    def __init__(self, config: AppConfig):
        self.config = config

    def _build_prompt(self, paper: Paper) -> str:
        return (
            "Summarize the following paper in 2-3 sentences. Focus on: the main contribution, "
            "methodology, and key findings relevant to the agentic AI field.\n\n"
            f"Title: {paper.title}\n\n"
            f"Abstract: {paper.abstract}"
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=8),
        reraise=True,
    )
    def _summarize_claude(self, paper: Paper) -> str:
        client = anthropic.Anthropic(api_key=self.config.llm.anthropic_api_key)
        response = client.messages.create(
            model=self.config.llm.claude_model,
            max_tokens=self.config.llm.max_tokens,
            system=self.SYSTEM_PROMPT,
            messages=[{"role": "user", "content": self._build_prompt(paper)}],
        )
        return response.content[0].text

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=8),
        reraise=True,
    )
    def _summarize_openai(self, paper: Paper) -> str:
        client = openai.OpenAI(api_key=self.config.llm.openai_api_key)
        response = client.chat.completions.create(
            model=self.config.llm.openai_model,
            max_tokens=self.config.llm.max_tokens,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": self._build_prompt(paper)},
            ],
        )
        return response.choices[0].message.content

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=2, max=8),
        reraise=True,
    )
    def _summarize_openrouter(self, paper: Paper) -> str:
        client = openai.OpenAI(
            api_key=self.config.llm.openrouter_api_key,
            base_url="https://openrouter.ai/api/v1",
        )
        response = client.chat.completions.create(
            model=self.config.llm.openrouter_model,
            max_tokens=self.config.llm.max_tokens,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": self._build_prompt(paper)},
            ],
        )
        return response.choices[0].message.content

    def summarize(self, paper: Paper) -> str:
        """Generate a summary for a single paper."""
        try:
            if self.config.llm.provider == "claude":
                return self._summarize_claude(paper)
            elif self.config.llm.provider == "openai":
                return self._summarize_openai(paper)
            elif self.config.llm.provider == "openrouter":
                return self._summarize_openrouter(paper)
            else:
                logger.warning(f"Unknown LLM provider: {self.config.llm.provider}")
                return "Summary unavailable."
        except Exception as e:
            logger.warning(f"Failed to summarize paper '{paper.title[:50]}...': {e}")
            return "Summary unavailable."

    def summarize_papers(self, papers: list[Paper]) -> list[Paper]:
        """Generate summaries for multiple papers with rate limiting."""
        total = len(papers)
        for i, paper in enumerate(papers):
            logger.info(f"Summarizing paper {i + 1}/{total}: {paper.title[:50]}...")
            paper.summary = self.summarize(paper)
            if i < total - 1:
                time.sleep(0.5)
        return papers

    def generate_biomedical_summary(self, papers: list[Paper]) -> str:
        """Generate a brief overview of all biomedical papers.

        Args:
            papers: List of biomedical papers (bioRxiv + medRxiv).

        Returns:
            LLM-generated summary paragraph, or empty string if no papers.
        """
        if not papers:
            return ""

        paper_descriptions = []
        for paper in papers[:20]:
            abstract_snippet = paper.abstract[:200] + ("..." if len(paper.abstract) > 200 else "")
            paper_descriptions.append(f"- {paper.title}: {abstract_snippet}")
        papers_text = "\n".join(paper_descriptions)

        prompt = (
            "Provide a brief overview (3-5 sentences) of the following biomedical papers "
            "that are relevant to AI agents in biomedicine. Summarize the key themes, "
            "methodologies, and areas of focus across these papers.\n\n"
            f"{papers_text}"
        )

        try:
            if self.config.llm.provider == "claude":
                client = anthropic.Anthropic(
                    api_key=self.config.llm.anthropic_api_key
                )
                response = client.messages.create(
                    model=self.config.llm.claude_model,
                    max_tokens=400,
                    system="You are a biomedical research analyst specializing in the intersection of AI agents and biomedicine.",
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text
            elif self.config.llm.provider == "openai":
                client = openai.OpenAI(api_key=self.config.llm.openai_api_key)
                response = client.chat.completions.create(
                    model=self.config.llm.openai_model,
                    max_tokens=400,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a biomedical research analyst specializing in the intersection of AI agents and biomedicine.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                )
                return response.choices[0].message.content
            elif self.config.llm.provider == "openrouter":
                client = openai.OpenAI(
                    api_key=self.config.llm.openrouter_api_key,
                    base_url="https://openrouter.ai/api/v1",
                )
                response = client.chat.completions.create(
                    model=self.config.llm.openrouter_model,
                    max_tokens=400,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a biomedical research analyst specializing in the intersection of AI agents and biomedicine.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                )
                return response.choices[0].message.content
            else:
                return "Biomedical summary unavailable."
        except Exception as e:
            logger.warning(f"Failed to generate biomedical summary: {e}")
            return "Biomedical summary unavailable."

    def generate_comparison_summary(
        self, current: ReportData, prev_stats: dict
    ) -> str:
        """Generate an LLM comparison summary between current and previous week.

        Args:
            current: Current week's report data.
            prev_stats: Previous week's stats dict.

        Returns:
            LLM-generated comparison summary string.
        """
        current_by_source = {
            source: len(papers)
            for source, papers in current.papers_by_source.items()
        }
        top_titles = [
            paper.title
            for papers in current.papers_by_source.values()
            for paper in papers[:5]
        ]

        prompt = (
            "Compare this week's AI agent paper trends with last week. "
            f"Current week: {current.total_papers_matched} papers "
            f"({', '.join(f'{s}: {c}' for s, c in current_by_source.items())}). "
            f"Previous week: {prev_stats.get('total_matched', 0)} papers "
            f"({', '.join(f'{s}: {c}' for s, c in prev_stats.get('by_source', {}).items())}). "
            f"Top paper titles this week: {top_titles[:10]}. "
            f"Previous week top papers: {prev_stats.get('top_papers', [])[:10]}. "
            "Highlight 3-5 notable points about trends, shifts in topics, "
            "or changes in volume across sources. Be concise."
        )

        try:
            if self.config.llm.provider == "claude":
                client = anthropic.Anthropic(
                    api_key=self.config.llm.anthropic_api_key
                )
                response = client.messages.create(
                    model=self.config.llm.claude_model,
                    max_tokens=500,
                    system="You are a research trend analyst specializing in AI agent systems.",
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text
            elif self.config.llm.provider == "openai":
                client = openai.OpenAI(api_key=self.config.llm.openai_api_key)
                response = client.chat.completions.create(
                    model=self.config.llm.openai_model,
                    max_tokens=500,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a research trend analyst specializing in AI agent systems.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                )
                return response.choices[0].message.content
            elif self.config.llm.provider == "openrouter":
                client = openai.OpenAI(
                    api_key=self.config.llm.openrouter_api_key,
                    base_url="https://openrouter.ai/api/v1",
                )
                response = client.chat.completions.create(
                    model=self.config.llm.openrouter_model,
                    max_tokens=500,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a research trend analyst specializing in AI agent systems.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                )
                return response.choices[0].message.content
            else:
                return "Comparison summary unavailable (unknown provider)."
        except Exception as e:
            logger.warning(f"Failed to generate comparison summary: {e}")
            return "Comparison summary unavailable."

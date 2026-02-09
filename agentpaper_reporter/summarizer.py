"""LLM summarization with Claude and OpenAI support."""

from __future__ import annotations

import logging
import time
from typing import TYPE_CHECKING

import anthropic
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

from agentpaper_reporter.models import Paper

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

    def summarize(self, paper: Paper) -> str:
        """Generate a summary for a single paper."""
        try:
            if self.config.llm.provider == "claude":
                return self._summarize_claude(paper)
            elif self.config.llm.provider == "openai":
                return self._summarize_openai(paper)
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

"""Unit tests for LLM summarization."""

import pytest
from datetime import date
from unittest.mock import patch, MagicMock
from agentpaper_reporter.models import Paper
from agentpaper_reporter.summarizer import Summarizer


def _make_paper(title="AI Agent Paper", abstract="About AI agents"):
    """Helper to create a Paper with defaults."""
    return Paper(
        id="1",
        title=title,
        authors=["Author A"],
        abstract=abstract,
        published_date=date(2024, 1, 1),
        source="arxiv",
        url="http://x.com",
    )


def _make_config(provider="claude"):
    """Helper to create a mock config."""
    config = MagicMock()
    config.llm.provider = provider
    config.llm.claude_model = "claude-sonnet-4-20250514"
    config.llm.openai_model = "gpt-4o-mini"
    config.llm.openrouter_model = "anthropic/claude-sonnet-4"
    config.llm.max_tokens = 300
    config.llm.anthropic_api_key = "test-key"
    config.llm.openai_api_key = "test-key"
    config.llm.openrouter_api_key = "test-key"
    return config


class TestSummarizer:
    """Tests for Summarizer class."""

    def test_init(self):
        """Summarizer initializes with config."""
        config = _make_config()
        s = Summarizer(config)
        assert s.config == config

    def test_build_prompt(self):
        """Prompt includes paper title and abstract."""
        s = Summarizer(_make_config())
        p = _make_paper(title="Test Title", abstract="Test Abstract")
        prompt = s._build_prompt(p)
        assert "Test Title" in prompt
        assert "Test Abstract" in prompt
        assert "Summarize" in prompt
        assert "2-3 sentences" in prompt

    @patch("agentpaper_reporter.summarizer.anthropic")
    def test_summarize_claude_success(self, mock_anthropic):
        """Summarize with Claude returns summary text."""
        mock_msg = MagicMock()
        mock_content = MagicMock()
        mock_content.text = "Summary text from Claude"
        mock_msg.content = [mock_content]
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        s = Summarizer(_make_config("claude"))
        result = s.summarize(_make_paper())

        assert result == "Summary text from Claude"
        mock_anthropic.Anthropic.assert_called_once_with(api_key="test-key")
        mock_client.messages.create.assert_called_once()
        call_kwargs = mock_client.messages.create.call_args[1]
        assert call_kwargs["model"] == "claude-sonnet-4-20250514"
        assert call_kwargs["max_tokens"] == 300

    @patch("agentpaper_reporter.summarizer.openai")
    def test_summarize_openai_success(self, mock_openai):
        """Summarize with OpenAI returns summary text."""
        mock_choice = MagicMock()
        mock_choice.message.content = "OpenAI summary text"
        mock_resp = MagicMock()
        mock_resp.choices = [mock_choice]
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_resp
        mock_openai.OpenAI.return_value = mock_client

        s = Summarizer(_make_config("openai"))
        result = s.summarize(_make_paper())

        assert result == "OpenAI summary text"
        mock_openai.OpenAI.assert_called_once_with(api_key="test-key")
        mock_client.chat.completions.create.assert_called_once()
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        assert call_kwargs["model"] == "gpt-4o-mini"
        assert call_kwargs["max_tokens"] == 300

    def test_summarize_unknown_provider(self):
        """Summarize with unknown provider returns unavailable message."""
        config = _make_config("unknown")
        s = Summarizer(config)
        result = s.summarize(_make_paper())
        assert result == "Summary unavailable."

    @patch("agentpaper_reporter.summarizer.anthropic")
    def test_summarize_claude_failure(self, mock_anthropic):
        """Summarize handles Claude API errors gracefully."""
        mock_anthropic.Anthropic.return_value.messages.create.side_effect = Exception(
            "API error"
        )

        s = Summarizer(_make_config("claude"))
        result = s.summarize(_make_paper())

        assert result == "Summary unavailable."

    @patch("agentpaper_reporter.summarizer.openai")
    def test_summarize_openai_failure(self, mock_openai):
        """Summarize handles OpenAI API errors gracefully."""
        mock_openai.OpenAI.return_value.chat.completions.create.side_effect = Exception(
            "API error"
        )

        s = Summarizer(_make_config("openai"))
        result = s.summarize(_make_paper())

        assert result == "Summary unavailable."

    @patch("agentpaper_reporter.summarizer.openai")
    def test_summarize_openrouter_success(self, mock_openai):
        """Summarize with OpenRouter returns summary text via OpenAI-compatible API."""
        mock_choice = MagicMock()
        mock_choice.message.content = "OpenRouter summary text"
        mock_resp = MagicMock()
        mock_resp.choices = [mock_choice]
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_resp
        mock_openai.OpenAI.return_value = mock_client

        s = Summarizer(_make_config("openrouter"))
        result = s.summarize(_make_paper())

        assert result == "OpenRouter summary text"
        mock_openai.OpenAI.assert_called_once_with(
            api_key="test-key",
            base_url="https://openrouter.ai/api/v1",
        )
        mock_client.chat.completions.create.assert_called_once()
        call_kwargs = mock_client.chat.completions.create.call_args[1]
        assert call_kwargs["model"] == "anthropic/claude-sonnet-4"
        assert call_kwargs["max_tokens"] == 300

    @patch("agentpaper_reporter.summarizer.openai")
    def test_summarize_openrouter_failure(self, mock_openai):
        """Summarize handles OpenRouter API errors gracefully."""
        mock_openai.OpenAI.return_value.chat.completions.create.side_effect = Exception(
            "API error"
        )

        s = Summarizer(_make_config("openrouter"))
        result = s.summarize(_make_paper())

        assert result == "Summary unavailable."

    @patch("agentpaper_reporter.summarizer.anthropic")
    @patch("agentpaper_reporter.summarizer.time")
    def test_summarize_papers_multiple(self, mock_time, mock_anthropic):
        """Summarize multiple papers with rate limiting."""
        mock_msg = MagicMock()
        mock_content = MagicMock()
        mock_content.text = "Summary"
        mock_msg.content = [mock_content]
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        s = Summarizer(_make_config("claude"))
        papers = [
            _make_paper(title="Paper 1"),
            _make_paper(title="Paper 2"),
            _make_paper(title="Paper 3"),
        ]
        result = s.summarize_papers(papers)

        assert len(result) == 3
        assert all(p.summary == "Summary" for p in result)
        # Should sleep between papers
        assert mock_time.sleep.call_count == 2

    @patch("agentpaper_reporter.summarizer.anthropic")
    def test_summarize_papers_single(self, mock_anthropic):
        """Summarize single paper does not sleep."""
        mock_msg = MagicMock()
        mock_content = MagicMock()
        mock_content.text = "Summary"
        mock_msg.content = [mock_content]
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        s = Summarizer(_make_config("claude"))
        papers = [_make_paper()]
        result = s.summarize_papers(papers)

        assert len(result) == 1
        assert result[0].summary == "Summary"

    @patch("agentpaper_reporter.summarizer.anthropic")
    def test_summarize_papers_empty(self, mock_anthropic):
        """Summarize empty list returns empty list."""
        s = Summarizer(_make_config("claude"))
        result = s.summarize_papers([])
        assert len(result) == 0

    @patch("agentpaper_reporter.summarizer.anthropic")
    def test_summarize_includes_system_prompt(self, mock_anthropic):
        """Summarize includes system prompt."""
        mock_msg = MagicMock()
        mock_content = MagicMock()
        mock_content.text = "Summary"
        mock_msg.content = [mock_content]
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_msg
        mock_anthropic.Anthropic.return_value = mock_client

        s = Summarizer(_make_config("claude"))
        s.summarize(_make_paper())

        call_kwargs = mock_client.messages.create.call_args[1]
        assert "system" in call_kwargs
        assert "scientific paper summarizer" in call_kwargs["system"]

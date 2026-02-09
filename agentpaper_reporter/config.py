"""Configuration management for agentpaper_reporter."""

import logging
import os
import sys
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field, field_validator


class SearchConfig(BaseModel):
    """Search configuration."""
    keywords: list[str]
    categories: list[str]


class SourceConfig(BaseModel):
    """Individual source configuration."""
    enabled: bool
    max_results: int


class SourcesConfig(BaseModel):
    """Sources configuration."""
    arxiv: SourceConfig
    biorxiv: SourceConfig
    medrxiv: SourceConfig


class LLMConfig(BaseModel):
    """LLM configuration."""
    provider: str = Field(description="LLM provider: 'claude' or 'openai'")
    claude_model: str
    openai_model: str
    max_tokens: int
    anthropic_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None

    @field_validator("provider")
    @classmethod
    def validate_provider(cls, v: str) -> str:
        """Validate LLM provider."""
        if v not in ("claude", "openai"):
            raise ValueError("provider must be 'claude' or 'openai'")
        return v


class ReportConfig(BaseModel):
    """Report generation configuration."""
    output_dir: str
    filename_pattern: str


class DatabaseConfig(BaseModel):
    """Database configuration."""
    path: str


class ScheduleConfig(BaseModel):
    """Schedule configuration."""
    lookback_days: int


class AppConfig(BaseModel):
    """Application configuration."""
    search: SearchConfig
    sources: SourcesConfig
    llm: LLMConfig
    report: ReportConfig
    database: DatabaseConfig
    schedule: ScheduleConfig


def load_config(config_path: Optional[str] = None) -> AppConfig:
    """
    Load configuration from YAML file with environment variable overrides.

    Args:
        config_path: Path to config file. Defaults to "config.yaml" in project root.

    Returns:
        AppConfig: Validated configuration object.

    Raises:
        FileNotFoundError: If config file not found.
        ValueError: If required API key not found for selected provider.
    """
    # Setup logging first
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr
    )
    logger = logging.getLogger(__name__)

    # Determine config path
    if config_path is None:
        # Find project root (directory containing config.yaml)
        project_root = Path(__file__).parent.parent
        config_path = str(project_root / "config.yaml")

    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    # Load YAML
    logger.info(f"Loading configuration from {config_path}")
    with open(config_file, "r") as f:
        config_data = yaml.safe_load(f)

    # Apply environment variable overrides
    llm_provider = os.getenv("LLM_PROVIDER")
    if llm_provider:
        logger.info(f"Overriding LLM provider from env: {llm_provider}")
        config_data["llm"]["provider"] = llm_provider

    lookback_days = os.getenv("LOOKBACK_DAYS")
    if lookback_days:
        logger.info(f"Overriding lookback_days from env: {lookback_days}")
        config_data["schedule"]["lookback_days"] = int(lookback_days)

    # Load API keys from environment
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if anthropic_api_key:
        config_data["llm"]["anthropic_api_key"] = anthropic_api_key
    if openai_api_key:
        config_data["llm"]["openai_api_key"] = openai_api_key

    # Validate configuration
    config = AppConfig(**config_data)

    # Validate API key for selected provider
    if config.llm.provider == "claude" and not config.llm.anthropic_api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable must be set when using Claude"
        )
    if config.llm.provider == "openai" and not config.llm.openai_api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable must be set when using OpenAI"
        )

    logger.info(f"Configuration loaded successfully: provider={config.llm.provider}, "
                f"lookback_days={config.schedule.lookback_days}")

    return config

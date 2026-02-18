"""Configuration management for agentpaper_reporter."""

import logging
import os
import sys
from pathlib import Path
from typing import Optional

import yaml
from dotenv import load_dotenv
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
    provider: str = Field(description="LLM provider: 'claude', 'openai', or 'openrouter'")
    claude_model: str
    openai_model: str
    openrouter_model: str = "anthropic/claude-sonnet-4"
    max_tokens: int
    anthropic_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    openrouter_api_key: Optional[str] = None

    @field_validator("provider")
    @classmethod
    def validate_provider(cls, v: str) -> str:
        """Validate LLM provider."""
        if v not in ("claude", "openai", "openrouter"):
            raise ValueError("provider must be 'claude', 'openai', or 'openrouter'")
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


class EmailConfig(BaseModel):
    """Email notification configuration."""
    enabled: bool = False
    recipients: list[str] = Field(default_factory=list)
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    use_tls: bool = True
    sender_name: str = "AI Paper Reporter"
    subject_pattern: str = "Weekly AI Paper Report - {date}"


class AppConfig(BaseModel):
    """Application configuration."""
    search: SearchConfig
    sources: SourcesConfig
    llm: LLMConfig
    report: ReportConfig
    database: DatabaseConfig
    schedule: ScheduleConfig
    email: EmailConfig = Field(default_factory=EmailConfig)


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
    # Load .env file (does not override existing env vars)
    project_root = Path(__file__).parent.parent
    load_dotenv(project_root / ".env")

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr
    )
    logger = logging.getLogger(__name__)

    # Determine config path
    if config_path is None:
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
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

    if anthropic_api_key:
        config_data["llm"]["anthropic_api_key"] = anthropic_api_key
    if openai_api_key:
        config_data["llm"]["openai_api_key"] = openai_api_key
    if openrouter_api_key:
        config_data["llm"]["openrouter_api_key"] = openrouter_api_key

    # Apply email overrides from environment
    email_enabled = os.getenv("EMAIL_ENABLED")
    if email_enabled:
        config_data.setdefault("email", {})
        config_data["email"]["enabled"] = email_enabled.lower() in ("true", "1", "yes")

    email_recipients = os.getenv("EMAIL_RECIPIENTS")
    if email_recipients:
        config_data.setdefault("email", {})
        config_data["email"]["recipients"] = [
            r.strip() for r in email_recipients.split(",") if r.strip()
        ]

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
    if config.llm.provider == "openrouter" and not config.llm.openrouter_api_key:
        raise ValueError(
            "OPENROUTER_API_KEY environment variable must be set when using OpenRouter"
        )

    logger.info(f"Configuration loaded successfully: provider={config.llm.provider}, "
                f"lookback_days={config.schedule.lookback_days}")

    return config

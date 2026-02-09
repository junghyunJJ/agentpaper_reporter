"""Report generation module for creating markdown reports from paper data."""

import logging
import pathlib
from datetime import datetime, date

from jinja2 import Environment, FileSystemLoader

from agentpaper_reporter.models import ReportData

logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generates markdown reports from paper data using Jinja2 templates."""

    def __init__(self, template_dir: str | None = None):
        """Initialize the report generator.

        Args:
            template_dir: Path to template directory. Defaults to templates/
                         relative to project root.
        """
        if template_dir is None:
            # Default to templates/ relative to project root
            # Project root is parent of agentpaper_reporter package
            package_dir = pathlib.Path(__file__).parent
            project_root = package_dir.parent
            template_dir = str(project_root / "templates")

        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template("report.md.j2")
        logger.debug(f"Initialized ReportGenerator with template_dir: {template_dir}")

    def generate(self, report_data: ReportData) -> str:
        """Generate markdown report from report data.

        Args:
            report_data: The report data to render.

        Returns:
            Rendered markdown string.
        """
        logger.info("Generating report")
        rendered = self.template.render(report=report_data)
        logger.debug(f"Generated report with {len(rendered)} characters")
        return rendered

    def save(
        self,
        content: str,
        output_dir: str,
        filename_pattern: str,
        date: date | None = None,
    ) -> pathlib.Path:
        """Save report content to file.

        Args:
            content: The report content to save.
            output_dir: Directory to save the report in.
            filename_pattern: Filename pattern (use {date} for date substitution).
            date: Date to use in filename. Defaults to today.

        Returns:
            Path object of the saved file.
        """
        if date is None:
            date = datetime.now().date()

        # Create output directory if it doesn't exist
        output_path = pathlib.Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Format filename
        filename = filename_pattern.replace("{date}", str(date))
        file_path = output_path / filename

        # Write content
        file_path.write_text(content, encoding="utf-8")
        logger.info(f"Report saved to {file_path}")

        return file_path

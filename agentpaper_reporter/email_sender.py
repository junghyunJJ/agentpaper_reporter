"""Email notification sender for weekly AI paper reports."""

import logging
import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import markdown

from agentpaper_reporter.config import EmailConfig

logger = logging.getLogger(__name__)

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
  h1 {{ color: #1a1a2e; border-bottom: 2px solid #16213e; padding-bottom: 8px; }}
  h2 {{ color: #16213e; margin-top: 24px; }}
  h3 {{ color: #0f3460; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
  th {{ background-color: #16213e; color: white; }}
  tr:nth-child(even) {{ background-color: #f9f9f9; }}
  a {{ color: #0f3460; }}
  details {{ margin: 8px 0; }}
  summary {{ cursor: pointer; font-weight: bold; }}
  code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
</style>
</head>
<body>
{content}
</body>
</html>
"""


class EmailSender:
    """Sends weekly report as HTML email via SMTP."""

    def __init__(self, config: EmailConfig):
        self.config = config

    def _convert_markdown_to_html(self, md_content: str) -> str:
        """Convert Markdown report to HTML with inline styles."""
        html_body = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code", "toc"],
        )
        return HTML_TEMPLATE.replace("{content}", html_body)

    @staticmethod
    def _get_smtp_credentials() -> tuple[str, str]:
        """Read SMTP credentials from environment variables.

        Returns:
            Tuple of (smtp_user, smtp_password).

        Raises:
            ValueError: If credentials are not set.
        """
        smtp_user = os.getenv("SMTP_USER")
        smtp_password = os.getenv("SMTP_PASSWORD")
        if not smtp_user or not smtp_password:
            raise ValueError(
                "SMTP_USER and SMTP_PASSWORD environment variables must be set"
            )
        return smtp_user, smtp_password

    def send(self, md_content: str, report_date: date) -> bool:
        """Send the report as an HTML email.

        Args:
            md_content: The Markdown report content.
            report_date: The report date (used in subject line).

        Returns:
            True if email sent successfully, False otherwise.
        """
        if not self.config.enabled:
            logger.debug("Email notifications disabled")
            return False

        if not self.config.recipients:
            logger.warning("Email enabled but no recipients configured")
            return False

        try:
            smtp_user, smtp_password = self._get_smtp_credentials()
        except ValueError as e:
            logger.warning(f"Skipping email: {e}")
            return False

        subject = self.config.subject_pattern.format(date=report_date.isoformat())
        html_content = self._convert_markdown_to_html(md_content)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"{self.config.sender_name} <{smtp_user}>"
        msg["To"] = ", ".join(self.config.recipients)

        msg.attach(MIMEText(md_content, "plain"))
        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.config.smtp_host, self.config.smtp_port, timeout=30) as server:
                if self.config.use_tls:
                    server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(smtp_user, self.config.recipients, msg.as_string())
            logger.info(f"Report emailed to {len(self.config.recipients)} recipient(s)")
            return True
        except Exception as e:
            logger.error(f"Failed to send email: {e}", exc_info=True)
            return False

"""Tests for email_sender module."""

import unittest
from datetime import date
from unittest.mock import MagicMock, patch

from agentpaper_reporter.config import EmailConfig
from agentpaper_reporter.email_sender import EmailSender


class TestEmailSender(unittest.TestCase):
    """Tests for EmailSender class."""

    def setUp(self):
        self.config = EmailConfig(
            enabled=True,
            recipients=["test@example.com"],
            smtp_host="smtp.gmail.com",
            smtp_port=587,
            use_tls=True,
        )
        self.sender = EmailSender(self.config)
        self.report_date = date(2026, 2, 16)
        self.md_content = "# Weekly Report\n\n| Col1 | Col2 |\n|---|---|\n| a | b |"

    def test_disabled_returns_false(self):
        """Email disabled in config should return False without sending."""
        self.config.enabled = False
        sender = EmailSender(self.config)
        result = sender.send(self.md_content, self.report_date)
        self.assertFalse(result)

    def test_no_recipients_returns_false(self):
        """Empty recipients list should return False."""
        self.config.recipients = []
        sender = EmailSender(self.config)
        result = sender.send(self.md_content, self.report_date)
        self.assertFalse(result)

    @patch.dict("os.environ", {}, clear=True)
    def test_missing_smtp_credentials_returns_false(self):
        """Missing SMTP credentials should return False."""
        result = self.sender.send(self.md_content, self.report_date)
        self.assertFalse(result)

    @patch("agentpaper_reporter.email_sender.smtplib.SMTP")
    @patch.dict("os.environ", {"SMTP_USER": "user@test.com", "SMTP_PASSWORD": "pass123"})
    def test_successful_send(self, mock_smtp_class):
        """Successful send should call starttls, login, sendmail."""
        mock_server = MagicMock()
        mock_smtp_class.return_value.__enter__ = MagicMock(return_value=mock_server)
        mock_smtp_class.return_value.__exit__ = MagicMock(return_value=False)

        result = self.sender.send(self.md_content, self.report_date)

        self.assertTrue(result)
        mock_smtp_class.assert_called_once_with("smtp.gmail.com", 587, timeout=30)
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with("user@test.com", "pass123")
        mock_server.sendmail.assert_called_once()
        args = mock_server.sendmail.call_args
        self.assertEqual(args[0][0], "user@test.com")
        self.assertEqual(args[0][1], ["test@example.com"])

    @patch("agentpaper_reporter.email_sender.smtplib.SMTP")
    @patch.dict("os.environ", {"SMTP_USER": "user@test.com", "SMTP_PASSWORD": "pass123"})
    def test_smtp_failure_returns_false(self, mock_smtp_class):
        """SMTP failure should return False, not raise."""
        mock_server = MagicMock()
        mock_server.sendmail.side_effect = Exception("Connection refused")
        mock_smtp_class.return_value.__enter__ = MagicMock(return_value=mock_server)
        mock_smtp_class.return_value.__exit__ = MagicMock(return_value=False)

        result = self.sender.send(self.md_content, self.report_date)

        self.assertFalse(result)

    @patch("agentpaper_reporter.email_sender.smtplib.SMTP")
    @patch.dict("os.environ", {"SMTP_USER": "user@test.com", "SMTP_PASSWORD": "pass123"})
    def test_tls_disabled(self, mock_smtp_class):
        """When use_tls=False, starttls should not be called."""
        self.config.use_tls = False
        sender = EmailSender(self.config)

        mock_server = MagicMock()
        mock_smtp_class.return_value.__enter__ = MagicMock(return_value=mock_server)
        mock_smtp_class.return_value.__exit__ = MagicMock(return_value=False)

        result = sender.send(self.md_content, self.report_date)

        self.assertTrue(result)
        mock_server.starttls.assert_not_called()

    def test_markdown_to_html_conversion(self):
        """Markdown content should be converted to HTML with tables and headings."""
        html = self.sender._convert_markdown_to_html(self.md_content)
        self.assertIn("Weekly Report</h1>", html)
        self.assertIn("<table>", html)
        self.assertIn("<th>Col1</th>", html)
        self.assertIn("</html>", html)

    def test_markdown_to_html_bold(self):
        """Bold Markdown should convert to <strong> tags."""
        html = self.sender._convert_markdown_to_html("**bold text**")
        self.assertIn("<strong>bold text</strong>", html)

    @patch("agentpaper_reporter.email_sender.smtplib.SMTP")
    @patch.dict("os.environ", {"SMTP_USER": "user@test.com", "SMTP_PASSWORD": "pass123"})
    def test_subject_contains_date(self, mock_smtp_class):
        """Subject line should contain the formatted report date."""
        mock_server = MagicMock()
        mock_smtp_class.return_value.__enter__ = MagicMock(return_value=mock_server)
        mock_smtp_class.return_value.__exit__ = MagicMock(return_value=False)

        self.sender.send(self.md_content, self.report_date)

        sendmail_args = mock_server.sendmail.call_args[0]
        msg_str = sendmail_args[2]
        self.assertIn("Weekly AI Paper Report - 2026-02-16", msg_str)

    @patch("agentpaper_reporter.email_sender.smtplib.SMTP")
    @patch.dict("os.environ", {"SMTP_USER": "user@test.com", "SMTP_PASSWORD": "pass123"})
    def test_multiple_recipients(self, mock_smtp_class):
        """Multiple recipients should all be included in sendmail."""
        self.config.recipients = ["a@test.com", "b@test.com", "c@test.com"]
        sender = EmailSender(self.config)

        mock_server = MagicMock()
        mock_smtp_class.return_value.__enter__ = MagicMock(return_value=mock_server)
        mock_smtp_class.return_value.__exit__ = MagicMock(return_value=False)

        result = sender.send(self.md_content, self.report_date)

        self.assertTrue(result)
        args = mock_server.sendmail.call_args[0]
        self.assertEqual(args[1], ["a@test.com", "b@test.com", "c@test.com"])


if __name__ == "__main__":
    unittest.main()

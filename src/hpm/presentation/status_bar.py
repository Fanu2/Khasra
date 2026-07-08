"""
Haryana Partition Manager (HPM)

Application status bar.
"""

from __future__ import annotations

from PySide6.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    """
    Main application status bar.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.show_ready()

    def show_ready(
        self,
    ) -> None:
        """
        Display the default message.
        """

        self.showMessage(
            "Ready",
        )

    def show_message(
        self,
        message: str,
    ) -> None:
        """
        Display a custom message.
        """

        self.showMessage(
            message,
        )
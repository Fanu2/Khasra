"""
Haryana Partition Manager (HPM)

Partition Case status bar.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QWidget,
)


class CaseStatusBar(QWidget):
    """
    Status information for the Case Browser.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._build_ui()

    def _build_ui(
        self,
    ) -> None:
        """
        Build the status bar.
        """

        self._case_count = QLabel(
            "Cases: 0",
        )

        self._status = QLabel(
            "Ready",
        )

        layout = QHBoxLayout()

        layout.addWidget(
            self._case_count,
        )

        layout.addStretch()

        layout.addWidget(
            self._status,
        )

        self.setLayout(
            layout,
        )

    def set_case_count(
        self,
        count: int,
    ) -> None:
        """
        Update the displayed case count.
        """

        self._case_count.setText(
            f"Cases: {count}",
        )

    def set_status(
        self,
        message: str,
    ) -> None:
        """
        Update the status message.
        """

        self._status.setText(
            message,
        )

    def show_ready(
        self,
    ) -> None:
        """
        Restore the default status.
        """

        self.set_status(
            "Ready",
        )
"""
Haryana Partition Manager (HPM)

Dashboard widget.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget

from hpm.application.application_context import ApplicationContext


class DashboardWidget(QWidget):
    """
    Initial dashboard.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent: QWidget | None = None,
    ) -> None:

        super().__init__(parent)

        self._context = context

        self._build_ui()

    def _build_ui(self) -> None:
        """
        Build the dashboard.
        """

        title = QLabel(
            self._context.application_name,
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )

        version = QLabel(
            f"Version {self._context.version}",
        )

        version.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )

        status = QLabel(
            "Development Build",
        )

        status.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )

        layout = QVBoxLayout()

        layout.addStretch()

        layout.addWidget(title)

        layout.addWidget(version)

        layout.addWidget(status)

        layout.addStretch()

        self.setLayout(layout)
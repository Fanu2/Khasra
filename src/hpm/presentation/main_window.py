"""
Haryana Partition Manager (HPM)

Main application window.
"""

from __future__ import annotations

from PySide6.QtWidgets import QMainWindow

from hpm.application.application_context import ApplicationContext
from hpm.presentation.dashboard.dashboard_widget import (
    DashboardWidget,
)


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(
        self,
        context: ApplicationContext,
    ) -> None:

        super().__init__()

        self._context = context

        self._initialize()

    def _initialize(
        self,
    ) -> None:
        """
        Initialize the main window.
        """

        self.setWindowTitle(
            self._context.application_name,
        )

        self.resize(
            1400,
            900,
        )

        self.setCentralWidget(
            DashboardWidget(
                self._context,
            ),
        )
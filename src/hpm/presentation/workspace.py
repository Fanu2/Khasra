"""
Haryana Partition Manager (HPM)

Application workspace.
"""

from __future__ import annotations

from PySide6.QtWidgets import QStackedWidget

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.dashboard.dashboard_widget import (
    DashboardWidget,
)


class Workspace(QStackedWidget):
    """
    Main application workspace.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._context = context

        self._dashboard = DashboardWidget(
            self._context,
        )

        self.addWidget(
            self._dashboard,
        )

        self.setCurrentWidget(
            self._dashboard,
        )

    @property
    def dashboard(
        self,
    ) -> DashboardWidget:
        """
        Return the dashboard page.
        """

        return self._dashboard
"""
Haryana Partition Manager (HPM)

Application workspace.
"""

from __future__ import annotations

from PySide6.QtWidgets import QStackedWidget

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.browser.case_browser_page import (
    CaseBrowserPage,
)
from hpm.presentation.dashboard.dashboard_page import (
    DashboardPage,
)


class Workspace(QStackedWidget):
    """
    Main application workspace.

    Owns and manages the application's top-level pages.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:
        """
        Initialize the workspace.
        """

        super().__init__(parent)

        self._context = context

        self._pages: dict[str, int] = {}

        self._register_pages()

    def _register_pages(
        self,
    ) -> None:
        """
        Register application pages.
        """

        self._add_page(
            "Dashboard",
            DashboardPage(
                self._context,
            ),
        )

        self._add_page(
            "Partition Cases",
            CaseBrowserPage(
                self._context,
            ),
        )

    def _add_page(
        self,
        name: str,
        page,
    ) -> None:
        """
        Add a page to the workspace.
        """

        self._pages[name] = self.addWidget(
            page,
        )

    def show_page(
        self,
        name: str,
    ) -> None:
        """
        Display the requested page.
        """

        if name not in self._pages:
            return

        self.setCurrentIndex(
            self._pages[name],
        )
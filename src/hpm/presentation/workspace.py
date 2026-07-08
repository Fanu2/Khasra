"""
Haryana Partition Manager (HPM)

Application workspace.
"""

from __future__ import annotations

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.browser.case_browser_page import (
    CaseBrowserPage,
)
from hpm.presentation.dashboard.dashboard_page import (
    DashboardPage,
)

from PySide6.QtWidgets import QStackedWidget


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
            CaseBrowserPage(),
        )

    def _add_page(
        self,
        name: str,
        page,
    ) -> None:
        """
        Register a page.
        """

        index = self.addWidget(
            page,
        )

        self._pages[name] = index

    def show_page(
        self,
        name: str,
    ) -> None:
        """
        Display a page.
        """

        index = self._pages.get(
            name,
        )

        if index is None:
            return

        self.setCurrentIndex(
            index,
        )
"""
Haryana Partition Manager (HPM)

Partition Case Browser page.
"""

from __future__ import annotations

from PySide6.QtWidgets import QLabel

from hpm.presentation.browser.components.case_search_bar import (
    CaseSearchBar,
)
from hpm.presentation.browser.components.case_status_bar import (
    CaseStatusBar,
)
from hpm.presentation.browser.components.case_table import (
    CaseTable,
)
from hpm.presentation.browser.components.case_tool_bar import (
    CaseToolBar,
)
from hpm.presentation.shared.page import (
    Page,
)


class CaseBrowserPage(Page):
    """
    Partition Case Browser.
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
        Build the page.
        """

        title = QLabel(
            "Partition Cases",
        )

        self._search_bar = CaseSearchBar()

        self._case_table = CaseTable()

        self._tool_bar = CaseToolBar()

        self._status_bar = CaseStatusBar()

        self.layout_container.addWidget(
            title,
        )

        self.layout_container.addWidget(
            self._search_bar,
        )

        self.layout_container.addWidget(
            self._case_table,
            1,
        )

        self.layout_container.addWidget(
            self._tool_bar,
        )

        self.layout_container.addWidget(
            self._status_bar,
        )
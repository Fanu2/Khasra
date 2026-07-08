"""
Haryana Partition Manager (HPM)

Partition Case Browser Page.
"""

from __future__ import annotations

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.browser.case_browser_widget import (
    CaseBrowserWidget,
)
from hpm.presentation.shared.page import (
    Page,
)


class CaseBrowserPage(Page):
    """
    Page hosting the Partition Case browser.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:
        """
        Initialize the page.
        """

        super().__init__(parent)

        self._context = context

        self.layout_container.addWidget(
            CaseBrowserWidget(
                context,
                self,
            )
        )
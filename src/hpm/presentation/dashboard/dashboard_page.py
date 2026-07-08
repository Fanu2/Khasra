"""
Haryana Partition Manager (HPM)

Dashboard page.
"""

from __future__ import annotations

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.dashboard.dashboard_widget import (
    DashboardWidget,
)
from hpm.presentation.shared.page import (
    Page,
)


class DashboardPage(Page):
    """
    Dashboard page.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:

        super().__init__(parent)

        dashboard = DashboardWidget(
            context,
        )

        self.layout_container.addWidget(
            dashboard,
        )
"""
Haryana Partition Manager (HPM)

Case Browser page.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from hpm.presentation.shared.page import Page


class CaseBrowserPage(Page):
    """
    Partition Case Browser.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        title = QLabel(
            "Partition Case Browser\n\nComing Soon",
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter,
        )

        self.layout_container.addStretch()

        self.layout_container.addWidget(
            title,
        )

        self.layout_container.addStretch()
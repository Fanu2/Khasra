"""
Haryana Partition Manager (HPM)

Application navigator.
"""

from __future__ import annotations

from PySide6.QtWidgets import QListWidget
from PySide6.QtWidgets import QListWidgetItem


class Navigator(QListWidget):
    """
    Main application navigator.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setMinimumWidth(220)

        self._build_items()

    def _build_items(
        self,
    ) -> None:
        """
        Build navigation items.
        """

        pages = [
            "Dashboard",
            "Partition Cases",
        ]

        for page in pages:

            self.addItem(
                QListWidgetItem(page),
            )

        self.setCurrentRow(
            0,
        )

    def current_page(
        self,
    ) -> str:
        """
        Return the selected page.
        """

        item = self.currentItem()

        if item is None:
            return ""

        return item.text()
"""
Haryana Partition Manager (HPM)

Partition Case search bar.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QWidget,
)


class CaseSearchBar(QWidget):
    """
    Search bar for partition cases.
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
        Build the search bar.
        """

        label = QLabel(
            "Search:",
        )

        self._search_edit = QLineEdit()

        self._search_edit.setPlaceholderText(
            "Search by case number, village or year..."
        )

        layout = QHBoxLayout()

        layout.addWidget(
            label,
        )

        layout.addWidget(
            self._search_edit,
            1,
        )

        self.setLayout(
            layout,
        )

    @property
    def search_text(
        self,
    ) -> str:
        """
        Return the current search text.
        """

        return self._search_edit.text().strip()

    def clear(
        self,
    ) -> None:
        """
        Clear the search box.
        """

        self._search_edit.clear()
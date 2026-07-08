"""
Haryana Partition Manager (HPM)

Partition Case table.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidget,
)


class CaseTable(QTableWidget):
    """
    Displays partition cases.
    """

    HEADERS = (
        "Case No",
        "Village",
        "Jamabandi",
        "Status",
        "Created",
        "Modified",
    )

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._initialize()

    def _initialize(
        self,
    ) -> None:
        """
        Initialize the table.
        """

        self.setColumnCount(
            len(self.HEADERS),
        )

        self.setHorizontalHeaderLabels(
            self.HEADERS,
        )

        self.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows,
        )

        self.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection,
        )

        self.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers,
        )

        self.setAlternatingRowColors(
            True,
        )

        self.setSortingEnabled(
            False,
        )

        self.verticalHeader().setVisible(
            False,
        )

        header = self.horizontalHeader()

        header.setStretchLastSection(
            True,
        )

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents,
        )

    def clear_cases(
        self,
    ) -> None:
        """
        Remove every displayed case.
        """

        self.setRowCount(
            0,
        )
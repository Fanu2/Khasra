"""
Haryana Partition Manager (HPM)

Partition Case browser widget.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.browser.case_table_model import (
    CaseTableModel,
)


class CaseBrowserWidget(QWidget):
    """
    Browser widget for partition cases.
    """

    def __init__(
        self,
        context: ApplicationContext,
        parent=None,
    ) -> None:
        """
        Initialize the browser widget.
        """

        super().__init__(parent)

        self._context = context

        self._model = CaseTableModel(
            self,
        )

        self._build_ui()

        self._connect_signals()

        self.refresh()

    def _build_ui(
        self,
    ) -> None:
        """
        Build the user interface.
        """

        layout = QVBoxLayout(
            self,
        )

        #
        # Toolbar
        #

        toolbar = QHBoxLayout()

        self.new_button = QPushButton(
            "New",
        )

        self.open_button = QPushButton(
            "Open",
        )

        self.refresh_button = QPushButton(
            "Refresh",
        )

        self.delete_button = QPushButton(
            "Delete",
        )

        toolbar.addWidget(
            self.new_button,
        )

        toolbar.addWidget(
            self.open_button,
        )

        toolbar.addWidget(
            self.refresh_button,
        )

        toolbar.addWidget(
            self.delete_button,
        )

        toolbar.addStretch()

        layout.addLayout(
            toolbar,
        )

        #
        # Table
        #

        self.table = QTableView(
            self,
        )

        self.table.setModel(
            self._model,
        )

        self.table.setSelectionBehavior(
            QTableView.SelectionBehavior.SelectRows,
        )

        self.table.setSelectionMode(
            QTableView.SelectionMode.SingleSelection,
        )

        self.table.setSortingEnabled(
            True,
        )

        self.table.setAlternatingRowColors(
            True,
        )

        self.table.verticalHeader().setVisible(
            False,
        )

        self.table.horizontalHeader().setStretchLastSection(
            True,
        )

        layout.addWidget(
            self.table,
        )

    def _connect_signals(
        self,
    ) -> None:
        """
        Connect widget signals.
        """

        self.refresh_button.clicked.connect(
            self.refresh,
        )

    def refresh(
        self,
    ) -> None:
        """
        Reload partition cases.
        """

        cases = (
            self._context
            .partition_case_service
            .list_cases()
        )

        self._model.set_cases(
            cases,
        )
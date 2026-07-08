"""
Haryana Partition Manager (HPM)

Partition Case toolbar.
"""

from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QWidget


class CaseToolBar(QWidget):
    """
    Toolbar for partition case operations.
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
        Build the toolbar.
        """

        self.new_action = QAction(
            "New",
            self,
        )

        self.open_action = QAction(
            "Open",
            self,
        )

        self.delete_action = QAction(
            "Delete",
            self,
        )

        self.refresh_action = QAction(
            "Refresh",
            self,
        )

        self.open_action.setEnabled(
            False,
        )

        self.delete_action.setEnabled(
            False,
        )

        layout = QHBoxLayout()

        layout.addStretch()

        layout.addWidget(
            self._create_button(
                self.new_action,
            ),
        )

        layout.addWidget(
            self._create_button(
                self.open_action,
            ),
        )

        layout.addWidget(
            self._create_button(
                self.delete_action,
            ),
        )

        layout.addWidget(
            self._create_button(
                self.refresh_action,
            ),
        )

        self.setLayout(
            layout,
        )

    def _create_button(
        self,
        action: QAction,
    ):
        """
        Create a toolbar button.
        """

        from PySide6.QtWidgets import QPushButton

        button = QPushButton(
            action.text(),
        )

        button.clicked.connect(
            action.trigger,
        )

        button.setEnabled(
            action.isEnabled(),
        )

        action.changed.connect(
            lambda: button.setEnabled(
                action.isEnabled(),
            )
        )

        return button
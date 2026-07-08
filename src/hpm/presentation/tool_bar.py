"""
Haryana Partition Manager (HPM)

Application tool bar.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


class ToolBar(QToolBar):
    """
    Main application toolbar.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__("Main Toolbar", parent)

        self.setMovable(False)

        self.setFloatable(False)

        self.setToolButtonStyle(
            Qt.ToolButtonTextUnderIcon,
        )

        self._build_actions()

    def _build_actions(
        self,
    ) -> None:
        """
        Build toolbar actions.
        """

        refresh_action = QAction(
            "Refresh",
            self,
        )

        refresh_action.setEnabled(
            False,
        )

        settings_action = QAction(
            "Settings",
            self,
        )

        settings_action.setEnabled(
            False,
        )

        about_action = QAction(
            "About",
            self,
        )

        about_action.setEnabled(
            False,
        )

        self.addAction(
            refresh_action,
        )

        self.addSeparator()

        self.addAction(
            settings_action,
        )

        self.addSeparator()

        self.addAction(
            about_action,
        )
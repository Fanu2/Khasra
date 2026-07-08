"""
Haryana Partition Manager (HPM)

Application menu bar.
"""

from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar


class MenuBar(QMenuBar):
    """
    Main application menu bar.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._build_menu()

    def _build_menu(
        self,
    ) -> None:
        """
        Build the application menu.
        """

        #
        # File
        #

        file_menu = self.addMenu(
            "&File",
        )

        exit_action = QAction(
            "E&xit",
            self,
        )

        file_menu.addAction(
            exit_action,
        )

        #
        # View
        #

        self.addMenu(
            "&View",
        )

        #
        # Help
        #

        self.addMenu(
            "&Help",
        )
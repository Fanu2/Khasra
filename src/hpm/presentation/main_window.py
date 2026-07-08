"""
Haryana Partition Manager (HPM)

Main application window.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QSplitter

from hpm.application.application_context import (
    ApplicationContext,
)
from hpm.presentation.menu_bar import (
    MenuBar,
)
from hpm.presentation.navigator import (
    Navigator,
)
from hpm.presentation.status_bar import (
    StatusBar,
)
from hpm.presentation.tool_bar import (
    ToolBar,
)
from hpm.presentation.workspace import (
    Workspace,
)


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(
        self,
        context: ApplicationContext,
    ) -> None:

        super().__init__()

        self._context = context

        self._initialize()

    def _initialize(
        self,
    ) -> None:
        """
        Initialize the application window.
        """

        self.setWindowTitle(
            self._context.application_name,
        )

        self.resize(
            1400,
            900,
        )

        #
        # Menu Bar
        #

        self._menu_bar = MenuBar(
            self,
        )

        self.setMenuBar(
            self._menu_bar,
        )

        #
        # Tool Bar
        #

        self._tool_bar = ToolBar(
            self,
        )

        self.addToolBar(
            self._tool_bar,
        )

        #
        # Status Bar
        #

        self._status_bar = StatusBar(
            self,
        )

        self.setStatusBar(
            self._status_bar,
        )

        #
        # Navigator
        #

        self._navigator = Navigator(
            self,
        )

        #
        # Workspace
        #

        self._workspace = Workspace(
            self._context,
            self,
        )

        #
        # Splitter
        #

        splitter = QSplitter(
            Qt.Orientation.Horizontal,
        )

        splitter.addWidget(
            self._navigator,
        )

        splitter.addWidget(
            self._workspace,
        )

        splitter.setStretchFactor(
            0,
            0,
        )

        splitter.setStretchFactor(
            1,
            1,
        )

        splitter.setSizes(
            [
                240,
                1160,
            ]
        )

        #
        # Connect Signals
        #

        self._connect_signals()

        #
        # Central Widget
        #

        self.setCentralWidget(
            splitter,
        )

        self.setCentralWidget(
            splitter,
        )

    def _connect_signals(
        self,
    ) -> None:
        """
        Connect application signals.
        """

        self._navigator.currentTextChanged.connect(
            self._workspace.show_page,
        )
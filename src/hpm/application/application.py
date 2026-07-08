"""
Haryana Partition Manager (HPM)

Application bootstrap.
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from hpm.application.application_context import ApplicationContext
from hpm.presentation.main_window import MainWindow


class Application:
    """
    Main application.
    """

    def __init__(self) -> None:

        self._qt = QApplication(sys.argv)

        self._context = ApplicationContext()

        self._window = MainWindow(
            self._context,
        )

    def run(self) -> int:
        """
        Start the application.
        """

        self._window.show()

        return self._qt.exec()
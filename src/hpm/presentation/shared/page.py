"""
Haryana Partition Manager (HPM)

Base page class.
"""

from __future__ import annotations

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Page(QWidget):
    """
    Base class for every application page.
    """

    def __init__(
        self,
        parent: QWidget | None = None,
    ) -> None:

        super().__init__(parent)

        self._layout = QVBoxLayout()

        self.setLayout(
            self._layout,
        )

    @property
    def layout_container(
        self,
    ) -> QVBoxLayout:
        """
        Return the page layout.
        """

        return self._layout

    def on_enter(
        self,
    ) -> None:
        """
        Called when the page becomes active.
        """

        pass

    def on_leave(
        self,
    ) -> None:
        """
        Called when the page is hidden.
        """

        pass

    def refresh(
        self,
    ) -> None:
        """
        Refresh page contents.
        """

        pass

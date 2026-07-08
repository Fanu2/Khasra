"""
Haryana Partition Manager (HPM)

Case creation wizard.
"""

from __future__ import annotations

from PySide6.QtWidgets import QWizard

from hpm.presentation.cases.wizard.general_page import GeneralPage
from hpm.presentation.cases.wizard.village_page import VillagePage
from hpm.presentation.cases.wizard.jamabandi_page import JamabandiPage
from hpm.presentation.cases.wizard.summary_page import SummaryPage


class CaseWizard(QWizard):
    """
    Wizard used to create a new partition case.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setWindowTitle(
            "New Partition Case",
        )

        self.resize(
            800,
            600,
        )

        self.addPage(
            GeneralPage(),
        )

        self.addPage(
            VillagePage(),
        )

        self.addPage(
            JamabandiPage(),
        )

        self.addPage(
            SummaryPage(),
        )
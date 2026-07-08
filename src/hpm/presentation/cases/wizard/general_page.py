"""
Haryana Partition Manager (HPM)

General information page.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QDateEdit,
    QFormLayout,
    QLineEdit,
    QWizardPage,
)

from PySide6.QtCore import QDate


class GeneralPage(QWizardPage):
    """
    General partition case information.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setTitle(
            "General Information",
        )

        self.setSubTitle(
            "Enter the basic information for the partition case.",
        )

        self._build_ui()

    def _build_ui(
        self,
    ) -> None:

        self.case_number = QLineEdit()

        self.case_type = QComboBox()

        self.case_type.addItems(
            [
                "General",
                "Court Ordered",
                "Appeal",
            ]
        )

        self.order_number = QLineEdit()

        self.order_date = QDateEdit()

        self.order_date.setCalendarPopup(
            True,
        )

        self.order_date.setDate(
            QDate.currentDate(),
        )

        self.revenue_officer = QLineEdit()

        layout = QFormLayout()

        layout.addRow(
            "Case Number",
            self.case_number,
        )

        layout.addRow(
            "Case Type",
            self.case_type,
        )

        layout.addRow(
            "Order Number",
            self.order_number,
        )

        layout.addRow(
            "Order Date",
            self.order_date,
        )

        layout.addRow(
            "Revenue Officer",
            self.revenue_officer,
        )

        self.setLayout(
            layout,
        )

        self.registerField(
            "case_number*",
            self.case_number,
        )

        self.registerField(
            "case_type",
            self.case_type,
            "currentText",
        )

        self.registerField(
            "order_number*",
            self.order_number,
        )

        self.registerField(
            "revenue_officer*",
            self.revenue_officer,
        )
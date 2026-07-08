"""
Haryana Partition Manager (HPM)

Qt table model for partition cases.
"""

from __future__ import annotations

from PySide6.QtCore import QAbstractTableModel
from PySide6.QtCore import QModelIndex
from PySide6.QtCore import Qt

from hpm.domain.entities.partition_case import PartitionCase


class CaseTableModel(QAbstractTableModel):
    """
    Qt model for displaying partition cases.
    """

    HEADERS = (
        "Case Number",
        "Type",
        "Village",
        "Status",
        "Order Date",
    )

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._cases: list[PartitionCase] = []

    def set_cases(
        self,
        cases: list[PartitionCase],
    ) -> None:
        """
        Replace the current data.
        """

        self.beginResetModel()

        self._cases = list(cases)

        self.endResetModel()

    def rowCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self._cases)

    def columnCount(
        self,
        parent: QModelIndex = QModelIndex(),
    ) -> int:

        return len(self.HEADERS)

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):

        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
        ):
            return self.HEADERS[section]

        return None

    def data(
        self,
        index: QModelIndex,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):

        if (
            not index.isValid()
            or role != Qt.ItemDataRole.DisplayRole
        ):
            return None

        case = self._cases[index.row()]

        match index.column():

            case 0:
                return case.case_number

            case 1:
                return case.case_type

            case 2:
                return case.village_name

            case 3:
                return case.status

            case 4:
                return case.order_date.isoformat()

        return None

    @property
    def cases(
        self,
    ) -> list[PartitionCase]:
        """
        Return the loaded cases.
        """

        return self._cases
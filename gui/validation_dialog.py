from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QLabel,
    QHeaderView
)

from PySide6.QtGui import QColor
from PySide6.QtCore import Qt


class ValidationDialog(QDialog):

    def __init__(self, results, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Allocation Validation Report")
        self.resize(950, 550)

        layout = QVBoxLayout(self)

        title = QLabel("Partition Allocation Validation")
        title.setStyleSheet(
            "font-size:18px;"
            "font-weight:bold;"
        )
        layout.addWidget(title)

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Owner",
            "Share",
            "Required Area",
            "Allocated Area",
            "Difference",
            "Status"
        ])

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )

        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(False)

        self.table.setRowCount(len(results))

        total_required = 0
        total_allocated = 0

        ok_count = 0
        short_count = 0
        excess_count = 0

        for row, item in enumerate(results):

            total_required += item["required_area"]
            total_allocated += item["allocated_area"]

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(item["owner_name"])
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(item["share"])
            )

            required_item = QTableWidgetItem(
                f'{item["required_area"]:.2f}'
            )
            required_item.setTextAlignment(Qt.AlignCenter)

            allocated_item = QTableWidgetItem(
                f'{item["allocated_area"]:.2f}'
            )
            allocated_item.setTextAlignment(Qt.AlignCenter)

            difference = item["difference"]

            if difference > 0:
                diff_text = f"+{difference:.2f}"
            else:
                diff_text = f"{difference:.2f}"

            difference_item = QTableWidgetItem(diff_text)
            difference_item.setTextAlignment(Qt.AlignCenter)

            status_item = QTableWidgetItem(item["status"])
            status_item.setTextAlignment(Qt.AlignCenter)

            if item["status"] == "OK":

                status_item.setBackground(
                    QColor("#C8E6C9")
                )

                ok_count += 1

            elif item["status"] == "SHORT":

                status_item.setBackground(
                    QColor("#FFF9C4")
                )

                short_count += 1

            else:

                status_item.setBackground(
                    QColor("#FFCDD2")
                )

                excess_count += 1

            self.table.setItem(row, 2, required_item)
            self.table.setItem(row, 3, allocated_item)
            self.table.setItem(row, 4, difference_item)
            self.table.setItem(row, 5, status_item)

        self.table.resizeColumnsToContents()

        layout.addWidget(self.table)

        summary = QLabel(
            f"Total Required Area : {total_required:.2f}    "
            f"Allocated Area : {total_allocated:.2f}    "
            f"OK : {ok_count}    "
            f"SHORT : {short_count}    "
            f"EXCESS : {excess_count}"
        )

        summary.setStyleSheet(
            "font-weight:bold;"
            "padding:6px;"
        )

        layout.addWidget(summary)

        buttons = QHBoxLayout()

        buttons.addStretch()

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)

        buttons.addWidget(close_button)

        layout.addLayout(buttons)
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem
)


class OwnershipHistoryDialog(QDialog):

    def __init__(
        self,
        history_rows,
        parent=None
    ):

        super().__init__(parent)

        self.setWindowTitle(
            "Ownership History"
        )

        self.resize(
            900,
            500
        )

        layout = QVBoxLayout()

        self.table = QTableWidget()

        self.table.setColumnCount(4)

        self.table.setHorizontalHeaderLabels(
            [
                "Date",
                "Owner",
                "Old Share",
                "New Share"
            ]
        )

        self.table.setRowCount(
            len(history_rows)
        )

        for row, h in enumerate(
            history_rows
        ):

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    h.changed_on.strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    h.owner_name
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    h.old_share
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    h.new_share
                )
            )

        layout.addWidget(
            self.table
        )

        self.setLayout(
            layout
        )
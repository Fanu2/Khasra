from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QCheckBox
)


class OwnerMatrixDialog(QDialog):

    def __init__(
        self,
        matrix,
        parent=None
    ):

        super().__init__(parent)

        self.matrix = matrix

        self.setWindowTitle(
            "Owner Matrix"
        )

        self.resize(
            1000,
            600
        )

        layout = QVBoxLayout()

        # -----------------
        # FILTER BAR
        # -----------------

        filter_bar = QHBoxLayout()

        self.chk_hide_rows = QCheckBox(
            "Hide Empty Rows"
        )

        self.chk_hide_cols = QCheckBox(
            "Hide Empty Columns"
        )

        filter_bar.addWidget(
            self.chk_hide_rows
        )

        filter_bar.addWidget(
            self.chk_hide_cols
        )

        layout.addLayout(
            filter_bar
        )

        self.chk_hide_rows.stateChanged.connect(
            self.refresh_matrix
        )

        self.chk_hide_cols.stateChanged.connect(
            self.refresh_matrix
        )

        # -----------------
        # TABLE
        # -----------------

        self.table = QTableWidget()

        owners = sorted(
            self.matrix.keys()
        )

        khewats = set()

        for data in self.matrix.values():

            for khewat in data.keys():

                khewats.add(
                    str(khewat)
                )

        khewats = sorted(
            list(khewats)
        )

        self.table.setRowCount(
            len(owners)
        )

        self.table.setColumnCount(
            len(khewats)
        )

        self.table.setVerticalHeaderLabels(
            owners
        )

        self.table.setHorizontalHeaderLabels(
            khewats
        )

        for row, owner in enumerate(
            owners
        ):

            for col, khewat in enumerate(
                khewats
            ):

                value = (
                    self.matrix
                    .get(owner, {})
                    .get(khewat, "")
                )

                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem(value)
                )

        self.table.resizeColumnsToContents()

        layout.addWidget(
            self.table
        )

        self.setLayout(
            layout
        )

    def refresh_matrix(self):

        print(
            "Rows:",
            self.chk_hide_rows.isChecked()
        )

        print(
            "Cols:",
            self.chk_hide_cols.isChecked()
        )
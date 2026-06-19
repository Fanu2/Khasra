from fractions import Fraction

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHBoxLayout
)

from database.db import SessionLocal

from database.models import (
    Owner,
    Ownership
)

from services.area_service import (
    AreaService
)


class OwnerLedgerDialog(QDialog):

    def __init__(
        self,
        owner_id,
        parent=None
    ):

        super().__init__(parent)

        self.owner_id = owner_id
        self.session = SessionLocal()

        self.setWindowTitle(
            "Owner Ledger"
        )

        self.resize(
            900,
            600
        )

        self.build_ui()

        self.load_data()

    def build_ui(self):

        layout = QVBoxLayout()

        self.lbl_owner = QLabel()

        layout.addWidget(
            self.lbl_owner
        )

        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels(
            [
                "Khewat",
                "Share",
                "Share %",
                "Area (Marlas)",
                "Area (K-M-S)"
            ]
        )

        layout.addWidget(
            self.table
        )

        self.lbl_total = QLabel()

        layout.addWidget(
            self.lbl_total
        )

        btn_bar = QHBoxLayout()

        self.btn_close = QPushButton(
            "Close"
        )

        btn_bar.addStretch()

        btn_bar.addWidget(
            self.btn_close
        )

        layout.addLayout(
            btn_bar
        )

        self.setLayout(
            layout
        )

        self.btn_close.clicked.connect(
            self.close
        )

    def load_data(self):

        owner = self.session.get(
            Owner,
            self.owner_id
        )

        if not owner:

            self.lbl_owner.setText(
                "Owner not found"
            )

            return

        self.lbl_owner.setText(
            f"Owner : {owner.owner_name}"
        )

        ownerships = (
            self.session.query(
                Ownership
            )
            .filter(
                Ownership.owner_id
                == self.owner_id
            )
            .all()
        )

        self.table.setRowCount(
            len(ownerships)
        )

        total_area = 0

        for row, own in enumerate(
            ownerships
        ):

            share = Fraction(
                own.numerator,
                own.denominator
            )

            pct = (
                float(share)
                * 100
            )

            area = (
                float(
                    own.khewat.total_area
                )
                * float(share)
            )

            total_area += area

            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(
                        own.khewat.khewat_no
                    )
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(share)
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    f"{pct:.2f}"
                )
            )

            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    f"{area:.2f}"
                )
            )

            self.table.setItem(
                row,
                4,
                QTableWidgetItem(
                    AreaService.format_area(
                        area
                    )
                )
            )

        self.table.resizeColumnsToContents()

        self.lbl_total.setText(
            f"Total Area : "
            f"{total_area:.2f} Marla"
            f"    "
            f"({AreaService.format_area(total_area)})"
        )

    def closeEvent(
        self,
        event
    ):

        try:
            self.session.close()
        except:
            pass

        event.accept()
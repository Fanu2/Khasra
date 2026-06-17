from fractions import Fraction

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QMessageBox
)

from database.db import SessionLocal

from database.models import (
    Khewat
)

from services.area_service import (
    AreaService
)


class KhewatWorkbench(QWidget):

    def __init__(self):

        super().__init__()

        self.session = SessionLocal()

        self.setWindowTitle(
            "Khewat Workbench"
        )

        self.resize(
            1200,
            800
        )

        self.build_ui()

        self.load_khewats()

    # =====================================
    # UI
    # =====================================

    def build_ui(self):

        layout = QVBoxLayout()

        top = QHBoxLayout()

        top.addWidget(
            QLabel("Select Khewat")
        )

        self.cmb_khewat = QComboBox()

        top.addWidget(
            self.cmb_khewat
        )

        self.btn_load = QPushButton(
            "Load"
        )

        top.addWidget(
            self.btn_load
        )

        layout.addLayout(top)

        # -----------------------------
        # Summary
        # -----------------------------

        self.summary = QTextEdit()

        self.summary.setReadOnly(
            True
        )

        layout.addWidget(
            self.summary
        )

        # -----------------------------
        # Ownership Table
        # -----------------------------

        layout.addWidget(
            QLabel("Ownership")
        )

        self.owner_table = QTableWidget()

        self.owner_table.setColumnCount(5)

        self.owner_table.setHorizontalHeaderLabels(
            [
                "Owner",
                "Share",
                "Share %",
                "Area Share",
                "Owner ID"
            ]
        )
        self.owner_table.setColumnHidden(
            4,
            True
        )
        layout.addWidget(
            self.owner_table
        )

        # -----------------------------
        # Khasra Table
        # -----------------------------

        layout.addWidget(
            QLabel("Khasras")
        )

        self.khasra_table = QTableWidget()

        self.khasra_table.setColumnCount(2)

        self.khasra_table.setHorizontalHeaderLabels(
            [
                "Khasra No",
                "Area"
            ]
        )

        layout.addWidget(
            self.khasra_table
        )

        # -----------------------------
        # Validation
        # -----------------------------

        self.lbl_validation = QLabel(
            ""
        )

        layout.addWidget(
            self.lbl_validation
        )

        self.setLayout(layout)

        self.btn_load.clicked.connect(
            self.load_selected_khewat
        )

    # =====================================
    # LOAD LIST
    # =====================================

    def load_khewats(self):

        self.cmb_khewat.clear()

        khewats = (
            self.session.query(Khewat)
            .order_by(
                Khewat.khewat_no
            )
            .all()
        )

        for k in khewats:

            self.cmb_khewat.addItem(
                str(k.khewat_no),
                k.id
            )

    # =====================================
    # LOAD KHEWAT
    # =====================================

    def load_selected_khewat(self):

        try:

            khewat_id = (
                self.cmb_khewat.currentData()
            )

            if not khewat_id:
                return

            khewat = (
                self.session.query(Khewat)
                .filter(
                    Khewat.id == khewat_id
                )
                .first()
            )

            if not khewat:
                return

            self.load_summary(
                khewat
            )

            self.load_owners(
                khewat
            )

            self.load_khasras(
                khewat
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Workbench Error",
                str(e)
            )

    # =====================================
    # SUMMARY
    # =====================================

    def load_summary(self, khewat):

        lines = []

        lines.append(
            "KHEWAT WORKBENCH"
        )

        lines.append("")

        lines.append(
            f"Village : {khewat.village.village_name}"
        )

        lines.append(
           f"Khewat No : {khewat.khewat_no}"
        )

        lines.append(
            f"Khatauni No : {khewat.khatauni_no}"
        )

        lines.append(
            f"Area : "
            f"{AreaService.format_area(khewat.total_area)}"
        )

        lines.append(
            f"Owners : "
            f"{len(khewat.ownerships)}"
        )

        lines.append(
            f"Khasras : "
            f"{len(khewat.khasras)}"
        )

        self.summary.setText(
            "\n".join(lines)
        )

    # =====================================
    # OWNERS
    # =====================================

    def load_owners(self, khewat):

        ownerships = khewat.ownerships

        self.owner_table.setRowCount(
            len(ownerships)
        )

        total_share = Fraction(
            0,
            1
          
        )
        named_owner_area = 0
        for row, own in enumerate(
            ownerships
        ):

            share = Fraction(
                own.numerator,
                own.denominator
            )

            total_share += share

            pct = (
                float(share)
                * 100
            )

            area_share = (
                float(khewat.total_area)
                * float(share)
                
            )
            named_owner_area += area_share
            self.owner_table.setItem(
                row,
                0,
                QTableWidgetItem(
                    own.owner.owner_name
                )
            )

            self.owner_table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(share)
                )
            )

            self.owner_table.setItem(
                row,
                2,
                QTableWidgetItem(
                    f"{pct:.2f}"
                )
            )

            self.owner_table.setItem(
                row,
                3,
                QTableWidgetItem(
                    AreaService.format_area(
                        area_share
                    )
                )
            )

            self.owner_table.setItem(
                row,
                4,
                QTableWidgetItem(
                    str(
                        own.owner.id
                    )
                )
            )
            others_area = (
                float(khewat.total_area)
                - named_owner_area
            )

            self.summary.append("")

            self.summary.append(
                f"Named Owners Area : "
                f"{AreaService.format_area(named_owner_area)}"
        )

            self.summary.append(
                f"Others Area : "
                f"{AreaService.format_area(others_area)}"
        )

            self.summary.append(
               f"Grand Total : "
               f"{AreaService.format_area(khewat.total_area)}"
               )
            
        if total_share == Fraction(1, 1):

            self.lbl_validation.setText(
                "✓ VALID OWNERSHIP (100%)"
            )

        else:

            self.lbl_validation.setText(
                f"⚠ SHARE MISMATCH ({total_share})"
            )

    # =====================================
    # KHASRAS
    # =====================================

    def load_khasras(self, khewat):

        khasras = khewat.khasras

        self.khasra_table.setRowCount(
            len(khasras)
        )

        for row, khasra in enumerate(
            khasras
        ):

            self.khasra_table.setItem(
                row,
                0,
                QTableWidgetItem(
                    khasra.khasra_no
                )
            )

            self.khasra_table.setItem(
                row,
                1,
                QTableWidgetItem(
                    AreaService.format_area(
                        khasra.area
                    )
                )
            )

    # =====================================
    # CLOSE
    # =====================================

    def closeEvent(self, event):

        try:
            self.session.close()
        except:
            pass

        event.accept()
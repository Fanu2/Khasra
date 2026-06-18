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
    QMessageBox,
    QAbstractItemView
)

from database.db import SessionLocal

from database.models import (
    Khewat,
    Ownership,
    Khasra,
    Owner,
    OwnershipHistory  
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

        self.btn_edit = QPushButton(
            "Edit Ownership"
        )

        top.addWidget(
            self.btn_edit
        )

        self.btn_save = QPushButton(
        "Save Ownership"
        )

        self.btn_save.setEnabled(False)

        top.addWidget(
        self.btn_save
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
        self.btn_edit.clicked.connect(
            self.enable_editing
        )

        self.btn_save.clicked.connect(
            self.save_ownerships
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
            self.current_khewat = khewat
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
        self.original_shares = {}
        for row, own in enumerate(
            ownerships
        ):

            share = Fraction(
                own.numerator,
                own.denominator
            )
            self.original_shares[
            own.owner.id
            ] = str(share)
            
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
    def enable_editing(self):

            QMessageBox.information(
                self,
                "Edit Mode",
                "Ownership editing enabled."
            )

            self.btn_save.setEnabled(
            True
        )
    def get_changed_rows(self):

        changes = []

        rows = self.owner_table.rowCount()

        for row in range(rows):

            owner = self.owner_table.item(
                row,
                0
            ).text()

            share = self.owner_table.item(
                row,
                1
            ).text()

            changes.append(
                (
                  owner,
                  share
                )
            )

        return changes        
    
    def persist_ownership_changes(self):

        ownerships = self.current_khewat.ownerships

        rows = self.owner_table.rowCount()

        for row in range(rows):

            share_text = (
                self.owner_table.item(
                    row,
                    1
                ).text().strip()
            )

            if "/" in share_text:

                num, den = share_text.split("/")

            else:

                num = share_text
                den = "1"

            old_share = (
                f"{ownerships[row].numerator}/"
                f"{ownerships[row].denominator}"
            )

            new_share = (
                f"{num}/{den}"
            )

            print(
                "COMPARE:",
                old_share,
                "vs",
                new_share
            )

            if old_share != new_share:

                print(
                    "HISTORY RECORD CREATED"
                )

                history = OwnershipHistory(

                    khewat_id=
                    self.current_khewat.id,

                    owner_id=
                    ownerships[row].owner.id,

                    owner_name=
                    ownerships[row].owner.owner_name,

                    old_share=
                    old_share,

                    new_share=
                    new_share,

                    remarks=
                    "Ownership edited in Workbench"
                )

                self.session.add(history)

            ownerships[row].numerator = int(num)
            ownerships[row].denominator = int(den)

        print("COMMITTING...")
        self.session.commit()
    
    def save_ownerships(self):

        total = self.validate_shares()

        if total is None:
         return

        if total != Fraction(1, 1):

            QMessageBox.warning(
                self,
                "Invalid Ownership",
                f"Total ownership is "
                f"{float(total)*100:.4f}%\n\n"
                f"Ownership must equal 100%."
            )

            return

        rows = self.get_changed_rows()

        msg = ""

        for owner, share in rows:

            msg += (
                f"{owner}"
                f" : "
                f"{share}\n"
            )

        reply = QMessageBox.question(
        self,
        "Confirm Ownership Update",
        msg + "\n\nSave these changes?",
        QMessageBox.Yes |
        QMessageBox.No
    )

        if reply != QMessageBox.Yes:
            return

        self.persist_ownership_changes()

        QMessageBox.information(
            self,
            "Saved",
            "Ownership changes saved."
        )

        self.load_selected_khewat()

    def validate_shares(self):

        total = Fraction(0, 1)

        rows = self.owner_table.rowCount()

        try:

            for row in range(rows):

                share_text = (
                    self.owner_table.item(
                       row,
                      1
                    ).text().strip()
                )

                if "/" in share_text:

                    num, den = share_text.split("/")

                    total += Fraction(
                        int(num),
                        int(den)
                    )

                else:

                    total += Fraction(
                        int(share_text),
                        1
                    )

            return total

        except Exception as e:

            QMessageBox.critical(
                self,
            "Validation Error",
            str(e)
        )

            return None
    # =====================================
    # CLOSE
    # =====================================

    def closeEvent(self, event):

        try:
            self.session.close()
        except:
            pass

        event.accept()
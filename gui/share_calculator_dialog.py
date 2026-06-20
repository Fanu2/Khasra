from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
    QTableWidget,
    QTableWidgetItem
)
from fractions import Fraction

class ShareCalculatorDialog(QDialog):

    def __init__(
        self,
        parent=None
    ):

        super().__init__(parent)

        self.setWindowTitle(
            "Share Calculator"
        )

        self.resize(
            900,
            600
        )

        layout = QVBoxLayout()

        # -------------------------
        # Area Section
        # -------------------------

        area_row = QHBoxLayout()

        area_row.addWidget(
            QLabel("Khewat No")
        )

        self.txt_khewat = QLineEdit()

        area_row.addWidget(
            self.txt_khewat
        )

        area_row.addWidget(
            QLabel("Kanal")
        )

        self.txt_kanal = QLineEdit()

        area_row.addWidget(
            self.txt_kanal
        )

        area_row.addWidget(
            QLabel("Marla")
        )

        self.txt_marla = QLineEdit()

        area_row.addWidget(
            self.txt_marla
        )

        layout.addLayout(
            area_row
        )

        # -------------------------
        # Owner Grid
        # -------------------------

        self.owners_widget = QWidget()

        self.owners_layout = QGridLayout()

        self.owners_widget.setLayout(
            self.owners_layout
        )

        self.owner_rows = []

        self.owners_layout.addWidget(
            QLabel("Owner Name"),
            0,
            0
        )

        self.owners_layout.addWidget(
            QLabel("Share"),
            0,
            1
        )

        self.owners_layout.addWidget(
            QLabel("Remarks"),
            0,
            2
        )

        layout.addWidget(
            self.owners_widget
        )

        # -------------------------
        # Buttons
        # -------------------------

        self.btn_add_owner = QPushButton(
            "Add Owner"
        )

        self.btn_calculate = QPushButton(
            "Calculate"
        )

        self.btn_add_owner.clicked.connect(
            self.add_owner_row
        )
        self.btn_calculate.clicked.connect(
            self.calculate_shares
        )

        layout.addWidget(
            self.btn_add_owner
        )

        layout.addWidget(
            self.btn_calculate
        )
        self.results_table = QTableWidget()
        
        self.results_table.setRowCount(
                0
        )
        self.results_table.setColumnCount(
                4
        )

        self.results_table.setHorizontalHeaderLabels(
            [
                "Owner",
                "Share",
                "Area",
                "Remarks"
            ]
        )

        layout.addWidget(
        self.results_table
        )
        self.lbl_total_area = QLabel(
            "Combined Area : 0K-0M-0S"
        )

        layout.addWidget(
            self.lbl_total_area
        )

        self.setLayout(
            layout
        )

        # First row automatically

        self.add_owner_row()
    
    def calculate_shares(self):

        try:

            kanal = int(
                self.txt_kanal.text() or 0
            )

            marla = int(
                self.txt_marla.text() or 0
            )

            total_marla = (
                kanal * 20
                + marla
            )

            self.results_table.setRowCount(
                0
            )

            row_no = 0
            
            total_owner_marla = 0
            
            for (
                txt_owner,
                txt_share,
                txt_remarks
            ) in self.owner_rows:

                owner = (
                    txt_owner.text().strip()
                )

                share_text = (
                    txt_share.text().strip()
                )

                remarks = (
                    txt_remarks.text().strip()
                )

                if not owner:
                    continue

                if not share_text:
                    continue

                try:

                    share = Fraction(
                        share_text
                )

                except Exception:

                    print(
                        "Invalid Share:",
                        share_text
                )

                    continue    

                owner_marla = (
                    float(share)
                    * total_marla
                )
                
                total_owner_marla += (
                    owner_marla
                )

                area_text = self.marla_to_kms(
                    owner_marla
                )

                self.results_table.insertRow(
                    row_no
                )

                self.results_table.setItem(
                    row_no,
                    0,
                    QTableWidgetItem(
                        owner
                    )
                )

                self.results_table.setItem(
                    row_no,
                    1,
                    QTableWidgetItem(
                        share_text
                    )
                )

                self.results_table.setItem(
                    row_no,
                    2,
                    QTableWidgetItem(
                        area_text
                    )
                )

                self.results_table.setItem(
                    row_no,
                    3,
                    QTableWidgetItem(
                        remarks
                    )
                )
            
                row_no += 1
            combined_area = (
                self.marla_to_kms
                    (total_owner_marla)
            )

            self.lbl_total_area.setText(
                f"Combined Area : {combined_area}"
        )

        except Exception as e:

            print(e)
    
    def marla_to_kms(
        self,
        marlas
    ):

        kanal = int(
            marlas // 20
        )

        rem_marla = (
            marlas
            - kanal * 20
        )

        whole_marla = int(
            rem_marla
        )

        sarsahi = round(
            (rem_marla - whole_marla)
            * 9
        )

        return (
            f"{kanal}K-"
            f"{whole_marla}M-"
            f"{sarsahi}S"
        )

    def add_owner_row(self):

        row = (
            len(self.owner_rows)
            + 1
        )

        txt_owner = QLineEdit()

        txt_share = QLineEdit()

        txt_remarks = QLineEdit()

        self.owners_layout.addWidget(
            txt_owner,
            row,
            0
        )

        self.owners_layout.addWidget(
            txt_share,
            row,
            1
        )

        self.owners_layout.addWidget(
            txt_remarks,
            row,
            2
        )

        self.owner_rows.append(
            (
                txt_owner,
                txt_share,
                txt_remarks
            )
        )
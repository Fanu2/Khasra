from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)


class AreaCalculatorDialog(QDialog):

    def __init__(
        self,
        parent=None
    ):

        super().__init__(parent)

        self.setWindowTitle(
            "Area Calculator"
        )

        self.resize(
            500,
            350
        )

        layout = QVBoxLayout()

        # -------------------------
        # Length
        # -------------------------

        layout.addWidget(
            QLabel(
                "Length (Karam)"
            )
        )

        self.txt_length = QLineEdit()

        layout.addWidget(
            self.txt_length
        )

        # -------------------------
        # Width
        # -------------------------

        layout.addWidget(
            QLabel(
                "Width (Karam)"
            )
        )

        self.txt_width = QLineEdit()

        layout.addWidget(
            self.txt_width
        )

        # -------------------------
        # Button
        # -------------------------

        self.btn_calc = QPushButton(
            "Calculate Rectangle"
        )

        self.btn_calc.clicked.connect(
            self.calculate_rectangle
        )

        layout.addWidget(
            self.btn_calc
        )

        # -------------------------
        # Result
        # -------------------------

        self.lbl_result = QLabel(
            "Area :"
        )

        layout.addWidget(
            self.lbl_result
        )

        self.setLayout(
            layout
        )

    def calculate_rectangle(self):

        try:

            length = float(
                self.txt_length.text()
        )

            width = float(
                self.txt_width.text()
        )

            sq_karam = (
                length * width
        )

            marla = (
                sq_karam / 9
        )

            kanal = (
                marla / 20
        )

            kms = self.marla_to_kms(
                marla
        )

            self.lbl_result.setText(
                f"Area:\n"
                f"{sq_karam:.2f} Sq Karam\n"
                f"{marla:.2f} Marla\n"
                f"{kanal:.2f} Kanal\n"
                f"{kms}"
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
            (
                rem_marla
                - whole_marla
            ) * 9
        )

        return (
            f"{kanal}K-"
            f"{whole_marla}M-"
            f"{sarsahi}S"
        )
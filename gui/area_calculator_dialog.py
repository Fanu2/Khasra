from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
    QTabWidget,
    QGridLayout
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

        self.tabs = QTabWidget()

        layout.addWidget(
            self.tabs
        )

# -------------------------
# Rectangle Tab
# -------------------------

        self.rectangle_tab = QWidget()

        self.tabs.addTab(
            self.rectangle_tab,
                "Rectangle"
        )

        rect_layout = QVBoxLayout()

        self.rectangle_tab.setLayout(
            rect_layout
        )

        rect_layout.addWidget(
        QLabel(
            "Length (Karam)"
            )
        )

        self.txt_length = QLineEdit()

        rect_layout.addWidget(
            self.txt_length
        )

        rect_layout.addWidget(
            QLabel(
                "Width (Karam)"
            )
        )

        self.txt_width = QLineEdit()

        rect_layout.addWidget(
                self.txt_width
        )

        self.btn_calc = QPushButton(
            "Calculate Rectangle"
        )

        self.btn_calc.clicked.connect(
            self.calculate_rectangle
        )

        rect_layout.addWidget(
            self.btn_calc
        )

        self.lbl_result = QLabel(
            "Area :"
        )

        rect_layout.addWidget(
            self.lbl_result
        )

# -------------------------
# Triangle Tab
# -------------------------

        self.triangle_tab = QWidget()

        self.tabs.addTab(
            self.triangle_tab,
                "Triangle"
        )

        tri_layout = QVBoxLayout()

        self.triangle_tab.setLayout(
            tri_layout
        )

        tri_layout.addWidget(
            QLabel(
                "Base (Karam)"
            )
        )
    

        self.txt_base = QLineEdit()

        tri_layout.addWidget(
            self.txt_base
        )

        tri_layout.addWidget(
            QLabel(
                "Height (Karam)"
            )
        )

        self.txt_height = QLineEdit()

        tri_layout.addWidget(
            self.txt_height
        )

        self.btn_triangle = QPushButton(
            "Calculate Triangle"
        )

        tri_layout.addWidget(
            self.btn_triangle
        )

        self.lbl_triangle_result = QLabel(
            "Area :"
        )

        tri_layout.addWidget(
        self.lbl_triangle_result
        )

        self.btn_triangle.clicked.connect(
            self.calculate_triangle
        )



        self.pyth_tab = QWidget()

        self.tabs.addTab(
            self.pyth_tab,
            "Pythagoras"
        )

        pyth_layout = QVBoxLayout()

        self.pyth_tab.setLayout(
            pyth_layout
        )

        pyth_layout.addWidget(
            QLabel(
                "Side A (Karam)"
            )
        )

        self.txt_side_a = QLineEdit()

        pyth_layout.addWidget(
            self.txt_side_a
        )

        pyth_layout.addWidget(
            QLabel(
                "Side B (Karam)"
            )
        )

        self.txt_side_b = QLineEdit()

        pyth_layout.addWidget(
            self.txt_side_b
        )

        self.btn_pyth = QPushButton(
            "Calculate Diagonal"
        )

        pyth_layout.addWidget(
            self.btn_pyth
        )

        self.lbl_pyth_result = QLabel(
            "Diagonal :"
        )

        pyth_layout.addWidget(
            self.lbl_pyth_result
        )

        self.btn_pyth.clicked.connect(
            self.calculate_pythagoras
        )

        self.setLayout(
            layout
        )

# -------------------------

# Polygon Tab
# -------------------------

        self.polygon_tab = QWidget()

        self.tabs.addTab(
    self.polygon_tab,
    "Polygon"
)

        poly_layout = QVBoxLayout()

        self.polygon_tab.setLayout(
            poly_layout
        )

# -------------------------
# Point Entry Grid
# -------------------------

        self.points_widget = QWidget()

        self.points_layout = QGridLayout()

        self.points_widget.setLayout(
            self.points_layout
        )

        poly_layout.addWidget(
            self.points_widget
    )

# Headers

        self.points_layout.addWidget(
            QLabel("X"),
            0,
            0
        )

        self.points_layout.addWidget(
            QLabel("Y"),
            0,
            1
        )

        self.point_rows = []

# -------------------------
# Buttons
# -------------------------

        self.btn_add_point = QPushButton(
            "Add Point"
        )

        poly_layout.addWidget(
            self.btn_add_point
        )

        self.btn_polygon = QPushButton(
            "Calculate Polygon"
        )

        poly_layout.addWidget(
            self.btn_polygon
        )

        self.lbl_polygon_result = QLabel(
    "Polygon Area :"
)

        poly_layout.addWidget(
            self.lbl_polygon_result
        )

# -------------------------
# Connections
# -------------------------

        self.btn_add_point.clicked.connect(
            self.add_point_row
        )

        self.btn_polygon.clicked.connect(
            self.calculate_polygon
        )

# -------------------------
# Initial Rows
# -------------------------

        for _ in range(4):
            self.add_point_row()

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

    def calculate_triangle(self):

        try:

            base = float(
                self.txt_base.text()
            )

            height = float(
                self.txt_height.text()
            )

            sq_karam = (
                base * height / 2
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

            self.lbl_triangle_result.setText(
                f"Area:\n"
                f"{sq_karam:.2f} Sq Karam\n"
                f"{marla:.2f} Marla\n"
                f"{kanal:.2f} Kanal\n"
                f"{kms}"
            )

        except Exception as e:

            print(e)

    def calculate_pythagoras(self):

            try:

                side_a = float(
                    self.txt_side_a.text()
            )

                side_b = float(
                    self.txt_side_b.text()
            )

                diagonal = (
                    side_a ** 2
                    + side_b ** 2
            )   ** 0.5

                self.lbl_pyth_result.setText(
                    f"Diagonal : "
                    f"{diagonal:.2f} Karam"
            )

            except Exception as e:

                print(e)
    def add_point_row(self):

        row = len(
            self.point_rows
        ) + 1

        txt_x = QLineEdit()

        txt_y = QLineEdit()

        self.points_layout.addWidget(
         txt_x,
            row,
            0
        )

        self.points_layout.addWidget(
            txt_y,
            row,
            1
        )

        self.point_rows.append(
            (
                txt_x,
                txt_y
            )
        )
    
    def calculate_polygon(self):

        try:

            points = []

            for (
                txt_x,
                txt_y
            ) in self.point_rows:

                x_text = (
                    txt_x.text().strip()
                )

                y_text = (
                    txt_y.text().strip()
                )

                if not x_text or not y_text:

                    continue

                points.append(
                    (
                        float(x_text),
                        float(y_text)
                    )
                )

            if len(points) < 3:

                self.lbl_polygon_result.setText(
                    "Minimum 3 points required"
                )

                return

            area = 0

            n = len(points)

            for i in range(n):

                x1, y1 = points[i]

                x2, y2 = points[
                (i + 1) % n
                ]

                area += (
                    x1 * y2
                    - y1 * x2
                )

            sq_karam = abs(
                area
            ) / 2

            marla = (
                sq_karam / 9
            )

            kms = self.marla_to_kms(
             marla
            )

            self.lbl_polygon_result.setText(
                f"Area:\n"
                f"{sq_karam:.2f} Sq Karam\n"
                f"{marla:.2f} Marla\n"
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
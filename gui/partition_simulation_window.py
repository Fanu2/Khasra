from graphics.parcel_item import ParcelItem
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QListWidget,
    QGraphicsView,
    QGraphicsScene,
    QFrame
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen


class PartitionSimulationWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Partition Simulation Workbench")
        self.resize(1400, 900)

        self.build_ui()
        self.load_villages()

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        # -----------------------------
        # Top controls
        # -----------------------------

        top = QHBoxLayout()

        self.village_combo = QComboBox()
        self.jamabandi_combo = QComboBox()
        self.khewat_combo = QComboBox()

        self.village_combo.addItem("Select Village")
        self.jamabandi_combo.addItem("Select Jamabandi")
        self.khewat_combo.addItem("Select Khewat")

        top.addWidget(QLabel("Village"))
        top.addWidget(self.village_combo)

        top.addWidget(QLabel("Jamabandi"))
        top.addWidget(self.jamabandi_combo)

        top.addWidget(QLabel("Khewat"))
        top.addWidget(self.khewat_combo)

        main_layout.addLayout(top)

        # -----------------------------
        # Middle
        # -----------------------------

        middle = QHBoxLayout()

        # Graphics

        self.scene = QGraphicsScene()

        
        colors = [
            QColor("#F4A261"),
            QColor("#2A9D8F"),
            QColor("#E9C46A"),
            QColor("#8AB6D6"),
            QColor("#90BE6D"),
            QColor("#F94144"),
        ]

        rects = [
            (40, 40, 180, 120),
            (240, 40, 220, 120),
            (40, 190, 150, 140),
            (210, 190, 250, 140),
            (490, 40, 180, 290),
            (40, 360, 630, 120),
        ]

        for i, (x, y, w, h) in enumerate(rects):

            parcel = ParcelItem(
                parcel_id=i + 1,
                khasra_no=f"18/{i+1}",
                owner_name=f"Owner {i+1}",
                area=2500,
                x=x,
                y=y,
                w=w,
                h=h,
                color=colors[i % len(colors)]
        )

        self.scene.addItem(parcel)

        text = self.scene.addText(f"Parcel {i+1}")
        text.setPos(
            x + 20,
            y + 20
        )
        self.view = QGraphicsView(self.scene)
        self.view.setFrameShape(QFrame.Box)

        middle.addWidget(self.view, 4)

        # Right panel

        right = QVBoxLayout()

        right.addWidget(QLabel("Owners"))

        self.owner_list = QListWidget()
        right.addWidget(self.owner_list)

        right.addWidget(QLabel("Allocation Summary"))

        self.summary = QListWidget()
        right.addWidget(self.summary)

        middle.addLayout(right, 1)

        main_layout.addLayout(middle)

        # -----------------------------
        # Bottom buttons
        # -----------------------------

        bottom = QHBoxLayout()

        bottom.addStretch()

        bottom.addWidget(QPushButton("Load"))
        bottom.addWidget(QPushButton("Validate"))
        bottom.addWidget(QPushButton("Commit"))
        bottom.addWidget(QPushButton("Close"))

        main_layout.addLayout(bottom)

        self.statusBar().showMessage("Partition Simulation Workbench Ready")
    
    def load_villages(self):

        from services.simulation_loader import SimulationLoader

        self.village_combo.clear()

        self.village_combo.addItem(
            "Select Village",
            None
        )

        villages = SimulationLoader.get_villages()

        for village in villages:

            self.village_combo.addItem(
                village.village_name,
                village.id
         )
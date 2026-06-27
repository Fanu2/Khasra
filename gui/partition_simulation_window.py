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

        self.village_combo.currentIndexChanged.connect(
        self.on_village_changed
        )

        self.khewat_combo.currentIndexChanged.connect(
        self.on_khewat_changed
        )

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

        
        self.scene = QGraphicsScene()

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
        self.load_demo_parcels()
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
        
    def on_village_changed(self):

        village_id = self.village_combo.currentData()

        print(f"Village selected: {village_id}")

        if village_id is None:

            self.khewat_combo.clear()
            self.khewat_combo.addItem("Select Khewat", None)
            return

        self.load_khewats(village_id)

    def load_khewats(self, village_id):

        from services.simulation_loader import SimulationLoader

        self.khewat_combo.clear()

        self.khewat_combo.addItem(
            "Select Khewat",
            None
        )

        khewats = SimulationLoader.get_khewats(village_id)

        print(f"Khewats returned: {len(khewats)}")

        for khewat in khewats:

               self.khewat_combo.addItem(
                    str(khewat.khewat_no),
                    khewat.id
        )
    def on_khewat_changed(self):

        khewat_id = self.khewat_combo.currentData()

        if khewat_id is None:
            return

        self.load_khasras(khewat_id)

    def load_khasras(self, khewat_id):

        from services.simulation_loader import SimulationLoader

        khasras = SimulationLoader.get_khasras(khewat_id)

        self.load_real_parcels(khasras)

    def load_demo_parcels(self):

        self.scene.clear()

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

            label = self.scene.addText(f"Parcel {i+1}")
            label.setPos(x + 15, y + 15)
    def load_real_parcels(self, khasras):

        self.scene.clear()

        colors = [
            QColor("#F4A261"),
            QColor("#2A9D8F"),
            QColor("#E9C46A"),
            QColor("#8AB6D6"),
            QColor("#90BE6D"),
            QColor("#F94144"),
        ]

        x = 40
        y = 40

        for i, khasra in enumerate(khasras):

            parcel = ParcelItem(
                parcel_id=khasra.id,
                khasra_no=khasra.khasra_no,
                owner_name="",
                area=khasra.area,
                x=x,
                y=y,
                w=140,
                h=80,
                color=colors[i % len(colors)]
            )

            self.scene.addItem(parcel)

            label = self.scene.addText(
                f"{khasra.khasra_no}\n{khasra.area}"
            )

            label.setPos(x + 10, y + 10)

            x += 170

            if x > 700:
                x = 40
                y += 110
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
from services.ownership_lookup import OwnershipLookup
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen
from services.allocation_engine import AllocationEngine
from gui.validation_dialog import ValidationDialog
from services.validation_engine import ValidationEngine
from gui.owner_summary_widget import OwnerSummaryWidget

class PartitionSimulationWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.engine = AllocationEngine()

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

        self.allocate_button.clicked.connect(
        self.allocate_selected_parcel
        )

        self.validate_button.clicked.connect(
        self.validate_partition
        )

        self.current_parcel = None
        self.current_khewat = None

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


        self.view = QGraphicsView(self.scene)
        self.view.setFrameShape(QFrame.Box)

        middle.addWidget(self.view, 4)
        
        # Right panel

        right = QVBoxLayout()

        title = QLabel("Parcel Information")
        title.setStyleSheet("font-size:16px;font-weight:bold;")
        right.addWidget(title)

        self.lbl_khasra = QLabel("Khasra No :")
        self.lbl_area = QLabel("Area :")
        self.lbl_remarks = QLabel("Remarks :")

        right.addWidget(self.lbl_khasra)
        right.addWidget(self.lbl_area)

# -------------------------
# Joint Owners
# -------------------------

        right.addWidget(QLabel("Joint Owners"))

        self.owner_list = QListWidget()
        right.addWidget(self.owner_list)

# -------------------------
# Allocate To
# -------------------------

        right.addWidget(QLabel("Allocate To"))

        self.owner_combo = QComboBox()
        right.addWidget(self.owner_combo)

        self.allocate_button = QPushButton("Allocate Selected Parcel")
        right.addWidget(self.allocate_button)

# -------------------------
# Current Allocation
# -------------------------
        right.addWidget(QLabel("Current Allocation"))

        self.allocation_list = QListWidget()
        right.addWidget(self.allocation_list)

        # -------------------------
        # Parcel Information
        # -------------------------

        right.addWidget(self.lbl_remarks)

        # -------------------------
        # Owner Summary
        # -------------------------

        self.owner_summary = OwnerSummaryWidget()
        right.addWidget(self.owner_summary)

        right.addStretch()

        middle.addLayout(right, 1)

        main_layout.addLayout(middle)
        # -----------------------------
        # Bottom buttons
        # -----------------------------

        bottom = QHBoxLayout()

        bottom.addStretch()

        bottom.addWidget(QPushButton("Load"))
        self.validate_button = QPushButton("Validate")
        bottom.addWidget(self.validate_button)
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

        village_name = self.village_combo.currentText()

        self.statusBar().showMessage(
            f"Village selected: {village_name}"
        )

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

        self.statusBar().showMessage(
            f"Loaded {len(khewats)} Khewats"
        )

        for khewat in khewats:

               self.khewat_combo.addItem(
                    str(khewat.khewat_no),
                    khewat.id
        )
    def on_khewat_changed(self):

        khewat_id = self.khewat_combo.currentData()

        if khewat_id is None:
         return

        print(f"Khewat selected: {khewat_id}")

        self.load_khasras(khewat_id)

    def load_khasras(self, khewat_id):

        from services.simulation_loader import SimulationLoader

        khasras = SimulationLoader.get_khasras(khewat_id)
        print(f"Khasras found: {len(khasras)}")

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
        

            parcel.main_window = self
            parcel.khewat_id = self.khewat_combo.currentData()

            self.scene.addItem(parcel)

            label = self.scene.addText(f"Parcel {i+1}")
            label.setPos(x + 15, y + 15)
    def load_real_parcels(self, khasras):

        self.scene.clear()

    # Get all current parcel allocations
        allocations = self.engine.get_all_allocations()

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

            parcel.main_window = self
            parcel.khewat_id = self.khewat_combo.currentData()

        # Restore owner allocation for this parcel
            parcel.owner_id = allocations.get(khasra.id)

            self.scene.addItem(parcel)

            label = self.scene.addText(
                f"{khasra.khasra_no}\n{khasra.area}"
            )

            label.setPos(x + 10, y + 10)

            x += 170

            if x > 700:
                x = 40
                y += 110
    ...
    def allocate_selected_parcel(self):

        selected = self.scene.selectedItems()

        if not selected:
            return

        parcel = selected[0]

        owner_id = self.owner_combo.currentData()

        if owner_id is None:
            return

    # Store allocation
        self.engine.allocate(
            parcel.parcel_id,
            owner_id
        )
        parcel.owner_id = owner_id
        
        # Store the owner inside the parcel object
        parcel.owner_id = owner_id

        self.refresh_allocation_panel()

        self.statusBar().showMessage(
            "Parcel allocated successfully."
        )
        

    # Owner colours
        owner_colors = [
            QColor("#4CAF50"),   # Green
            QColor("#2196F3"),   # Blue
            QColor("#FF9800"),   # Orange
            QColor("#9C27B0"),   # Purple
            QColor("#F44336"),   # Red
            QColor("#009688"),   # Teal
            QColor("#795548"),   # Brown
            QColor("#607D8B"),   # Blue Grey
        ]

        color = owner_colors[
            (owner_id - 1) % len(owner_colors)
        ]

        parcel.set_owner_color(color)

    # Refresh allocation display
        self.refresh_allocation_panel()

        self.statusBar().showMessage(
            "Parcel allocated successfully."
        )

        print()
        print("===== CURRENT ALLOCATIONS =====")

        for parcel_id, owner in self.engine.get_all_allocations().items():
            print(f"Parcel {parcel_id} -> Owner {owner}")

        print("===============================")
    def refresh_allocation_panel(self):

        self.allocation_list.clear()

        allocations = self.engine.get_all_allocations()

        for parcel_id, owner_id in allocations.items():

            owner_name = self.owner_lookup.get(
                owner_id,
                f"Owner {owner_id}"
            )

            self.allocation_list.addItem(
                f"Parcel {parcel_id} → {owner_name}"
            )

    def update_information_panel(
        self,
        khasra_no,
        area,
        khewat_id,
        remarks=""
    ):

        self.current_parcel = khasra_no
        self.current_khewat = khewat_id

        self.lbl_khasra.setText(
            f"Khasra No : {khasra_no}"
        )

        self.lbl_area.setText(
            f"Area : {area}"
        )

        self.lbl_remarks.setText(
            f"Remarks : {remarks}"
        )

    # Clear previous information
        self.owner_list.clear()
        self.owner_combo.clear()

    # Reset owner lookup dictionary
        self.owner_lookup = {}

    # Load owners for this khewat
        owners = OwnershipLookup.get_joint_owners(khewat_id)

        for ownership in owners:

            owner = ownership.owner

            self.owner_lookup[owner.id] = owner.owner_name

        # Joint Owners panel
            self.owner_list.addItem(
                f"{owner.owner_name} ({ownership.share_text})"
            )

        # Allocate To combo
            self.owner_combo.addItem(
                owner.owner_name,
                owner.id
            )
        self.view.viewport().update()   # if your QGraphicsView is named self.view

    # Refresh allocation display using owner names
        self.refresh_allocation_panel()
    def validate_partition(self):

        if self.current_khewat is None:

            self.statusBar().showMessage(
                "Please select a parcel first."
            )
            return

        allocations = self.engine.get_all_allocations()

        if not allocations:

            self.statusBar().showMessage(
                "No parcel allocations found."
            )
            return

        results = ValidationEngine.validate_allocations(
            self.current_khewat,
            allocations
        )
        
        self.last_validation_results = results
        
        dialog = ValidationDialog(
            results,
            self
        )

       

    # Connect the signal BEFORE showing the dialog
        dialog.ownerSelected.connect(
            self.highlight_owner
        )

        dialog.exec()

    def highlight_owner(self, owner_id):

        selected_owner = None
        parcels = []

    # Highlight parcels and collect parcel numbers
        for item in self.scene.items():

            if isinstance(item, ParcelItem):

                item.highlight(owner_id)

                if item.owner_id == owner_id:
                    parcels.append(str(item.khasra_no))

    # Find owner details from the last validation results
        if hasattr(self, "last_validation_results"):

            for owner in self.last_validation_results:

                if owner["owner_id"] == owner_id:
                    selected_owner = owner
                    break

    # Update Owner Summary
        if selected_owner:

            self.owner_summary.set_owner(
                owner_name=selected_owner["owner_name"],
                share=selected_owner["share"],
                required=selected_owner["required_area"],
                allocated=selected_owner["allocated_area"],
                difference=selected_owner["difference"],
                parcels=parcels
        )
from PySide6.QtWidgets import (
    QGroupBox,
    QFormLayout,
    QLabel
)


class OwnerSummaryWidget(QGroupBox):

    def __init__(self):

        super().__init__("Owner Summary")

        layout = QFormLayout()

        self.lbl_name = QLabel("-")
        self.lbl_share = QLabel("-")
        self.lbl_required = QLabel("-")
        self.lbl_allocated = QLabel("-")
        self.lbl_difference = QLabel("-")
        self.lbl_parcels = QLabel("-")

        layout.addRow("Owner", self.lbl_name)
        layout.addRow("Share", self.lbl_share)
        layout.addRow("Required", self.lbl_required)
        layout.addRow("Allocated", self.lbl_allocated)
        layout.addRow("Difference", self.lbl_difference)
        layout.addRow("Parcels", self.lbl_parcels)

        self.setLayout(layout)

    # ------------------------------------
    # Add Step 2 HERE
    # ------------------------------------

    def clear(self):

        self.lbl_name.setText("-")
        self.lbl_share.setText("-")
        self.lbl_required.setText("-")
        self.lbl_allocated.setText("-")
        self.lbl_difference.setText("-")
        self.lbl_parcels.setText("-")

    # ------------------------------------
    # Add Step 3 HERE
    # ------------------------------------

    def set_owner(
        self,
        owner_name,
        share,
        required,
        allocated,
        difference,
        parcels
    ):

        self.lbl_name.setText(owner_name)
        self.lbl_share.setText(share)
        self.lbl_required.setText(f"{required:.2f}")
        self.lbl_allocated.setText(f"{allocated:.2f}")
        self.lbl_difference.setText(f"{difference:.2f}")
        self.lbl_parcels.setText(", ".join(parcels))
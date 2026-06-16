
from PySide6.QtWidgets import (
    QWidget,QVBoxLayout,QFormLayout,QComboBox,QLineEdit,
    QPushButton,QLabel,QListWidget,QMessageBox
)
from database.db import SessionLocal
from database.models import Khewat, Khasra, KhasraAllocation, KhasraHistory

class KhasraAllocationWizard(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Khasra Allocation Wizard")

        layout = QVBoxLayout()
        form = QFormLayout()

        self.target_khewat = QComboBox()
        self.parent_khewat = QComboBox()
        self.area_edit = QLineEdit()

        self.required_lbl = QLabel("0.0000")
        self.allocated_lbl = QLabel("0.0000")
        self.remaining_lbl = QLabel("0.0000")

        self.khasra_list = QListWidget()

        form.addRow("Target Khewat", self.target_khewat)
        form.addRow("Required Area", self.required_lbl)
        form.addRow("Allocated Area", self.allocated_lbl)
        form.addRow("Remaining Area", self.remaining_lbl)
        form.addRow("Parent Khewat", self.parent_khewat)
        form.addRow("Allocate Area", self.area_edit)

        layout.addLayout(form)
        layout.addWidget(QLabel("Available Khasras"))
        layout.addWidget(self.khasra_list)

        self.preview_btn = QPushButton("Preview")
        self.preview_btn.clicked.connect(self.preview_split)
        layout.addWidget(self.preview_btn)

        self.allocate_btn = QPushButton("Allocate")
        self.allocate_btn.clicked.connect(self.allocate_khasra)
        layout.addWidget(self.allocate_btn)

        self.setLayout(layout)

        self.load_khewats()
        self.parent_khewat.currentIndexChanged.connect(self.load_khasras)
        self.target_khewat.currentIndexChanged.connect(self.update_target_info)

    def load_khewats(self):
        s = SessionLocal()
        try:
            self.target_khewat.clear()
            self.parent_khewat.clear()

            for k in s.query(Khewat).all():
                kno = str(k.khewat_no)
                status = str(getattr(k, "status", ""))

                if ("PARTIAL" in status.upper()
                    or "ALLOCATED" in status.upper()
                    or kno != "402"):
                    self.target_khewat.addItem(kno, k.id)

                self.parent_khewat.addItem(kno, k.id)
        finally:
            s.close()

        self.update_target_info()
        self.load_khasras()

    def update_target_info(self):
        s = SessionLocal()
        try:
            kid = self.target_khewat.currentData()
            if not kid:
                return
            k = s.get(Khewat, kid)
            area = float(getattr(k, "total_area", 0) or 0)
            self.required_lbl.setText(f"{area:.4f}")
            self.allocated_lbl.setText("0.0000")
            self.remaining_lbl.setText(f"{area:.4f}")
        finally:
            s.close()

    def load_khasras(self):
        self.khasra_list.clear()
        kid = self.parent_khewat.currentData()
        if not kid:
            return
        s = SessionLocal()
        try:
            for k in s.query(Khasra).filter(Khasra.khewat_id == kid).all():
                self.khasra_list.addItem(f"{k.khasra_no} ({k.area})")
        finally:
            s.close()

    def preview_split(self):
        if self.khasra_list.currentRow() < 0:
            QMessageBox.warning(self,"Validation","Select a khasra.")
            return

        txt = self.area_edit.text().strip()
        if not txt:
            QMessageBox.warning(self,"Validation","Enter allocation area.")
            return

        try:
            alloc = float(txt)
        except:
            QMessageBox.warning(self,"Validation","Invalid area.")
            return

        item = self.khasra_list.currentItem().text()
        area = float(item.split("(")[1].replace(")",""))

        if alloc <= 0 or alloc > area:
            QMessageBox.warning(self,"Validation","Allocation exceeds khasra area.")
            return

        remaining = area - alloc

        QMessageBox.information(
            self,
            "Split Preview",
            f"Current Area: {area:.4f}\n\n"
            f"Allocate: {alloc:.4f}\n\n"
            f"Result:\n"
            f"Khasra A: {remaining:.4f}\n"
            f"Khasra B: {alloc:.4f}"
        )


    def allocate_khasra(self):

        if self.khasra_list.currentRow() < 0:
            QMessageBox.warning(
                self,
                "Validation",
                "Select a khasra."
            )
            return

        try:
            alloc = float(
                self.area_edit.text().strip()
            )

        except:
            QMessageBox.warning(
                self,
                "Validation",
                "Invalid area."
            )
            return

        session = SessionLocal()

        try:

            parent_khewat_id = (
                self.parent_khewat.currentData()
            )

            target_khewat_id = (
                self.target_khewat.currentData()
            )

            item = (
                self.khasra_list.currentItem()
                .text()
            )

            khasra_no = (
                item.split("(")[0]
                .strip()
            )

            khasra = (
                session.query(Khasra)
                .filter(
                    Khasra.khasra_no == khasra_no
                )
                .first()
            )

            if not khasra:
                raise Exception(
                    "Khasra not found"
                )

            old_area = float(
                khasra.area or 0
            )

            remaining = (
                old_area - alloc
            )

            allocation = KhasraAllocation(
                target_khewat_id=target_khewat_id,
                parent_khewat_id=parent_khewat_id,
                source_khasra_id=khasra.id,
                source_khasra_no=khasra.khasra_no,
                allocated_area=alloc,
                remarks="Allocation Wizard"
            )

            session.add(allocation)

            history = KhasraHistory(
                khasra_no=khasra.khasra_no,
                action_type="ALLOCATE",
                old_area=old_area,
                new_area=remaining,
                remarks=f"Allocated {alloc}"
            )

            session.add(history)

            session.commit()

            QMessageBox.information(
                self,
                "Success",
                "Allocation recorded."
            )

        except Exception as e:

            session.rollback()

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            session.close()

        try:
            alloc = float(
                self.area_edit.text().strip()
            )

        except:
            QMessageBox.warning(
                self,
                "Validation",
                "Invalid area."
            )
            return

        session = SessionLocal()

        try:

            parent_khewat_id = (
                self.parent_khewat.currentData()
            )

            target_khewat_id = (
                self.target_khewat.currentData()
            )

            item = (
                self.khasra_list.currentItem()
                .text()
            )

            khasra_no = (
                item.split("(")[0]
                .strip()
            )

            khasra = (
                session.query(Khasra)
                .filter(
                    Khasra.khasra_no == khasra_no
                )
                .first()
            )

            if not khasra:
                raise Exception(
                    "Khasra not found"
                )

            old_area = float(
                khasra.area or 0
            )

            remaining = (
                old_area - alloc
            )

            allocation = KhasraAllocation(
                target_khewat_id=target_khewat_id,
                parent_khewat_id=parent_khewat_id,
                source_khasra_id=khasra.id,
                source_khasra_no=khasra.khasra_no,
                allocated_area=alloc,
                remarks="Allocation Wizard"
            )

            session.add(allocation)

            history = KhasraHistory(
                khasra_no=khasra.khasra_no,
                action_type="ALLOCATE",
                old_area=old_area,
                new_area=remaining,
                remarks=f"Allocated {alloc}"
            )

            session.add(history)

            session.commit()

            QMessageBox.information(
                self,
                "Success",
                "Allocation recorded."
            )

        except Exception as e:

            session.rollback()

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

        finally:

            session.close()
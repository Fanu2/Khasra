
from PySide6.QtWidgets import QWidget,QVBoxLayout,QFormLayout,QComboBox,QLineEdit,QPushButton,QMessageBox
from database.db import SessionLocal
from database.models import Khewat, Ownership, Owner
from services.partial_partition_engine import PartialPartitionEngine

class PartialPartitionWizard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Partial Partition Wizard")
        self.resize(800,600)
        l=QVBoxLayout(); f=QFormLayout()
        self.khewat_combo=QComboBox(); self.owner_combo=QComboBox()
        self.current_share=QLineEdit(); self.current_share.setReadOnly(True)
        self.num_edit=QLineEdit(); self.den_edit=QLineEdit(); self.new_khewat=QLineEdit()
        for a,b in [("Source Khewat",self.khewat_combo),("Owner",self.owner_combo),("Current Share",self.current_share),("Transfer Numerator",self.num_edit),("Transfer Denominator",self.den_edit),("New Khewat No",self.new_khewat)]:
            f.addRow(a,b)
        l.addLayout(f)
        p=QPushButton("Preview"); e=QPushButton("Execute")
        p.clicked.connect(self.preview); e.clicked.connect(self.execute)
        l.addWidget(p); l.addWidget(e)
        self.setLayout(l)
        self.load_khewats()
        self.khewat_combo.currentIndexChanged.connect(self.load_owners)
        self.owner_combo.currentIndexChanged.connect(self.update_share)

    def load_khewats(self):
        self.khewat_combo.clear()
        s=SessionLocal()
        try:
            for k in s.query(Khewat).all():
                self.khewat_combo.addItem(f"Khewat {k.khewat_no}",k.id)
        finally:s.close()
        self.load_owners()

    def load_owners(self):
        self.owner_combo.clear()
        kid=self.khewat_combo.currentData()
        if not kid:return
        s=SessionLocal()
        try:
            for o in s.query(Ownership).filter(Ownership.khewat_id==kid):
                owner=s.get(Owner,o.owner_id)
                self.owner_combo.addItem(f"{owner.owner_name} ({o.numerator}/{o.denominator})",o.owner_id)
        finally:s.close()
        self.update_share()

    def update_share(self):
        kid=self.khewat_combo.currentData(); oid=self.owner_combo.currentData()
        if not kid or not oid:return
        s=SessionLocal()
        try:
            o=s.query(Ownership).filter(Ownership.khewat_id==kid,Ownership.owner_id==oid).first()
            if o:self.current_share.setText(f"{o.numerator}/{o.denominator}")
        finally:s.close()

    def preview(self):
        try:
            r=PartialPartitionEngine.preview(self.khewat_combo.currentData(),self.owner_combo.currentData(),self.num_edit.text(),self.den_edit.text())
            QMessageBox.information(self,"Preview",f"Current: {r['current']}\nTransfer: {r['transfer']}\nRemaining: {r['remaining']}\nArea: {r['area']} marla")
        except Exception as e:
            QMessageBox.critical(self,"Error",str(e))

    def execute(self):
        try:
            r=PartialPartitionEngine.preview(self.khewat_combo.currentData(),self.owner_combo.currentData(),self.num_edit.text(),self.den_edit.text())
            msg=f"Current: {r['current']}\nTransfer: {r['transfer']}\nRemaining: {r['remaining']}\n\nCreate Khewat: {self.new_khewat.text()} ?"
            if QMessageBox.question(self,"Confirm",msg)!=QMessageBox.StandardButton.Yes:
                return
            res=PartialPartitionEngine.execute(self.khewat_combo.currentData(),self.owner_combo.currentData(),self.num_edit.text(),self.den_edit.text(),self.new_khewat.text())
            QMessageBox.information(self,"Success",f"Created Khewat {res['khewat_no']}")
            self.load_khewats()
            self.num_edit.clear(); self.den_edit.clear(); self.new_khewat.clear()
        except Exception as e:
            QMessageBox.critical(self,"Error",str(e))

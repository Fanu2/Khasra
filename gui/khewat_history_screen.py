from PySide6.QtWidgets import QWidget,QVBoxLayout,QTextEdit
from database.db import SessionLocal
try:
 from database.models import PartitionEvent
except: PartitionEvent=None
class KhewatHistoryScreen(QWidget):
    def __init__(self):
      super().__init__(); self.setWindowTitle("Khewat History"); self.resize(700,500)
      t=QTextEdit(); t.setReadOnly(True); l=QVBoxLayout(); l.addWidget(t); self.setLayout(l)
      s=SessionLocal(); txt=[]
      try:
       if PartitionEvent:
        for e in s.query(PartitionEvent).all(): txt.append(str(e))
      except Exception as ex: txt.append(str(ex))
      finally: s.close()
      t.setText("\n".join(txt) if txt else "No partition events found")

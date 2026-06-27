from PySide6.QtWidgets import (
    QGraphicsRectItem,
    QGraphicsItem
)

from PySide6.QtGui import (
    QColor,
    QBrush,
    QPen
)

from PySide6.QtCore import Qt


class ParcelItem(QGraphicsRectItem):

    def __init__(
        self,
        parcel_id,
        khasra_no,
        owner_name,
        area,
        x,
        y,
        w,
        h,
        color
    ):

        super().__init__(x, y, w, h)

        self.parcel_id = parcel_id
        self.khasra_no = khasra_no
        self.owner_name = owner_name
        self.area = area

        self.default_brush = QBrush(color)
        self.selected_brush = QBrush(QColor("yellow"))

        self.setBrush(self.default_brush)

        pen = QPen(QColor("black"))
        pen.setWidth(2)
        self.setPen(pen)

        self.setFlag(
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable,
            True
        )

        self.setAcceptHoverEvents(True)

        # <-- ADD THIS HERE
        self.setToolTip(
            f"Khasra : {self.khasra_no}\n"
            f"Owner  : {self.owner_name}\n"
            f"Area   : {self.area}"
        )

    def hoverEnterEvent(self, event):
    # Future: update status bar or owner panel
    
        super().hoverEnterEvent(event)

    def itemChange(self, change, value):

        if change == QGraphicsItem.GraphicsItemChange.ItemSelectedHasChanged:

            if self.isSelected():
                self.setBrush(self.selected_brush)
            else:
                self.setBrush(self.default_brush)

        return super().itemChange(change, value)
    
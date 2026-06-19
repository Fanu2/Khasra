from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)

from database.db import SessionLocal
from database.models import (
    Khewat,
    Ownership,
    Khasra
)


class KhewatDetailsDialog(QDialog):

    def __init__(
        self,
        khewat_id,
        parent=None
    ):
        super().__init__(parent)

        self.session = SessionLocal()
        self.khewat_id = khewat_id

        self.setWindowTitle(
            "Khewat Details"
        )

        self.resize(
            1000,
            700
        )

        self.khewat = self.session.get(
            Khewat,
            khewat_id
        )

        if not self.khewat:

            QMessageBox.warning(
                self,
                "Not Found",
                "Khewat not found."
            )

            self.close()
            return

        self.build_ui()

    def build_ui(self):

        main_layout = QVBoxLayout()

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        header = QLabel(
            f"""
            <h2>Khewat No. {self.khewat.khewat_no}</h2>
            <b>Khatauni:</b> {self.khewat.khatauni_no}
            &nbsp;&nbsp;&nbsp;
            <b>Area:</b> {self.khewat.total_area}
            """
        )

        main_layout.addWidget(header)

        # -------------------------------------------------
        # Tabs
        # -------------------------------------------------

        self.tabs = QTabWidget()

        self.tabs.addTab(
            self.create_summary_tab(),
            "Summary"
        )

        self.tabs.addTab(
            self.create_owners_tab(),
            "Owners"
        )

        self.tabs.addTab(
            self.create_khasras_tab(),
            "Khasras"
        )

        self.tabs.addTab(
            self.create_history_tab(),
            "History"
        )

        main_layout.addWidget(
            self.tabs
        )

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        button_bar = QHBoxLayout()

        self.btn_owner_matrix = QPushButton(
            "Owner Matrix"
        )

        self.btn_allocation = QPushButton(
            "Khasra Allocation"
        )

        self.btn_export = QPushButton(
            "Export Report"
        )

        self.btn_close = QPushButton(
            "Close"
        )

        button_bar.addWidget(
            self.btn_owner_matrix
        )

        button_bar.addWidget(
            self.btn_allocation
        )

        button_bar.addStretch()

        button_bar.addWidget(
            self.btn_export
        )

        button_bar.addWidget(
            self.btn_close
        )

        main_layout.addLayout(
            button_bar
        )

        self.btn_close.clicked.connect(
            self.close
        )

        self.btn_owner_matrix.clicked.connect(
            self.show_owner_matrix
        )

        self.btn_allocation.clicked.connect(
            self.open_allocation
        )

        self.btn_export.clicked.connect(
            self.export_report
        )

        self.setLayout(
            main_layout
        )

    # =====================================================
    # SUMMARY TAB
    # =====================================================

    def create_summary_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        ownerships = (
            self.session.query(Ownership)
            .filter_by(
                khewat_id=self.khewat.id
            )
            .all()
        )

        khasras = (
            self.session.query(Khasra)
            .filter_by(
                khewat_id=self.khewat.id
            )
            .all()
        )

        summary = QLabel(
            f"""
            <h3>Khewat Summary</h3>

            <b>Khewat No:</b>
            {self.khewat.khewat_no}<br>

            <b>Khatauni No:</b>
            {self.khewat.khatauni_no}<br>

            <b>Total Area:</b>
            {self.khewat.total_area}<br>

            <b>Owner Count:</b>
            {len(ownerships)}<br>

            <b>Khasra Count:</b>
            {len(khasras)}<br>
            """
        )

        layout.addWidget(summary)

        widget.setLayout(layout)

        return widget

    # =====================================================
    # OWNERS TAB
    # =====================================================

    def create_owners_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        table = QTableWidget()

        owners = (
            self.session.query(Ownership)
            .filter_by(
                khewat_id=self.khewat.id
            )
            .all()
        )

        table.setRowCount(
            len(owners)
        )

        table.setColumnCount(2)

        table.setHorizontalHeaderLabels(
            [
                "Owner",
                "Share"
            ]
        )

        for row, item in enumerate(owners):

            table.setItem(
                row,
                0,
                QTableWidgetItem(
                    item.owner.owner_name
                )
            )

            table.setItem(
                row,
                1,
                QTableWidgetItem(
                    f"{item.numerator}/{item.denominator}"
                )
            )

        layout.addWidget(table)

        widget.setLayout(layout)

        return widget

    # =====================================================
    # KHASRAS TAB
    # =====================================================

    def create_khasras_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        table = QTableWidget()

        khasras = (
            self.session.query(Khasra)
            .filter_by(
                khewat_id=self.khewat.id
            )
            .all()
        )

        table.setRowCount(
            len(khasras)
        )

        table.setColumnCount(2)

        table.setHorizontalHeaderLabels(
            [
                "Khasra No",
                "Area"
            ]
        )

        for row, item in enumerate(khasras):

            table.setItem(
                row,
                0,
                QTableWidgetItem(
                    str(item.khasra_no)
                )
            )

            table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(item.area)
                )
            )

        layout.addWidget(table)

        widget.setLayout(layout)

        return widget

    # =====================================================
    # HISTORY TAB
    # =====================================================

    def create_history_tab(self):

        widget = QWidget()

        layout = QVBoxLayout()

        label = QLabel(
            "History Viewer coming in next sprint."
        )

        layout.addWidget(label)

        widget.setLayout(layout)

        return widget

    # =====================================================
    # ACTIONS
    # =====================================================

    def show_owner_matrix(self):

        QMessageBox.information(
            self,
            "Owner Matrix",
            "Owner Matrix integration coming next step."
        )

    def open_allocation(self):

        QMessageBox.information(
            self,
            "Allocation",
            "Khasra Allocation integration coming next step."
        )

    def export_report(self):

        QMessageBox.information(
            self,
            "Export",
            "Report export coming next step."
        )
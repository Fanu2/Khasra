from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem
)

import pandas as pd


class JamabandiImportDialog(QDialog):

    def __init__(
        self,
        parent=None
    ):

        super().__init__(parent)

        self.setWindowTitle(
            "Jamabandi HTML Import"
        )

        self.resize(
            1000,
            700
        )

        self.file_path = ""
        self.df = None

        layout = QVBoxLayout()

        # -------------------------
        # File Selection
        # -------------------------

        file_row = QHBoxLayout()

        self.lbl_file = QLabel(
            "No file selected"
        )

        self.btn_browse = QPushButton(
            "Browse HTML"
        )

        self.btn_load = QPushButton(
            "Load Table"
        )

        self.btn_export_excel = QPushButton(
            "Export Excel"
        )
        file_row.addWidget(
            self.lbl_file
        )

        file_row.addWidget(
            self.btn_browse
        )

        file_row.addWidget(
            self.btn_load
        )

        file_row.addWidget(
            self.btn_export_excel
        )

        layout.addLayout(
            file_row
        )

        # -------------------------
        # Table Preview
        # -------------------------

        self.table = QTableWidget()

        self.btn_analyze = QPushButton(
            "Analyze Owners"
        )

        layout.addWidget(
            self.btn_analyze
        )

        self.lbl_summary = QLabel(
            "Owner Summary"
        )

        layout.addWidget(
            self.lbl_summary
        )

        layout.addWidget(
            self.table
        )

        self.setLayout(
            layout
        )

        # -------------------------
        # Signals
        # -------------------------

        self.btn_browse.clicked.connect(
            self.browse_file
        )

        self.btn_load.clicked.connect(
            self.load_html
        )

        self.btn_export_excel.clicked.connect(
            self.export_excel
        )

        self.btn_analyze.clicked.connect(
            self.analyze_owners
        )
        
    
    def browse_file(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select HTML File",
            "",
            "HTML Files (*.html *.htm)"
        )

        if file_name:

            self.file_path = file_name

            self.lbl_file.setText(
                file_name
            )

    def load_html(self):

        try:

            if not self.file_path:

                QMessageBox.warning(
                    self,
                    "No File",
                    "Please select an HTML file."
                )

                return

            tables = pd.read_html(
                self.file_path,
                encoding="utf-8"
            )

            if not tables:

                QMessageBox.warning(
                    self,
                    "No Tables",
                    "No HTML tables found."
                )

                return

            self.df = max(
                tables,
                key=lambda t: (
                    len(t.index),
                    len(t.columns)
                )
            )
            self.df = self.df.fillna("")
            
            self.show_dataframe()

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def show_dataframe(self):

        if self.df is None:
            return

        rows = len(self.df.index)
        cols = len(self.df.columns)

        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)

        self.table.setHorizontalHeaderLabels(
            [str(c) for c in self.df.columns]
        )

        for r in range(rows):

            for c in range(cols):

                value = self.df.iloc[r, c]

                if pd.isna(value):
                    value = ""

                self.table.setItem(
                    r,
                    c,
                    QTableWidgetItem(
                        str(value)
                    )
                )
    def analyze_owners(self):

        if self.df is None:

            self.lbl_summary.setText(
                "No table loaded."
            )

            return

        rows = len(self.df.index)
        cols = len(self.df.columns)

        self.lbl_summary.setText(
            f"Rows : {rows}\n"
            f"Columns : {cols}"
        )
    def export_excel(self):

        if self.df is None:

            QMessageBox.warning(
                self,
                "No Data",
                "Please load a table first."
        )

            return

        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Excel",
            "",
            "Excel Files (*.xlsx)"
        )

        if not file_name:

            return

        try:

            self.df.to_excel(
                file_name,
                index=False
        )

            QMessageBox.information(
                self,
                "Success",
                "Excel file saved successfully."
        )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
        )
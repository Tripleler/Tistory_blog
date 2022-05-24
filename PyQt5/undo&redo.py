import sys
from PyQt5.QtWidgets import *
import pandas as pd
from collections import deque


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        header = ['a', 'b', 'c', 'd']
        self.table = QTableWidget()
        self.table.setRowCount(20)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(header)
        k = 1
        df_list = []
        for i in range(20):
            df_list2 = []
            for j in range(4):
                self.table.setItem(i, j, QTableWidgetItem(str(k)))
                df_list2.append(str(k))
                k += 1
            df_list.append(df_list2)
        self.data = pd.DataFrame(df_list, columns=header)
        self.table.itemChanged.connect(self.change)

        self.btn_undo = QPushButton(self)
        self.btn_undo.setIcon(app.style().standardIcon(QStyle.SP_ArrowLeft))
        self.btn_undo.setEnabled(False)
        self.btn_undo.clicked.connect(self.undo)
        self.undo_list = deque(maxlen=5)

        self.btn_redo = QPushButton(self)
        self.btn_redo.setIcon(app.style().standardIcon(QStyle.SP_ArrowRight))
        self.btn_redo.setEnabled(False)
        self.btn_redo.clicked.connect(self.redo)
        self.redo_list = deque()

        layout = QGridLayout()
        layout.addWidget(self.btn_undo, 0, 0, 1, 1)
        layout.addWidget(self.btn_redo, 0, 1, 1, 1)
        layout.addWidget(self.table, 1, 0, 10, 2)
        self.setLayout(layout)

        self.setWindowTitle('undo&redo')
        self.setGeometry(300, 100, 600, 400)
        self.show()

    def undo(self):
        if len(self.undo_list):
            self.redo_list.append(self.data.copy())
            self.btn_redo.setEnabled(True)
            self.table.blockSignals(True)
            self.data = self.undo_list.pop()
            rows, cols = self.data.shape
            for row in range(rows):
                for col in range(cols):
                    self.table.setItem(row, col, QTableWidgetItem(str(self.data.iloc[row, col])))
            self.table.blockSignals(False)
            self.btn_redo.setEnabled(True)
            if not len(self.undo_list):
                self.btn_undo.setEnabled(False)

    def redo(self):
        if len(self.redo_list):
            self.undo_list.append(self.data.copy())
            self.btn_undo.setEnabled(True)
            self.table.blockSignals(True)
            self.data = self.redo_list.pop()
            rows, cols = self.data.shape
            for row in range(rows):
                for col in range(cols):
                    self.table.setItem(row, col, QTableWidgetItem(str(self.data.iloc[row, col])))
            self.table.blockSignals(False)
            self.btn_redo.setEnabled(True)
            if not len(self.redo_list):
                self.btn_redo.setEnabled(False)

    def change(self, item):
        self.undo_list.append(self.data.copy())
        self.redo_list.clear()
        self.btn_undo.setEnabled(True)
        self.btn_redo.setEnabled(False)
        self.data.iloc[item.row(), item.column()] = item.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

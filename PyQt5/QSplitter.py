import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame()
        topright.setFrameShape(QFrame.Panel)

        bottomleft = QFrame()
        bottomleft.setFrameShape(QFrame.WinPanel)
        bottomleft.setFrameShadow(QFrame.Sunken)

        bottomright = QFrame()
        bottomright.setFrameShape(QFrame.StyledPanel)

        self.splittertop = QSplitter(Qt.Horizontal)
        self.splittertop.addWidget(topleft)
        self.splittertop.addWidget(topright)
        self.splittertop.splitterMoved.connect(self.replace)

        self.splitterbottom = QSplitter(Qt.Horizontal)
        self.splitterbottom.addWidget(bottomleft)
        self.splitterbottom.addWidget(bottomright)
        self.splitterbottom.splitterMoved.connect(self.replace)

        self.splitterv = QSplitter(Qt.Vertical)
        self.splitterv.addWidget(self.splittertop)
        self.splitterv.addWidget(self.splitterbottom)

        hbox.addWidget(self.splitterv)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    def replace(self, index, pos):
        splitter = self.splitterbottom if self.sender() == self.splittertop else self.splittertop
        splitter.blockSignals(True)
        splitter.moveSplitter(index, pos)
        splitter.blockSignals(False)


app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())
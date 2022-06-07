import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
width = size.width()
height = size.height()


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cent_widget = CentWidget()
        self.setCentralWidget(self.cent_widget)
        self.setWindowTitle('QStackedWidget')
        self.setGeometry(width // 10, height // 10, width // 5 * 4, height // 5 * 4)
        self.show()


class CentWidget(QWidget):
    def __init__(self):
        super().__init__()
        base = QPixmap('../icon/base.JPG')
        self.lbl_img = QLabel()
        self.lbl_img.setScaledContents(True)
        self.lbl_img.setPixmap(base)

        self.list = QListWidget()
        self.list.addItem('pixmap')
        self.list.addItem('buttons')
        self.list.addItem('labels')
        self.list.itemClicked.connect(self.show_stack)

        self.widget1 = QWidget()
        layout1 = QGridLayout()
        layout1.addWidget(self.lbl_img)
        self.widget1.setLayout(layout1)

        self.widget2 = QWidget()
        btn_1 = QPushButton('button1')
        btn_2 = QPushButton('button2')
        btn_3 = QPushButton('button3')
        layout2 = QVBoxLayout()
        layout2.addWidget(btn_1)
        layout2.addWidget(btn_2)
        layout2.addWidget(btn_3)
        self.widget2.setLayout(layout2)

        self.widget3 = QWidget()
        lbl_1 = QLabel('label1')
        lbl_2 = QLabel('label2')
        lbl_3 = QLabel('label3')
        layout3 = QVBoxLayout()
        layout3.addWidget(lbl_1)
        layout3.addWidget(lbl_2)
        layout3.addWidget(lbl_3)
        self.widget3.setLayout(layout3)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.widget1)
        self.stack.addWidget(self.widget2)
        self.stack.addWidget(self.widget3)

        grid = QGridLayout()
        grid.addWidget(self.list, 0, 0, 2, 1)
        grid.addWidget(self.stack, 0, 1, 2, 1)
        self.setLayout(grid)

    def show_stack(self, _):
        self.stack.setCurrentIndex(self.list.currentIndex().row())


ex = MyApp()
sys.exit(app.exec_())

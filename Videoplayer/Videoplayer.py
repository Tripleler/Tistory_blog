import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtTest import QTest
import cv2
import numpy as np

app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
width = size.width()
height = size.height()


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cent_widget = CentWidget()
        self.setCentralWidget(self.cent_widget)
        self.setWindowTitle('Video Player')
        self.setGeometry(width // 10, height // 10, width // 5 * 4, height // 5 * 4)
        menubar = self.menuBar()
        file = QMenu('파일', self)
        menubar.addMenu(file)
        load = QAction('불러오기', self)
        file.addAction(load)
        load.triggered.connect(self.cent_widget.load)
        self.show()


class CentWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.videothread = VideoThread()
        base = QPixmap('base.JPG')

        self.lbl_img = QLabel()
        self.lbl_img.setScaledContents(True)
        self.lbl_img.setPixmap(base)

        icon_pp = QIcon()
        icon_pp.addPixmap(QPixmap("./icon/pause.png"), QIcon.Normal, QIcon.On)
        icon_pp.addPixmap(QPixmap("./icon/play.png"), QIcon.Active, QIcon.Off)
        icon_pp.addPixmap(QPixmap("./icon/pause.png"), QIcon.Active, QIcon.On)

        self.btn_pp = QPushButton()
        self.btn_pp.setCheckable(True)
        self.btn_pp.setIcon(icon_pp)
        self.btn_pp.clicked.connect(self.pp)

        speed_opt = QComboBox(self)
        [speed_opt.addItem(i) for i in ['빠르게', '보통', '느리게']]
        speed_opt.setCurrentIndex(1)
        speed_opt.activated.connect(self.videothread.speed)

        self.sliframe = QSlider(Qt.Horizontal, self)
        self.sliframe.setSingleStep(1)
        self.sliframe.setRange(0, 0)
        self.sliframe.valueChanged.connect(self.frame_chg)
        self.sliframe.sliderPressed.connect(self.videothread.pause)
        self.sliframe.sliderReleased.connect(self.videothread.play)

        grid = QGridLayout()
        grid.addWidget(self.lbl_img, 0, 0, 19, 20)
        grid.addWidget(self.btn_pp, 19, 0, 1, 5)
        grid.addWidget(speed_opt, 19, 5, 1, 5)
        grid.addWidget(self.sliframe, 19, 10, 1, 10)
        self.setLayout(grid)

        self.videothread.send_img.connect(self.show)
        self.videothread.send_frames.connect(self.set_frames)
        self.videothread.send_frame.connect(self.sli_chg)
        self.videothread.send_status.connect(self.status)

    def show(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                     QImage.Format_RGB888)
        self.lbl_img.setPixmap(QPixmap.fromImage(img))

    def load(self):
        fname = QFileDialog.getOpenFileName(self, '동영상 선택하기', filter='*.mp4')
        if fname[0]:
            if self.videothread.isRunning():
                self.videothread.status = False
                QTest.qWait(1000)
                self.videothread.cap.release()
                self.videothread.status = True
                self.videothread.terminate()
            self.videothread.source = fname[0]
            self.btn_pp.setChecked(True)
            self.videothread.start()

    def pp(self):
        if self.btn_pp.isChecked():
            self.videothread.play()
        else:
            self.videothread.pause()

    def frame_chg(self):
        num = int(self.sliframe.value())
        if not self.videothread.status:
            self.videothread.cap.set(1, num)
            self.videothread.frame = num

    def set_frames(self, frames):
        self.sliframe.setRange(1, frames)

    def sli_chg(self, frame):
        self.sliframe.setValue(frame)

    def status(self, sign):
        if sign and not self.btn_pp.isChecked():
            self.btn_pp.setChecked(True)
        if not sign and self.btn_pp.isChecked():
            self.btn_pp.setChecked(False)


class VideoThread(QThread):
    send_img = pyqtSignal(np.ndarray)
    send_frame = pyqtSignal(int)
    send_frames = pyqtSignal(int)
    send_status = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.source = ''
        self.cond = QWaitCondition()
        self.status = True
        self.mutex = QMutex()
        self.delay = 30

    def run(self):
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            print("Camera open failed!")
        self.send_frames.emit(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))
        self.frame = 0
        while True:
            self.mutex.lock()
            if not self.status:
                self.cond.wait(self.mutex)
            ret, frame = self.cap.read()
            if ret:
                self.frame += 1
                self.send_frame.emit(self.frame)
            else:
                self.mutex.unlock()
                self.status = False
                continue
            self.send_img.emit(frame)
            cv2.waitKey(self.delay)
            self.mutex.unlock()

    def play(self):
        self.status = True
        self.send_status.emit(True)
        self.cond.wakeAll()

    def pause(self):
        self.status = False
        self.send_status.emit(False)

    def speed(self, e):
        if not e:
            self.delay = 1
        elif e == 1:
            self.delay = 30
        elif e == 2:
            self.delay = 100


ex = MyApp()
sys.exit(app.exec_())
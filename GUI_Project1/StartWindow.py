from PyQt6.QtWidgets import *
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import *
from MainWindow import MainWindow
import sys


class StartWindow(QMainWindow):

    def __init__(self):
        super(StartWindow, self).__init__()

        self.new = None

        self.setFixedWidth(350)
        self.setFixedHeight(250)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.label = QLabel(self)
        self.movie = QMovie('Images/start-window/star-bg.gif')
        self.label.resize(350, 250)
        self.label.setMovie(self.movie)
        self.movie.start()

        self.create_widget()

    def create_widget(self):

        # create close button
        button_exit = QPushButton(self)
        button_exit.resize(30, 30)
        button_exit.setStyleSheet("""
                    QPushButton {
                        border-image:url(Images/start-window/x-btn/x-btni.png);
                    }
                    QPushButton:hover {
                        border-image:url(Images/start-window/x-btn/x-btnf.png)
                    }""")
        button_exit.clicked.connect(self.close)
        button_exit.move(313, 5)

        # create start button (open new window)
        button_start = QPushButton(self)
        button_start.resize(160, 65)
        button_start.setStyleSheet("""
                            QPushButton {
                                border-image:url(Images/start-window/start-btn/start-btni.png);
                            }
                            QPushButton:hover {
                                border-image:url(Images/start-window/start-btn/start-btnf.png)
                            }""")
        button_start.clicked.connect(self.new_window)
        button_start.move(100, 90)

    def new_window(self):
        self.close()
        self.new = MainWindow()
        self.new.show()


app = QApplication([])
window = StartWindow()
window.show()
sys.exit(app.exec())

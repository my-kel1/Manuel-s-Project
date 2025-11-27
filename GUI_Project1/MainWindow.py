from PyQt6.QtWidgets import *
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import *
import sys


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setFixedWidth(600)
        self.setFixedHeight(281)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.label = QLabel(self)
        self.label.resize(600, 340)
        self.label.setStyleSheet("border-image:url(Images/main-window/home-page/plain-bg.png)")
        self.label.move(0, 0)

        self.home_section()
        self.exit_button()

    ####################################################################################################################

    # create button
    def exit_button(self):

        # close button
        self.button_exit = QPushButton(self)
        self.button_exit.resize(30, 30)
        self.button_exit.setStyleSheet("""
            QPushButton {
                border-image:url(Images/start-window/x-btn/x-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/start-window/x-btn/x-btnf.png)
            }
        """)
        self.button_exit.clicked.connect(self.close)
        self.button_exit.move(560, 5)
        self.button_exit.show()

    ####################################################################################################################

    # home section
    def home_section(self):

        # add gif background
        self.label_gif_home = QLabel(self)
        self.movie_gif_home = QMovie('Images/main-window/home-page/1-bg.gif')
        self.label_gif_home.resize(500, 281)
        self.label_gif_home.move(150, 0)
        self.label_gif_home.setMovie(self.movie_gif_home)
        self.movie_gif_home.start()

        # plant1
        self.label_plant1_home = QLabel(self)
        self.label_plant1_home.resize(90, 200)
        self.label_plant1_home.setStyleSheet("border-image:url(Images/main-window/home-page/add-ons/plant1.png)")
        self.label_plant1_home.move(-20, 100)

        # textbox
        self.label_txtbox_home = QLabel(self)
        self.label_txtbox_home.resize(400, 250)
        self.label_txtbox_home.setStyleSheet("border-image:url(Images/main-window/home-page/start.png)")
        self.label_txtbox_home.move(175, 15)

        # info button
        self.button_info_home = QPushButton(self)
        self.button_info_home.resize(150, 60)
        self.button_info_home.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/home-page/info-btn/info-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/home-page/info-btn/info-btnf.png)
            }
        """)
        self.button_info_home.clicked.connect(self.info_section)
        self.button_info_home.move(0, 30)

        # self section button
        self.button_self_home = QPushButton(self)
        self.button_self_home.resize(150, 60)
        self.button_self_home.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/home-page/self-btn/self-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/home-page/self-btn/self-btnf.png)
            }
        """)
        self.button_self_home.clicked.connect(self.self_section)
        self.button_self_home.move(0, 105)

        # dreams section button
        self.button_dreams_home = QPushButton(self)
        self.button_dreams_home.resize(150, 60)
        self.button_dreams_home.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/home-page/dreams-btn/dreams-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/home-page/dreams-btn/dreams-btnf.png)
            }
        """)
        self.button_dreams_home.clicked.connect(self.dreams)
        self.button_dreams_home.move(0, 180)

        # plant2 (add-on)
        self.label_plant2_home = QLabel(self)
        self.label_plant2_home.resize(65, 130)
        self.label_plant2_home.setStyleSheet("border-image:url(Images/main-window/home-page/add-ons/plant2.png)")
        self.label_plant2_home.move(90, -30)

    ####################################################################################################################

    # info section
    def info_section(self):

        # home widgets
        self.label_gif_home.hide()
        self.label_plant1_home.hide()
        self.label_plant2_home.hide()
        self.label_txtbox_home.hide()
        self.button_info_home.hide()
        self.button_self_home.hide()
        self.button_dreams_home.hide()

        # add gif background
        self.label_gif_info = QLabel(self)
        self.movie_gif_info = QMovie('Images/main-window/info-page/info-bg.gif')
        self.label_gif_info.resize(600, 281)
        self.label_gif_info.setMovie(self.movie_gif_info)
        self.movie_gif_info.start()
        self.label_gif_info.move(0, 0)
        self.label_gif_info.show()

        self.exit_button()

        # frame
        self.label_frame_info = QLabel(self)
        self.label_frame_info.resize(150, 150)
        self.label_frame_info.setStyleSheet("border-image:url(Images/main-window/info-page/frame.png)")
        self.label_frame_info.move(60, 70)
        self.label_frame_info.show()

        # info box
        self.label_info = QLabel(self)
        self.label_info.resize(320, 200)
        self.label_info.setStyleSheet("border-image:url(Images/main-window/info-page/info-box.png)")
        self.label_info.move(220, 40)
        self.label_info.show()

        # back button
        self.button_back_info = QPushButton(self)
        self.button_back_info.resize(70, 30)
        self.button_back_info.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/home-page/back-btn/back-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/home-page/back-btn/back-btnf.png)
            }
        """)
        self.button_back_info.clicked.connect(self.back_main_home_info)
        self.button_back_info.move(5, 5)
        self.button_back_info.show()

    def back_main_home_info(self):

        self.button_back_info.hide()

        self.label_gif_home.show()
        self.label_plant1_home.show()
        self.label_plant2_home.show()
        self.label_txtbox_home.show()
        self.button_info_home.show()
        self.button_self_home.show()
        self.button_dreams_home.show()

        self.label_gif_info.hide()
        self.label_frame_info.hide()
        self.label_info.hide()

    ####################################################################################################################

    # self section
    def self_section(self):

        self.label_gif_home.hide()
        self.label_plant1_home.hide()
        self.label_plant2_home.hide()
        self.label_txtbox_home.hide()
        self.button_info_home.hide()
        self.button_self_home.hide()
        self.button_dreams_home.hide()

        # gif
        self.label_gif_self = QLabel(self)
        self.movie_gif_self = QMovie('Images/main-window/self-window/self-bg.gif')
        self.label_gif_self.resize(600, 281)
        self.label_gif_self.setMovie(self.movie_gif_self)
        self.movie_gif_self.start()
        self.label_gif_self.move(0, 0)
        self.label_gif_self.show()

        self.exit_button()

        # text box
        self.label_frame_self = QLabel(self)
        self.label_frame_self.resize(450, 240)
        self.label_frame_self.setStyleSheet("border-image:url(Images/main-window/self-window/self-txt-box.png)")
        self.label_frame_self.move(70, 20)
        self.label_frame_self.show()

        # back button
        self.button_back_self = QPushButton(self)
        self.button_back_self.resize(70, 30)
        self.button_back_self.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/self-window/self-back-btn/self-back-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/self-window/self-back-btn/self-back-btnf.png)
            }
        """)
        self.button_back_self.clicked.connect(self.back_main_home_self)
        self.button_back_self.move(5, 5)
        self.button_back_self.show()

    def back_main_home_self(self):

        self.label_gif_home.show()
        self.label_plant1_home.show()
        self.label_plant2_home.show()
        self.label_txtbox_home.show()
        self.button_info_home.show()
        self.button_self_home.show()
        self.button_dreams_home.show()

        self.label_gif_self.hide()
        self.label_frame_self.hide()
        self.button_back_self.hide()

    ####################################################################################################################

    # dreams section
    def dreams(self):

        self.label_gif_home.hide()
        self.label_plant1_home.hide()
        self.label_plant2_home.hide()
        self.label_txtbox_home.hide()
        self.button_info_home.hide()
        self.button_self_home.hide()
        self.button_dreams_home.hide()

        # gif
        self.label_gif_dreams = QLabel(self)
        self.movie_gif_dreams = QMovie('Images/main-window/dreams-page/dreams-bg.gif')
        self.label_gif_dreams.resize(600, 281)
        self.label_gif_dreams.setMovie(self.movie_gif_dreams)
        self.movie_gif_dreams.start()
        self.label_gif_dreams.move(110, 0)
        self.label_gif_dreams.show()

        self.exit_button()

        # envelope button
        self.button_env_dreams = QPushButton(self)
        self.button_env_dreams.resize(70, 70)
        self.button_env_dreams.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/dreams-page/envelope-btn/envelope-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/dreams-page/envelope-btn/envelope-btnf.png)
            }
        """)
        self.button_env_dreams.clicked.connect(self.message1)
        self.button_env_dreams.move(20, 200)
        self.button_env_dreams.show()

        # back
        self.button_back_dreams = QPushButton(self)
        self.button_back_dreams.resize(70, 30)
        self.button_back_dreams.setStyleSheet("""
            QPushButton {
                border-image:url(Images/main-window/dreams-page/dreams-back-btn/dreams-back-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/main-window/dreams-page/dreams-back-btn/dreams-back-btnf.png)
            }
        """)
        self.button_back_dreams.clicked.connect(self.back_main_home_dreams)
        self.button_back_dreams.move(5, 5)
        self.button_back_dreams.show()

    def message1(self):
        self.new = Message1()
        self.new.show()

    def back_main_home_dreams(self):

        self.label_gif_home.show()
        self.label_plant1_home.show()
        self.label_plant2_home.show()
        self.label_txtbox_home.show()
        self.button_info_home.show()
        self.button_self_home.show()
        self.button_dreams_home.show()

        self.label_gif_dreams.hide()
        self.button_env_dreams.hide()
        self.button_back_dreams.hide()


class Message1(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(300)
        self.setFixedHeight(200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.label_message1 = QLabel(self)
        self.movie_message1 = QMovie('Images/main-window/dreams-page/envelope-btn/message.gif')
        self.label_message1.resize(300, 200)
        self.label_message1.setMovie(self.movie_message1)
        self.movie_message1.start()

        self.button_exit = QPushButton(self)
        self.button_exit.resize(30, 30)
        self.button_exit.setStyleSheet("""
            QPushButton {
                border-image:url(Images/start-window/x-btn/x-btni.png);
            }
            QPushButton:hover {
                border-image:url(Images/start-window/x-btn/x-btnf.png)
            }
        """)
        self.button_exit.clicked.connect(self.close)
        self.button_exit.move(263, 5)
        self.button_exit.show()

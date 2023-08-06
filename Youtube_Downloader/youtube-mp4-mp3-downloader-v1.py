from fileinput import filename
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from pytube import YouTube
import sys
import time
import threading
import os
from pathlib import Path


class Main(QMainWindow):

    # init function, main function
    def __init__(self):
        super(Main, self).__init__()

        # set window's title, width, and height
        self.setWindowTitle("Youtube Downloader")
        self.setFixedWidth(400)
        self.setFixedHeight(135)

        # label for downloading progress
        self.label_prog = QLabel(" ", self)
        self.label_prog.move(150, 70)

        # label for url input line
        self.label_url = QLabel("URL: ", self)
        self.label_url.move(50, 27)

        # label for file type combo box
        self.label_type = QLabel("File Type: ", self)
        self.label_type.move(50, 60)

        # input url
        self.entry_url = QLineEdit(self)
        self.entry_url.resize(250, 20)
        self.entry_url.move(80, 30)

        # choose file type (that will be downloaded)
        self.cb = QComboBox(self)
        self.cb.addItem("mp4")
        self.cb.addItem("mp3")
        self.cb.move(110, 65)
        self.cb.resize(55, 20)

        # button to download url
        # connect to download() event
        self.btn_download = QPushButton("Download", self)
        self.btn_download.clicked.connect(self.initiate)
        self.btn_download.resize(65, 22)
        self.btn_download.move(266, 64)

    # thread function. prevents window from freezing
    def initiate(self):

        # call threading and set target to -> download()
        self.task = threading.Thread(target = self.download)
        self.task.start()

    # download url in mp4 format
    def mp4(self):

        # hide some main widgets
        self.btn_download.hide()
        self.label_type.hide()
        self.cb.hide()

        # show progress label
        self.label_prog.show()

        # config progress label
        self.label_prog.setText("Downloading...")
        self.label_prog.move(160, 60)
        self.label_prog.show()

        try:
            # gets user's input link
            url = self.entry_url.text()
            yt_link = YouTube(url) # use pytube module

            # download -> mp4
            downloads_path = str(Path.home() / "Downloads")
            yt_link.streams.get_highest_resolution().download(output_path=downloads_path)

            # config progress label
            self.label_prog.setText("Successfully Downloaded!")
            self.label_prog.resize(200, 20)
            self.label_prog.move(125, 60)
            self.label_prog.show()

            # set 3 second...
            time.sleep(3)
            # set input to " "
            self.entry_url.setText(" ")
            self.btn_download.show()
            self.label_type.show()
            self.cb.show()
            self.label_prog.hide()

        except:

            # config progress label
            self.label_prog.setText("Unsuccessfully Downloaded!")
            self.label_prog.resize(195, 20)
            self.label_prog.move(125, 60)
            self.label_prog.show()

            # set 3 second...
            time.sleep(3)
            # set input to " "
            self.entry_url.setText(" ")
            self.btn_download.show()
            self.label_type.show()
            self.cb.show()
            self.label_prog.hide()

    # download url in mp3 format
    def mp3(self):

        # hide some main widgets
        self.btn_download.hide()
        self.label_type.hide()
        self.cb.hide()

        # show progress label
        self.label_prog.show()

        # config progress label
        self.label_prog.setText("Downloading...")
        self.label_prog.move(160, 60)
        self.label_prog.show()

        try:
            print('starting...')
            # get audio of the link
            url = self.entry_url.text()
            yt_link = YouTube(url)
            
            video = yt_link.streams.filter(only_audio=True).first()

            # set's file location
            downloads_path = str(Path.home() / "Downloads")

            # download -> mp3
            out_file = video.download(output_path=downloads_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # config progress label
            self.label_prog.setText("Successfully Downloaded!")
            self.label_prog.resize(200, 20)
            self.label_prog.move(125, 60)
            self.label_prog.show()

            # set 3 second...
            time.sleep(3)
            # set input to " "
            self.entry_url.setText(" ")
            self.btn_download.show()
            self.label_type.show()
            self.cb.show()
            self.label_prog.hide()

        except:

            # config progress label
            self.label_prog.setText("Unsuccessfully Downloaded!")
            self.label_prog.resize(195, 20)
            self.label_prog.move(125, 60)
            self.label_prog.show()

            # set 3 second...
            time.sleep(3)
            # set input to " "
            self.entry_url.setText(" ")
            self.btn_download.show()
            self.label_type.show()
            self.cb.show()
            self.label_prog.hide()

    # function to start downloading
    def download(self):

        # gets value of combo box
        cb = self.cb.currentText()

        # condition
        if cb == "mp4":
            self.mp4()
        if cb == "mp3":
            self.mp3()


# starts the gui
app = QApplication([])
window = Main()
window.show()
sys.exit(app.exec())
import os
import time
import winsound
import datetime
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QMessageBox
from PyQt6.uic.uiparser import QtGui
from add_database import mainDb
from notif_database import notification
from progress_database import prog
from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
                              QChartView, QValueAxis)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_widget(QDialog):

    timeSave = []
    timeAdd = []

    value = ''

    def setupUi(self, widget):

        widget.setObjectName("widget")
        widget.resize(980, 500)
        widget.setWindowIcon(QIcon('images/paalala-logo.png'))

        self.background = QtWidgets.QLabel(parent=widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 980, 500))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("images/main-window/background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        self.calendar_button = QtWidgets.QPushButton(parent=widget)
        self.calendar_button.setEnabled(True)
        self.calendar_button.setGeometry(QtCore.QRect(30, 50, 100, 70))
        self.calendar_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button.setMouseTracking(True)
        self.calendar_button.setAutoFillBackground(False)
        self.calendar_button.setStyleSheet("QPushButton {\n"
                                           "border-image:url(images/main-window/calendar_button/8.png);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "border-image:url(images/main-window/calendar_button/9.png);\n"
                                           "}")
        self.calendar_button.setText("")
        self.calendar_button.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button.setObjectName("calendar_button")
        self.statistics_button = QtWidgets.QPushButton(parent=widget)
        self.statistics_button.setGeometry(QtCore.QRect(30, 130, 100, 70))
        self.statistics_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.statistics_button.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/statistics_button/11.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/statistics_button/12.png);\n"
                                             "}")
        self.statistics_button.setText("")
        self.statistics_button.setObjectName("statistics_button")
        self.medication_button = QtWidgets.QPushButton(parent=widget)
        self.medication_button.setGeometry(QtCore.QRect(30, 210, 100, 70))
        self.medication_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.medication_button.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/medication_button/14.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/medication_button/15.png);\n"
                                             "}")
        self.medication_button.setText("")
        self.medication_button.setObjectName("medication_button")
        self.add_button = QtWidgets.QPushButton(parent=widget)
        self.add_button.setGeometry(QtCore.QRect(30, 290, 100, 70))
        self.add_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add_button.setStyleSheet("QPushButton {\n"
                                      "border-image:url(images/main-window/add_button/17.png);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "border-image:url(images/main-window/add_button/18.png);\n"
                                      "}")
        self.add_button.setText("")
        self.add_button.setObjectName("add_button")
        self.notification_button = QtWidgets.QPushButton(parent=widget)
        self.notification_button.setGeometry(QtCore.QRect(30, 370, 100, 70))
        self.notification_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.notification_button.setStyleSheet("QPushButton {\n"
                                               "border-image:url(images/main-window/notification_button/20.png);\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "border-image:url(images/main-window/notification_button/21.png);\n"
                                               "}")
        self.notification_button.setText("")
        self.notification_button.setObjectName("notification_button")
        self.calendar_canvas = QtWidgets.QLabel(parent=widget)
        self.calendar_canvas.setGeometry(QtCore.QRect(100, 30, 800, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calendar_canvas.setFont(font)
        self.calendar_canvas.setText("")
        self.calendar_canvas.setPixmap(QtGui.QPixmap("images/main-window/calendar_canvas.png"))
        self.calendar_canvas.setScaledContents(True)
        self.calendar_canvas.setObjectName("calendar_canvas")
        self.about_button = QtWidgets.QPushButton(parent=widget)
        self.about_button.setEnabled(True)
        self.about_button.setGeometry(QtCore.QRect(900, 440, 50, 35))
        self.about_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.about_button.setMouseTracking(True)
        self.about_button.setAutoFillBackground(False)
        self.about_button.setStyleSheet("QPushButton {\n"
                                        "border-image:url(images/main-window/about_button/23.png);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border-image:url(images/main-window/about_button/24.png);\n"
                                        "}")
        self.about_button.setText("")
        self.about_button.setIconSize(QtCore.QSize(200, 80))
        self.about_button.setObjectName("about_button")
        self.profile_button = QtWidgets.QPushButton(parent=widget)
        self.profile_button.setEnabled(True)
        self.profile_button.setGeometry(QtCore.QRect(850, 30, 140, 70))
        self.profile_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.profile_button.setMouseTracking(True)
        self.profile_button.setAutoFillBackground(False)
        self.profile_button.setStyleSheet("QPushButton {\n"
                                          "border-image:url(images/main-window/other/3.png)}")
        self.profile_button.setToolTip(f'User: {os.getlogin()}')
        self.profile_button.setText("")
        self.profile_button.setIconSize(QtCore.QSize(200, 80))
        self.profile_button.setObjectName("profile_button")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=widget)
        self.stackedWidget.setGeometry(QtCore.QRect(143, 66, 711, 378))
        self.stackedWidget.setObjectName("stackedWidget")
        self.calendar_page = QtWidgets.QWidget()
        self.calendar_page.setObjectName("calendar_page")
        self.cDate = QtWidgets.QLabel(parent=self.calendar_page)
        self.cDate.setGeometry(QtCore.QRect(20, -5, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.cDate.setFont(font)
        self.cDate.setObjectName("cDate")
        self.line1 = QtWidgets.QLabel(parent=self.calendar_page)
        self.line1.setGeometry(QtCore.QRect(20, 60, 651, 2))
        self.line1.setText("")
        self.line1.setPixmap(QtGui.QPixmap("images/main-window/black.png"))
        self.line1.setScaledContents(True)
        self.line1.setObjectName("line1")
        self.sun = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun.setGeometry(QtCore.QRect(30, 60, 80, 52))
        self.sun.setText("")
        self.sun.setPixmap(QtGui.QPixmap("images/main-window/days_str/52.png"))
        self.sun.setScaledContents(True)
        self.sun.setObjectName("sun")
        self.sun_2 = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun_2.setGeometry(QtCore.QRect(125, 60, 80, 52))
        self.sun_2.setText("")
        self.sun_2.setPixmap(QtGui.QPixmap("images/main-window/days_str/53.png"))
        self.sun_2.setScaledContents(True)
        self.sun_2.setObjectName("sun_2")
        self.sun_3 = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun_3.setGeometry(QtCore.QRect(215, 60, 80, 52))
        self.sun_3.setText("")
        self.sun_3.setPixmap(QtGui.QPixmap("images/main-window/days_str/54.png"))
        self.sun_3.setScaledContents(True)
        self.sun_3.setObjectName("sun_3")
        self.sun_4 = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun_4.setGeometry(QtCore.QRect(305, 60, 80, 52))
        self.sun_4.setText("")
        self.sun_4.setPixmap(QtGui.QPixmap("images/main-window/days_str/55.png"))
        self.sun_4.setScaledContents(True)
        self.sun_4.setObjectName("sun_4")
        self.sun_6 = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun_6.setGeometry(QtCore.QRect(395, 60, 80, 52))
        self.sun_6.setText("")
        self.sun_6.setPixmap(QtGui.QPixmap("images/main-window/days_str/56.png"))
        self.sun_6.setScaledContents(True)
        self.sun_6.setObjectName("sun_6")
        self.sun_5 = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun_5.setGeometry(QtCore.QRect(485, 60, 80, 52))
        self.sun_5.setText("")
        self.sun_5.setPixmap(QtGui.QPixmap("images/main-window/days_str/57.png"))
        self.sun_5.setScaledContents(True)
        self.sun_5.setObjectName("sun_5")
        self.sun_7 = QtWidgets.QLabel(parent=self.calendar_page)
        self.sun_7.setGeometry(QtCore.QRect(575, 60, 80, 52))
        self.sun_7.setText("")
        self.sun_7.setPixmap(QtGui.QPixmap("images/main-window/days_str/58.png"))
        self.sun_7.setScaledContents(True)
        self.sun_7.setObjectName("sun_7")
        self.line1_2 = QtWidgets.QLabel(parent=self.calendar_page)
        self.line1_2.setGeometry(QtCore.QRect(20, 110, 651, 2))
        self.line1_2.setText("")
        self.line1_2.setPixmap(QtGui.QPixmap("images/main-window/black.png"))
        self.line1_2.setScaledContents(True)
        self.line1_2.setObjectName("line1_2")

        self.day1 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.day1.setEnabled(True)
        self.day1.setGeometry(QtCore.QRect(405, 120, 61, 41))
        self.day1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.day1.setMouseTracking(True)
        self.day1.setAutoFillBackground(False)
        self.day1.setStyleSheet("QPushButton {\n"
                                 "border-image:url(images/main-window/days_int/d1.png);\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "border-image:url(images/main-window/days_int/d1.1.png);\n"
                                 "}")
        self.day1.setText("")
        self.day1.setIconSize(QtCore.QSize(200, 80))
        self.day1.setObjectName("d1")

        self.d14 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.d14.setEnabled(True)
        self.d14.setGeometry(QtCore.QRect(405, 220, 61, 41))
        self.d14.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.d14.setMouseTracking(True)
        self.d14.setAutoFillBackground(False)
        self.d14.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/days_int/d14.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/days_int/d14.1.png);\n"
                                             "}")
        self.d14.setText("")
        self.d14.setIconSize(QtCore.QSize(200, 80))
        self.d14.setObjectName("d14")

        self.day8 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.day8.setEnabled(True)
        self.day8.setGeometry(QtCore.QRect(405, 170, 61, 41))
        self.day8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.day8.setMouseTracking(True)
        self.day8.setAutoFillBackground(False)
        self.day8.setStyleSheet("QPushButton {\n"
                                 "border-image:url(images/main-window/days_int/8.png);\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "border-image:url(images/main-window/days_int/8.1.png);\n"
                                 "}")
        self.day8.setText("")
        self.day8.setIconSize(QtCore.QSize(200, 80))
        self.day8.setObjectName("june8")

        self.d26 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.d26.setEnabled(True)
        self.d26.setGeometry(QtCore.QRect(135, 320, 61, 41))
        self.d26.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.d26.setMouseTracking(True)
        self.d26.setAutoFillBackground(False)
        self.d26.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/days_int/d26.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/days_intn/d26.1.png);\n"
                                             "}")
        self.d26.setText("")
        self.d26.setIconSize(QtCore.QSize(200, 80))
        self.d26.setObjectName("d26")

        self.day2 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.day2.setEnabled(True)
        self.day2.setGeometry(QtCore.QRect(495, 120, 61, 41))
        self.day2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.day2.setMouseTracking(True)
        self.day2.setAutoFillBackground(False)
        self.day2.setStyleSheet("QPushButton {\n"
                                 "border-image:url(images/main-window/days_int/d2.png);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "border-image:url(images/main-window/days_int/d2.1.png);\n"
                                 "}")
        self.day2.setText("")
        self.day2.setIconSize(QtCore.QSize(200, 80))
        self.day2.setObjectName("d2")

        self.day3 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.day3.setEnabled(True)
        self.day3.setGeometry(QtCore.QRect(585, 120, 61, 41))
        self.day3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.day3.setMouseTracking(True)
        self.day3.setAutoFillBackground(False)
        self.day3.setStyleSheet("QPushButton {\n"
                                 "border-image:url(images/main-window/days_int/d3.png);\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "border-image:url(images/main-window/days_int/d3.1.png);\n"
                                 "}")
        self.day3.setText("")
        self.day3.setIconSize(QtCore.QSize(200, 80))
        self.day3.setObjectName("june3")

        self.d9 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.d9.setEnabled(True)
        self.d9.setGeometry(QtCore.QRect(495, 170, 61, 41))
        self.d9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.d9.setMouseTracking(True)
        self.d9.setAutoFillBackground(False)
        self.d9.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/days_int/d9.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/days_int/d9.1.png);\n"
                                             "}")
        self.d9.setText("")
        self.d9.setIconSize(QtCore.QSize(200, 80))
        self.d9.setObjectName("d9")

        self.d10 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.d10.setEnabled(True)
        self.d10.setGeometry(QtCore.QRect(585, 170, 61, 41))
        self.d10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.d10.setMouseTracking(True)
        self.d10.setAutoFillBackground(False)
        self.d10.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/days_int/d10.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/days_int/d10.1.png);\n"
                                             "}")
        self.d10.setText("")
        self.d10.setIconSize(QtCore.QSize(200, 80))
        self.d10.setObjectName("d10")

        self.d16 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.d16.setEnabled(True)
        self.d16.setGeometry(QtCore.QRect(495, 220, 61, 41))
        self.d16.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.d16.setMouseTracking(True)
        self.d16.setAutoFillBackground(False)
        self.d16.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/days_int/d16.png);\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/days_int/d16.1.png);\n"
                                             "}")
        self.d16.setText("")
        self.d16.setIconSize(QtCore.QSize(200, 80))
        self.d16.setObjectName("d16")

        self.d17 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.d17.setEnabled(True)
        self.d17.setGeometry(QtCore.QRect(585, 220, 61, 41))
        self.d17.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.d17.setMouseTracking(True)
        self.d17.setAutoFillBackground(False)
        self.d17.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/d17.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/days_int/d17.1.png);\n"
                                              "}")
        self.d17.setText("")
        self.d17.setIconSize(QtCore.QSize(200, 80))
        self.d17.setObjectName("d17")

        self.calendar_button_11 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_11.setEnabled(True)
        self.calendar_button_11.setGeometry(QtCore.QRect(405, 270, 61, 41))
        self.calendar_button_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_11.setMouseTracking(True)
        self.calendar_button_11.setAutoFillBackground(False)
        self.calendar_button_11.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/34.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/35.png);\n"
                                              "}")
        self.calendar_button_11.setText("")
        self.calendar_button_11.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_11.setObjectName("calendar_button_11")
        self.calendar_button_12 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_12.setEnabled(True)
        self.calendar_button_12.setGeometry(QtCore.QRect(495, 270, 61, 41))
        self.calendar_button_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_12.setMouseTracking(True)
        self.calendar_button_12.setAutoFillBackground(False)
        self.calendar_button_12.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/59.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/37.png);\n"
                                              "}")
        self.calendar_button_12.setText("")
        self.calendar_button_12.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_12.setObjectName("calendar_button_12")
        self.calendar_button_13 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_13.setEnabled(True)
        self.calendar_button_13.setGeometry(QtCore.QRect(225, 320, 61, 41))
        self.calendar_button_13.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_13.setMouseTracking(True)
        self.calendar_button_13.setAutoFillBackground(False)
        self.calendar_button_13.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/38.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/39.png);\n"
                                              "}")
        self.calendar_button_13.setText("")
        self.calendar_button_13.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_13.setObjectName("calendar_button_13")
        self.calendar_button_14 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_14.setEnabled(True)
        self.calendar_button_14.setGeometry(QtCore.QRect(315, 320, 61, 41))
        self.calendar_button_14.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_14.setMouseTracking(True)
        self.calendar_button_14.setAutoFillBackground(False)
        self.calendar_button_14.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/40.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/41.png);\n"
                                              "}")
        self.calendar_button_14.setText("")
        self.calendar_button_14.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_14.setObjectName("calendar_button_14")
        self.calendar_button_15 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_15.setEnabled(True)
        self.calendar_button_15.setGeometry(QtCore.QRect(35, 170, 61, 41))
        self.calendar_button_15.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_15.setMouseTracking(True)
        self.calendar_button_15.setAutoFillBackground(False)
        self.calendar_button_15.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/42.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/43.png);\n"
                                              "}")
        self.calendar_button_15.setText("")
        self.calendar_button_15.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_15.setObjectName("calendar_button_15")
        self.calendar_button_16 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_16.setEnabled(True)
        self.calendar_button_16.setGeometry(QtCore.QRect(135, 170, 61, 41))
        self.calendar_button_16.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_16.setMouseTracking(True)
        self.calendar_button_16.setAutoFillBackground(False)
        self.calendar_button_16.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/44.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/45.png);\n"
                                              "}")
        self.calendar_button_16.setText("")
        self.calendar_button_16.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_16.setObjectName("calendar_button_16")
        self.calendar_button_17 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_17.setEnabled(True)
        self.calendar_button_17.setGeometry(QtCore.QRect(225, 170, 61, 41))
        self.calendar_button_17.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_17.setMouseTracking(True)
        self.calendar_button_17.setAutoFillBackground(False)
        self.calendar_button_17.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/46.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/47.png);\n"
                                              "}")
        self.calendar_button_17.setText("")
        self.calendar_button_17.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_17.setObjectName("calendar_button_17")
        self.calendar_button_18 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_18.setEnabled(True)
        self.calendar_button_18.setGeometry(QtCore.QRect(315, 170, 61, 41))
        self.calendar_button_18.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_18.setMouseTracking(True)
        self.calendar_button_18.setAutoFillBackground(False)
        self.calendar_button_18.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/48.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/49.png);\n"
                                              "}")
        self.calendar_button_18.setText("")
        self.calendar_button_18.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_18.setObjectName("calendar_button_18")
        self.calendar_button_19 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_19.setEnabled(True)
        self.calendar_button_19.setGeometry(QtCore.QRect(35, 220, 61, 41))
        self.calendar_button_19.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_19.setMouseTracking(True)
        self.calendar_button_19.setAutoFillBackground(False)
        self.calendar_button_19.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/50.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/51.png);\n"
                                              "}")
        self.calendar_button_19.setText("")
        self.calendar_button_19.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_19.setObjectName("calendar_button_19")
        self.calendar_button_20 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_20.setEnabled(True)
        self.calendar_button_20.setGeometry(QtCore.QRect(135, 220, 61, 41))
        self.calendar_button_20.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_20.setMouseTracking(True)
        self.calendar_button_20.setAutoFillBackground(False)
        self.calendar_button_20.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/52.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/53.png);\n"
                                              "}")
        self.calendar_button_20.setText("")
        self.calendar_button_20.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_20.setObjectName("calendar_button_20")
        self.calendar_button_21 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_21.setEnabled(True)
        self.calendar_button_21.setGeometry(QtCore.QRect(315, 220, 61, 41))
        self.calendar_button_21.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_21.setMouseTracking(True)
        self.calendar_button_21.setAutoFillBackground(False)
        self.calendar_button_21.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/54.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/55.png);\n"
                                              "}")
        self.calendar_button_21.setText("")
        self.calendar_button_21.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_21.setObjectName("calendar_button_21")
        self.calendar_button_22 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_22.setEnabled(True)
        self.calendar_button_22.setGeometry(QtCore.QRect(225, 220, 61, 41))
        self.calendar_button_22.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_22.setMouseTracking(True)
        self.calendar_button_22.setAutoFillBackground(False)
        self.calendar_button_22.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/56.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/57.png);\n"
                                              "}")
        self.calendar_button_22.setText("")
        self.calendar_button_22.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_22.setObjectName("calendar_button_22")
        self.calendar_button_23 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_23.setEnabled(True)
        self.calendar_button_23.setGeometry(QtCore.QRect(35, 270, 61, 41))
        self.calendar_button_23.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_23.setMouseTracking(True)
        self.calendar_button_23.setAutoFillBackground(False)
        self.calendar_button_23.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/58.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/59.png);\n"
                                              "}")
        self.calendar_button_23.setText("")
        self.calendar_button_23.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_23.setObjectName("calendar_button_23")
        self.calendar_button_24 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_24.setEnabled(True)
        self.calendar_button_24.setGeometry(QtCore.QRect(135, 270, 61, 41))
        self.calendar_button_24.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_24.setMouseTracking(True)
        self.calendar_button_24.setAutoFillBackground(False)
        self.calendar_button_24.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/60.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/61.png);\n"
                                              "}")
        self.calendar_button_24.setText("")
        self.calendar_button_24.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_24.setObjectName("calendar_button_24")
        self.calendar_button_25 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_25.setEnabled(True)
        self.calendar_button_25.setGeometry(QtCore.QRect(225, 270, 61, 41))
        self.calendar_button_25.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_25.setMouseTracking(True)
        self.calendar_button_25.setAutoFillBackground(False)
        self.calendar_button_25.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/62.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/63.png);\n"
                                              "}")
        self.calendar_button_25.setText("")
        self.calendar_button_25.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_25.setObjectName("calendar_button_25")
        self.calendar_button_26 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_26.setEnabled(True)
        self.calendar_button_26.setGeometry(QtCore.QRect(315, 270, 61, 41))
        self.calendar_button_26.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_26.setMouseTracking(True)
        self.calendar_button_26.setAutoFillBackground(False)
        self.calendar_button_26.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/64.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/65.png);\n"
                                              "}")
        self.calendar_button_26.setText("")
        self.calendar_button_26.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_26.setObjectName("calendar_button_26")
        self.calendar_button_27 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_27.setEnabled(True)
        self.calendar_button_27.setGeometry(QtCore.QRect(585, 270, 61, 41))
        self.calendar_button_27.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_27.setMouseTracking(True)
        self.calendar_button_27.setAutoFillBackground(False)
        self.calendar_button_27.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/66.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/67.png);\n"
                                              "}")
        self.calendar_button_27.setText("")
        self.calendar_button_27.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_27.setObjectName("calendar_button_27")
        self.calendar_button_28 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_28.setEnabled(True)
        self.calendar_button_28.setGeometry(QtCore.QRect(35, 320, 61, 41))
        self.calendar_button_28.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_28.setMouseTracking(True)
        self.calendar_button_28.setAutoFillBackground(False)
        self.calendar_button_28.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/68.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/69.png);\n"
                                              "}")
        self.calendar_button_28.setText("")
        self.calendar_button_28.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_28.setObjectName("calendar_button_28")
        self.calendar_button_7 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_7.setEnabled(True)
        self.calendar_button_7.setGeometry(QtCore.QRect(405, 320, 61, 41))
        self.calendar_button_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_7.setMouseTracking(True)
        self.calendar_button_7.setAutoFillBackground(False)
        self.calendar_button_7.setStyleSheet("QPushButton {\n"
                                             "border-image:url(images/main-window/days_int/69.png)\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "border-image:url(images/main-window/calendar_button/30.png);\n"
                                             "}")
        self.calendar_button_7.setText("")
        self.calendar_button_7.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_7.setObjectName("calendar_button_7")
        self.calendar_button_29 = QtWidgets.QPushButton(parent=self.calendar_page)
        self.calendar_button_29.setEnabled(True)
        self.calendar_button_29.setGeometry(QtCore.QRect(495, 320, 61, 41))
        self.calendar_button_29.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.calendar_button_29.setMouseTracking(True)
        self.calendar_button_29.setAutoFillBackground(False)
        self.calendar_button_29.setStyleSheet("QPushButton {\n"
                                              "border-image:url(images/main-window/days_int/70.png);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "border-image:url(images/main-window/calendar_button/71.png);\n"
                                              "}")
        self.calendar_button_29.setText("")
        self.calendar_button_29.setIconSize(QtCore.QSize(200, 80))
        self.calendar_button_29.setObjectName("calendar_button_29")
        self.stackedWidget.addWidget(self.calendar_page)
        self.notification_page = QtWidgets.QWidget()
        self.notification_page.setObjectName("notification_page")
        self.cDate_2 = QtWidgets.QLabel(parent=self.notification_page)
        self.cDate_2.setGeometry(QtCore.QRect(20, -5, 410, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.cDate_2.setFont(font)
        self.cDate_2.setObjectName("cDate_2")
        self.line1_5 = QtWidgets.QLabel(parent=self.notification_page)
        self.line1_5.setGeometry(QtCore.QRect(20, 60, 661, 2))
        self.line1_5.setText("")
        self.line1_5.setPixmap(QtGui.QPixmap(".\\images/main-window/black.png"))
        self.line1_5.setScaledContents(True)
        self.line1_5.setObjectName("line1_5")
        self.notifications_list = QtWidgets.QListWidget(parent=self.notification_page)
        self.notifications_list.setGeometry(QtCore.QRect(20, 70, 661, 281))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(14)
        self.notifications_list.setFont(font)
        self.notifications_list.setMouseTracking(True)
        self.notifications_list.setObjectName("notifications_list")
        self.try_notif = QtWidgets.QPushButton(parent=self.notification_page)
        self.try_notif.setGeometry(QtCore.QRect(20, 350, 75, 24))
        self.try_notif.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.try_notif.setObjectName("try_notif")
        self.stackedWidget.addWidget(self.notification_page)
        self.med_page = QtWidgets.QWidget()
        self.med_page.setObjectName("med_page")
        self.medicationsTxt = QtWidgets.QLabel(parent=self.med_page)
        self.medicationsTxt.setGeometry(QtCore.QRect(20, -5, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.medicationsTxt.setFont(font)
        self.medicationsTxt.setObjectName("medicationsTxt")
        self.line1_4 = QtWidgets.QLabel(parent=self.med_page)
        self.line1_4.setGeometry(QtCore.QRect(25, 60, 651, 2))
        self.line1_4.setText("")
        self.line1_4.setPixmap(QtGui.QPixmap(".\\images/main-window/black.png"))
        self.line1_4.setScaledContents(True)
        self.line1_4.setObjectName("line1_4")
        self.listMedIncomplete = QtWidgets.QListWidget(parent=self.med_page)
        self.listMedIncomplete.setGeometry(QtCore.QRect(110, 110, 231, 231))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(14)
        font.setBold(False)
        self.listMedIncomplete.setFont(font)
        self.listMedIncomplete.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.listMedIncomplete.setStyleSheet("QListWidget{\n"
                                             "background: (255, 255, 255, 0.5);\n"
                                             "border: 0.5px solid;\n"
                                             "}")
        self.listMedIncomplete.setObjectName("listMedIncomplete")
        self.medicationsTxt_2 = QtWidgets.QLabel(parent=self.med_page)
        self.medicationsTxt_2.setGeometry(QtCore.QRect(110, 60, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.medicationsTxt_2.setFont(font)
        self.medicationsTxt_2.setObjectName("medicationsTxt_2")
        self.listMedComplete = QtWidgets.QListWidget(parent=self.med_page)
        self.listMedComplete.setGeometry(QtCore.QRect(400, 110, 231, 231))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(14)
        font.setBold(False)
        self.listMedComplete.setFont(font)
        self.listMedComplete.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.listMedComplete.setStyleSheet("QListWidget{\n"
                                           "background: (255, 255, 255, 0.5);\n"
                                           "border: 0.5px solid;\n"
                                           "}")
        self.listMedComplete.setAutoScrollMargin(16)
        self.listMedComplete.setObjectName("listMedComplete")
        self.medicationsTxt_3 = QtWidgets.QLabel(parent=self.med_page)
        self.medicationsTxt_3.setGeometry(QtCore.QRect(400, 60, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.medicationsTxt_3.setFont(font)
        self.medicationsTxt_3.setObjectName("medicationsTxt_3")
        self.stackedWidget.addWidget(self.med_page)
        self.stats_page = QtWidgets.QWidget()
        self.stats_page.setObjectName("stats_page")
        self.medicationsTxt_4 = QtWidgets.QLabel(parent=self.stats_page)
        self.medicationsTxt_4.setGeometry(QtCore.QRect(20, -5, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.medicationsTxt_4.setFont(font)
        self.medicationsTxt_4.setObjectName("medicationsTxt_4")
        self.line1_6 = QtWidgets.QLabel(parent=self.stats_page)
        self.line1_6.setGeometry(QtCore.QRect(25, 60, 651, 2))
        self.line1_6.setText("")
        self.line1_6.setPixmap(QtGui.QPixmap(".\\images/main-window/black.png"))
        self.line1_6.setScaledContents(True)
        self.line1_6.setObjectName("line1_6")
        self.stackedWidget.addWidget(self.stats_page)
        self.addMed_page = QtWidgets.QWidget()
        self.addMed_page.setObjectName("addMed_page")
        self.addTitle = QtWidgets.QLabel(parent=self.addMed_page)
        self.addTitle.setGeometry(QtCore.QRect(20, -5, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.addTitle.setFont(font)
        self.addTitle.setObjectName("addTitle")
        self.line1_3 = QtWidgets.QLabel(parent=self.addMed_page)
        self.line1_3.setGeometry(QtCore.QRect(20, 60, 661, 2))
        self.line1_3.setText("")
        self.line1_3.setPixmap(QtGui.QPixmap(".\\images/main-window/black.png"))
        self.line1_3.setScaledContents(True)
        self.line1_3.setObjectName("line1_3")
        self.medecineTxt = QtWidgets.QLabel(parent=self.addMed_page)
        self.medecineTxt.setGeometry(QtCore.QRect(80, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.medecineTxt.setFont(font)
        self.medecineTxt.setObjectName("medecineTxt")
        self.medicineInput = QtWidgets.QLineEdit(parent=self.addMed_page)
        self.medicineInput.setGeometry(QtCore.QRect(180, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.medicineInput.setFont(font)
        self.medicineInput.setStyleSheet("QLineEdit{\n"
                                         "border: 1px solid black;\n"
                                         "border-radius: 5px;\n"
                                         "padding: 0 8px;\n"
                                         "selection-background-color: rgb(255, 158, 170);\n"
                                         "}")
        self.medicineInput.setObjectName("medicineInput")
        self.daysTxt = QtWidgets.QLabel(parent=self.addMed_page)
        self.daysTxt.setGeometry(QtCore.QRect(80, 170, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.daysTxt.setFont(font)
        self.daysTxt.setObjectName("daysTxt")
        self.daysInput = QtWidgets.QLineEdit(parent=self.addMed_page)
        self.daysInput.setGeometry(QtCore.QRect(230, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.daysInput.setFont(font)
        self.daysInput.setStyleSheet("QLineEdit{\n"
                                     "border: 1px solid black;\n"
                                     "border-radius: 5px;\n"
                                     "padding: 0 8px;\n"
                                     "selection-background-color: rgb(255, 158, 170);\n"
                                     "}")
        self.daysInput.setObjectName("daysInput")
        self.timeTxt = QtWidgets.QLabel(parent=self.addMed_page)
        self.timeTxt.setGeometry(QtCore.QRect(80, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.timeTxt.setFont(font)
        self.timeTxt.setObjectName("timeTxt")
        self.timeIntake = QtWidgets.QTimeEdit(parent=self.addMed_page)
        self.timeIntake.setGeometry(QtCore.QRect(230, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.timeIntake.setFont(font)
        self.timeIntake.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.timeIntake.setStyleSheet("border: 1px solid black;\n"
                                      "border-radius: 5px;")
        self.timeIntake.setObjectName("timeIntake")
        self.addTime_button = QtWidgets.QPushButton(parent=self.addMed_page)
        self.addTime_button.setGeometry(QtCore.QRect(380, 225, 31, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.addTime_button.setFont(font)
        self.addTime_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addTime_button.setStyleSheet("border: 1px solid black;\n"
                                          "border-radius: 10px;\n"
                                          "background-color: white;\n"
                                          "\n"
                                          "QPushButton#pushButton:hover {\n"
                                          "     background-color: rgb(255, 158, 170);\n"
                                          " }\n"
                                          "")
        self.addTime_button.setObjectName("addTime_button")
        self.addButton = QtWidgets.QPushButton(parent=self.addMed_page)
        self.addButton.setGeometry(QtCore.QRect(570, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.addButton.setStyleSheet("border: 1px solid black;\n"
                                     "border-radius: 10px;\n"
                                     "background-color: white;\n"
                                     "\n"
                                     "QPushButton#pushButton:hover {\n"
                                     "     background-color: rgb(255, 158, 170);\n"
                                     " }\n"
                                     "")
        self.addButton.setObjectName("addButton")
        self.successTxt = QtWidgets.QLabel(parent=self.addMed_page)
        self.successTxt.setGeometry(QtCore.QRect(592, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        self.successTxt.setFont(font)
        self.successTxt.setText("")
        self.successTxt.setObjectName("successTxt")
        self.addedTxt = QtWidgets.QLabel(parent=self.addMed_page)
        self.addedTxt.setGeometry(QtCore.QRect(210, 260, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        self.addedTxt.setFont(font)
        self.addedTxt.setText("")
        self.addedTxt.setObjectName("addedTxt")
        self.stackedWidget.addWidget(self.addMed_page)

        self.retranslateUi(widget)
        self.stackedWidget.setCurrentIndex(0)
        self.listMedIncomplete.setCurrentRow(-1)
        self.listMedComplete.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(widget)

        self.calendar()
        self.updateMedList()
        self.notification()

        # thread to minimize crashes
        self.thread_manager = QThreadPool()
        self.thread_manager.start(self.setTime)

        # pages
        self.add_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.addMed_page))
        self.statistics_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.stats_page))
        self.notification_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.notification_page))
        self.medication_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.med_page))
        self.calendar_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.calendar_page))

        # button
        self.addTime_button.clicked.connect(self.addTime)
        self.addButton.clicked.connect(self.saveMedication)
        self.medication_button.clicked.connect(self.updateMedList)
        self.notification_button.clicked.connect(self.notification)
        self.statistics_button.clicked.connect(self.plotCanvas)

        self.try_notif.clicked.connect(self.tryButton)

    def calendar(self):

        # current date
        current_date = datetime.datetime.now()
        month = current_date.month
        day = current_date.day
        year = current_date.year

        if month == 1:
            self.cDate.setText(f'JANUARY {str(day)}, {str(year)}')
        elif month == 2:
            self.cDate.setText(f'FEBRUARY {str(day)}, {str(year)}')
        elif month == 3:
            self.cDate.setText(f'MARCH {str(day)}, {str(year)}')
        elif month == 4:
            self.cDate.setText(f'APRIL {str(day)}, {str(year)}')
        elif month == 5:
            self.cDate.setText(f'MAY {str(day)}, {str(year)}')
        elif month == 6:
            self.cDate.setText(f'JUNE {str(day)}, {str(year)}')
        elif month == 7:
            self.cDate.setText(f'JULY {str(day)}, {str(year)}')
        elif month == 8:
            self.cDate.setText(f'AUGUST {str(day)}, {str(year)}')
        elif month == 9:
            self.cDate.setText(f'SEPTEMBER {str(day)}, {str(year)}')
        elif month == 10:
            self.cDate.setText(f'OCTOBER {str(day)}, {str(year)}')
        elif month == 11:
            self.cDate.setText(f'NOVEMBER {str(day)}, {str(year)}')
        elif month == 12:
            self.cDate.setText(f'DECEMBER {str(day)}, {str(year)}')

    def saveMedication(self):

        try:
            self.time_con = ''

            if len(Ui_widget.timeAdd) == 0:
                setTime = self.timeIntake.time()
                setTimeConverted = setTime.toPyTime()
                Ui_widget.timeSave.append(str(setTimeConverted))
                for time in Ui_widget.timeSave:
                    self.time_con += time
                    self.time_con += ';'
            else:
                for time in Ui_widget.timeAdd:
                    self.time_con += time
                    self.time_con += ';'

            db = mainDb()
            data = [(str(self.medicineInput.text()).lower(), str(self.daysInput.text()).lower(), self.time_con)]
            db.create_table_info()
            db.insert_data_info(data)
            db.close_conn_info()

            Ui_widget.timeSave.clear()
            Ui_widget.timeAdd.clear()

            self.successTxt.setText('Saved')
            self.medicineInput.setText('')
            self.daysInput.setText('')
            self.successTxt.setText('')
            self.addedTxt.setText('')

            self.listMedComplete.clear()
            self.listMedIncomplete.clear()
            self.updateMedList()
        except:
            print('There is a Problem')

    def addTime(self):

        try:
            setTime = self.timeIntake.time()
            setTimeConverted = (setTime.toPyTime())
            Ui_widget.timeAdd.append(str(setTimeConverted))

            self.addedTxt.setText(f'{setTimeConverted} is Successfully Added!')
        except:
            print('there is a problem')

    def updateMedList(self):

        self.listMedComplete.clear()
        self.listMedIncomplete.clear()

        db = mainDb()
        db.fetch_data_info()

        complete = db.list_medication_complete
        self.listMedComplete.addItems(complete)

        incomplete = db.list_medication_incomplete
        self.listMedIncomplete.addItems(incomplete)

        self.listMedComplete.itemClicked.connect(self.launchPopUp)
        self.listMedIncomplete.itemClicked.connect(self.launchPopUp)

        db.close_conn_info()

    def launchPopUp(self, item):

        mainDb.value = str(item.text()).lower()

        self.new = popUp()
        self.new.show()

    def notification(self):

        self.notifications_list.clear()

        db = notification()
        db.create_table_notifs()
        db.pull_notif()

        notifs = notification.notif_list

        self.notifications_list.addItems(notifs)
        self.notifications_list.setCurrentRow(0)

        db.close_conn_notif()

    def tryButton(self):

        t = 3

        while t > 0:
            print(t)
            time.sleep(1)
            t -= 1

        if t == 0:
            self.showNotif()

    def showNotif(self):

        db = notification()
        db.create_table_notifs()

        pdb = prog()
        pdb.create_table_progress()

        dialog = QMessageBox(self)
        msg = 'Take your medicine!'
        dialog.setText(msg)
        dialog.setWindowTitle('NOTIFICATION!')
        dialog.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        x = dialog.exec()

        if x == QtWidgets.QMessageBox.StandardButton.Yes:
            pdb.insert_progress(['taken'])
            pdb.fetch_progress()

            now = datetime.datetime.now()
            formatted = now.strftime("%Y-%m-%d at %H:%M")
            data = [('User take the scheduled Medicine', formatted)]
            db.insert_notif(data)

            self.thread_manager.start(self.notification)
        else:
            pdb.insert_progress(['notTaken'])
            pdb.fetch_progress()

            now = datetime.datetime.now()
            formatted = now.strftime("%Y-%m-%d at %H:%M")
            data = [('User does not take the scheduled Medicine', formatted)]
            db.insert_notif(data)

            self.thread_manager.start(self.notification)

    def setTime(self):

        d = mainDb()
        d.fetch_time()

        print(d.list_time)

        for x in d.list_time:
            print(f'{x} is set')
            while True:
                time.sleep(1)
                current_time = datetime.datetime.now()
                if current_time.strftime('%H:%M:%S') == x:
                    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
                    print(f'{x} alarmed')
                    break

        d.close_conn_info()

    def plotCanvas(self):

        print('a')
        self.new = TestChart()
        print('a')
        self.new.show()
        print('a')

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "PAALALA"))
        self.cDate.setText(_translate("widget", "DATE DITO"))
        self.cDate_2.setText(_translate("widget", "NOTIFICATIONS"))
        self.try_notif.setText(_translate("widget", "try"))
        self.medicationsTxt.setText(_translate("widget", "MEDICATIONS"))
        self.medicationsTxt_2.setText(_translate("widget", "In-Progress"))
        self.medicationsTxt_3.setText(_translate("widget", "Completed"))
        self.medicationsTxt_4.setText(_translate("widget", "STATISTICS"))
        self.addTitle.setText(_translate("widget", "ADD MEDICATION"))
        self.medecineTxt.setText(_translate("widget", "Medicine:"))
        self.daysTxt.setText(_translate("widget", "Days of Intake: "))
        self.timeTxt.setText(_translate("widget", "Time of Intake: "))
        self.addTime_button.setText(_translate("widget", "+"))
        self.addButton.setText(_translate("widget", "Add"))


class popUp(QWidget):

    def __init__(self):
        super().__init__()

        db = mainDb()
        db.pullData()

        self.setWindowTitle(db.medName)
        self.setFixedWidth(289)
        self.setFixedHeight(155)
        self.setWindowIcon(QIcon('images/paalala-logo.png'))

        self.medName_popUp = QLabel("Medication Name", self)
        self.medName_popUp.setGeometry(QRect(20, 10, 161, 41))
        self.medName_popUp.setFont(QFont('Segoe UI', 14))
        self.medName_popUp.setStyleSheet("font-weight: bold")
        self.medName_popUp.setText(str(db.medName))

        self.progressLabel = QLabel("Progress:", self)
        self.progressLabel.setGeometry(QRect(20, 50, 61, 21))
        self.progressLabel.setFont(QFont('Segoe UI', 9))
        self.progressLabel.setStyleSheet("font-weight: bold")

        self.progress_popUp = QLabel("progress_type", self)
        self.progress_popUp.setGeometry(QRect(80, 50, 91, 21))
        self.progress_popUp.setFont(QFont('Segoe UI', 9))
        self.progress_popUp.setText(str(db.prog))

        self.timeLabel = QLabel("Time:", self)
        self.timeLabel.setGeometry(QRect(20, 70, 61, 21))
        self.timeLabel.setFont(QFont('Segoe UI', 9))
        self.timeLabel.setStyleSheet("font-weight: bold")

        self.time_popUp = QLabel("time_list", self)
        self.time_popUp.setGeometry(QRect(80, 70, 261, 21))
        self.time_popUp.setFont(QFont('Segoe UI', 9))
        self.time_popUp.setText(str(db.time))

        self.line = QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setGeometry(QRect(20, 96, 251, 16))

        self.remLabel = QLabel("Remaining:", self)
        self.remLabel.setGeometry(QRect(20, 110, 71, 21))
        self.remLabel.setFont(QFont('Segoe UI', 9))
        self.remLabel.setStyleSheet("font-weight: bold")

        self.r_popUp = QLabel("R", self)
        self.r_popUp.setGeometry(QRect(90, 110, 16, 21))
        self.r_popUp.setFont(QFont('Segoe UI', 9))
        self.r_popUp.setText(db.r)

        self.slash = QLabel("/", self)
        self.slash.setGeometry(QRect(105, 110, 16, 21))
        self.slash.setFont(QFont('Segoe UI', 9))

        self.a_popUp = QLabel("A", self)
        self.a_popUp.setGeometry(QRect(115, 110, 16, 21))
        self.a_popUp.setFont(QFont('Segoe UI', 9))
        self.a_popUp.setText(db.a)

        db.close_conn_info()


class TestChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(200)
        self.setFixedWidth(360)
        self.setWindowTitle('Statistics')
        self.setWindowIcon(QIcon('images/paalala-logo.png'))

        self.set_0 = QBarSet("Taken")
        self.set_1 = QBarSet("Not Taken")

        db = prog()
        db.fetch_progress()

        self.set_0.append([db.taken])
        self.set_1.append([db.notTaken])

        self.series = QBarSeries()
        self.series.append(self.set_0)
        self.series.append(self.set_1)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QDialog()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())

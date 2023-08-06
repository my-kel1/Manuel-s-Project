import sys
import time
import winsound
import datetime
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets
from PyQt6.uic.uiparser import QtGui

from add_database import mainDb
from notif_database import notification
from progress_database import prog

from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
                              QChartView, QValueAxis)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow


class MainScreen(QDialog):

    timeSave = []
    timeAdd = []

    value = ''

    def __init__(self):
        super(MainScreen, self).__init__()

        self.setFixedWidth(980)
        self.setFixedHeight(500)

        loadUi("paalala.ui", self)

        self.calendar()
        self.updateMedList()
        self.notification()

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

        if month == 1:
            print('January')
        elif month == 2:
            print('February')
        elif month == 3:
            print('March')
        elif month == 4:
            print('April')
        elif month == 5:
            print('May')
        elif month == 6:
            self.cDate.setText('JUNE ' + str(day))

    def saveMedication(self):

        try:
            self.time_con = ''

            if len(MainScreen.timeAdd) == 0:
                setTime = self.timeIntake.time()
                setTimeConverted = setTime.toPyTime()
                MainScreen.timeSave.append(str(setTimeConverted))
                for time in MainScreen.timeSave:
                    self.time_con += time
                    self.time_con += ';'
            else:
                for time in MainScreen.timeAdd:
                    self.time_con += time
                    self.time_con += ';'

            db = mainDb()
            data = [(str(self.medicineInput.text()).lower(), str(self.daysInput.text()).lower(), self.time_con)]
            db.create_table_info()
            db.insert_data_info(data)
            db.close_conn_info()

            MainScreen.timeSave.clear()
            MainScreen.timeAdd.clear()

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
            MainScreen.timeAdd.append(str(setTimeConverted))

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

        db = mainDb()

        mainDb.value = str(item.text()).lower()
        print(f'Main: {mainDb.value}')

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

        print('asa dialog ka na')
        dialog = QMessageBox(self)
        msg = 'Take your medicine!'
        dialog.setText(msg)
        dialog.setWindowTitle('NOTIFICATION!')
        dialog.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        x = dialog.exec()

        if x == QtWidgets.QMessageBox.StandardButton.Yes:
            pdb.insert_progress(['taken'])
            pdb.fetch_progress()
            print(pdb.taken)

            now = datetime.datetime.now()
            formatted = now.strftime("%Y-%m-%d at %H:%M")
            data = [('User take the scheduled Medicine', formatted)]
            db.insert_notif(data)

            self.thread_manager.start(self.notification)
        else:
            pdb.insert_progress(['notTaken'])
            pdb.fetch_progress()
            print(pdb.notTaken)

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

        self.new = TestChart()
        self.new.show()


class popUp(QWidget):

    def __init__(self):
        super().__init__()

        db = mainDb()
        db.pullData()

        self.setWindowTitle(db.medName)
        self.setFixedWidth(289)
        self.setFixedHeight(155)

        print(f'ito {db.medName}')

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


# run
if __name__ == "__main__":
    app = QApplication([])
    window = MainScreen()
    window.show()
    try:
        print('Starting')
        sys.exit(app.exec())
    except:
        print('Exited')
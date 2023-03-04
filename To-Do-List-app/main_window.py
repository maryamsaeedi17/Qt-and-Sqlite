# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(396, 549)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_new_task = QLineEdit(self.centralwidget)
        self.tb_new_task.setObjectName(u"tb_new_task")
        font = QFont()
        font.setPointSize(14)
        self.tb_new_task.setFont(font)
        self.tb_new_task.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.tb_new_task)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        self.btn_new_task.setFont(font)
        self.btn_new_task.setStyleSheet(u"background-color: rgb(121, 255, 12);")

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 161);")

        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 161);")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.tb_date = QLineEdit(self.centralwidget)
        self.tb_date.setObjectName(u"tb_date")
        self.tb_date.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tb_date.setCursorPosition(0)

        self.gridLayout.addWidget(self.tb_date, 0, 1, 1, 2)

        self.tb_time = QLineEdit(self.centralwidget)
        self.tb_time.setObjectName(u"tb_time")
        self.tb_time.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.tb_time, 1, 1, 1, 2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 161);")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.rdb_high = QRadioButton(self.centralwidget)
        self.rdb_high.setObjectName(u"rdb_high")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.rdb_high.setFont(font2)
        self.rdb_high.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.rdb_high, 2, 1, 1, 1)

        self.rdb_low = QRadioButton(self.centralwidget)
        self.rdb_low.setObjectName(u"rdb_low")
        self.rdb_low.setFont(font2)
        self.rdb_low.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.rdb_low, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tb_description = QTextEdit(self.centralwidget)
        self.tb_description.setObjectName(u"tb_description")
        self.tb_description.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.tb_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 396, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List-app. \ud83d\udcdd", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Enter time(hh:mm):", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enter date(yyyy/mm/dd):", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Priority(high/low):", None))
        self.rdb_high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.rdb_low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
    # retranslateUi


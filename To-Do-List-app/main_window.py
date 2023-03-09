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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTextEdit, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(440, 574)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"background-color: rgb(255, 248, 169);")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 248, 169);")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.tb_title = QLineEdit(self.centralwidget)
        self.tb_title.setObjectName(u"tb_title")
        font2 = QFont()
        font2.setPointSize(11)
        self.tb_title.setFont(font2)
        self.tb_title.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.tb_title, 0, 1, 1, 3)

        self.rdb_high = QRadioButton(self.centralwidget)
        self.rdb_high.setObjectName(u"rdb_high")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.rdb_high.setFont(font3)
        self.rdb_high.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_2.addWidget(self.rdb_high, 3, 1, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 248, 169);")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.tb_description = QTextEdit(self.centralwidget)
        self.tb_description.setObjectName(u"tb_description")
        self.tb_description.setFont(font2)
        self.tb_description.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.tb_description, 4, 0, 1, 4)

        self.rdb_low = QRadioButton(self.centralwidget)
        self.rdb_low.setObjectName(u"rdb_low")
        self.rdb_low.setFont(font3)
        self.rdb_low.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.rdb_low, 3, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 248, 169);")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 248, 169);")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.btn_add.setFont(font4)
        self.btn_add.setStyleSheet(u"background-color: rgb(255, 248, 169);\n"
"color: rgb(85, 170, 127);")

        self.gridLayout_2.addWidget(self.btn_add, 5, 0, 1, 4)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font1)
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setFont(font1)
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.timeEdit, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 440, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoList-app. 📝", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Do more of what makes you happy!", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.rdb_high.setText(QCoreApplication.translate("MainWindow", u"High", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.rdb_low.setText(QCoreApplication.translate("MainWindow", u"Low", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
    # retranslateUi


import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.db=Database()
        self.read_from_database()
        

        self.ui.btn_new_task.clicked.connect(self.new_task)

    def new_task(self):
        new_title=self.ui.tb_new_task.text()
        new_description=self.ui.tb_description.toPlainText()
        if self.ui.rdb_high.isChecked():
            prt="high"
        elif self.ui.rdb_low.isChecked():
            prt="low"
        new_date=self.ui.tb_date.text()
        new_time=self.ui.tb_time.text()
        feedback=self.db.add_new_task(new_title, new_description, prt, new_date, new_time)
        if feedback==True:
            self.read_from_database()
            self.ui.tb_new_task.setText("")
            self.ui.tb_description.setText("")
            self.ui.tb_date.setText("")
            self.ui.tb_time.setText("")
        elif feedback==False:
            msg_box=QMessageBox()
            msg_box.setText("There is a problem!")
            msg_box.exec()


    def read_from_database(self):
        tasks=self.db.get_tasks()
        for i in range(len(tasks)):
            new_chechbox=QCheckBox()
            new_lable=QLabel()
            new_btn=QPushButton()

            new_lable.setText(tasks[i][1])
            new_btn.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-radius: 10px; border-color: beige; font: bold 14px; max-width: 1em; padding: 6px;")
            new_btn.setText("🗑")

            self.ui.gl_tasks.addWidget(new_chechbox, i, 0)
            self.ui.gl_tasks.addWidget(new_lable, i, 1)
            self.ui.gl_tasks.addWidget(new_btn, i, 2)

            #QToolTip.setFont(('SansSerif', 10))
            new_lable.setToolTip(tasks[i][2] + "\n" + tasks[i][5] + "\n" + tasks[i][6])
            new_lable.show()




if __name__=="__main__":
    app=QApplication(sys.argv)

    main_window=MainWindow()
    main_window.show()

    app.exec()

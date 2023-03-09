import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tb_description.setPlaceholderText("Enter descriotion here.")

        self.db=Database()
        self.read_from_database()
        

        self.ui.btn_add.clicked.connect(self.new_task)
        

    def new_task(self):
        new_title=self.ui.tb_title.text()
        new_description=self.ui.tb_description.toPlainText()
        if self.ui.rdb_high.isChecked():
            prt="high"
        elif self.ui.rdb_low.isChecked():
            prt="low"
        new_date=self.ui.dateEdit.text()
        new_time=self.ui.timeEdit.text()
        feedback=self.db.add_new_task(new_title, new_description, prt, new_date, new_time)
        if feedback==True:
            self.read_from_database()
            self.ui.tb_title.setText("")
            self.ui.tb_description.setText("")
            #self.ui.dateEdit.setText("")
            #self.ui.timeEdit.setText("")
        elif feedback==False:
            msg_box=QMessageBox.warning()
            msg_box.setText("There is a problem!")
            msg_box.exec()


    def read_from_database(self):
        tasks=self.db.get_tasks()
        for i in range(len(tasks)):
            new_checkbox=QCheckBox()
            new_lable=QLabel()
            new_btn=QPushButton()

            new_lable.setText(tasks[i][1])
            new_btn.setStyleSheet("background-color: red; border-style: outset; border-width: 2px; border-radius: 10px; border-color: beige; font: bold 14px; max-width: 1em; padding: 6px;")
            new_btn.setText("🗑")
            new_btn.clicked.connect(partial(self.db.remove_tasks, tasks[i][0]))

            new_checkbox.clicked.connect(partial(self.db.task_done, tasks[i][0]))

            if tasks[i][3] == 1:
                new_checkbox.setChecked(True)
                new_lable.setStyleSheet("text-decoration: line-through")
            else :
                new_checkbox.setChecked(False) 

            if tasks[i][4] == "high":
                new_lable.setStyleSheet("color:red")
            # else :
            #     new_label1.setStyleSheet("color:white")

            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
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

import sys
#from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    

if __name__ == "__main__":
    app=QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()
from windows.Window_Login import *
from PyQt5.QtWidgets import QApplication,QWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QPushButton,QMainWindow
from PyQt5.QtGui import QIcon
import sys
from conf import *
from until import Path

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = widget_width
        self.h = widget_hight
        self.func_btn_text = ["机器人设置","充值中心","消息群发","拉黑名单查询","意见与反馈","检查更新"]
        self.func_btn_w = 80
        self.func_btn_h = 60
        self.initUI()

    def initUI(self):
        self.resize(self.w,self.h)
        self.setWindowTitle("DeyLies Wechat Helper")
        self.center()
        self.setWindowIcon(QIcon(Path('static','icon','app_icon.jpg')))
        self.show()

    def MainBtn(self,text):
        btn = QPushButton(text)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget()
    sys.exit(app.exec_())
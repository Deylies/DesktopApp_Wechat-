# encoding:utf-8
# __author__:DeyLies,WangYu
from widgets.widget_login import Ui_Login
from widgets.widget_regist import Ui_regist
from widgets.widget_reback import Ui_reback
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon
from until import Path


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.UI = Ui_Login()
        self.initUI()

    def initUI(self):
        self.UI.setupUi(self)
        self.UI.bnt_regist.mousePressEvent = self.regist
        self.UI.bnt_reback.mousePressEvent = self.reback
        self.UI.login.mousePressEvent = self.login
        self.setWindowTitle("登陆DeyLies微信助手")
        self.setWindowIcon(QIcon(Path('static', 'icon', 'app_icon.jpg')))
        self.setFixedSize(self.width(), self.height())
        self.show()

    def regist(self, e):
        window = Regist()
        print("***************")
        print("regist")

    def reback(self, e):
        window = Reback()
        print("***************")
        print("reback")

    def login(self, e):
        print("***************")
        print(self.UI.number.text())
        print(self.UI.passwd.text())
        print(self.UI.checkBox_remenber.checkState())
        print(self.UI.checkbox_autologin.checkState())
        print('login')


class Regist(QWidget):
    def __init__(self):
        super().__init__()
        self.UI = Ui_regist()
        # self.setWindowTitle("注册DeyLies微信助手")
        # self.setWindowIcon(Icon)
        self.initUI()

    def initUI(self):
        self.UI.setupUi(self)
        self.UI.confirm.mousePressEvent = self.submit
        self.UI.back_label.mousePressEvent = self.back
        self.setWindowTitle("注册DeyLies微信助手")
        self.setWindowIcon(QIcon(Path('static', 'icon', 'app_icon.jpg')))
        self.setFixedSize(self.width(), self.height())
        self.show()

    def back(self, e):
        self.close()

    def submit(self, e):
        print('*' * 10)
        print(self.UI.passwd.text())
        print(self.UI.passwd2.text())
        print(self.UI.username.text())
        print(self.UI.phone_num.text())
        print(self.UI.keys.text())


class Reback(QWidget):
    def __init__(self):
        super().__init__()
        self.UI = Ui_reback()
        # self.setWindowIcon(Icon)
        self.initUI()

    def initUI(self):
        self.UI.setupUi(self)
        self.UI.confirm.mousePressEvent = self.submit
        self.UI.back_label.mousePressEvent = self.back
        self.setWindowTitle("找回密码")
        self.setWindowIcon(QIcon(Path('static', 'icon', 'app_icon.jpg')))
        self.setFixedSize(self.width(), self.height())
        self.show()

    def back(self, e):
        self.close()

    def submit(self, e):
        print('*' * 10)
        print(self.UI.passwd.text())
        print(self.UI.passwd2.text())
        print(self.UI.username.text())
        print(self.UI.phone_num.text())

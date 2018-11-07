from widgets.widget_main import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWidget()
    sys.exit(app.exec_())
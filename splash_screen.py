from PySide6.QtWidgets import QMainWindow
from windows import *


class SplashScreen(QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.ui = Ui_wndw_splash_screen()
        self.ui.setupUi(self)

        self.ui.pb_next.clicked.connect(self.open_app)
        self.ui.pb_exit.clicked.connect(self.close)


    def open_app(self):
        from application import TechBook
        self.app_window = TechBook()
        self.app_window.show()
        self.close()

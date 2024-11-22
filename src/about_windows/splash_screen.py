from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
from src.windows import *


class SplashScreen(QMainWindow):
    """
    Окно SplashScreen
    """
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.ui = Ui_wndw_splash_screen()
        self.ui.setupUi(self)

        self.ui.pb_next.clicked.connect(self.open_app)
        self.ui.pb_exit.clicked.connect(self.close)

        self.timer = QTimer(self)
        self.timer.setInterval(60000) # Установка таймера на 60 секунд
        self.timer.timeout.connect(self.close)
        self.timer.start()

    # Открытие главного окна приложения
    def open_app(self):
        from src.application import TechBook
        self.app_window = TechBook()
        self.app_window.show()
        self.close()

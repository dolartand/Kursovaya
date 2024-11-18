from PySide6.QtWidgets import QMainWindow
from windows import Ui_help_wndw


class Help(QMainWindow):
    def __init__(self):
        super(Help, self).__init__()
        self.ui = Ui_help_wndw()
        self.ui.setupUi(self)

        self.ui.pb_exit.clicked.connect(self.close)

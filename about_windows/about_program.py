from PySide6.QtWidgets import QMainWindow
from windows import Ui_wndw_about_program


class AboutProgram(QMainWindow):
    def __init__(self):
        super(AboutProgram, self).__init__()
        self.ui = Ui_wndw_about_program()
        self.ui.setupUi(self)

        self.ui.pb_back.clicked.connect(self.close)

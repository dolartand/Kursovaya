from PySide6.QtWidgets import QMainWindow
from windows import Ui_wndw_about_author


class AboutAuthor(QMainWindow):
    """
    Окно "Об авторе"
    """
    def __init__(self):
        super(AboutAuthor, self).__init__()
        self.ui = Ui_wndw_about_author()
        self.ui.setupUi(self)

        self.ui.pb_back.clicked.connect(self.close)

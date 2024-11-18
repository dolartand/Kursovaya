import sys
from PySide6.QtWidgets import QApplication
from splash_screen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
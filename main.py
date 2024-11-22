"""
Книга компьютерной техники

Данный проект представляет собой настольное приложение, разработанное с использованием PySide6 и SQLite,
для управления данными о компьютерной технике. Программа обеспечивает отображение информации в табличном виде
и предоставляет функционал сортировки, поиска и редактирования данных.

@author Dolenko Artur
@email dolartand@gmail.com
@version 1.0 22.11.2024
@group 10701323
"""

import sys
from PySide6.QtWidgets import QApplication
from about_windows.splash_screen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
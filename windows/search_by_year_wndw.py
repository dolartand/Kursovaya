from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_wndw_search_by_year(object):
    def setupUi(self, wndw_search_by_year):
        if not wndw_search_by_year.objectName():
            wndw_search_by_year.setObjectName(u"Поиск")
        wndw_search_by_year.resize(400, 390)
        wndw_search_by_year.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_table_search_by_year = QFrame(wndw_search_by_year)
        self.frm_table_search_by_year.setObjectName(u"frm_table_search_by_year")
        self.frm_table_search_by_year.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_year.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_year.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_year.setFrameShadow(QFrame.Shadow.Raised)
        self.tv_search_by_year = QTableView(self.frm_table_search_by_year)
        self.tv_search_by_year.setObjectName(u"tv_search_by_year")
        self.tv_search_by_year.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_year.setStyleSheet(u"background-color: rgba(254,254,34, 10)")
        self.frm_search_by_year = QFrame(wndw_search_by_year)
        self.frm_search_by_year.setObjectName(u"frm_search_by_year")
        self.frm_search_by_year.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_year.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_year.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_year.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_search_by_year = QLabel(self.frm_search_by_year)
        self.lbl_search_by_year.setObjectName(u"lbl_search_by_year")
        self.lbl_search_by_year.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_year.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_year.setFont(font)
        self.lbl_search_by_year.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_search_by_year.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_enter_year = QLabel(self.frm_search_by_year)
        self.lbl_enter_year.setObjectName(u"lbl_enter_year")
        self.lbl_enter_year.setGeometry(QRect(10, 50, 151, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_year.setFont(font1)
        self.lbl_enter_year.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.le_enter_year = QLineEdit(self.frm_search_by_year)
        self.le_enter_year.setObjectName(u"le_enter_year")
        self.le_enter_year.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_year.setFont(font1)
        self.pushButton = QPushButton(self.frm_search_by_year)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 90, 151, 24))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"backgroung-color: rgba(254,254,34, 30);\n"
"border: 1px solid rgba(254,254,34, 20);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(254,254,34, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(254,254,34, 70);\n"
"}")

        self.retranslateUi(wndw_search_by_year)

        QMetaObject.connectSlotsByName(wndw_search_by_year)
    # setupUi

    def retranslateUi(self, wndw_search_by_year):
        wndw_search_by_year.setWindowTitle(QCoreApplication.translate("wndw_search_by_year", u"Поиск", None))
        self.lbl_search_by_year.setText(QCoreApplication.translate("wndw_search_by_year", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0433\u043e\u0434\u0443 \u0432\u044b\u043f\u0443\u0441\u043a\u0430 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.lbl_enter_year.setText(QCoreApplication.translate("wndw_search_by_year", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0433\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("wndw_search_by_year", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438", None))
    # retranslateUi


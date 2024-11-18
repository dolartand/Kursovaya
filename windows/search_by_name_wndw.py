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

class Ui_wndw_search_by_name(object):
    def setupUi(self, wndw_search_by_name):
        if not wndw_search_by_name.objectName():
            wndw_search_by_name.setObjectName(u"wndw_search_by_name")
        wndw_search_by_name.resize(400, 391)
        wndw_search_by_name.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_search_by_name = QFrame(wndw_search_by_name)
        self.frm_search_by_name.setObjectName(u"frm_search_by_name")
        self.frm_search_by_name.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_name.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_name.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_name.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_search_by_name = QLabel(self.frm_search_by_name)
        self.lbl_search_by_name.setObjectName(u"lbl_search_by_name")
        self.lbl_search_by_name.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_name.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_name.setFont(font)
        self.lbl_search_by_name.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_search_by_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_enter_name = QLabel(self.frm_search_by_name)
        self.lbl_enter_name.setObjectName(u"lbl_enter_name")
        self.lbl_enter_name.setGeometry(QRect(10, 50, 132, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_name.setFont(font1)
        self.lbl_enter_name.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.le_enter_name = QLineEdit(self.frm_search_by_name)
        self.le_enter_name.setObjectName(u"le_enter_name")
        self.le_enter_name.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_name.setFont(font1)
        self.pb_show = QPushButton(self.frm_search_by_name)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
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
        self.frm_table_search_by_name = QFrame(wndw_search_by_name)
        self.frm_table_search_by_name.setObjectName(u"frm_table_search_by_name")
        self.frm_table_search_by_name.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_name.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_name.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_name.setFrameShadow(QFrame.Shadow.Raised)
        self.tv__search_by_name = QTableView(self.frm_table_search_by_name)
        self.tv__search_by_name.setObjectName(u"tv__search_by_name")
        self.tv__search_by_name.setGeometry(QRect(10, 10, 361, 221))
        self.tv__search_by_name.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        self.retranslateUi(wndw_search_by_name)

        QMetaObject.connectSlotsByName(wndw_search_by_name)
    # setupUi

    def retranslateUi(self, wndw_search_by_name):
        wndw_search_by_name.setWindowTitle(QCoreApplication.translate("wndw_search_by_name", u"Dialog", None))
        self.lbl_search_by_name.setText(QCoreApplication.translate("wndw_search_by_name", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u044e \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.lbl_enter_name.setText(QCoreApplication.translate("wndw_search_by_name", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.pb_show.setText(QCoreApplication.translate("wndw_search_by_name", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438", None))
    # retranslateUi


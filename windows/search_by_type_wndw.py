from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_wndw_search_by_type(object):
    def setupUi(self, wndw_search_by_type):
        if not wndw_search_by_type.objectName():
            wndw_search_by_type.setObjectName(u"wndw_search_by_type")
        wndw_search_by_type.resize(400, 429)
        wndw_search_by_type.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_table_search_by_type = QFrame(wndw_search_by_type)
        self.frm_table_search_by_type.setObjectName(u"frm_table_search_by_type")
        self.frm_table_search_by_type.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_type.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_type.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_type.setFrameShadow(QFrame.Shadow.Raised)
        self.tv_search_by_type = QTableView(self.frm_table_search_by_type)
        self.tv_search_by_type.setObjectName(u"tv_search_by_type")
        self.tv_search_by_type.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_type.setStyleSheet(u"background-color: rgba(254,254,34, 10)")
        self.frm_search_by_type = QFrame(wndw_search_by_type)
        self.frm_search_by_type.setObjectName(u"frm_search_by_type")
        self.frm_search_by_type.setGeometry(QRect(10, 10, 381, 121))
        self.frm_search_by_type.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search_by_type.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search_by_type.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_search_by_type = QLabel(self.frm_search_by_type)
        self.lbl_search_by_type.setObjectName(u"lbl_search_by_type")
        self.lbl_search_by_type.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_type.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_type.setFont(font)
        self.lbl_search_by_type.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_search_by_type.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_enter_type = QLabel(self.frm_search_by_type)
        self.lbl_enter_type.setObjectName(u"lbl_enter_type")
        self.lbl_enter_type.setGeometry(QRect(0, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_type.setFont(font1)
        self.lbl_enter_type.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.pb_show = QPushButton(self.frm_search_by_type)
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
        self.cb_type_tech = QComboBox(self.frm_search_by_type)
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.setObjectName(u"cb_type_tech")
        self.cb_type_tech.setGeometry(QRect(180, 40, 191, 31))
        self.cb_type_tech.setFont(font)

        self.retranslateUi(wndw_search_by_type)

        QMetaObject.connectSlotsByName(wndw_search_by_type)
    # setupUi

    def retranslateUi(self, wndw_search_by_type):
        wndw_search_by_type.setWindowTitle(QCoreApplication.translate("wndw_search_by_type", u"Dialog", None))
        self.lbl_search_by_type.setText(QCoreApplication.translate("wndw_search_by_type", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0442\u0438\u043f\u0443 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.lbl_enter_type.setText(QCoreApplication.translate("wndw_search_by_type", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.pb_show.setText(QCoreApplication.translate("wndw_search_by_type", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438", None))
        self.cb_type_tech.setItemText(0, QCoreApplication.translate("wndw_search_by_type", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.cb_type_tech.setItemText(1, QCoreApplication.translate("wndw_search_by_type", u"\u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u043a\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.cb_type_tech.setItemText(2, QCoreApplication.translate("wndw_search_by_type", u"\u0412\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442\u0430", None))
        self.cb_type_tech.setItemText(3, QCoreApplication.translate("wndw_search_by_type", u"\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.cb_type_tech.setItemText(4, QCoreApplication.translate("wndw_search_by_type", u"SSD", None))
        self.cb_type_tech.setItemText(5, QCoreApplication.translate("wndw_search_by_type", u"\u0416\u0451\u0441\u0442\u043a\u0438\u0439 \u0434\u0438\u0441\u043a", None))
        self.cb_type_tech.setItemText(6, QCoreApplication.translate("wndw_search_by_type", u"\u0411\u043b\u043e\u043a \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.cb_type_tech.setItemText(7, QCoreApplication.translate("wndw_search_by_type", u"\u041a\u043e\u0440\u043f\u0443\u0441", None))

    # retranslateUi


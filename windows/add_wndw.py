# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_wndw.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_wndw_add(object):
    def setupUi(self, wndw_add):
        if not wndw_add.objectName():
            wndw_add.setObjectName(u"wndw_add")
        wndw_add.resize(400, 543)
        wndw_add.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_add = QFrame(wndw_add)
        self.frm_add.setObjectName(u"frm_add")
        self.frm_add.setGeometry(QRect(20, 10, 361, 521))
        self.frm_add.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_add.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_add.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frm_add)
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_value = QLineEdit(self.frm_add)
        self.le_value.setObjectName(u"le_value")
        font = QFont()
        font.setPointSize(12)
        self.le_value.setFont(font)

        self.gridLayout.addWidget(self.le_value, 4, 1, 1, 1)

        self.lbl_number_aud = QLabel(self.frm_add)
        self.lbl_number_aud.setObjectName(u"lbl_number_aud")
        self.lbl_number_aud.setMaximumSize(QSize(150, 20))
        self.lbl_number_aud.setFont(font)
        self.lbl_number_aud.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_number_aud, 7, 0, 1, 1)

        self.lbl_name = QLabel(self.frm_add)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_name, 2, 0, 1, 1)

        self.le_year = QLineEdit(self.frm_add)
        self.le_year.setObjectName(u"le_year")
        self.le_year.setFont(font)

        self.gridLayout.addWidget(self.le_year, 3, 1, 1, 1)

        self.lbl_year = QLabel(self.frm_add)
        self.lbl_year.setObjectName(u"lbl_year")
        self.lbl_year.setFont(font)
        self.lbl_year.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_year, 3, 0, 1, 1)

        self.lbl_sost = QLabel(self.frm_add)
        self.lbl_sost.setObjectName(u"lbl_sost")
        self.lbl_sost.setFont(font)
        self.lbl_sost.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_sost, 6, 0, 1, 1)

        self.lbl_otv = QLabel(self.frm_add)
        self.lbl_otv.setObjectName(u"lbl_otv")
        self.lbl_otv.setMaximumSize(QSize(150, 20))
        self.lbl_otv.setFont(font)
        self.lbl_otv.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_otv, 8, 0, 1, 1)

        self.le_name = QLineEdit(self.frm_add)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setFont(font)

        self.gridLayout.addWidget(self.le_name, 2, 1, 1, 1)

        self.pb_add = QPushButton(self.frm_add)
        self.pb_add.setObjectName(u"pb_add")
        font1 = QFont()
        font1.setPointSize(14)
        self.pb_add.setFont(font1)
        self.pb_add.setStyleSheet(u"QPushButton {\n"
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
        self.pb_add.setFlat(False)

        self.gridLayout.addWidget(self.pb_add, 9, 0, 1, 2)

        self.lbl_value = QLabel(self.frm_add)
        self.lbl_value.setObjectName(u"lbl_value")
        self.lbl_value.setFont(font)
        self.lbl_value.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_value, 4, 0, 1, 1)

        self.le_amount = QLineEdit(self.frm_add)
        self.le_amount.setObjectName(u"le_amount")
        self.le_amount.setFont(font)

        self.gridLayout.addWidget(self.le_amount, 5, 1, 1, 1)

        self.cb_add_sost = QComboBox(self.frm_add)
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.setObjectName(u"cb_add_sost")
        self.cb_add_sost.setFont(font1)

        self.gridLayout.addWidget(self.cb_add_sost, 6, 1, 1, 1)

        self.le_number_aud = QLineEdit(self.frm_add)
        self.le_number_aud.setObjectName(u"le_number_aud")
        self.le_number_aud.setFont(font)

        self.gridLayout.addWidget(self.le_number_aud, 7, 1, 1, 1)

        self.lbl_amount = QLabel(self.frm_add)
        self.lbl_amount.setObjectName(u"lbl_amount")
        self.lbl_amount.setMaximumSize(QSize(150, 20))
        self.lbl_amount.setFont(font)
        self.lbl_amount.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.gridLayout.addWidget(self.lbl_amount, 5, 0, 1, 1)

        self.lbl_add = QLabel(self.frm_add)
        self.lbl_add.setObjectName(u"lbl_add")
        self.lbl_add.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(20)
        self.lbl_add.setFont(font2)
        self.lbl_add.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_add.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lbl_add, 0, 0, 1, 2)

        self.cb_add_type = QComboBox(self.frm_add)
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.addItem("")
        self.cb_add_type.setObjectName(u"cb_add_type")
        self.cb_add_type.setFont(font1)

        self.gridLayout.addWidget(self.cb_add_type, 1, 0, 1, 2)

        self.le_otvetstv = QLineEdit(self.frm_add)
        self.le_otvetstv.setObjectName(u"le_otvetstv")
        self.le_otvetstv.setFont(font)

        self.gridLayout.addWidget(self.le_otvetstv, 8, 1, 1, 1)


        self.retranslateUi(wndw_add)

        self.pb_add.setDefault(False)


        QMetaObject.connectSlotsByName(wndw_add)
    # setupUi

    def retranslateUi(self, wndw_add):
        wndw_add.setWindowTitle(QCoreApplication.translate("wndw_add", u"Dialog", None))
        self.lbl_number_aud.setText(QCoreApplication.translate("wndw_add", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438", None))
        self.lbl_name.setText(QCoreApplication.translate("wndw_add", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lbl_year.setText(QCoreApplication.translate("wndw_add", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430", None))
        self.lbl_sost.setText(QCoreApplication.translate("wndw_add", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.lbl_otv.setText(QCoreApplication.translate("wndw_add", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043e\u0442\u0432\u0435\u0442\u0441\u0432-\u0433\u043e", None))
        self.pb_add.setText(QCoreApplication.translate("wndw_add", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.lbl_value.setText(QCoreApplication.translate("wndw_add", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.cb_add_sost.setItemText(0, QCoreApplication.translate("wndw_add", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.cb_add_sost.setItemText(1, QCoreApplication.translate("wndw_add", u"\u0412 \u0440\u0435\u043c\u043e\u043d\u0442\u0435", None))
        self.cb_add_sost.setItemText(2, QCoreApplication.translate("wndw_add", u"\u0421\u043f\u0438\u0441\u0430\u043d\u0430", None))

        self.lbl_amount.setText(QCoreApplication.translate("wndw_add", u"\u041a\u043e\u043b-\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.lbl_add.setText(QCoreApplication.translate("wndw_add", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.cb_add_type.setItemText(0, QCoreApplication.translate("wndw_add", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.cb_add_type.setItemText(1, QCoreApplication.translate("wndw_add", u"\u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u043a\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.cb_add_type.setItemText(2, QCoreApplication.translate("wndw_add", u"\u0412\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442\u0430", None))
        self.cb_add_type.setItemText(3, QCoreApplication.translate("wndw_add", u"\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.cb_add_type.setItemText(4, QCoreApplication.translate("wndw_add", u"SSD", None))
        self.cb_add_type.setItemText(5, QCoreApplication.translate("wndw_add", u"\u0416\u0451\u0441\u0442\u043a\u0438\u0439 \u0434\u0438\u0441\u043a", None))
        self.cb_add_type.setItemText(6, QCoreApplication.translate("wndw_add", u"\u0411\u043b\u043e\u043a \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.cb_add_type.setItemText(7, QCoreApplication.translate("wndw_add", u"\u041a\u043e\u0440\u043f\u0443\u0441", None))

    # retranslateUi


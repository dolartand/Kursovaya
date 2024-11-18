# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_wndw.ui'
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
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_wndw_edit(object):
    def setupUi(self, wndw_edit):
        if not wndw_edit.objectName():
            wndw_edit.setObjectName(u"wndw_edit")
        wndw_edit.resize(400, 464)
        wndw_edit.setStyleSheet(u"background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"        stop:0 rgba(139,0,255, 20), \n"
"        stop:1 rgba(115,102,189, 40));")
        self.frm_edit = QFrame(wndw_edit)
        self.frm_edit.setObjectName(u"frm_edit")
        self.frm_edit.setGeometry(QRect(10, 10, 386, 446))
        self.frm_edit.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_edit.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_edit.setFrameShadow(QFrame.Shadow.Raised)
        self.lbl_edit = QLabel(self.frm_edit)
        self.lbl_edit.setObjectName(u"lbl_edit")
        self.lbl_edit.setGeometry(QRect(20, 10, 341, 41))
        self.lbl_edit.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_edit.setFont(font)
        self.lbl_edit.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.lbl_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gb_new_data = QGroupBox(self.frm_edit)
        self.gb_new_data.setObjectName(u"gb_new_data")
        self.gb_new_data.setGeometry(QRect(10, 50, 361, 351))
        font1 = QFont()
        font1.setPointSize(11)
        self.gb_new_data.setFont(font1)
        self.gb_new_data.setStyleSheet(u"background-color: none;\n"
"border: 1px solid rgba(254,254,34, 20);")
        self.cb_type_tech = QComboBox(self.gb_new_data)
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.addItem("")
        self.cb_type_tech.setObjectName(u"cb_type_tech")
        self.cb_type_tech.setGeometry(QRect(10, 30, 341, 31))
        self.cb_type_tech.setFont(font)
        self.lbl_name = QLabel(self.gb_new_data)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(10, 70, 127, 26))
        font2 = QFont()
        font2.setPointSize(12)
        self.lbl_name.setFont(font2)
        self.lbl_name.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.le_name = QLineEdit(self.gb_new_data)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setGeometry(QRect(140, 70, 208, 26))
        self.le_name.setFont(font2)
        self.lbl_year = QLabel(self.gb_new_data)
        self.lbl_year.setObjectName(u"lbl_year")
        self.lbl_year.setGeometry(QRect(10, 110, 127, 26))
        self.lbl_year.setFont(font2)
        self.lbl_year.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.le_year = QLineEdit(self.gb_new_data)
        self.le_year.setObjectName(u"le_year")
        self.le_year.setGeometry(QRect(140, 110, 208, 26))
        self.le_year.setFont(font2)
        self.lbl_value = QLabel(self.gb_new_data)
        self.lbl_value.setObjectName(u"lbl_value")
        self.lbl_value.setGeometry(QRect(10, 150, 127, 26))
        self.lbl_value.setFont(font2)
        self.lbl_value.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.le_value = QLineEdit(self.gb_new_data)
        self.le_value.setObjectName(u"le_value")
        self.le_value.setGeometry(QRect(140, 150, 208, 26))
        self.le_value.setFont(font2)
        self.lbl_amount = QLabel(self.gb_new_data)
        self.lbl_amount.setObjectName(u"lbl_amount")
        self.lbl_amount.setGeometry(QRect(10, 190, 127, 20))
        self.lbl_amount.setMaximumSize(QSize(150, 20))
        self.lbl_amount.setFont(font2)
        self.lbl_amount.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.le_amount = QLineEdit(self.gb_new_data)
        self.le_amount.setObjectName(u"le_amount")
        self.le_amount.setGeometry(QRect(140, 190, 208, 26))
        self.le_amount.setFont(font2)
        self.cb_add_sost = QComboBox(self.gb_new_data)
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.addItem("")
        self.cb_add_sost.setObjectName(u"cb_add_sost")
        self.cb_add_sost.setGeometry(QRect(160, 230, 187, 31))
        self.cb_add_sost.setFont(font)
        self.lbl_number_aud = QLabel(self.gb_new_data)
        self.lbl_number_aud.setObjectName(u"lbl_number_aud")
        self.lbl_number_aud.setGeometry(QRect(10, 270, 148, 20))
        self.lbl_number_aud.setMaximumSize(QSize(150, 20))
        self.lbl_number_aud.setFont(font2)
        self.lbl_number_aud.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.le_number_aud = QLineEdit(self.gb_new_data)
        self.le_number_aud.setObjectName(u"le_number_aud")
        self.le_number_aud.setGeometry(QRect(160, 270, 187, 26))
        self.le_number_aud.setFont(font2)
        self.lbl_otv = QLabel(self.gb_new_data)
        self.lbl_otv.setObjectName(u"lbl_otv")
        self.lbl_otv.setGeometry(QRect(10, 310, 148, 20))
        self.lbl_otv.setMaximumSize(QSize(150, 20))
        self.lbl_otv.setFont(font2)
        self.lbl_otv.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.le_otvetstv = QLineEdit(self.gb_new_data)
        self.le_otvetstv.setObjectName(u"le_otvetstv")
        self.le_otvetstv.setGeometry(QRect(160, 310, 187, 26))
        self.le_otvetstv.setFont(font2)
        self.lbl_sost = QLabel(self.gb_new_data)
        self.lbl_sost.setObjectName(u"lbl_sost")
        self.lbl_sost.setGeometry(QRect(10, 230, 148, 31))
        self.lbl_sost.setFont(font2)
        self.lbl_sost.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.pb_save = QPushButton(self.frm_edit)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setGeometry(QRect(20, 410, 341, 28))
        self.pb_save.setFont(font)
        self.pb_save.setStyleSheet(u"QPushButton {\n"
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
        self.pb_save.setFlat(False)

        self.retranslateUi(wndw_edit)

        self.pb_save.setDefault(False)


        QMetaObject.connectSlotsByName(wndw_edit)
    # setupUi

    def retranslateUi(self, wndw_edit):
        wndw_edit.setWindowTitle(QCoreApplication.translate("wndw_edit", u"Dialog", None))
        self.lbl_edit.setText(QCoreApplication.translate("wndw_edit", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.gb_new_data.setTitle(QCoreApplication.translate("wndw_edit", u"\u041d\u043e\u0432\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.cb_type_tech.setItemText(0, QCoreApplication.translate("wndw_edit", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.cb_type_tech.setItemText(1, QCoreApplication.translate("wndw_edit", u"\u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u043a\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.cb_type_tech.setItemText(2, QCoreApplication.translate("wndw_edit", u"\u0412\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442\u0430", None))
        self.cb_type_tech.setItemText(3, QCoreApplication.translate("wndw_edit", u"\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.cb_type_tech.setItemText(4, QCoreApplication.translate("wndw_edit", u"SSD", None))
        self.cb_type_tech.setItemText(5, QCoreApplication.translate("wndw_edit", u"\u0416\u0451\u0441\u0442\u043a\u0438\u0439 \u0434\u0438\u0441\u043a", None))
        self.cb_type_tech.setItemText(6, QCoreApplication.translate("wndw_edit", u"\u0411\u043b\u043e\u043a \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.cb_type_tech.setItemText(7, QCoreApplication.translate("wndw_edit", u"\u041a\u043e\u0440\u043f\u0443\u0441", None))

        self.lbl_name.setText(QCoreApplication.translate("wndw_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.lbl_year.setText(QCoreApplication.translate("wndw_edit", u"\u0413\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430", None))
        self.lbl_value.setText(QCoreApplication.translate("wndw_edit", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c", None))
        self.lbl_amount.setText(QCoreApplication.translate("wndw_edit", u"\u041a\u043e\u043b-\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435", None))
        self.cb_add_sost.setItemText(0, QCoreApplication.translate("wndw_edit", u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435", None))
        self.cb_add_sost.setItemText(1, QCoreApplication.translate("wndw_edit", u"\u0412 \u0440\u0435\u043c\u043e\u043d\u0442\u0435", None))
        self.cb_add_sost.setItemText(2, QCoreApplication.translate("wndw_edit", u"\u0421\u043f\u0438\u0441\u0430\u043d\u0430", None))

        self.lbl_number_aud.setText(QCoreApplication.translate("wndw_edit", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u0438", None))
        self.lbl_otv.setText(QCoreApplication.translate("wndw_edit", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u043e\u0442\u0432\u0435\u0442\u0441\u0432-\u0433\u043e", None))
        self.lbl_sost.setText(QCoreApplication.translate("wndw_edit", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.pb_save.setText(QCoreApplication.translate("wndw_edit", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi


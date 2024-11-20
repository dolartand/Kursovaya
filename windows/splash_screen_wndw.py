# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen_wndw.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_wndw_splash_screen(object):
    def setupUi(self, wndw_splash_screen):
        if not wndw_splash_screen.objectName():
            wndw_splash_screen.setObjectName(u"SplashScreen")
        wndw_splash_screen.resize(807, 520)
        wndw_splash_screen.setStyleSheet(u"background-color: white;")
        self.label = QLabel(wndw_splash_screen)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 381, 21))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: black;")
        self.label_2 = QLabel(wndw_splash_screen)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 40, 421, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: black;")
        self.label_3 = QLabel(wndw_splash_screen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 70, 461, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: black;")
        self.label_4 = QLabel(wndw_splash_screen)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 150, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: black;")
        self.label_5 = QLabel(wndw_splash_screen)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 190, 311, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: black;")
        self.label_6 = QLabel(wndw_splash_screen)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 220, 341, 21))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: black;")
        self.label_7 = QLabel(wndw_splash_screen)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 270, 261, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: black;")
        self.label_8 = QLabel(wndw_splash_screen)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(520, 300, 191, 21))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: black;")
        self.label_9 = QLabel(wndw_splash_screen)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 350, 211, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: black;")
        self.label_10 = QLabel(wndw_splash_screen)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(520, 380, 231, 21))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: black;")
        self.label_11 = QLabel(wndw_splash_screen)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(360, 410, 91, 21))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: black;")
        self.label_12 = QLabel(wndw_splash_screen)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 250, 131, 151))
        self.label_12.setPixmap(QPixmap(u"resourses/splash_screen_logo.png"))
        self.pb_next = QPushButton(wndw_splash_screen)
        self.pb_next.setObjectName(u"pb_next")
        self.pb_next.setGeometry(QRect(20, 440, 391, 51))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(16)
        self.pb_next.setFont(font2)
        self.pb_next.setStyleSheet(u"color: black;")
        self.pb_exit = QPushButton(wndw_splash_screen)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(410, 440, 391, 51))
        self.pb_exit.setFont(font2)
        self.pb_exit.setStyleSheet(u"color: black;")

        self.retranslateUi(wndw_splash_screen)

        QMetaObject.connectSlotsByName(wndw_splash_screen)
    # setupUi

    def retranslateUi(self, wndw_splash_screen):
        wndw_splash_screen.setWindowTitle(QCoreApplication.translate("wndw_splash_screen", u"SplashScreen", None))
        self.label.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0411\u0435\u043b\u043e\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0438\u0442\u0435\u0442", None))
        self.label_2.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0424\u0430\u043a\u0443\u043b\u044c\u0442\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439 \u0438 \u0440\u043e\u0431\u043e\u0442\u043e\u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("wndw_splash_screen", u"\u041a\u0430\u0444\u0435\u0434\u0440\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u043e\u0433\u043e \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0439", None))
        self.label_4.setText(QCoreApplication.translate("wndw_splash_screen", u"\u041a\u0443\u0440\u0441\u043e\u0432\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("wndw_splash_screen", u"\u041f\u043e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0435 \"\u042f\u0437\u044b\u043a\u0438 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f\"", None))
        self.label_6.setText(QCoreApplication.translate("wndw_splash_screen", u"\u041a\u043d\u0438\u0433\u0430 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.label_7.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u043b: \u0441\u0442\u0443\u0434\u0435\u043d\u0442 \u0433\u0440\u0443\u043f\u043f\u044b 10701323", None))
        self.label_8.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0414\u043e\u043b\u0435\u043d\u043a\u043e \u0410\u0440\u0442\u0443\u0440 \u0410\u043d\u0434\u0440\u0435\u0435\u0432\u0438\u0447", None))
        self.label_9.setText(QCoreApplication.translate("wndw_splash_screen", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c: \u043a.\u0444.-\u043c.\u043d., \u0434\u043e\u0446.", None))
        self.label_10.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0421\u0438\u0434\u043e\u0440\u0438\u043a \u0412\u0430\u043b\u0435\u0440\u0438\u0439 \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447", None))
        self.label_11.setText(QCoreApplication.translate("wndw_splash_screen", u"\u041c\u0438\u043d\u0441\u043a, 2024", None))
        self.label_12.setText("")
        self.pb_next.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.pb_exit.setText(QCoreApplication.translate("wndw_splash_screen", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi


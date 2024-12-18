from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton, QTableView

class Ui_wndw_search_by_value(object):
    def setupUi(self, wndw_search_by_value):
        """
        Method to set up the UI for the window searching by value of technology.
        """
        if not wndw_search_by_value.objectName():
            wndw_search_by_value.setObjectName(u"Поиск")

        # Set window size and style
        wndw_search_by_value.resize(400, 385)
        wndw_search_by_value.setStyleSheet(u"background-color: qlineargradient(\n"
                                            "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                            "        stop:0 rgba(139,0,255, 20), \n"
                                            "        stop:1 rgba(115,102,189, 40));")

        # Frame for displaying search results
        self.frm_table_search_by_value = QFrame(wndw_search_by_value)
        self.frm_table_search_by_value.setObjectName(u"frm_table_search_by_value")
        self.frm_table_search_by_value.setGeometry(QRect(10, 140, 381, 241))
        self.frm_table_search_by_value.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table_search_by_value.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table_search_by_value.setFrameShadow(QFrame.Shadow.Raised)

        # Table for displaying search results
        self.tv_search_by_value = QTableView(self.frm_table_search_by_value)
        self.tv_search_by_value.setObjectName(u"tv_search_by_value")
        self.tv_search_by_value.setGeometry(QRect(10, 10, 361, 221))
        self.tv_search_by_value.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Frame for the search input
        self.frm__search_by_value = QFrame(wndw_search_by_value)
        self.frm__search_by_value.setObjectName(u"frm__search_by_value")
        self.frm__search_by_value.setGeometry(QRect(10, 10, 381, 121))
        self.frm__search_by_value.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm__search_by_value.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm__search_by_value.setFrameShadow(QFrame.Shadow.Raised)

        # Label for search header
        self.lbl_search_by_value = QLabel(self.frm__search_by_value)
        self.lbl_search_by_value.setObjectName(u"lbl_search_by_value")
        self.lbl_search_by_value.setGeometry(QRect(20, 0, 341, 41))
        self.lbl_search_by_value.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(14)
        self.lbl_search_by_value.setFont(font)
        self.lbl_search_by_value.setStyleSheet(u"background-color: none;\n"
                                               "border: none;")
        self.lbl_search_by_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Label for entering value
        self.lbl_enter_value = QLabel(self.frm__search_by_value)
        self.lbl_enter_value.setObjectName(u"lbl_enter_value")
        self.lbl_enter_value.setGeometry(QRect(10, 50, 141, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lbl_enter_value.setFont(font1)
        self.lbl_enter_value.setStyleSheet(u"background-color: none;\n"
                                            "border:none;")

        # Line edit for entering value
        self.le_enter_value = QLineEdit(self.frm__search_by_value)
        self.le_enter_value.setObjectName(u"le_enter_value")
        self.le_enter_value.setGeometry(QRect(170, 50, 191, 21))
        self.le_enter_value.setFont(font1)

        # Button to show results
        self.pb_show = QPushButton(self.frm__search_by_value)
        self.pb_show.setObjectName(u"pb_show")
        self.pb_show.setGeometry(QRect(110, 90, 151, 24))
        self.pb_show.setFont(font)
        self.pb_show.setStyleSheet(u"QPushButton {\n"
                                    "color: white;\n"
                                    "background-color: rgba(254,254,34, 30);\n"  # Fixed typo here
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

        # Call method to set text for UI elements
        self.retranslateUi(wndw_search_by_value)

        # Connect slots and signals
        QMetaObject.connectSlotsByName(wndw_search_by_value)

    def retranslateUi(self, wndw_search_by_value):
        """
        Method to set text for UI elements.
        """
        wndw_search_by_value.setWindowTitle(QCoreApplication.translate("wndw_search_by_value", u"Поиск", None))
        self.lbl_search_by_value.setText(QCoreApplication.translate("wndw_search_by_value", u"Поиск по стоимости техники", None))
        self.lbl_enter_value.setText(QCoreApplication.translate("wndw_search_by_value", u"Введите стоимость", None))
        self.pb_show.setText(QCoreApplication.translate("wndw_search_by_value", u"Вывести", None))
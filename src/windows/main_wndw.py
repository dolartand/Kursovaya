from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont)
from PySide6.QtWidgets import (QFrame, QLabel,
                               QMenu, QMenuBar, QPushButton,
                               QRadioButton, QTableView, QVBoxLayout,
                               QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Метод, который настраивает UI для главного окна.
        """
        # Установка имени окна, если оно еще не задано
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Книга компьютерной техники")

        # Настройка размеров и стиля окна
        MainWindow.resize(800, 616)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
                                 "background-color: qlineargradient(\n"
                                 "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                 "        stop:0 rgba(139,0,255, 20), \n"
                                 "        stop:1 rgba(115,102,189, 40)  \n"
                                 "    );\n"
                                 "}")

        # Создание действий для меню
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.add_action = QAction(MainWindow)
        self.add_action.setObjectName(u"add_action")
        self.delete_action = QAction(MainWindow)
        self.delete_action.setObjectName(u"delete_action")
        self.edit_action = QAction(MainWindow)
        self.edit_action.setObjectName(u"edit_action")
        self.archive_action = QAction(MainWindow)
        self.archive_action.setObjectName(u"archive_action")
        self.about_author_action = QAction(MainWindow)
        self.about_author_action.setObjectName(u"about_author_action")
        self.about_program_action = QAction(MainWindow)
        self.about_program_action.setObjectName(u"about_program_action")
        self.exit_action = QAction(MainWindow)
        self.exit_action.setObjectName(u"exit_action")
        self.help_action = QAction(MainWindow)
        self.help_action.setObjectName(u"help_action")

        # Центральный виджет
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Настройка рамки для таблицы
        self.frm_table = QFrame(self.centralwidget)
        self.frm_table.setObjectName(u"frm_table")
        self.frm_table.setGeometry(QRect(10, 50, 541, 521))
        self.frm_table.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_table.setFrameShadow(QFrame.Shadow.Raised)

        # Кнопка удаления
        self.pb_delete = QPushButton(self.frm_table)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setGeometry(QRect(180, 450, 135, 41))

        font = QFont()
        font.setPointSize(12)
        self.pb_delete.setFont(font)
        self.pb_delete.setStyleSheet(u"QPushButton {\n"
                                     "color: white;\n"
                                     "background-color: rgba(254,254,34, 20);\n"
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

        # Таблица для отображения данных
        self.tv_main_table = QTableView(self.frm_table)
        self.tv_main_table.setObjectName(u"tv_main_table")
        self.tv_main_table.setGeometry(QRect(20, 10, 491, 431))
        self.tv_main_table.setStyleSheet(u"background-color: rgba(254,254,34, 10)")

        # Кнопка редактирования
        self.pb_edit = QPushButton(self.frm_table)
        self.pb_edit.setObjectName(u"pb_edit")
        self.pb_edit.setGeometry(QRect(320, 450, 194, 41))
        self.pb_edit.setFont(font)
        self.pb_edit.setStyleSheet(u"QPushButton {\n"
                                   "color: white;\n"
                                   "background-color: rgba(254,254,34, 20);\n"
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

        # Кнопка добавления
        self.pb_add = QPushButton(self.frm_table)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setGeometry(QRect(20, 450, 150, 41))
        self.pb_add.setFont(font)
        self.pb_add.setStyleSheet(u"QPushButton {\n"
                                  "color: white;\n"
                                  "background-color: rgba(254,254,34, 20);\n"
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
        # Настройка рамки для поиска
        self.frm_search = QFrame(self.centralwidget)
        self.frm_search.setObjectName(u"frm_search")
        self.frm_search.setGeometry(QRect(560, 50, 231, 331))
        self.frm_search.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_search.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_search.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2 = QVBoxLayout(self.frm_search)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Метка для поиска данных
        self.lbl_search_data = QLabel(self.frm_search)
        self.lbl_search_data.setObjectName(u"lbl_search_data")
        font1 = QFont()
        font1.setPointSize(16)
        self.lbl_search_data.setFont(font1)
        self.lbl_search_data.setStyleSheet(u"border: none;\nbackground-color: none;")
        self.lbl_search_data.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(self.lbl_search_data)

        # Метка для выбора критерия поиска
        self.lbl_search_by = QLabel(self.frm_search)
        self.lbl_search_by.setObjectName(u"lbl_search_by")
        self.lbl_search_by.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.lbl_search_by.setFont(font2)
        self.lbl_search_by.setStyleSheet(u"background-color: none;\nborder: none;")
        self.lbl_search_by.setAlignment(
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_2.addWidget(self.lbl_search_by)

        # Радиокнопки для выбора критерия поиска
        self.rb_name = QRadioButton(self.frm_search)
        self.rb_name.setObjectName(u"rb_name")
        self.rb_name.setFont(font)
        self.rb_name.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_name)

        self.rb_type = QRadioButton(self.frm_search)
        self.rb_type.setObjectName(u"rb_type")
        self.rb_type.setFont(font)
        self.rb_type.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_type)

        self.rb_year = QRadioButton(self.frm_search)
        self.rb_year.setObjectName(u"rb_year")
        self.rb_year.setFont(font)
        self.rb_year.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_year)

        self.rb_value = QRadioButton(self.frm_search)
        self.rb_value.setObjectName(u"rb_value")
        self.rb_value.setFont(font)
        self.rb_value.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_value)

        self.rb_amount = QRadioButton(self.frm_search)
        self.rb_amount.setObjectName(u"rb_amount")
        self.rb_amount.setFont(font)
        self.rb_amount.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_amount)

        self.rb_condition = QRadioButton(self.frm_search)
        self.rb_condition.setObjectName(u"rb_condition")
        self.rb_condition.setFont(font)
        self.rb_condition.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_condition)

        self.rb_number_aud = QRadioButton(self.frm_search)
        self.rb_number_aud.setObjectName(u"rb_number_aud")
        self.rb_number_aud.setFont(font)
        self.rb_number_aud.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_number_aud)

        self.rb_otvetstv = QRadioButton(self.frm_search)
        self.rb_otvetstv.setObjectName(u"rb_otvetstv")
        self.rb_otvetstv.setFont(font)
        self.rb_otvetstv.setStyleSheet(u"background-color: none;\nborder: none;")
        self.verticalLayout_2.addWidget(self.rb_otvetstv)

        # Кнопка поиска
        self.pb_search = QPushButton(self.frm_search)
        self.pb_search.setObjectName(u"pb_search")
        self.pb_search.setFont(font)
        self.pb_search.setStyleSheet(u"QPushButton {\n"
                                     "color: white;\n"
                                     "background-color: rgba(254,254,34, 20);\n"
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
        self.verticalLayout_2.addWidget(self.pb_search)

        # Настройка рамки для кнопок
        self.frm_buttons = QFrame(self.centralwidget)
        self.frm_buttons.setObjectName(u"frm_buttons")
        self.frm_buttons.setGeometry(QRect(560, 390, 231, 181))
        self.frm_buttons.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frm_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_buttons.setFrameShadow(QFrame.Shadow.Raised)

        # Кнопка выхода
        self.pb_exit = QPushButton(self.frm_buttons)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(30, 130, 181, 41))
        self.pb_exit.setFont(font)
        self.pb_exit.setStyleSheet(u"QPushButton {\n"
                                   "color: white;\n"
                                   "background-color: rgba(254,254,34, 20);\n"
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

        # Кнопки "Об авторе", "О программе" и "Открыть архив"
        self.pb_about_author = QPushButton(self.frm_buttons)
        self.pb_about_author.setObjectName(u"pb_about_author")
        self.pb_about_author.setGeometry(QRect(10, 10, 101, 61))
        self.pb_about_author.setFont(font)
        self.pb_about_author.setStyleSheet(self.pb_exit.styleSheet())

        self.pb_about_program = QPushButton(self.frm_buttons)
        self.pb_about_program.setObjectName(u"pb_about_program")
        self.pb_about_program.setGeometry(QRect(120, 10, 101, 61))
        self.pb_about_program.setFont(font)
        self.pb_about_program.setStyleSheet(self.pb_exit.styleSheet())

        self.pb_show_archive = QPushButton(self.frm_buttons)
        self.pb_show_archive.setObjectName(u"pb_show_archive")
        self.pb_show_archive.setGeometry(QRect(30, 80, 181, 41))
        self.pb_show_archive.setFont(font)
        self.pb_show_archive.setStyleSheet(self.pb_exit.styleSheet())

        # Основная метка
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 381, 31))
        font3 = QFont()
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"border: none;\nbackground-color: none;")

        # Установка центрального виджета в главное окно
        MainWindow.setCentralWidget(self.centralwidget)

        # Настройка меню
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInformation = QMenu(self.menubar)
        self.menuInformation.setObjectName(u"menuInformation")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        # Установка порядка табуляции
        QWidget.setTabOrder(self.pb_delete, self.pb_add)
        QWidget.setTabOrder(self.pb_add, self.pb_edit)
        QWidget.setTabOrder(self.pb_edit, self.tv_main_table)

        # Добавление действий в меню
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInformation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.add_action)
        self.menuFile.addAction(self.delete_action)
        self.menuFile.addAction(self.edit_action)
        self.menuFile.addAction(self.archive_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit_action)
        self.menuInformation.addAction(self.about_author_action)
        self.menuInformation.addAction(self.about_program_action)
        self.menuHelp.addAction(self.help_action)

        # Завершение настройки интерфейса
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        """
        Метод для перевода текста виджетов интерфейса.
        """
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Книга компьютерной техники"))

        # Установка текста для действий меню
        self.action.setText(QCoreApplication.translate("MainWindow", u"Программа"))
        self.add_action.setText(QCoreApplication.translate("MainWindow", u"Добавить запись"))
        self.delete_action.setText(QCoreApplication.translate("MainWindow", u"Удалить запись"))
        self.edit_action.setText(QCoreApplication.translate("MainWindow", u"Редактировать запись"))
        self.archive_action.setText(QCoreApplication.translate("MainWindow", u"Открыть архив удалённых записей"))

        # Установка текста для информации
        self.about_author_action.setText(QCoreApplication.translate("MainWindow", u"Об авторе"))
        self.about_program_action.setText(QCoreApplication.translate("MainWindow", u"О программе"))
        self.exit_action.setText(QCoreApplication.translate("MainWindow", u"Выход"))
        self.help_action.setText(QCoreApplication.translate("MainWindow", u"Помощь"))

        # Установка текста для кнопок
        self.pb_delete.setText(QCoreApplication.translate("MainWindow", u"Удалить запись"))
        self.pb_edit.setText(QCoreApplication.translate("MainWindow", u"Редактировать запись"))
        self.pb_add.setText(QCoreApplication.translate("MainWindow", u"Добавить запись"))

        # Установка текста для меток поиска
        self.lbl_search_data.setText(QCoreApplication.translate("MainWindow", u"Поиск данных"))
        self.lbl_search_by.setText(QCoreApplication.translate("MainWindow", u"Поиск по:"))

        # Установка текста для радиокнопок
        self.rb_name.setText(QCoreApplication.translate("MainWindow", u"Названию"))
        self.rb_type.setText(QCoreApplication.translate("MainWindow", u"Типу техники"))
        self.rb_year.setText(QCoreApplication.translate("MainWindow", u"Году поступления"))
        self.rb_value.setText(QCoreApplication.translate("MainWindow", u"Цене"))
        self.rb_amount.setText(QCoreApplication.translate("MainWindow", u"Количество на складе"))
        self.rb_condition.setText(QCoreApplication.translate("MainWindow", u"Состоянию техники"))
        self.rb_number_aud.setText(QCoreApplication.translate("MainWindow", u"Номеру аудитории"))
        self.rb_otvetstv.setText(QCoreApplication.translate("MainWindow", u"Фамилии ответственного"))

        # Установка текста для кнопки поиска и выхода
        self.pb_search.setText(QCoreApplication.translate("MainWindow", u"Искать"))
        self.pb_exit.setText(QCoreApplication.translate("MainWindow", u"Выход"))

        # Установка текста для кнопок "Об авторе" и "О программе"
        self.pb_about_author.setText(QCoreApplication.translate("MainWindow", u"Об авторе"))
        self.pb_about_program.setText(QCoreApplication.translate("MainWindow", u"О программе"))
        self.pb_show_archive.setText(QCoreApplication.translate("MainWindow", u"Открыть архив"))

        # Установка текста для главной метки
        self.label.setText(QCoreApplication.translate("MainWindow", u"Книга компьютерной техники"))

        # Установка заголовков для меню
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Файл"))
        self.menuInformation.setTitle(QCoreApplication.translate("MainWindow", u"Информация"))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Помощь"))
    # retranslateUi


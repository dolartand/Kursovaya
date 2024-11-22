from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QFrame, QLabel,
    QPushButton, QTextEdit)

class Ui_help_wndw(object):
    def setupUi(self, help_wndw):
        if not help_wndw.objectName():
            help_wndw.setObjectName(u"help_wndw")
        help_wndw.resize(802, 468)
        help_wndw.setStyleSheet(u"background-color: qlineargradient(\n"
                                "        spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
                                "        stop:0 rgba(139,0,255, 20), \n"
                                "        stop:1 rgba(115,102,189, 40)  \n"
                                "    );\n"
                                "\n"
                                "")
        self.frame = QFrame(help_wndw)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 781, 451))
        self.frame.setStyleSheet(u"background-color: rgba(254,254,34, 5)")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 50, 761, 341))
        self.textEdit.setStyleSheet(u"background-color: rgba(254,254,34, 10)")
        self.textEdit.setReadOnly(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 10, 111, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: none;\n"
                                 "background-color: none;")
        self.pb_exit = QPushButton(self.frame)
        self.pb_exit.setObjectName(u"pb_exit")
        self.pb_exit.setGeometry(QRect(290, 400, 181, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.pb_exit.setFont(font1)
        self.pb_exit.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(help_wndw)

        QMetaObject.connectSlotsByName(help_wndw)
    # setupUi

    def retranslateUi(self, help_wndw):
        help_wndw.setWindowTitle(QCoreApplication.translate("help_wndw", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("help_wndw", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
        self.textEdit.setHtml(QCoreApplication.translate(
    "help_wndw",
    """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
    <head>
        <meta name="qrichtext" content="1" />
        <meta charset="utf-8" />
        <style type="text/css">
            p, li { white-space: pre-wrap; }
            p{
                font-weight: bold;
                margin:0;
            }
        </style>
    </head>
    <body style="font-family:Arial; font-size:15px; font-weight:400; font-style:normal; color:white; line-height: 1.5;">
        <h2 style="font-size:14pt; font-weight:bold;">Описание программы</h2>
        <article>
            Программа предназначена для управления записями о компьютерной технике. Она предоставляет удобный интерфейс для добавления, редактирования, удаления, поиска записей, а также предоставляет доступ к архиву удалённых записей. Дополнительно программа содержит информацию об авторе и самой программе.
        </article>
        <hr />
        <h2 style="font-size:14pt; font-weight:bold;">Функциональные возможности</h2>
        <ol style="line-height: 10.5px; padding:0 1;">
            <li><p>Отображение записей о компьютерной технике</p>
                <ul type="disc">
                    <li style="line-height: 1.2;">Основное окно программы отображает таблицу, содержащую записи о компьютерной технике.</li>
                    <li>В таблице указаны поля:
                        <ul style="line-height: 7px;">
                            <li>ID записи;</li>
                            <li>Название оборудования;</li>
                            <li>Тип оборудования (процессор, видеокарта и т.д.);</li>
                            <li>Год выпуска;</li>
                            <li>Стоимость;</li>
                            <li>Количество на складе;</li>
                            <li>Состояние (в работе, списана, в ремонте);</li>
                            <li>Номер аудитории;</li>
                            <li>Фамилия ответственного.</li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li><p>Добавление новой записи</p>
                <ul type="disc">
                    <li>Для добавления записи:
                        <ol style="line-height: 8px;">
                            <li>Нажмите кнопку <b>"Добавить запись"</b>.</li>
                            <li style="line-height: 1.2;">Откроется окно с полями для ввода данных (название, тип и т.д.).</li>
                            <li>Заполните необходимые поля.</li>
                            <li style="line-height: 1.2;">Нажмите кнопку <b>"Сохранить"</b>, чтобы новая запись отобразилась в таблице.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Удаление записи</p>
                <ul type="disc">
                    <li>Для удаления записи:
                        <ol style="line-height: 7px;">
                            <li>Выделите строку в таблице.</li>
                            <li>Нажмите кнопку <b>"Удалить запись"</b>.</li>
                            <li style="line-height: 1.2;">Запись будет удалена из основной таблицы и перемещена в архив.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Редактирование записи</p>
                <ul type="disc">
                    <li>Для редактирования записи:
                        <ol>
                            <li>Выделите строку в таблице.</li>
                            <li>Нажмите кнопку <b>"Редактировать запись"</b>.</li>
                            <li style="line-height: 1.2;">Откроется окно редактирования, содержащее данные выбранной записи.</li>
                            
                            <li>Внесите изменения в поля.</li>
                            <li style="line-height: 1.2;">Нажмите кнопку <b>"Сохранить"</b>, чтобы обновить запись в таблице.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Поиск записи</p>
                <ul type="disc">
                    <li>Для поиска записи:
                        <ol>
                            <li style="line-height: 1.2;">Выберите критерий поиска, отметив соответствующий радиокнопкой (например, "По названию", "По типу техники", "По цене").</li>
                            <li>Нажмите кнопку <b>"Искать"</b>.</li>
                            <li>Откроется окно поиска.</li>
                            <li>Введите ключевое слово (например, название или цену).</li>
                            <li style="line-height: 1.2;">Нажмите кнопку <b>"Вывести"</b>, чтобы отобразить найденные записи.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Информация об авторе</p>
                <ul type="disc">
                    <li>Для просмотра информации об авторе:
                        <ol>
                            <li>Нажмите кнопку <b>"Об авторе"</b>.</li>
                            <li>Откроется окно с данными об авторе работы.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Информация о программе</p>
                <ul type="disc">
                    <li>Для получения информации о программе:
                        <ol>
                            <li>Нажмите кнопку <b>"О программе"</b>.</li>
                            <li style="line-height: 1.2;">Откроется окно с кратким описанием программы, версией.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Открытие архива записей</p>
                <ul type="disc">
                    <li>Для просмотра архива:
                        <ol>
                            <li>Нажмите кнопку <b>"Открыть архив"</b>.</li>
                            <li style="line-height: 1.2;">Откроется таблица, содержащая записи, которые были удалены из основной таблицы.</li>
                        </ol>
                    </li>
                </ul>
            </li>
            <li><p>Завершение работы программы</p>
                <ul type="disc">
                    <li>Для выхода из программы:
                        <ol>
                            <li>Нажмите кнопку <b>"Выход"</b>.</li>
                            <li>Программа завершит работу.</li>
                        </ol>
                    </li>
                </ul>
            </li>
        </ol>
        <hr />
        <h2 style="font-size:14pt; font-weight:bold; margin:0;">Примечания</h2>
        <ul>
            <li>Все изменения (добавление, удаление, редактирование) автоматически сохраняются в базе данных.</li>
            <li>Данные из архива доступны для просмотра и удаления, но не для редактирования.</li>
        </ul>
        <h2 style="font-weight: bold; margin: 0.3;">Поддержка</h2>
        <article>Для Дополнительной информации обратитесь к автору через окно "Об авторе", где указана электронная почта.</article>
    </body>
</html>
"""
))
        self.pb_exit.setText(QCoreApplication.translate("help_wndw", u"\u041d\u0430\u0437\u0430\u0434", None))



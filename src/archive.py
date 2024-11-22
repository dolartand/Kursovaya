from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from src.windows import Ui_wndw_archive
from database import  ArchiveDatabase

class Archive(QMainWindow):
    """
    Окно архива

    Функционал:
    Отображение данных архива в табличном виде.
    Удаление записей из архива.
    """
    def __init__(self, item_id=None):
        super(Archive, self).__init__()
        self.item_id = item_id
        self.db = ArchiveDatabase("databases/archive.db")
        self.ui = Ui_wndw_archive()
        self.ui.setupUi(self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Название', 'Тип', 'Год', 'Стоимость', 'Кол-во', 'Состояние',
                                              'Номер аудитории', 'Фамилия ответственного'])
        self.ui.tv_archive.setModel(self.model)

        self.ui.tv_archive.setSortingEnabled(True)
        self.ui.tv_archive.setColumnWidth(0, 15)
        self.ui.tv_archive.setColumnWidth(3, 50)
        self.ui.tv_archive.setColumnWidth(5, 50)
        self.ui.tv_archive.setColumnWidth(7, 120)
        self.ui.tv_archive.setColumnWidth(8, 150)
        self.ui.tv_archive.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        self.ui.pb_exit.clicked.connect(self.close)
        self.ui.pb_delete.clicked.connect(self.delete_from_archive)

        self.load_archive()

    # Загрузка данных из архива
    def load_archive(self):
        self.model.removeRows(0, self.model.rowCount())
        items = self.db.fetch_all_items()

        for item in items:
            row = [
                QStandardItem(str(item[0])),
                QStandardItem(item[1]),
                QStandardItem(item[2]),
                QStandardItem(str(item[3])),
                QStandardItem(str(item[4])),
                QStandardItem(str(item[5])),
                QStandardItem(item[6]),
                QStandardItem(str(item[7])),
                QStandardItem(item[8])
            ]
            self.model.appendRow(row)

    # Удаление записи из архива
    def delete_from_archive(self):
        selected_indexes = self.ui.tv_archive.selectionModel().selectedRows()

        if not selected_indexes:
            QMessageBox.warning(self, "Удаление записи", "Пожалуйста, выберите запись для удаления.")
            return

        selected_row = selected_indexes[0].row()
        item_id = int(self.model.item(selected_row, 0).text())

        confirmation = QMessageBox.question(self, "Подтверждение удаления",
                                            f"Вы уверены, что хотите удалить запись с ID {item_id}?",
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirmation == QMessageBox.StandardButton.Yes:
            self.db.delete_item(item_id)
            self.model.removeRow(selected_row)
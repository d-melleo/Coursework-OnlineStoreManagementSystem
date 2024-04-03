from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
import sys

from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QTreeView
from PyQt5.QtCore import Qt
from logics.database.models import User
from logics.database.database import dbQ
from PyQt5.QtWidgets import QMessageBox

class UserAdminInterface(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("User Admin")
        self.db = dbQ
        # Підключення до бази даних
        if not self.db.open():
            print("Cannot open database")
            return

        # Створення та розміщення елементів інтерфейсу
        self.create_widgets()

    def create_widgets(self):
        # Створення головного віджета
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Створення layout для головного віджета
        layout = QVBoxLayout(central_widget)

        # Створення моделі для QTreeView
        self.model = QSqlTableModel()
        self.model.setTable("users")
        self.model.setHeaderData(1, Qt.Horizontal, "Username")
        self.model.setHeaderData(2, Qt.Horizontal, "Password")
        self.model.setHeaderData(3, Qt.Horizontal, "First Name")
        self.model.setHeaderData(4, Qt.Horizontal, "Last Name")
        self.model.setHeaderData(5, Qt.Horizontal, "Role")
        self.model.setHeaderData(6, Qt.Horizontal, "Access")
        self.model.select()

        # Створення QTreeView та підключення до моделі
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)

        # Дозвіл редагування вмісту QTreeView
        self.tree_view.setEditTriggers(QTreeView.DoubleClicked)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.setColumnHidden(0, True)  # Приховання колонки з ID

        layout.addWidget(self.tree_view)

        # Кнопка для збереження даних
        save_button = QPushButton("Зберегти зміни")
        save_button.clicked.connect(self.save_data)
        layout.addWidget(save_button)

        # Кнопка для видалення вибраних записів
        delete_selected_button = QPushButton("Видалити вибрані")
        delete_selected_button.clicked.connect(self.delete_selected)
        layout.addWidget(delete_selected_button)

        # Кнопка для додавання нового запису
        add_button = QPushButton("Додати")
        add_button.clicked.connect(self.add_record)
        layout.addWidget(add_button)

    def save_data(self):
        self.model.database().transaction()
        if self.model.submitAll():
            self.model.database().commit()
            QMessageBox.information(self, "Успіх", "Зміни збережено успішно!", QMessageBox.Ok)
        else:
            self.model.database().rollback()

    def delete_selected(self):
        selected_indexes = self.tree_view.selectedIndexes()
        rows_to_delete = set()
        for index in selected_indexes:
            rows_to_delete.add(index.row())

        for row in sorted(rows_to_delete, reverse=True):
            self.model.removeRow(row)
        self.save_data()

    def add_record(self):
        # Отримання кількості рядків у моделі
        row_count = self.model.rowCount()
        # Вставлення нового рядка на позицію row_count
        self.model.insertRow(row_count)
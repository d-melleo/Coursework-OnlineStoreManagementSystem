import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from .users import UserAdminInterface


class MainMenuRoot(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Головне меню для суперюзера")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.current_frame = None

        self.show_admin_menu()

    def show_admin_menu(self):
        # Очищаємо екран перед створенням нового вмісту

        # Додати інші елементи головного меню для адміністратора
        self.admin_label = QLabel("Суперюзер меню")
        self.central_layout = QVBoxLayout()
        self.central_layout.addWidget(self.admin_label)

        # Створення бічного меню
        self.side_menu = QWidget()
        self.side_menu_layout = QVBoxLayout()
        self.side_menu.setLayout(self.side_menu_layout)
        self.central_layout.addWidget(self.side_menu)

        # Список опцій для бічного меню
        options = ["Користувачі", "Категорії товарів"]
        for option in options:
            btn = QPushButton(option)
            btn.clicked.connect(lambda state, o=option: self.show_selected_option(o))
            self.side_menu_layout.addWidget(btn)

        self.central_widget.setLayout(self.central_layout)

    def show_selected_option(self, option):
        # Видалення попереднього вмісту
        if self.current_frame:
            self.current_frame.deleteLater()

        # Створення нового контейнера для вмісту
        self.current_frame = QWidget()
        self.current_frame_layout = QVBoxLayout()
        self.current_frame.setLayout(self.current_frame_layout)
        self.central_layout.addWidget(self.current_frame)

        if option == "Користувачі":
            users = UserAdminInterface(self)
            self.setCentralWidget(users)

        elif option == "Категорії товарів":
            # Показати вміст для опції "Постачальники"
            self.show_users()

    def show_categories(self):
        # Видалення попереднього вмісту з контейнера
        self.clear_container()

        # Вміст для опції "Користувачі"
        label = QLabel("Вміст для опції 'Товари'")
        self.current_frame_layout.addWidget(label)

    def show_users(self):
        # Видалення попереднього вмісту з контейнера
        self.clear_container()

        # Вміст для опції "Постачальники"     label = tk.Label(self.current_fr
        users_admin = UserAdminInterface(self)
        self.current_frame_layout.addWidget(users_admin)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from logics.database.auth import register, login
from logics.database.models import User
from .dicts import dict_ui_key_role
from .admin.main_menu import MainMenuAdmin
from .store.main_menu import MainMenuUser
from .root.main_menu import MainMenuRoot

class LoginRegisterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Увійти або Зареєструватись")
        self.show_login_window()

    def show_login_window(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        username_label = QLabel("Ім'я користувача:")
        self.username_entry = QLineEdit()

        password_label = QLabel("Пароль:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Увійти")
        login_button.clicked.connect(self.login_user)

        register_button = QPushButton("Зареєструватись")
        register_button.clicked.connect(self.show_register_window)

        self.result_label = QLabel()

        layout.addWidget(username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(login_button)
        layout.addWidget(register_button)
        layout.addWidget(self.result_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_register_window(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        username_label = QLabel("Ім'я користувача:")
        self.username_entry = QLineEdit()

        password_label = QLabel("Пароль:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        firstname_label = QLabel("Ім'я:")
        self.firstname_entry = QLineEdit()

        lastname_label = QLabel("Прізвище:")
        self.lastname_entry = QLineEdit()

        role_label = QLabel("Роль:")
        self.role_combobox = QComboBox()
        self.role_combobox.addItems(list(dict_ui_key_role.keys()))

        register_button = QPushButton("Зареєструватись")
        register_button.clicked.connect(self.register_user)

        login_button = QPushButton("Увійти")
        login_button.clicked.connect(self.show_login_window)

        self.result_label = QLabel()

        layout.addWidget(username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(firstname_label)
        layout.addWidget(self.firstname_entry)
        layout.addWidget(lastname_label)
        layout.addWidget(self.lastname_entry)
        layout.addWidget(role_label)
        layout.addWidget(self.role_combobox)
        layout.addWidget(register_button)
        layout.addWidget(login_button)
        layout.addWidget(self.result_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def login_user(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        result = login(username, password)
        if isinstance(result, User):
            if result.is_admin():
                main_menu = MainMenuRoot(user=result)
                self.setCentralWidget(main_menu)
            elif result.is_user():
                main_menu = MainMenuRoot(user=result)
                self.setCentralWidget(main_menu)
            elif result.is_root():
                main_menu = MainMenuRoot(user=result)
                self.setCentralWidget(main_menu)
        else:
            self.result_label.setText(result)

    def register_user(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        firstname = self.firstname_entry.text()
        lastname = self.lastname_entry.text()
        role = dict_ui_key_role[self.role_combobox.currentText()]
        result = register(username, password, role, firstname, lastname)
        if result:
            self.result_label.setText("Реєстрація успішна")
        else:
            self.result_label.setText(result)

def main():
    app = QApplication(sys.argv)
    window = LoginRegisterApp()
    window.show()
    sys.exit(app.exec_())
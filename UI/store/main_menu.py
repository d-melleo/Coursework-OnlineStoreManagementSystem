import tkinter as tk


class MainMenuUser:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Головне меню для користувача")

        self.current_frame = None

        self.show_user_menu()

    def show_user_menu(self):
        # Очищаємо екран перед створенням нового вмісту
        self.clear_window()

        # Додати інші елементи головного меню для користувача
        self.user_label = tk.Label(self.root, text="Меню для користувача")
        self.user_label.pack()
        # Додати інші кнопки та функціонал для користувача

    def clear_window(self):
        # Видаляємо всі дочірні віджети з кореневого вікна
        for widget in self.root.winfo_children():
            widget.destroy()

import tkinter as tk


class MainMenuAdmin:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Головне меню для адміністратора")

        self.current_frame = None

        self.show_admin_menu()

    def show_admin_menu(self):
        # Очищаємо екран перед створенням нового вмісту
        self.clear_window()

        # Додати інші елементи головного меню для адміністратора
        self.admin_label = tk.Label(self.root, text="Адміністраторське меню")
        self.admin_label.pack()

        # Створення бічного меню
        self.side_menu = tk.Frame(self.root, bg="lightgray", width=150)
        self.side_menu.pack(side="left", fill="y")

        # Список опцій для бічного меню
        options = ["Товари", "Постачальники", "Продажі", "Необроблені продажі", "Звіти", "Користувачі"]
        for option in options:
            btn = tk.Button(self.side_menu, text=option, width=15, command=lambda o=option: self.show_selected_option(o))
            btn.pack(fill="x", padx=5, pady=2)

    def show_selected_option(self, option):
        # Видалення попереднього вмісту
        if self.current_frame:
            self.current_frame.destroy()

        # Створення нового вмісту в залежності від обраної опції
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(side="right", fill="both", expand=True)

        if option == "Товари":
            # Показати вміст для опції "Товари"
            self.show_products_content()
        elif option == "Постачальники":
            # Показати вміст для опції "Постачальники"
            self.show_suppliers_content()
        elif option == "Продажі":
            # Показати вміст для опції "Продажі"
            self.show_sales_content()
        # Додайте інші умови для інших опцій

    def show_products_content(self):
        # Вміст для опції "Товари"
        label = tk.Label(self.current_frame, text="Вміст для опції 'Товари'")
        label.pack()

    def show_suppliers_content(self):
        # Вміст для опції "Постачальники"
        label = tk.Label(self.current_frame, text="Вміст для опції 'Постачальники'")
        label.pack()

    def show_sales_content(self):
        # Вміст для опції "Продажі"
        label = tk.Label(self.current_frame, text="Вміст для опції 'Продажі'")
        label.pack()

    # Додайте функції для інших опцій

    def clear_window(self):
        # Видалення всіх дочірніх віджетів з кореневого вікна
        for widget in self.root.winfo_children():
            widget.destroy()
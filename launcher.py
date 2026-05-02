import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Game Launcher")
        self.geometry("400x450")

        # Заголовок
        self.label = ctk.CTkLabel(self, text="Налаштування підключення", font=("Arial", 20, "bold"))
        self.label.pack(pady=(20, 10))

        # Поле для Нікнейму
        self.nick_entry = ctk.CTkEntry(self, placeholder_text="Ваш нікнейм", width=250)
        self.nick_entry.pack(pady=10)

        # Поле для IP
        self.ip_entry = ctk.CTkEntry(self, placeholder_text="IP-адреса сервера (напр. 127.0.0.1)", width=250)
        self.ip_entry.pack(pady=10)

        # Поле для Порту
        self.port_entry = ctk.CTkEntry(self, placeholder_text="Порт (напр. 7777)", width=250)
        self.port_entry.pack(pady=10)

        # Кнопка запуску
        self.start_button = ctk.CTkButton(self, text="ГРАТИ", command=self.start_game, 
                                          fg_color="green", hover_color="#228B22", font=("Arial", 16, "bold"))
        self.start_button.pack(pady=30)

        # Вивід статусу (для тестів)
        self.status_label = ctk.CTkLabel(self, text="", text_color="gray")
        self.status_label.pack()

    def start_game(self):
        nick = self.nick_entry.get()
        ip = self.ip_entry.get()
        port = self.port_entry.get()

        if not nick or not ip or not port:
            self.status_label.configure(text="Помилка: Заповніть усі поля!", text_color="red")
        else:
            self.status_label.configure(text=f"Запуск... {nick} підключається до {ip}:{port}", text_color="lightgreen")
            # Тут можна додати код запуску гри:
            # subprocess.Popen([f"game.exe", "-n", nick, "-h", ip, "-p", port])

if __name__ == "__main__":
    app = AppLauncher()
    app.mainloop()

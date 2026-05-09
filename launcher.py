import customtkinter as ctk


class Launcher(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Game Launcher")
        self.geometry("400x450")

        self._build_ui()

        self.username = None
        self.host = None
        self.port = None

    def _build_ui(self):
        self.label = ctk.CTkLabel(
            self,
            text="Налаштування підключення",
            font=("Arial", 20, "bold")
        )
        self.label.pack(pady=(20, 10))

        self.nick_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ваш нікнейм",
            width=250
        )
        self.nick_entry.pack(pady=10)

        self.ip_entry = ctk.CTkEntry(
            self,
            placeholder_text="IP-адреса сервера (напр. 127.0.0.1)",
            width=250
        )
        self.ip_entry.pack(pady=10)

        self.port_entry = ctk.CTkEntry(
            self,
            placeholder_text="Порт (напр. 7777)",
            width=250
        )
        self.port_entry.pack(pady=10)

        self.start_button = ctk.CTkButton(
            self,
            text="ГРАТИ",
            command=self.start_game,
            fg_color="green",
            hover_color="#228B22",
            font=("Arial", 16, "bold")
        )
        self.start_button.pack(pady=30)

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            text_color="gray"
        )
        self.status_label.pack()

    def start_game(self):
        nick = self.nick_entry.get().strip()
        ip = self.ip_entry.get().strip()
        port = self.port_entry.get().strip()
        self.username = self.entry_name.get()
        self.host = self.entry_ip.get()
        self.port = int(self.entry_port.get())
        
        
        if not nick or not ip or not port:
            self.status_label.configure(
                text="Помилка: Заповніть усі поля!",
                text_color="red"
            )
            return

        self.status_label.configure(
            text=f"Запуск... {nick} підключається до {ip}:{port}",
            text_color="lightgreen"
        )

        # приклад запуску гри
        # subprocess.Popen(["game.exe", "-n", nick, "-h", ip, "-p", port])


if __name__ == "__main__":
    app = Launcher()
    app.mainloop()

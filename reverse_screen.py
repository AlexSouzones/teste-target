import tkinter as tk
from utils import reverse_text


class ReverseScreen:
    def show_reverse(self):
        self.result.config(text=reverse_text(self.entry.get()))

    def show_reverse_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack(
            anchor="w", pady=10, padx=10
        )

        tk.Label(self.root, text="Digite uma Palavra:").pack(pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        tk.Button(self.root, text="Inverter", command=self.show_reverse).pack(pady=10)
        self.result = tk.Label(self.root, text="")
        self.result.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    ...

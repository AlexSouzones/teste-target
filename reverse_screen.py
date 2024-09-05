import tkinter as tk
from utils import (
    reverse_text,
    label_style_title,
    button_style_pages,
    label_style_result,
    label_style_info,
)


class ReverseScreen:
    def show_reverse(self):
        self.result.config(text=reverse_text(self.entry.get()))

    def show_reverse_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack(
            anchor="w", pady=10, padx=10
        )

        tk.Label(self.root, text="Digite uma Palavra:", **label_style_title).pack(
            pady=10
        )
        self.entry = tk.Entry(
            self.root,
            width=15,
            justify="center",
            font=("Arial", 20),
        )
        self.entry.pack(pady=10)
        tk.Button(
            self.root, text="Inverter", **button_style_pages, command=self.show_reverse
        ).pack(pady=10)
        self.result = tk.Label(self.root, text="", **label_style_result)
        self.result.pack(pady=10)

        self.info_title = tk.Label(
            self.root,
            text="""INFORMAÇÃO""",
            **label_style_title,
        )
        self.info_title.pack(pady=10)

        self.info_fibonacci = tk.Label(
            self.root,
            text="""Qualquer palavra digitada será invertida :)""",
            **label_style_info,
        )
        self.info_fibonacci.pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    ...

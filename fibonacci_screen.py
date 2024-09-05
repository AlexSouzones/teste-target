import tkinter as tk
from utils import (
    is_fibonacci,
    button_style_pages,
    label_style_pages,
    label_style_info,
    label_style_result,
    label_style_title,
)
from tkinter import messagebox


class FibonacciScreen:
    def check_fibonacci(self):
        number = self.entry.get()
        if not number.isdigit():
            messagebox.showwarning("Aviso", "Insira um número, por favor!")
        else:
            number = int(self.entry.get())
            if is_fibonacci(number):
                self.result.config(
                    text=f"{number} pertence à sequência de Fibonacci.", fg="green"
                )
            else:
                self.result.config(
                    text=f"{number} não pertence à sequência de Fibonacci.", fg="red"
                )

    def show_fibonacci_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack(
            anchor="w", pady=10, padx=10
        )

        tk.Label(self.root, text="Digite um número:", **label_style_pages).pack(pady=10)
        self.entry = tk.Entry(
            self.root,
            width=5,
            font=("Arial", 30),
        )
        self.entry.pack(pady=10)
        tk.Button(
            self.root,
            text="VERIFICAR",
            command=self.check_fibonacci,
            **button_style_pages,
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
            text="""Na matemática, a sucessão de Fibonacci, é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.""",
            **label_style_info,
        )
        self.info_fibonacci.pack(pady=10)


if __name__ == "__main__":
    ...

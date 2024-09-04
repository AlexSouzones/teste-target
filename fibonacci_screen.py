import tkinter as tk
from utils import is_fibonacci
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

        tk.Label(self.root, text="Digite um número:").pack(pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        tk.Button(self.root, text="Verificar", command=self.check_fibonacci).pack(
            pady=10
        )
        self.result = tk.Label(self.root, text="")
        self.result.pack(pady=10)


if __name__ == "__main__":
    ...

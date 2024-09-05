import tkinter as tk
from utils import button_style


class HomeScreen:
    def create_main_screen(self):
        self.clear_screen()

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        tk.Button(
            main_frame,
            text="Fibonacci",
            command=self.show_fibonacci_screen,
            **button_style
        ).pack(pady=10)
        tk.Button(
            main_frame,
            text="Renda Mensal Empresarial",
            command=self.show_renda_mensal_screen,
            **button_style
        ).pack(pady=10)
        tk.Button(
            main_frame,
            text="Gráfico Faturamento Empresarial",
            command=self.show_grafico_screen,
            **button_style
        ).pack(pady=10)
        tk.Button(
            main_frame, text="Reverse", command=self.show_reverse_screen, **button_style
        ).pack(pady=10)


if __name__ == "__main__":
    ...

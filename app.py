import tkinter as tk
from reverse_screen import ReverseScreen
from fibonacci_screen import FibonacciScreen
from monthly_income_screen import MonthlyIncomeScreen
from graphic_screen import GraphicScreen


class App(ReverseScreen, FibonacciScreen, MonthlyIncomeScreen, GraphicScreen):
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo")
        self.root.geometry("800x600")
        self.create_main_screen()

    def create_main_screen(self):
        self.clear_screen()

        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        tk.Button(
            main_frame, text="Fibonacci", command=self.show_fibonacci_screen
        ).pack(pady=10)
        tk.Button(
            main_frame,
            text="Renda Mensal Empresarial",
            command=self.show_renda_mensal_screen,
        ).pack(pady=10)
        tk.Button(
            main_frame,
            text="Gráfico Faturamento Empresarial",
            command=self.show_grafico_screen,
        ).pack(pady=10)
        tk.Button(main_frame, text="Reverse", command=self.show_reverse_screen).pack(
            pady=10
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from reverse_screen import ReverseScreen
from fibonacci_screen import FibonacciScreen
from monthly_income_screen import MonthlyIncomeScreen
from graphic_screen import GraphicScreen
from home_screen import HomeScreen


class App(
    ReverseScreen, FibonacciScreen, MonthlyIncomeScreen, GraphicScreen, HomeScreen
):
    def __init__(self, root):
        self.root = root
        self.root.title("Teste Técnico Target Sistemas")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.create_main_screen()
        self.setup_ui()
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Helvetica", 14))
        self.style.configure("Treeview", font=("Helvetica", 12))
    def setup_ui(self):
        self.root.configure(bg="lightblue")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

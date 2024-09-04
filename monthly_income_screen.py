import tkinter as tk
from tkinter import filedialog, messagebox
import json
import xml.etree.ElementTree as ET
from utils import load_data


class MonthlyIncomeScreen:

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("XML files", "*.xml")]
        )
        if file_path:
            load_data(file_path)
        else:
            messagebox.showwarning("Not Found!", "Nenhum arquivo selecionado!")

    def show_renda_mensal_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack(
            anchor="w", pady=10, padx=10
        )

        tk.Button(self.root, text="Escolher arquivo", command=self.load_file).pack(
            pady=10
        )

        min_income_var = tk.StringVar()
        max_income_var = tk.StringVar()
        days_above_avg_var = tk.StringVar()

        tk.Label(self.root, text="Faturamento Mínimo Mensal:").pack(pady=5)
        tk.Entry(self.root, textvariable=min_income_var).pack(pady=5)

        tk.Label(self.root, text="Faturamento Máximo Mensal:").pack(pady=5)
        tk.Entry(self.root, textvariable=max_income_var).pack(pady=5)

        tk.Label(self.root, text="Dias de Faturamento Acima da Média:").pack(pady=5)
        tk.Entry(self.root, textvariable=days_above_avg_var).pack(pady=5)


if __name__ == "__main__":
    ...

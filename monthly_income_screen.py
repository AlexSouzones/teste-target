import tkinter as tk
from tkinter import filedialog, messagebox
from utils import load_data, state_values
from utils import (
    label_style_info,
    label_style_legend,
    button_style_pages,
    label_style_title,
)


class MonthlyIncomeScreen:

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            data = load_data(file_path)
            if data:
                ref_info = state_values(data)
                print(ref_info)
                self.min_income_var.set(f"R$ {ref_info['min value']['valor']:.4f}")
                self.max_income_var.set(f"R$ {ref_info['max value']['valor']:.4f}")
                self.mid_income_var.set(f"R$ {ref_info['mid value']:.4f}")
                self.days_above_avg_var.set(f"DIAS: {ref_info['best days']}")
        else:
            messagebox.showwarning("Not Found!", "Nenhum arquivo selecionado!")

    def show_renda_mensal_screen(self):
        self.clear_screen()

        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack(
            anchor="w", pady=10, padx=10
        )
        tk.Button(
            self.root,
            text="Escolher arquivo",
            command=self.load_file,
            **button_style_pages,
        ).pack(pady=10)

        frame = tk.Frame(self.root, bg="darkgray")
        frame.pack(pady=10)

        self.min_income_var = tk.StringVar(value="R$ 0,00")
        self.max_income_var = tk.StringVar(value="R$ 0,00")
        self.mid_income_var = tk.StringVar(value="R$ 0,00")
        self.days_above_avg_var = tk.StringVar(value="0 dias")

        tk.Label(frame, text="Faturamento Mínimo Mensal:", **label_style_legend).grid(
            row=0, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Label(frame, textvariable=self.min_income_var, **label_style_info).grid(
            row=0, column=1, padx=10, pady=5, sticky="w"
        )

        tk.Label(frame, text="Faturamento Máximo Mensal:", **label_style_legend).grid(
            row=1, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Label(frame, textvariable=self.max_income_var, **label_style_info).grid(
            row=1, column=1, padx=10, pady=5, sticky="w"
        )

        tk.Label(frame, text="Faturamento Médio Mensal:", **label_style_legend).grid(
            row=2, column=0, padx=10, pady=5, sticky="e"
        )
        tk.Label(frame, textvariable=self.mid_income_var, **label_style_info).grid(
            row=2, column=1, padx=10, pady=5, sticky="w"
        )

        tk.Label(
            frame, text="Dias Faturando Acima da Média:", **label_style_legend
        ).grid(row=3, column=0, padx=10, pady=5, sticky="e")
        tk.Label(frame, textvariable=self.days_above_avg_var, **label_style_info).grid(
            row=3, column=1, padx=10, pady=5, sticky="w"
        )

        self.info_title = tk.Label(
            self.root,
            text="""INFORMAÇÃO""",
            **label_style_title,
        )
        self.info_title.pack(pady=10)

        self.info_files = tk.Label(
            self.root,
            text="Os arquivos a serem enviados devem estar nos formatos JSON ou XML e seguir o padrão da atividade.",
            **label_style_info,
        )
        self.info_files.pack(pady=5)


if __name__ == "__main__":
    ...

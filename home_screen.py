import tkinter as tk
from utils import button_style, linkedin_link, github_link
from tkinter import Menu, PhotoImage


class HomeScreen:

    def create_main_screen(self):

        self.clear_screen()

        main_frame = tk.Frame(self.root, bg="lightblue")
        main_frame.pack(fill="both", expand=True)

        self.barrademenu = Menu(self.root)
        self.root.config(menu=self.barrademenu)
        self.icon_github = PhotoImage(file="icons/github.png").subsample(5, 5)
        self.icon_linkedin = PhotoImage(file="icons/linkedin.png").subsample(5, 5)
        contatos = Menu(self.barrademenu, tearoff=0, bg="#F5F5DC")

        self.barrademenu.add_cascade(label="CONTATOS", menu=contatos)
        contatos.add_command(
            label="Linkedin", image=self.icon_linkedin, command=linkedin_link
        )
        contatos.add_command(
            label="Github", image=self.icon_github, command=github_link
        )

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
            text="Gráfico Faturamento",
            command=self.show_grafico_screen,
            **button_style
        ).pack(pady=10)
        tk.Button(
            main_frame, text="Reverse", command=self.show_reverse_screen, **button_style
        ).pack(pady=10)


if __name__ == "__main__":
    ...

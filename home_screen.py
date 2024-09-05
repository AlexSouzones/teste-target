import tkinter as tk
from utils import button_style, linkedin_link, github_link
from tkinter import Menu, Text, INSERT


class HomeScreen:

    def contatos(self):
        self.window = tk.Tk()
        self.window.title("Onde me Encontrar :')")
        self.window.configure(bg="lightblue")
        self.window.resizable(False, False)

        infos = "\nEmail: alexandresouzones@gmail.com\n\nGithub: https://github.com/AlexSouzones\n\nLinkedin: https://www.linkedin.com/in/alexandre-p-souza-0b9532211"
        lbinfo = Text(self.window, width=40, height=7, bg="#FFFACD")
        lbinfo.insert(INSERT, infos)
        lbinfo.config(state="disabled")
        lbinfo.grid(row=0, column=0, padx=5, pady=5)

        self.window.mainloop()

    def create_main_screen(self):

        self.clear_screen()

        main_frame = tk.Frame(self.root, bg="lightblue")
        main_frame.pack(fill="both", expand=True)

        self.barrademenu = Menu(self.root)
        self.root.config(menu=self.barrademenu)

        contatos = Menu(self.barrademenu, tearoff=0)
        self.barrademenu.add_cascade(label="contatos", menu=contatos)
        contatos.add_command(label="Contatos", command=self.contatos)
        contatos.add_command(label="Linkedin", command=linkedin_link)
        contatos.add_command(label="Github", command=github_link)

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

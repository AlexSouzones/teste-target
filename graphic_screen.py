import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from utils import calculate_percentage


class GraphicScreen:
    def show_grafico_screen(self):
        self.clear_screen()

        self.states = {}
        self.colors = {}

        tk.Button(self.root, text="Voltar", command=self.create_main_screen).pack(
            anchor="w", pady=10, padx=10
        )

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Nome do Estado:").grid(row=0, column=0, padx=5)
        state_entry = tk.Entry(input_frame)
        state_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Valor:").grid(row=1, column=0, padx=5)
        value_entry = tk.Entry(input_frame)
        value_entry.grid(row=1, column=1, padx=5)

        tk.Button(
            input_frame,
            text="Adicionar",
            command=lambda: self.add_state(state_entry, value_entry),
        ).grid(row=2, columnspan=2, pady=10)

        self.tree = ttk.Treeview(
            self.root, columns=("Estado", "Valor", "Porcentagem"), show="headings"
        )
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Valor", text="Valor")
        self.tree.heading("Porcentagem", text="Porcentagem")
        self.tree.pack(pady=5)

        global graph_frame
        graph_frame = tk.Frame(self.root)
        graph_frame.pack(pady=10)

    def add_state(self, state_entry, value_entry):
        state = state_entry.get()
        value = float(value_entry.get())
        self.states[state] = value
        color = plt.cm.tab20(len(self.states) % 20)[:3]
        self.colors[state] = color
        self.update_treeview()
        state_entry.delete(0, tk.END)
        value_entry.delete(0, tk.END)
        self.plot_graph()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        total = sum(self.states.values())
        for state, value in self.states.items():
            percentage = calculate_percentage(value, total)
            self.tree.insert("", "end", values=(state, value, f"{percentage:.2f}%"))

    def plot_graph(self):
        fig, ax = plt.subplots(figsize=(4, 4))
        sizes = self.states.values()
        colors = [self.colors[state] for state in self.states]
        ax.pie(sizes, colors=colors, labels=None, autopct="%1.1f%%", startangle=140)
        ax.axis("equal")

        for widget in graph_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    ...

# Parte visual 

import tkinter as tk
from tkinter import ttk

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Biblioteca Escolar")
        self.janela.geometry("900x600")

        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(fill="both", expand=True)

        self.aba_livros = ttk.Frame(self.notebook)
        self.aba_alunos = ttk.Frame(self.notebook)
        self.aba_emprestimos = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_livros, text="Livros")
        self.notebook.add(self.aba_alunos, text="Alunos")
        self.notebook.add(self.aba_emprestimos, text="Empréstimos")

        self.janela.mainloop()
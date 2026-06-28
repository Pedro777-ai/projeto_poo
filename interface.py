# Parte visual 

import tkinter as tk
from tkinter import ttk
from biblioteca import Biblioteca
from livro import Livro

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Biblioteca Escolar")
        self.janela.geometry("900x600")
        self.biblioteca = Biblioteca()

        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(fill="both", expand=True)

        self.aba_livros = ttk.Frame(self.notebook)
        self.aba_alunos = ttk.Frame(self.notebook)
        self.aba_emprestimos = ttk.Frame(self.notebook)

        self.notebook.add(self.aba_livros, text="Livros")
        self.notebook.add(self.aba_alunos, text="Alunos")
        self.notebook.add(self.aba_emprestimos, text="Empréstimos")

        ttk.Label(self.aba_livros, text="Título: ").grid(row=0, column=0, padx=10, pady=10)
        self.entry_titulo = ttk.Entry(self.aba_livros, width=40)
        self.entry_titulo.grid(row=0, column=1)

        ttk.Label(self.aba_livros, text="Autor: ").grid(row=1, column=0, padx=10, pady=10)
        self.entry_autor = ttk.Entry(self.aba_livros, width=40)
        self.entry_autor.grid(row=1, column=1)

        ttk.Button(self.aba_livros, text="Cadastrar", command=self.cadastrar_livro).grid(row=2, column=1, pady=15)


        self.janela.mainloop()

    def cadastrar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        livro = Livro(titulo, autor)
        self.biblioteca.adicionar_livro(livro)

        print(f"Livro cadastrado: {livro}")

        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
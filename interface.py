# Parte visual 

import tkinter as tk
from tkinter import ttk, messagebox
from biblioteca import Biblioteca
from livro import Livro
from aluno import Aluno

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

<<<<<<< HEAD
        ttk.Button(self.aba_livros, text="Cadastrar", command=self.cadastrar_livro).grid(row=2, column=1, pady=15)
        
=======
        ttk.Label(self.aba_livros, text="Editora:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_editora = ttk.Entry(self.aba_livros, width=40)
        self.entry_editora.grid(row=2, column=1)

        ttk.Label(self.aba_livros, text="Categoria:").grid(row=3, column=0, padx=10, pady=10)

        self.combo_categoria = ttk.Combobox(
            self.aba_livros,
            values=[
                "Romance",
                "Ficção",
                "História",
                "Ciência",
                "Informática",
                "Biografia",
                "Outros"
            ],
            state="readonly",
            width=37
        )

        self.combo_categoria.grid(row=3, column=1)
        self.combo_categoria.current(0)

        #Livro
        ttk.Label(self.aba_livros, text="Ano:").grid(row=4, column=0, padx=10, pady=10)
        self.entry_ano = ttk.Entry(self.aba_livros, width=40)
        self.entry_ano.grid(row=4, column=1)

        ttk.Label(self.aba_livros, text="Quantidade:").grid(row=5, column=0, padx=10, pady=10)
        self.entry_quantidade = ttk.Entry(self.aba_livros, width=40)
        self.entry_quantidade.grid(row=5, column=1)
        
        
        ttk.Button(self.aba_livros, text="Cadastrar Livro", command=self.cadastrar_livro).grid(row=6, column=1, pady=20)

        #Aluno
        ttk.Label(self.aba_alunos, text="Nome Completo: ").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome = ttk.Entry(self.aba_alunos, width=40)
        self.entry_nome.grid(row=0, column=1)

        ttk.Label(self.aba_alunos, text="Matrícula: ").grid(row=1, column=0, padx=10, pady=10)
        self.entry_matricula = ttk.Entry(self.aba_alunos, width=40)
        self.entry_matricula.grid(row=1, column=1)

        ttk.Label(self.aba_alunos, text="Email Escolar:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_email = ttk.Entry(self.aba_alunos, width=40)
        self.entry_email.grid(row=2, column=1)

        ttk.Button(self.aba_alunos, text="Cadastrar Aluno", command=self.cadastrar_aluno).grid(row=6, column=1, pady=20)
        

>>>>>>> c8634010301623078932f237688513ad3300dd96

        self.janela.mainloop()

    def cadastrar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        editora = self.entry_editora.get()
        categoria = self.combo_categoria.get()
        ano = self.entry_ano.get()
        quantidade = self.entry_quantidade.get()
        if not titulo:
            messagebox.showerror(
            "Erro",
            "O título é obrigatório."
        )
            return
        if not autor:
            messagebox.showerror(
            "Erro",
            "O autor é obrigatório."
        )
            return
        if not editora:
            messagebox.showerror(
            "Erro",
            "A editora é obrigatório."
        )
            return
        if not ano:
            messagebox.showerror(
            "Erro",
            "O ano é obrigatório."
        )
            return
        if not quantidade:
            messagebox.showerror(
            "Erro",
            "A quantidade é obrigatório."
        )
            return
        livro = Livro(
            titulo,
            autor,
            editora,
            categoria,
            ano,
            quantidade
        )
        self.biblioteca.adicionar_livro(livro)
        
        print(f"Livro cadastrado: {livro}")

        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_editora.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)

    def cadastrar_aluno(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        email = self.entry_email.get()
        if not nome:
            messagebox.showerror(
            "Erro",
            "O nome é obrigatório."
        )
            return
        if not matricula:
            messagebox.showerror(
            "Erro",
            "A matricula é obrigatória."
        )
            return
        if not email:
            messagebox.showerror(
            "Erro",
            "O email é obrigatório."
        )
            return
        aluno = Aluno(
            nome,
            matricula,
            email
        )
        self.biblioteca.adicionar_aluno(aluno)
        
        print(f"Aluno cadastrado: {aluno}")

        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        

    
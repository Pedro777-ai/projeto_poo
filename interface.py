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
        self.janela.geometry("1300x700")
        self.biblioteca = Biblioteca()
        self.livro_selecionado = None

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

        colunas = ("Título", "Autor", "Editora", "Categoria", "Ano", "Quantidade", "Disponíveis")

        self.tabela_livros = ttk.Treeview(
            self.aba_livros,
            columns=colunas,
            show="headings",
            height=10
        )

        for coluna in colunas:
            self.tabela_livros.heading(coluna, text=coluna)
            self.tabela_livros.column(coluna, width=180)

        self.tabela_livros.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=10,
            pady=20
        )
        
        ttk.Button(
            self.aba_livros,
            text="Editar",
            command=self.editar_livro
        ).grid(row=8, column=0, pady=10)

        ttk.Button(
            self.aba_livros,
            text="Excluir",
            command=self.excluir_livro
        ).grid(row=8, column=1, pady=10)

        self.tabela_livros.bind(
            "<<TreeviewSelect>>",
            self.selecionar_livro)



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
        self.atualizar_tabela_livros()


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
        if self.biblioteca.adicionar_livro(livro):
            self.atualizar_tabela_livros()

            messagebox.showinfo(
                "Sucesso",
                "Livro cadastrado com sucesso!"
            )

            self.entry_titulo.delete(0, tk.END)
            self.entry_autor.delete(0, tk.END)
            self.entry_editora.delete(0, tk.END)
            self.entry_ano.delete(0, tk.END)
            self.entry_quantidade.delete(0, tk.END)

        else:
            messagebox.showerror(
                "Erro",
                "Este livro já está cadastrado."
            )
        
        print(f"Livro cadastrado: {livro}")

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
        
    def atualizar_tabela_livros(self):
        
        for item in self.tabela_livros.get_children():
            self.tabela_livros.delete(item)

        
        for livro in self.biblioteca.livros:
            self.tabela_livros.insert(
                "",
                tk.END,
                values=(
                    livro.titulo,
                    livro.autor,
                    livro.editora,
                    livro.categoria,
                    livro.ano,
                    livro.quantidade,
                    livro.disponiveis
                )
            )

    def selecionar_livro(self, event):
        selecionado = self.tabela_livros.selection()

        if not selecionado:
            return

        valores = self.tabela_livros.item(selecionado[0], "values")
        titulo = valores[0]
        autor = valores[1]

        for livro in self.biblioteca.livros:
            if livro.titulo == titulo and livro.autor == autor:
                self.livro_selecionado = livro
                break

        self.entry_titulo.delete(0, tk.END)
        self.entry_titulo.insert(0, valores[0])

        self.entry_autor.delete(0, tk.END)
        self.entry_autor.insert(0, valores[1])

        self.entry_editora.delete(0, tk.END)
        self.entry_editora.insert(0, valores[2])

        self.combo_categoria.set(valores[3])

        self.entry_ano.delete(0, tk.END)
        self.entry_ano.insert(0, valores[4])

        self.entry_quantidade.delete(0, tk.END)
        self.entry_quantidade.insert(0, valores[5])

    def editar_livro(self):
        if self.livro_selecionado is None:
            messagebox.showwarning(
                "Aviso",
                "Selecione um livro para editar."
            )
            return

        self.livro_selecionado.titulo = self.entry_titulo.get()
        self.livro_selecionado.autor = self.entry_autor.get()
        self.livro_selecionado.editora = self.entry_editora.get()
        self.livro_selecionado.categoria = self.combo_categoria.get()
        self.livro_selecionado.ano = self.entry_ano.get()
        self.livro_selecionado.quantidade = int(self.entry_quantidade.get())

        self.biblioteca.salvar_livros()

        self.atualizar_tabela_livros()

        messagebox.showinfo(
            "Sucesso",
            "Livro atualizado com sucesso!"
        )
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_editora.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)

    def excluir_livro(self):
        if self.livro_selecionado is None:
            messagebox.showwarning(
                "Aviso",
                "Selecione um livro."
            )
            return

        resposta = messagebox.askyesno(
            "Confirmação",
            f"Deseja excluir '{self.livro_selecionado.titulo}'?"
        )

        if not resposta:
            return

        self.biblioteca.excluir_livro(
            self.livro_selecionado.titulo,
            self.livro_selecionado.autor
        )

        self.atualizar_tabela_livros()

        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_editora.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)

        self.combo_categoria.current(0)

        self.livro_selecionado = None

        messagebox.showinfo(
            "Sucesso",
            "Livro excluído com sucesso."
        )
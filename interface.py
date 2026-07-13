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
        self.aluno_selecionado = None

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

            #===============
            #   LIVRO
            #===============

        ttk.Label(self.aba_livros, text="Ano:").grid(row=4, column=0, padx=10, pady=10)
        self.entry_ano = ttk.Entry(self.aba_livros, width=40)
        self.entry_ano.grid(row=4, column=1)

        ttk.Label(self.aba_livros, text="Quantidade:").grid(row=5, column=0, padx=10, pady=10)
        self.entry_quantidade = ttk.Entry(self.aba_livros, width=40)
        self.entry_quantidade.grid(row=5, column=1)
        
        
        ttk.Button(self.aba_livros, text="Cadastrar Livro", command=self.cadastrar_livro).grid(row=6, column=1, pady=20)

        ttk.Label(self.aba_livros, text="Pesquisar:").grid(row=7, column=0, padx=10)

        self.entry_pesquisa = ttk.Entry(self.aba_livros, width=40)
        self.entry_pesquisa.grid(row=7, column=1, sticky="w")

        ttk.Button(
            self.aba_livros,
            text="Pesquisar",
            command=self.pesquisar_livro
        ).grid(row=7, column=2, padx=10)


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
            row=8,
            column=0,
            columnspan=3,
            padx=10,
            pady=20
        )
        
        ttk.Button(
            self.aba_livros,
            text="Editar",
            command=self.editar_livro
        ).grid(row=9, column=0, pady=10)

        ttk.Button(
            self.aba_livros,
            text="Excluir",
            command=self.excluir_livro
        ).grid(row=9, column=1, pady=10)

        self.tabela_livros.bind(
            "<<TreeviewSelect>>",
            self.selecionar_livro)

            #================
            #      ALUNO
            #================

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
       
        ttk.Button(
            self.aba_alunos,
            text="Editar",
            command=self.editar_aluno
        ).grid(row=6, column=0, pady=20)


        ttk.Button(
            self.aba_alunos,
            text="Excluir",
            command=self.excluir_aluno
        ).grid(row=6, column=2, pady=20)
        
        colunas = ("Nome", "Matrícula", "Email")

        self.tabela_alunos = ttk.Treeview(
            self.aba_alunos,
            columns=colunas,
            show="headings",
            height=10
        )

        for coluna in colunas:
            self.tabela_alunos.heading(coluna, text=coluna)
            self.tabela_alunos.column(coluna, width=250)

        self.tabela_alunos.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=10,
            pady=20
        )
        self.tabela_alunos.bind(
        "<<TreeviewSelect>>",
        self.selecionar_aluno)

        self.atualizar_tabela_alunos()

        #================
        #  EMPRÉSTIMOS
        #================
        
        ttk.Label(
            self.aba_emprestimos,
            text="Aluno:"
        ).grid(row=0, column=0, padx=10, pady=10)


        self.combo_alunos = ttk.Combobox(
            self.aba_emprestimos,
            width=40,
            state="readonly"
        )

        self.combo_alunos.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )


        ttk.Label(
            self.aba_emprestimos,
            text="Livro:"
        ).grid(row=1, column=0, padx=10, pady=10)


        self.combo_livros = ttk.Combobox(
            self.aba_emprestimos,
            width=40,
            state="readonly"
        )

        self.combo_livros.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )


        ttk.Button(
            self.aba_emprestimos,
            text="Realizar Empréstimo",
            command=self.realizar_emprestimo
        ).grid(
            row=2,
            column=1,
            pady=20
        )

        colunas_emprestimo = (
            "Aluno",
            "Livro",
            "Status"
        )


        self.tabela_emprestimos = ttk.Treeview(
            self.aba_emprestimos,
            columns=colunas_emprestimo,
            show="headings",
            height=12
        )


        for coluna in colunas_emprestimo:
            self.tabela_emprestimos.heading(
                coluna,
                text=coluna
            )

            self.tabela_emprestimos.column(
                coluna,
                width=250
            )


        self.tabela_emprestimos.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=10,
            pady=20
        )

        self.atualizar_combos_emprestimo()

        
        self.janela.mainloop()
            #===============
            #   LIVRO
            #===============
    def cadastrar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        editora = self.entry_editora.get()
        categoria = self.combo_categoria.get()
        ano = self.entry_ano.get()
        try:
            quantidade = int(self.entry_quantidade.get())

        except ValueError:
            messagebox.showerror(
                "Erro",
                "A quantidade deve ser um número."
            )
            return
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
    
    def pesquisar_livro(self):
        texto = self.entry_pesquisa.get().lower().strip()

        if texto == "":
            self.atualizar_tabela_livros()
            return  
        
        for item in self.tabela_livros.get_children():
            self.tabela_livros.delete(item)

        for livro in self.biblioteca.livros:
            if (
                texto in livro.titulo.lower()
                or texto in livro.autor.lower()
                or texto in livro.categoria.lower()
            ):
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
            #================
            #      ALUNO
            #================
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
        
        if self.biblioteca.adicionar_aluno(aluno):
            self.atualizar_tabela_alunos()

            messagebox.showinfo(
                "Sucesso",
                "Aluno cadastrado com sucesso!"
            )

            self.entry_nome.delete(0, tk.END)
            self.entry_matricula.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)

        else:
            messagebox.showerror(
                "Erro",
                "Este aluno já está cadastrado."
            )
        print(f"Aluno cadastrado: {aluno}")

        

    def atualizar_tabela_alunos(self):

        for item in self.tabela_alunos.get_children():
            self.tabela_alunos.delete(item)

        for aluno in self.biblioteca.alunos:
            self.tabela_alunos.insert(
                "",
                tk.END,
                values=(
                    aluno.nome,
                    aluno.matricula,
                    aluno.email
                )
            )
    def selecionar_aluno(self, event):

        selecionado = self.tabela_alunos.selection()

        if not selecionado:
            return

        valores = self.tabela_alunos.item(
            selecionado[0],
            "values"
        )

        nome = valores[0]
        matricula = valores[1]

        for aluno in self.biblioteca.alunos:
            if (
                aluno.nome == nome
                and aluno.matricula == matricula
            ):
                self.aluno_selecionado = aluno
                break


        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, valores[0])

        self.entry_matricula.delete(0, tk.END)
        self.entry_matricula.insert(0, valores[1])

        self.entry_email.delete(0, tk.END)
        self.entry_email.insert(0, valores[2])

    def editar_aluno(self):

        if self.aluno_selecionado is None:
            messagebox.showwarning(
                "Aviso",
                "Selecione um aluno."
            )
            return


        self.aluno_selecionado.nome = self.entry_nome.get()
        self.aluno_selecionado.matricula = self.entry_matricula.get()
        self.aluno_selecionado.email = self.entry_email.get()


        self.biblioteca.editar_aluno(
            self.aluno_selecionado
        )


        self.atualizar_tabela_alunos()


        messagebox.showinfo(
            "Sucesso",
            "Aluno atualizado com sucesso!"
        )

    def excluir_aluno(self):

        if self.aluno_selecionado is None:
            messagebox.showwarning(
                "Aviso",
                "Selecione um aluno."
            )
            return


        resposta = messagebox.askyesno(
            "Confirmação",
            f"Deseja excluir {self.aluno_selecionado.nome}?"
        )


        if not resposta:
            return


        self.biblioteca.excluir_aluno(
            self.aluno_selecionado.matricula
        )


        self.atualizar_tabela_alunos()
        self.atualizar_combos_emprestimo()


        self.entry_nome.delete(0, tk.END)
        self.entry_matricula.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)


        self.aluno_selecionado = None


        messagebox.showinfo(
            "Sucesso",
            "Aluno excluído com sucesso!"
        )    

        #================
        #  EMPRÉSTIMOS
        #================

    def atualizar_combos_emprestimo(self):
        alunos = []

        for aluno in self.biblioteca.alunos:
            alunos.append(
                aluno.nome
            )
        livros = []
        for livro in self.biblioteca.livros:
            if livro.disponiveis > 0:
                livros.append(
                    livro.titulo
                )
        self.combo_alunos["values"] = alunos
        self.combo_livros["values"] = livros

    def realizar_emprestimo(self):
        aluno_nome = self.combo_alunos.get()
        livro_titulo = self.combo_livros.get()

        if not aluno_nome:
            messagebox.showerror(
                "Erro",
                "Selecione um aluno."
            )
            return

        if not livro_titulo:
            messagebox.showerror(
                "Erro",
                "Selecione um livro."
            )
            return

        aluno = None
        livro = None

        for a in self.biblioteca.alunos:
            if a.nome == aluno_nome:
                aluno = a
                break

        for l in self.biblioteca.livros:
            if l.titulo == livro_titulo:
                livro = l
                break

        if aluno and livro:
            sucesso = self.biblioteca.realizar_emprestimo(
                aluno,
                livro
            )

            if sucesso:
                messagebox.showinfo(
                    "Sucesso",
                    "Empréstimo realizado!"
                )

                self.atualizar_tabela_livros()
                self.atualizar_combos_emprestimo()
                self.atualizar_tabela_emprestimos()

            else:
                messagebox.showerror(
                    "Erro",
                    "Livro indisponível."
                )

    def atualizar_tabela_emprestimos(self):

        for item in self.tabela_emprestimos.get_children():
            self.tabela_emprestimos.delete(item)

        for emprestimo in self.biblioteca.emprestimos:

            self.tabela_emprestimos.insert(
                "",
                tk.END,
                values=(
                    emprestimo.aluno.nome,
                    emprestimo.livro.titulo,
                    emprestimo.status
                )
            )
        
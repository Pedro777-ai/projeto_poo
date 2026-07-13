# Controla os livros e alunos
import json
from livro import Livro
from aluno import Aluno

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

        self.carregar_livros()
        self.carregar_alunos()

    def adicionar_livro(self, livro):
       for livro_existente in self.livros:
            if (
                livro_existente.titulo.lower() == livro.titulo.lower()
                and
                livro_existente.autor.lower() == livro.autor.lower()
            ):
                return False
            self.livros.append(livro)
            self.salvar_livros()
            return True
        
    def salvar_livros(self):
        dados = []

        for livro in self.livros:
            dados.append({
            "titulo": livro.titulo,
            "autor": livro.autor,
            "editora": livro.editora,
            "categoria": livro.categoria,
            "ano": livro.ano,
            "quantidade": livro.quantidade,
            "disponiveis": livro.disponiveis
        })


        with open("dados/livros.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_livros(self):
        try:
            with open("dados/livros.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                for item in dados:
                    livro = Livro(
                      item["titulo"],
                      item["autor"],
                      item["editora"],
                      item["categoria"],
                      item["ano"],
                      item["quantidade"]
                    )

                    livro.disponiveis = item["disponiveis"]

                    self.livros.append(livro)

        except FileNotFoundError:
            pass

    def editar_livro(self, livro):
        self.salvar_livros()

    def excluir_livro(self, titulo, autor):
        for livro in self.livros:
            if livro.titulo == titulo and livro.autor == autor:
                self.livros.remove(livro)
                self.salvar_livros()
                return True

        return False

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        self.salvar_alunos()
    
    def salvar_alunos(self):
        dados = []

        for aluno in self.alunos:
            dados.append({
            "nome": aluno.nome,
            "matricula": aluno.matricula,
            "email": aluno.email
        })


        with open("dados/alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_alunos(self):
        try:
            with open("dados/alunos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                for item in dados:
                    aluno = Aluno(
                      item["nome"],
                      item["matricula"],
                      item["email"]
                    )

                    self.alunos.append(aluno)

        except FileNotFoundError:
            pass

    def editar_aluno(self, aluno):
        self.salvar_alunos()

    def excluir_aluno(self, matricula):

        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                self.salvar_alunos()
                return True

        return False
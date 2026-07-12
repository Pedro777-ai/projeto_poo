# Controla os livros e alunos
import json
from livro import Livro
from aluno import Aluno

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

        self.carregar_livros()

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        self.salvar_livros()
        
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

# Classe que representa um empréstimo

class Emprestimo:

    def __init__(self, aluno, livro):
        self.aluno = aluno
        self.livro = livro
        self.status = "Ativo"


    def devolver(self):
        self.status = "Devolvido"


    def __str__(self):
        return f"{self.aluno.nome} - {self.livro.titulo} - {self.status}"
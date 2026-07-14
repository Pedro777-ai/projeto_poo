# Classe que representa um empréstimo
from datetime import datetime, timedelta

class Emprestimo:

    def __init__(self, aluno, livro):
        self.aluno = aluno
        self.livro = livro

        self.data_emprestimo = datetime.now()

        self.data_devolucao = (
            self.data_emprestimo +
            timedelta(days=21)
        )

        self.status = "Ativo"


    def devolver(self):
        self.status = "Devolvido"


    def __str__(self):
        return f"{self.aluno.nome} - {self.livro.titulo} - {self.status}"
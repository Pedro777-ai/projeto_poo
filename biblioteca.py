# Controla os livros e alunos

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
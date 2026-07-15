# Classe Aluno

class Aluno:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def __str__(self):
        return f"\n{self.nome} \n({self.matricula}) \n{self.email}"
        
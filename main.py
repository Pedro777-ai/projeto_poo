from livro import Livro
from aluno import Aluno
from biblioteca import Biblioteca

biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro( "1984", "George Orwell")

aluno1 = Aluno("Pedro", "20251174010002")
aluno2 = Aluno("Igor", "20251174010035")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_aluno(aluno1)
biblioteca.adicionar_aluno(aluno2)

print("Livros cadastrados:")
for livro in biblioteca.livros:
    print(livro)

print("\nAlunos cadastrados:")
for aluno in biblioteca.alunos:
    print(aluno)




from livro import Livro

livro = Livro("Dom Casmurro", "Machado de Assis")

print(livro)
print(livro.disponivel)

livro.emprestar()

print(livro.disponivel)
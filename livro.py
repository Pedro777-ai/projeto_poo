# Classe Livro

class Livro:
    def __init__(self, titulo, autor, editora, categoria, ano, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.quantidade = quantidade
        self.disponiveis = quantidade
        
    
    def emprestar(self):
        if self.disponiveis > 0:
            self.disponiveis -= 1
    
    def devolver(self):
        if self.disponiveis < self.quantidade:
            self.disponiveis += 1

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.editora} - {self.categoria} - {self.ano} - {self.quantidade}"
    
    
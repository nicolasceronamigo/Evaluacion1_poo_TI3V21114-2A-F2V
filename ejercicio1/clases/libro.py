#Se asume que copias es un número positivo

class Libro:
    def __init__(self, titulo:str, autor:str, copias:int):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
    
    def mostrar_estado(self):
        print(f"| Titulo: {self.titulo} | Autor: {self.autor} | Copias: {self.copias} |")
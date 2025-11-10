from .libro import Libro

class Biblioteca:
    def __init__(self):
        self.catalogo: list[Libro] = []
    
    #Método para registrar libros
    def registrar_libro(self, titulo: str, autor: str, copias: int):
        libro = Libro(titulo, autor, copias)
        #Se asume que solo se puede registrar un libro si es que no existe en la biblioteca
        if not self.libro_existe(libro.titulo):
            self.catalogo.append(libro)
            return f"Libro {titulo} registrado en biblioteca"
        return f"El libro {libro.titulo} ya existe en la bilbioteca"
    
    #Método para mostrar los estados de todos los libros registrados
    def mostrar_catalogo(self):
        catalogo = f"Catálogo biblioteca\n"
        for libro in self.catalogo:
            catalogo += libro.mostrar_estado() + "\n"
        return catalogo
    
    #Método para determinar si un libro existe, buscando por titulo
    def libro_existe(self, titulo: str) -> dict:
        for libro in self.catalogo:
            #Si el libro existe, se retorna el libro
            if titulo == libro.titulo:
                return libro
        #Si el libro no existe, se retorna None
        return None
    
    #Método para buscar un libro por titulo
    def buscar_libro(self, titulo: str):
        busqueda = f"Resultado de búsqueda {titulo}:\n"
        #Si existe, retorna los datos del libro 
        if self.libro_existe(titulo):
            return busqueda + self.libro_existe(titulo).mostrar_estado()
        #Si no existe, retorna un mensaje que lo indica
        return busqueda + f"El libro {titulo} no existe en la biblioteca"
    
    #Método para prestar una copia de un libro
    def prestar_libro(self, titulo: str):
        #Si el libro existe y quedan copias, se retirna el estado del libro actualizado
        if self.libro_existe(titulo):
            libro = self.libro_existe(titulo)
            if libro.copias > 0:
                libro.copias -= 1
                return f"Préstamo de {titulo} realizado\n" + libro.mostrar_estado()
            #Si no quedan copias, se retorna un mensaje de error 
            return f"Error en préstamo. El libro {titulo} no tiene copias disponibles en la biblioteca"
        #Si el libro no existe, se retorna un mensaje de error 
        return f"Error en préstamo. El libro {titulo} no existe en la biblioteca"
    
    #Método para devolver copia de un libro
    def devolver_libro(self, titulo: str):
        #Si el libro existe, se retorna el estado del libro actualizado
        if self.libro_existe(titulo):
            libro = self.libro_existe(titulo)        
            libro.copias += 1
            return "Devolución realizada\n" + libro.mostrar_estado()
        #Si el libro no existe, se retorna un mensaje de error
        return f"Error en devolución. El libro {titulo} no existe en la biblioteca"
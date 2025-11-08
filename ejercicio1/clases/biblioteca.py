from .libro import Libro

class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo: list[Libro] = []
    
    #Método para registrar libros
    def registrar_libro(self, libro: Libro):
        #Se asume que solo se puede registrar un libro si es que no existe en la biblioteca
        if not self.libro_existe(libro.titulo)["existe"]:
            self.catalogo.append(libro)
        else:
            print(f"El libro {libro.titulo} ya existe en la bilbioteca {self.nombre}")
    
    #Método para mostrar los estados de todos los libros registrados
    def mostrar_catalogo(self):
        print(f"| Catálogo biblioteca {self.nombre} |")
        for libro in self.catalogo:
            print(libro.mostrar_estado())
    
    #Método para determinar si un libro existe, buscando por titulo
    def libro_existe(self, titulo: str) -> dict:
        for libro in self.catalogo:
            #Si el libro existe, se retorna dentro de un diccionario junto con un True
            if titulo == libro.titulo:
                return {"libro": libro, "existe": True}
        #Si el libro no existe, se retorna None dentro de un diccionario junto con un False
        return {"libro": None, "existe": False}
    
    #Método para buscar un libro por titulo
    def buscar_libro(self, titulo: str):
        print(f"Resultado de búsqueda {titulo}:")
        #Si existe, imprime los datos del libro 
        if self.libro_existe(titulo)["existe"]:
            print(self.libro_existe(titulo)["libro"].mostrar_estado())
        #Si no existe, imprime un mensaje que lo indica
        else:
            print(f"El libro {titulo} no existe en la biblioteca {self.nombre}")
    
    #Método para prestar una copia de un libro
    def prestar_libro(self, titulo: str):
        #Si el libro existe y quedan copias, se imprime el estado del libro actualizado
        if self.libro_existe(titulo)["existe"]:
            libro = self.libro_existe(titulo)["libro"]
            if libro.copias > 0:
                libro.copias -= 1
                print("Préstamo realizado")
                print(libro.mostrar_estado())
            #Si no quedan copias, se imprime un mensaje de error 
            else:
                print("Error en préstamo:")
                print(f"El libro {titulo} no tiene copias disponibles en la biblioteca {self.nombre}")
        #Si el libro no existe, se imprime un mensaje de error 
        else:
            print("Error en préstamo:")
            print(f"El libro {titulo} no existe en la biblioteca {self.nombre}")
    
    #Método para devolver copia de un libro
    def devolver_libro(self, titulo: str):
        #Si el libro existe, se imprime el estado del libro actualizado
        if self.libro_existe(titulo)["existe"]:
            libro = self.libro_existe(titulo)["libro"]        
            libro.copias += 1
            print("Devolución realizada")
            print(libro.mostrar_estado())
        #Si el libro no existe, se imprime un mensaje de error
        else:
            print("Error en devolución:")
            print(f"El libro {titulo} no existe en la biblioteca {self.nombre}")
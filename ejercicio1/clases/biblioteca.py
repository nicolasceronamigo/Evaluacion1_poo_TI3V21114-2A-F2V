from .libro import Libro

class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo: list[Libro] = []
    
    def registrar_libro(self, libro: Libro):
        self.catalogo.append(libro)
    
    def mostrar_catalogo(self):
        print(f"| Catálogo biblioteca {self.nombre} |")
        for libro in self.catalogo:
            libro.mostrar_estado()
    
    def libro_existe(self, titulo: str) -> dict:
        for libro in self.catalogo:
            if titulo == libro.titulo:
                return {"libro": libro, "existe": True}
        return {"libro": None, "existe": False}
    
    def buscar_libro(self, titulo: str):
        print(f"Resultado de búsqueda {titulo}:")
        if self.libro_existe(titulo)["existe"]:
            self.libro_existe(titulo)["libro"].mostrar_estado()
        else:
            print(f"El libro {titulo} no existe en la biblioteca {self.nombre}")
    
    def prestar_libro(self, titulo: str):
        if self.libro_existe(titulo)["existe"]:
            libro = self.libro_existe(titulo)["libro"]
            if libro.copias > 0:
                libro.copias -= 1
                print("Préstamo realizado")
                libro.mostrar_estado()
            else:
                print("Error en préstamo:")
                print(f"El libro {titulo} no tiene copias disponibles en la biblioteca {self.nombre}")
        else:
            print("Error en préstamo:")
            print(f"El libro {titulo} no existe en la biblioteca {self.nombre}")
    
    def devolver_libro(self, titulo: str):
        if self.libro_existe(titulo)["existe"]:
            libro = self.libro_existe(titulo)["libro"]        
            libro.copias += 1
            print("Devolución realizada")
            libro.mostrar_estado()
        else:
            print("Error en devolución:")
            print(f"El libro {titulo} no existe en la biblioteca {self.nombre}")
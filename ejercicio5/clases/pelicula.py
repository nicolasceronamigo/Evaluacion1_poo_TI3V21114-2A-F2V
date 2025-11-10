class Pelicula:
    def __init__(self, titulo: str, genero: str, año_lanzamiento: int):
        self.titulo = titulo
        self.genero = genero
        self.año_lanzamiento = año_lanzamiento
    
    #Método para mostrar información
    def mostrar_info(self):
        return f"| Título: {self.titulo} | Género: {self.genero} | Año de lanzamiento: {self.año_lanzamiento} |"
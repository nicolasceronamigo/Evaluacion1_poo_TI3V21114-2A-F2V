from clases.pelicula import Pelicula

class Catalogo:
    def __init__(self):
        self.lista_peliculas: list[Pelicula] = []
    
    #Método para determinar si una película existe
    def pelicula_existe(self, titulo: str):
        for pelicula in self.lista_peliculas:
            if titulo == pelicula.titulo:
                return pelicula
        return None
    
    #Método para registrar una película
    def registrar_pelicula(self, titulo: str, genero: str, año_lanzamiento: int):
        pelicula = Pelicula(titulo, genero, año_lanzamiento)
        if not self.pelicula_existe(titulo):
            self.lista_peliculas.append(pelicula)
            return f"Resultado registro:\n" + self.consultar_catálogo()
        return f"Error en registro\n" + f"La película {pelicula.titulo} ya esá registrada en el catálogo"

    #Método para buscar una película por su título
    def buscar_pelicula(self, titulo: str):
        encabezado = f"Resultado búsqueda {titulo}:\n"
        if self.pelicula_existe(titulo):
            return encabezado + self.pelicula_existe(titulo).mostrar_info()
        return encabezado +" "+ f"La película {titulo} no está registrada en el catálogo"
    
    #Método para filtrar películas por género
    def filtrar_pelicula(self, genero: str):
        catalogo_filtro = Catalogo()
        for pelicula in self.lista_peliculas:
            if genero == pelicula.genero:
                catalogo_filtro.registrar_pelicula(pelicula.titulo, pelicula.genero, pelicula.año_lanzamiento)
        if len(catalogo_filtro.lista_peliculas):
            return f"Resultado filtro {genero}:\n" + catalogo_filtro.consultar_catálogo()
        return f"No hay películas del genero {genero} registradas en el catálogo"
    
    #Método para consultar el catálogo
    def consultar_catálogo(self):
        catalogo = "Catálogo de películas \n"
        for pelicula in self.lista_peliculas:
            catalogo += pelicula.mostrar_info() + "\n"
        return catalogo
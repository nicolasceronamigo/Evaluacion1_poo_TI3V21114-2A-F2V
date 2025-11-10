from clases.catalogo import Catalogo
from clases.pelicula import Pelicula

#Crear catálogo
catalogo1 = Catalogo()

print("\n--------------------------------------------------------------------\n")

#Registrar películas
print(catalogo1.registrar_pelicula("titulo_pelicula_1", "genero_1", 2001))
print(catalogo1.registrar_pelicula("titulo_pelicula_2", "genero_2", 2002))
print(catalogo1.registrar_pelicula("titulo_pelicula_3", "genero_1", 2003))
print(catalogo1.registrar_pelicula("titulo_pelicula_4", "genero_2", 2004))

print("\n--------------------------------------------------------------------\n")

#Buscar películas
print(catalogo1.buscar_pelicula("titulo_pelicula_1"))
print(catalogo1.buscar_pelicula("titulo_pelicula_2"))
print(catalogo1.buscar_pelicula("titulo_pelicula_5"))
print(catalogo1.buscar_pelicula("titulo_pelicula_6"))

print("\n--------------------------------------------------------------------\n")

#Filtrar película por género
print(catalogo1.filtrar_pelicula("genero_1"))
print(catalogo1.filtrar_pelicula("genero_2"))
print(catalogo1.filtrar_pelicula("genero_3"))
print(catalogo1.filtrar_pelicula("genero_4"))

print("\n--------------------------------------------------------------------\n")

#Visualizar catálogo completo
print(catalogo1.consultar_catálogo())

print("\n--------------------------------------------------------------------\n")
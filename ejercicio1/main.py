from clases.libro import Libro
from clases.biblioteca import Biblioteca

#Creacion de biblioteca
biblioteca1 = Biblioteca()

print("\n--------------------------------------------------------------------\n")

#Registro de libros
print(biblioteca1.registrar_libro("titulo_libro_1", "autor_libro_1", 1))
print(biblioteca1.registrar_libro("titulo_libro_2", "autor_libro_2", 2))
print(biblioteca1.registrar_libro("titulo_libro_3", "autor_libro_3", 3))
print(biblioteca1.registrar_libro("titulo_libro_4", "autor_libro_4", 4))

print("\n--------------------------------------------------------------------\n")

#Mostrar catálogo de libros
print(biblioteca1.mostrar_catalogo())

print("\n--------------------------------------------------------------------\n")

#Búsqueda de libros
print(biblioteca1.buscar_libro("titulo_libro_1"))
print(biblioteca1.buscar_libro("titulo_libro_2"))
print(biblioteca1.buscar_libro("titulo_libro_5"))
print(biblioteca1.buscar_libro("titulo_libro_6"))

print("\n--------------------------------------------------------------------\n")

#Préstamo de libros
print(biblioteca1.prestar_libro("titulo_libro_1"))
print(biblioteca1.prestar_libro("titulo_libro_1"))
print(biblioteca1.prestar_libro("titulo_libro_2"))
print(biblioteca1.prestar_libro("titulo_libro_3"))
print(biblioteca1.prestar_libro("titulo_libro_5"))

print("\n--------------------------------------------------------------------\n")

#Devolución de libros
print(biblioteca1.devolver_libro("titulo_libro_1"))
print(biblioteca1.devolver_libro("titulo_libro_2"))
print(biblioteca1.devolver_libro("titulo_libro_3"))
print(biblioteca1.devolver_libro("titulo_libro_5"))

print("\n--------------------------------------------------------------------\n")
from clases.libro import Libro
from clases.biblioteca import Biblioteca

#Creacion de biblioteca
biblioteca1 = Biblioteca("nombre_biblio_1")

#Registro de libros
biblioteca1.registrar_libro("titulo_libro_1", "autor_libro_1", 1)
biblioteca1.registrar_libro("titulo_libro_2", "autor_libro_2", 2)
biblioteca1.registrar_libro("titulo_libro_3", "autor_libro_3", 3)
biblioteca1.registrar_libro("titulo_libro_4", "autor_libro_4", 4)

#Mostrar catálogo de libros
biblioteca1.mostrar_catalogo()

print("")
print("--------------------------------------------------------------------")
print("")

#Búsqueda de libros
biblioteca1.buscar_libro("titulo_libro_1")
print("")
biblioteca1.buscar_libro("titulo_libro_2")
print("")
biblioteca1.buscar_libro("titulo_libro_5")
print("")
biblioteca1.buscar_libro("titulo_libro_6")

print("")
print("--------------------------------------------------------------------")
print("")

#Préstamo de libros
biblioteca1.prestar_libro("titulo_libro_1")
print("")
biblioteca1.prestar_libro("titulo_libro_1")
print("")
biblioteca1.prestar_libro("titulo_libro_2")
print("")
biblioteca1.prestar_libro("titulo_libro_3")
print("")
biblioteca1.prestar_libro("titulo_libro_5")

print("")
print("--------------------------------------------------------------------")
print("")

#Devolución de libros
biblioteca1.devolver_libro("titulo_libro_1")
print("")
biblioteca1.devolver_libro("titulo_libro_2")
print("")
biblioteca1.devolver_libro("titulo_libro_3")
print("")
biblioteca1.devolver_libro("titulo_libro_5")
print("")
print("--------------------------------------------------------------------")
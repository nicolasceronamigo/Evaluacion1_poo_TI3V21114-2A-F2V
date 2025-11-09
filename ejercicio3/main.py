from clases.item import Item
from clases .pedido import Pedido

#Crear pedido
pedido1 = Pedido(1)

#Consultar listado de items
pedido1.consultar_listado()

print("")
print("--------------------------------------------------------------------")
print("")

#Agregar items
pedido1.agregar_item("nombre_item_1", 1000, 1)
pedido1.agregar_item("nombre_item_2", 2000, 2)
pedido1.agregar_item("nombre_item_3", 3000, 3)
pedido1.agregar_item("nombre_item_4", 4000, 4)
pedido1.agregar_item("nombre_item_4", 4000, 1)

print("")
print("--------------------------------------------------------------------")
print("")

#Consultar listado de items
pedido1.consultar_listado()

print("")
print("--------------------------------------------------------------------")
print("")

#Mostrar total final a pagar
pedido1.mostrar_total()

print("")
print("--------------------------------------------------------------------")
print("")
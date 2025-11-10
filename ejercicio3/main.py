from clases.item import Item
from clases .pedido import Pedido

#Crear pedido
pedido1 = Pedido()

#Consultar listado de items
print(pedido1.consultar_listado())

print("\n--------------------------------------------------------------------\n")

#Agregar items
print(pedido1.agregar_item("nombre_item_1", 1000, 1))
print(pedido1.agregar_item("nombre_item_2", 2000, 2))
print(pedido1.agregar_item("nombre_item_3", 3000, 3))
print(pedido1.agregar_item("nombre_item_4", 4000, 4))
print(pedido1.agregar_item("nombre_item_4", 4000, 1))

print("\n--------------------------------------------------------------------\n")

#Consultar listado de items
print(pedido1.consultar_listado())

print("\n--------------------------------------------------------------------\n")

#Mostrar total final a pagar
print(pedido1.mostrar_total())

print("\n--------------------------------------------------------------------\n")
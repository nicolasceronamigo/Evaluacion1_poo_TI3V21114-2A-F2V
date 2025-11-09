from clases.item import Item

class Pedido:
    def __init__(self, numero: int):
        self.numero = numero
        self.listado: list[Item] = []
    
    #Método para determinar si un item ya está registrado en el pedido
    def item_existe(self, nombre: str):
        for item in self.listado:
            if nombre == item.nombre:
                return item
        return None
    
    #Método para agregar un item al pedido
    def agregar_item(self, nombre: str, precio: int, cantidad: int):
        item = Item(nombre, precio, cantidad)
        if not self.item_existe(item.nombre):
            self.listado.append(item)
        else:
            print("Error al agregar item")
            print(f"El item {item.nombre} ya está agregado en el pedido {self.numero}")
    
    #Método para consultar listado de items
    def consultar_listado(self):
        print(f"Listado pedido {self.numero}")
        for item in self.listado:
            print(item.mostrar_datos())
    
    #Método para calcular el total del pedido
    def calcular_total(self):
        total = 0
        for item in self.listado:
            total += item.calcular_subtotal()
        return total
    
    #Método para ver detalle y total final a pagar
    def mostrar_total(self):
        self.consultar_listado()
        print(f"| Total a pagar ${self.calcular_total()}")
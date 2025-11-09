class Item:
    def __init__(self, nombre: str, precio: int, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    #Método para calcular el subtotal del item
    def calcular_subtotal(self):
        subtotal = self.precio * self.cantidad
        return subtotal
    
    #Método para mostrar datos del item
    def mostrar_datos(self):
        return f"| Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio} | Subtotal: ${self.calcular_subtotal()}"
class Contacto:
    def __init__(self, nombre: str, telefono: str, correo_electronico: str):
        self.nombre = nombre
        self.telefono = telefono
        self.correo_electronico = correo_electronico
    #Método para mostrar contacto
    def mostrar_datos(self):
        return f"| Nombre: {self.nombre} | Teléfono: {self.telefono} | Correo electronico: {self.correo_electronico}"
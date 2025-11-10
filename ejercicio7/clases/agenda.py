from clases.contacto import Contacto

class Agenda:
    def __init__(self):
        self.lista_contactos: list[Contacto] = []
    
    #Método para mostrar estado de la agenda
    def mostrar_estado(self):
        estado = "Agenda\n"
        for contacto in self.lista_contactos:
            estado += contacto.mostrar_datos() + "\n"
        return estado
    
    #Método para determinar si un contacto existe
    def contacto_existe(self, identificador: str):
        for contacto in self.lista_contactos:
            identificadores = [contacto.nombre, contacto.telefono, contacto.correo_electronico]
            if identificador in identificadores:
                return contacto
        return None
    
    #Método para agregar contacto
    def agregar_contacto(self, nombre: str, telefono: str, correo_electronico: str):
        if not self.contacto_existe(nombre):
            contacto = Contacto(nombre, telefono, correo_electronico)
            self.lista_contactos.append(contacto)
            return f"Contacto {nombre} agregado\n" + self.mostrar_estado()
        return f"El contacto {nombre} ya existe"
    
    #Método para buscar contactos
    def buscar_contacto(self, nombre: str):
        busqueda = f"Resultado búsqueda {nombre}\n"
        agenda_buscar = Agenda()
        if self.contacto_existe(nombre):
            contacto = self.contacto_existe(nombre)
            agenda_buscar.agregar_contacto(contacto.nombre, contacto.telefono, contacto.correo_electronico)
            return busqueda + agenda_buscar.mostrar_estado()
        return busqueda + f"Contacto {nombre} no existe\n"
    
    #Método para eliinar contacto
    def eliminar_contacto(self, identificador: str):
        if self.contacto_existe(identificador):
            self.lista_contactos.remove(self.contacto_existe(identificador))
            return f"Contacto con {identificador} eliminado\n" + self.mostrar_estado()
        return f"Error en eliminación: contacto con {identificador} no existe\n"
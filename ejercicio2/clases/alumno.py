class Alumno:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    #Método para devolver el nombre de un alumno
    def mostrar_nombre(self):
        return self.nombre
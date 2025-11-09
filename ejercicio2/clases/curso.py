from clases.alumno import Alumno

class Curso:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.lista_alumnos:list[Alumno] = []
        
    #Método para determinar si un alumno existe en el curso, buscando por nombre
    def alumno_existe(self, nombre):
        for alumno in self.lista_alumnos:
            if nombre == alumno.nombre:
                return alumno
        return None
    
    #Método para registrar un alumno
    def registrar_alumno(self, nombre):
        alumno = Alumno(nombre)
        if not self.alumno_existe(alumno.nombre):
            self.lista_alumnos.append(alumno)
        else:
            print("Error en el registro")
            print(f"El alumno {alumno.nombre} ya está registrado en el curso {self.nombre}")
    
    #Método para remover un alumno
    def remover_alumno(self, nombre):
        if self.alumno_existe(nombre):
            self.lista_alumnos.remove(self.alumno_existe(nombre))
        else:
            print("Error al remover")
            print(f"El alumno {nombre} no está registrado en el curso {self.nombre}")
    
    #Método para mostrar el estado del curso
    def mostrar_estado(self):
        estado = f"Estado curso: {self.nombre} \n"
        numero = 0
        for alumno in self.lista_alumnos:
            numero += 1
            estado += f"| {numero} | {alumno.nombre} \n"
        return estado
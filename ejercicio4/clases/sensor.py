from clases.medicion import Medicion

class Sensor:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.lista_mediciones: list[Medicion] = []
    
    #Método para registrar una medición
    def registrar_medicion(self, valor: float):
        medicion = Medicion(valor)
        self.lista_mediciones.append(medicion)
    
    #Método para consultar el promedio de las mediciones
    def consultar_promedio(self):
        suma = 0
        for medicion in self.lista_mediciones:
            suma += medicion.valor
        return suma / len(self.lista_mediciones)
    
    #Método para consultar el máximo de las mediciones
    def consultar_max(self):
        lista_valores = []
        for medicion in self.lista_mediciones:
            lista_valores.append(medicion.valor)
        return max(lista_valores)
    
    #Método para consultar el mínimo de las mediciones
    def consultar_min(self):
        lista_valores = []
        for medicion in self.lista_mediciones:
            lista_valores.append(medicion.valor)
        return min(lista_valores)
    
    #Método para visualizar resumen de mediciones
    def mostrar_resumen(self):
        sensor = f"Resumen sensor {self.nombre}:\n"
        promedio = f"| Promedio: {self.consultar_promedio()} |\n"
        maximo = f"| Máximo: {self.consultar_max()} |\n"
        minimo = f"| Mínimo: {self.consultar_min()} |"
        return sensor + promedio + maximo + minimo
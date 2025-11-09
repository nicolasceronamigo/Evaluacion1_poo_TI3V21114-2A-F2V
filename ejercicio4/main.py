from clases.medicion import Medicion
from clases.sensor import Sensor

#Definir un sensor
sensor1 = Sensor("nombre_sensor_1")

#Registrar mediciones
sensor1.registrar_medicion(10)
sensor1.registrar_medicion(20)
sensor1.registrar_medicion(30)
sensor1.registrar_medicion(40)

print("")
print("--------------------------------------------------------------------")
print("")

#Consultar promedio
print(f"Promedio sensor: {sensor1.nombre}: {sensor1.consultar_promedio()}")

print("")
print("--------------------------------------------------------------------")
print("")

#Consultar máximo
print(f"Promedio sensor: {sensor1.nombre}: {sensor1.consultar_max()}")

print("")
print("--------------------------------------------------------------------")
print("")

#Consultar mínimo
print(f"Promedio sensor: {sensor1.nombre}: {sensor1.consultar_min()}")

print("")
print("--------------------------------------------------------------------")
print("")

#Mostrar resumen
print(sensor1.mostrar_resumen())

print("")
print("--------------------------------------------------------------------")
print("")
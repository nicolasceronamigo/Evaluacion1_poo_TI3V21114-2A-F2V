from clases.agenda import Agenda
from clases.contacto import Contacto

#Crear agenda
agenda1 = Agenda()

print("\n--------------------------------------------------------------------\n")

#Agregar contactos
print(agenda1.agregar_contacto("nombre_contacto_1", "telefono_contacto_1", "correo_elec_contacto_1"))
print(agenda1.agregar_contacto("nombre_contacto_2", "telefono_contacto_2", "correo_elec_contacto_2"))
print(agenda1.agregar_contacto("nombre_contacto_3", "telefono_contacto_3", "correo_elec_contacto_3"))
print(agenda1.agregar_contacto("nombre_contacto_4", "telefono_contacto_4", "correo_elec_contacto_4"))

print("\n--------------------------------------------------------------------\n")

#Mostrar contactos
print(agenda1.mostrar_estado())

print("\n--------------------------------------------------------------------\n")

#Buscar contacto
print(agenda1.buscar_contacto("nombre_contacto_1"))
print(agenda1.buscar_contacto("nombre_contacto_2"))
print(agenda1.buscar_contacto("nombre_contacto_5"))
print(agenda1.buscar_contacto("nombre_contacto_6"))

print("\n--------------------------------------------------------------------\n")

#Eliminar contacto
print(agenda1.eliminar_contacto("nombre_contacto_1"))
print(agenda1.eliminar_contacto("nombre_contacto_1"))
print(agenda1.eliminar_contacto("telefono_contacto_2"))
print(agenda1.eliminar_contacto("telefono_contacto_2"))
print(agenda1.eliminar_contacto("correo_elec_contacto_3"))
print(agenda1.eliminar_contacto("correo_elec_contacto_3"))

print("\n--------------------------------------------------------------------\n")
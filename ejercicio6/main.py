from clases.registro import Registro
from clases.usuario import Usuario

#Creación de registro
registro1 = Registro()

print("\n--------------------------------------------------------------------\n")

#Registro de usuarios
print(registro1.registrar_usuario("nombre_usuario_1", "contraseña_usuario_1"))
print(registro1.registrar_usuario("nombre_usuario_2", "contraseña_usuario_2"))
print(registro1.registrar_usuario("nombre_usuario_3", "contraseña_usuario_3"))
print(registro1.registrar_usuario("nombre_usuario_4", "contraseña_usuario_4"))
print(registro1.registrar_usuario("nombre_usuario_1", "contraseña_usuario_1"))
print(registro1.registrar_usuario("nombre_usuario_2", "contraseña_usuario_2"))

print("\n--------------------------------------------------------------------\n")

#Inicio de sesión
print(registro1.iniciar_sesion("nombre_usuario_1", "contraseña_usuario_1"))
print(registro1.iniciar_sesion("nombre_usuario_2", "contraseña_usuario_2"))
print(registro1.iniciar_sesion("nombre_usuario_3", "contraseña_usuario_5"))
print(registro1.iniciar_sesion("nombre_usuario_4", "contraseña_usuario_6"))

print("\n--------------------------------------------------------------------\n")

#Consultar si un usuario está registrado
print(registro1.consulta_registro("nombre_usuario_1"))
print(registro1.consulta_registro("nombre_usuario_2"))
print(registro1.consulta_registro("nombre_usuario_5"))
print(registro1.consulta_registro("nombre_usuario_6"))

print("\n--------------------------------------------------------------------\n")
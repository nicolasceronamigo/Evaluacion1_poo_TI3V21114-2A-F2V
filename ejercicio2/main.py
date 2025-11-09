from clases.alumno import Alumno
from clases.curso import Curso

#Definir un nuevo curso
curso1 = Curso("nombre_curso_1")

print("")
print("--------------------------------------------------------------------")
print("")

#Mostrar estado del curso antes de registrar alumnos
print(curso1.mostrar_estado())

print("")
print("--------------------------------------------------------------------")
print("")

#Registrar alumnos
curso1.registrar_alumno("nombre_alumno_1")
curso1.registrar_alumno("nombre_alumno_2")
curso1.registrar_alumno("nombre_alumno_3")
curso1.registrar_alumno("nombre_alumno_4")
curso1.registrar_alumno("nombre_alumno_4")

print("")
print("--------------------------------------------------------------------")
print("")

#Mostrar estado del curso después de registrar alumnos
print(curso1.mostrar_estado())

print("")
print("--------------------------------------------------------------------")
print("")

#Remover alumnos
curso1.remover_alumno("nombre_alumno_3")
curso1.remover_alumno("nombre_alumno_4")
curso1.remover_alumno("nombre_alumno_5")
curso1.remover_alumno("nombre_alumno_6")

print("")
print("--------------------------------------------------------------------")
print("")

#Mostrar estado del curso después de remover algunos alumnos
print(curso1.mostrar_estado())

print("")
print("--------------------------------------------------------------------")
print("")
from clases.alumno import Alumno
from clases.curso import Curso

#Definir un nuevo curso
curso1 = Curso("nombre_curso_1")

print("\n--------------------------------------------------------------------\n")

#Mostrar estado del curso antes de registrar alumnos
print(curso1.mostrar_estado())

print("\n--------------------------------------------------------------------\n")

#Registrar alumnos
print(curso1.registrar_alumno("nombre_alumno_1"))
print(curso1.registrar_alumno("nombre_alumno_2"))
print(curso1.registrar_alumno("nombre_alumno_3"))
print(curso1.registrar_alumno("nombre_alumno_4"))
print(curso1.registrar_alumno("nombre_alumno_4"))

print("\n--------------------------------------------------------------------\n")

#Mostrar estado del curso después de registrar alumnos
print(curso1.mostrar_estado())

print("\n--------------------------------------------------------------------\n")

#Remover alumnos
print(curso1.remover_alumno("nombre_alumno_3"))
print(curso1.remover_alumno("nombre_alumno_4"))
print(curso1.remover_alumno("nombre_alumno_5"))
print(curso1.remover_alumno("nombre_alumno_6"))

print("\n--------------------------------------------------------------------\n")

#Mostrar estado del curso después de remover algunos alumnos
print(curso1.mostrar_estado())

print("\n--------------------------------------------------------------------\n")
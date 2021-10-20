print("Tienes que elegir unas asignaturas ")
print("Asignaturas optativas: Programacion - Software - Accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("programacion", "software", "accesibilidad"):
	print("Asignatura elegida " + asignatura)

else:
	print("La asignatura elegida no existe")






# NOTA linea 5. Si estuviesemos manejando valores numerales, no se usan comillas
#comas si, para separarlos, pero no entrecomillado como en el ejemplo


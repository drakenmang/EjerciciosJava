print("Confirme su contraseña (2) ")

pw=(input("escriba su contraseña: "))

lim = 3

print("Tiene " + str(lim) + " intentos para confirmar su contraseña ")
pw2=(input("Escriba de nuevo su contraseña "))
contador=1


while pw != pw2 and contador < limite:
	print("Las contraseñas no coinciden. Hagalo de nuevo ")
	pw2=(input("Escriba de nuevo su contraseña "))
	contador+-1

if pw == pw2:
	print("todo ok chao ")

else:
	print("Todo mal ")


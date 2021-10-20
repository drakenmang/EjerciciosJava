correo=input("Pon tu correo: ")

arroba=correo.count('@')

if (arroba!=1 or correo.rfind('@')==(len(correo)-1) or correo.find('@')==0):
	print("mail incorrecto")
else:
	print("mail correcto")




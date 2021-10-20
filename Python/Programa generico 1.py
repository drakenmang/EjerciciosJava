_________________IMC_________________

peso=int(input("¿Cuanto pesa?"))
altura=int(input("Cuanto mide en metros?"))
resultado=0

resultado=(peso/altura*altura)/3.0

if resultado >= 30:
  print("Su indice de IMC" + str(resultado)*1 + "es muy alto")

if resultado <= 30:
  print("Ta biem")

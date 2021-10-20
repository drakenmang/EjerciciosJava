Correo=input("Introduce tu correo electrónico : ")

while (Correo.startswith("@")) or (Correo.endswith("@")):
    print("Por favor, introduzca un correo válido: ")

    Correo=input("Introduce un correo electrónico válido: ")

arroba='@'
count = 0

for caracter in Correo:
    if caracter==arroba:
        count=count+1

while count>=2 or count==0:
    Correo=input("Introduce un correo electrónico válido: ")

if count == 1:
    print("Correo correcto")
#!/usr/local/bin/python
# coding: latin-1
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):

	try:	
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir por cero")
		return "Operacion erronea"

try:
	op1=(int(input("Introduce el primer n�mero: ")))	

	op2=(int(input("Introduce el segundo n�mero: ")))
except ValueError:
	print("Los valores introducidos no son correctos")		
	
operacion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

try:
	if operacion=="suma":
		print(suma(op1,op2))

	elif operacion=="resta":
		print(resta(op1,op2))

	elif operacion=="multiplica":
		print(multiplica(op1,op2))

	elif operacion=="divide":
		print(divide(op1,op2))

	else:
		print ("Operaci�n no contemplada")

except NameError:
	print("No se puede operar con caracteres")

print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n de el programa ")

#Hay que manejar la excepcion del programa para que no divida por 0 y el programa
#continue.
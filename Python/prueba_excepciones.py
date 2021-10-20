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
	op1=(int(input("Introduce el primer número: ")))	

	op2=(int(input("Introduce el segundo número: ")))
except ValueError:
	print("Los valores introducidos no son correctos")		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

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
		print ("Operación no contemplada")

except NameError:
	print("No se puede operar con caracteres")

print("Operación ejecutada. Continuación de ejecúción de el programa ")

#Hay que manejar la excepcion del programa para que no divida por 0 y el programa
#continue.
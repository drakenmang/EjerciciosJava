class Coche():       #Clase
	
	def __init__(self): #Usando un constructor, le damos el estado inicial a una clase.

		self.__largoChasis=250	#Añadimos self. delante y los metemos dentro del constructor identandolo.
		self.__anchoChasis=120              # Esto es el estado inicial. Lo que tendran los objetos pertenecientes a esta clase
		self.__Ruedas=4		#Si añadimos dos barras bajas, El valor se encapsula y es inaccesible desde fuera de la clase
		self.__Engine=False

	def Arrancar(self,arrancamos):
		self.__Engine=arrancamos

		if(self.__Engine):
			chequeo=self.__chequeo_interno()

		if(self.__Engine and chequeo):
			return "El coche está en marcha"

		elif(self.__Engine and chequeo==False):
			return "Algo ha ido mal, no se puede arrancar"
		else:
			return "El coche está apagado"

	
	def estado(self):
		print("El coche tiene", self.__Ruedas, " ruedas. Un ancho de", self.__anchoChasis, "Y un largo de ", self.__largoChasis)

	def __chequeo_interno(self):
		print("Realizando chequeo interno")


		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True

		else:

			return False




miCoche=Coche()    #Primer Objeto
print(miCoche.Arrancar(True))

miCoche.estado()



print("-----------A continuacion creamos el segundo objeto -----------")

#Self es a el mismo. 

#Pass funcion que no hace nada hasta que se lo digamos pero aparece por defecto.

# al usar def (method) aparece como metodo o como funcion, cuando usamos def como metodo
#estamos usando una funcion especial que pertenece a la clase donde está creando, mientras que
#def (function) no pertenece a ninguna clase.

miCoche2=Coche()     #Segundo objeto

print(miCoche2.Arrancar(False))
    

miCoche2.estado()
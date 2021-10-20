class coche():

	def desplazamiento(self):
		print("Me muevo usando cuatro ruedas")

class moto():
	def desplazamiento(self):
		print("Me muevo usando dos ruedas")

class camion():
	def desplazamiento(self):
		print("Me muevo usando seis ruedas")

"""miVehiculo=moto()

miVehiculo.desplazamiento()

miVehiculo2=coche()

miVehiculo2.desplazamiento()

miVehiculo3=camion()

miVehiculo3.desplazamiento()"""

def desplazamientovehiculo(vehiculo): #Aqui se almacena el vehiculo que queramos llamar.
	vehiculo.desplazamiento()

miVehiculo=camion() #o camion, o coche... 

desplazamientovehiculo(miVehiculo)

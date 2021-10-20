class vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo  # propiedades desde el init
		self.engine=False
		self.acelera=False
		self.frena=False


	def arrancar(self):
		self.engine=True
	def acelerar(self):
		self.acelera=True
	def frenar(self):
		self.frena=True
	def estado(self):
		print ("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nMotor: ", self.engine,
		 "\nAcelerando : ", self.frena, "\nFrenando :", self.frena)  # propiedades desde el estado 


class Furgoneta(vehiculos):
	pass

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta está cargada"

		else:
			return "La furgoneta no está cargada"


class Moto(vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito= "Voy haciendo el caballito"

	def estado(self): #el objeto sobreescribe el estado del "padre" por el suyo propio
		print ("Marca; ", self.marca, "\nModelo: ", self.modelo, "\nMotor: ", self.engine,
		 "\nAcelerando : ", self.frena, "\nFrenando :", self.frena, "\n", self.hcaballito)


class VElectricos(vehiculos):    
	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)
		self.autonomia=100

	def cargarEnergia(self):
		
		self.cargando=True





miMoto=Moto("Honda", "CBR")

miMoto.caballito()  #Propiedad propia

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos,vehiculos): #Dentro del parentesis de la clase bicielectrica, vemos que puede tener herencia multiple de dos clases.
	pass  			#Cuando hay herencia multiple, se coge la info del primer constructor.


miBici=BicicletaElectrica("orbea", "15HBE")


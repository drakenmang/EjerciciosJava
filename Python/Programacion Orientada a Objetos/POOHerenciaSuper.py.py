class persona():
	def __init__(self, nombre, edad, lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def  descripcion(self):

		print("Nombre: ", self.nombre, "edad: ", self.edad, "Residencia: ", self.lugar_residencia)


class empleado(persona):

	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
		self.salario=salario
		
		self.antiguedad=antiguedad
	
	def descripcion(self):
		
		super().descripcion()

		print("Salario: ", self.salario, "antiguedad: ",self.antiguedad)

Antonio=empleado("1500", 20, "Manuel", 55, "colombia") #Antonio es empleado, pero deberia pertenecer a la clase persona

Antonio.descripcion()

print(isinstance(Antonio, persona))

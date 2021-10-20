from tkinter import *
from tkinter import messagebox #NEcesario para ventanas emergentes.


root=Tk()

# _____________ FUNCIONES ______________________________#
def infoAdicional():  #Dentro de messagebox, primero el texto de la ventana y luego el contenido
	messagebox.showinfo("Procesador de Jose", "Procesador de textos 2021")
def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU") #Para enseñar un warning
def salirAplicacion():
	#valor=messagebox.askquestion("Salir", "¿Desea abandonarme?") #Esto seria para hacer une pregunta si o no.
	valor=messagebox.askokcancel("Salir", "¿Desea abandonarme?")
	if valor==True: 
	#if valor=="yes": Valido solo para askquestion
		root.destroy()

def cerrarDocumento(): #Funcion para reintentar.
	valor=messagebox.askretrycancel("Reintentar", "No se puede salir")
	if valor==False:
		root.destroy()

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

#__________Barras de menu_______________________________________

archivoMenu=Menu(barramenu, tearoff=0) #quitar linea de puntos en el desplegable
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #Añade barra separadora entre elementos.
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)






archivoEdicion=Menu(barramenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barramenu)

archivoAyuda=Menu(barramenu, tearoff=0)

archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)
archivoAyuda.add_command(label="Version")

#_____________________________________________________________________________

barramenu.add_cascade(label="Archivo", menu=archivoMenu)

barramenu.add_cascade(label="Edicion", menu=archivoEdicion)

barramenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

barramenu.add_cascade(label="Ayuda", menu=archivoAyuda)
root.mainloop()
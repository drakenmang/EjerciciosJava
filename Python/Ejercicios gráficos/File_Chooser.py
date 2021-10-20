from tkinter import *
from tkinter import filedialog # Necesario para poner apertura de archivos


root=Tk()

def abreFichero():
#Askopenfilename usado para poder abrir archivos #initialdir para directorio de inicio.
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel","*.xlsx"),
		("Ficheros de Texto", "*.txt"), ("Todos los ficheros", "*.*")))
# en filetypes se usan tantos parentesis porque se trata de una tupla.
	print(fichero)

Button (root, text="Abrir fichero", command=abreFichero).pack()


root.mainloop()
from tkinter import *

root=Tk()

varOpcion=IntVar()

def imprimir():

	#print(varOpcion.get())
	if varOpcion.get()==1:
		etiqueta.config(text="Has elegido masculino")
	elif varOpcion.get()==2:
		etiqueta.config(text="Has elegido femenino")
	else: #varOpcion.get()==3:
		etiqueta.config(text="Has elegido no binario")


Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(root, text="No binario", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()
root.mainloop()
from tkinter import *

root= Tk()
root.title("Programa test")
#root.iconbitmap('nando.ico')
miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1)

cuadropass=Entry(miFrame)
cuadropass.grid(row=1, column=1)
cuadropass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=4, column=1, padx=10,pady=10 )

scrollvert=Scrollbar(miFrame, command=textoComentarios.yview) # La variable scrollvertical es igual a Scrollbar pertenece a textoComentarios
#y el yview nos indica que funciona de forma vertical al igual que la funcion command.
scrollvert.grid(row=4, column=2, sticky="nsew") #Aparece en la columna 2 para que se situe a derecha del cuadro de texto
# usamos sticky="nsew" para que se adapte al tamaño "textocomentarios"
textoComentarios.config(yscrollcommand=scrollvert.set)
#Usamos yscrollcommand para que el cuadradito de la barrita de scroll se haga mas pequeño
#conforme rellenemos el cuadro de texto.


nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

passLabel=Label(miFrame, text="Contraseña: ")
passLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)


def codigoBoton():
	minombre.set("Aceptar")

botonEnvio=Button(root, text="Aceptar", command=codigoBoton)

botonEnvio.pack()


Button(miFrame, text='Cancelar', command=root.quit).grid(row=6, column=1, sticky="w", pady=4)


root.mainloop()
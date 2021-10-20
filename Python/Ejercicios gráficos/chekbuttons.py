from tkinter import *

root=Tk()
root.iconbitmap('nando.ico')
root.title("Viajando con fernando")

Playa=IntVar()
Montania=IntVar()
TurismoRural=IntVar()

def opcionesviaje():

	opcionelegida=""

	if(Playa.get()==1):
		opcionelegida+=" Playa"
	if(Montania.get()==1):
		opcionelegida+=" Montaña"
	if(TurismoRural.get()==1):
		opcionelegida+=" Turismo rural"

	textofinal.config(text=opcionelegida)

foto=PhotoImage(file="bobs.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige tu destino para viajar con fernando", width=50).pack()

Checkbutton(frame, text="Playa", variable=Playa, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(frame, text="Montaña", variable=Montania, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(frame, text="Turismo rural", variable=TurismoRural, onvalue=1, offvalue=0, command=opcionesviaje).pack()

textofinal=Label(frame)
textofinal.pack()
root.mainloop()
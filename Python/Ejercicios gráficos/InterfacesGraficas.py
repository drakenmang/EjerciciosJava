from tkinter import *

raiz=Tk()
raiz.title("Programa")

raiz.resizable(1,1)

raiz.iconbitmap('nando.ico')

#raiz.geometry("300x300")

raiz.config(bg="red")

miImagen=PhotoImage(file="bobs.png")



miFrame=Frame()

miFrame.pack()

miLabel= Label((miFrame), image=miImagen)

#miFrame.pack(side="right", anchor="s")

miFrame.config(bg="blue")


miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")

raiz.mainloop()
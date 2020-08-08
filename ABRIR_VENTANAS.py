from tkinter import *

ventana1 = Tk()
ventana1.title("Ventana1")
ventana1.geometry("170x100+300+100")

ventana2 = Tk()
ventana2.title("Ventana2")
ventana2.geometry("170x100+460+100")
ventana2.withdraw()

def volver_Ventana1():
	ventana2.withdraw()
	ventana1.deiconify()

def abrir_Ventana2():
	ventana1.withdraw()
	ventana2.deiconify()
	
Label(ventana1, text="ESTOY EN VENTANA 1", bg="yellow").pack(ipadx=5, ipady=10)
Button(ventana1, text="IR A VENTANA 2", bg="blue", fg="white", command=abrir_Ventana2).pack(pady=2, ipadx=19, ipady=5)
Label(ventana2, text="ESTOY EN VENTANA 2").pack(padx=10, pady=10)
Button(ventana2, text="IR A VENTANA 1", command=volver_Ventana1).pack(padx=5, pady=5, ipadx=5, ipady=5)

ventana1.mainloop()
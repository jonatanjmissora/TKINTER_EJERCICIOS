from tkinter import *
from tkinter import messagebox

def validar():
	if entrada.get()=="kato":
		abrir_ventana2()
	else:
		entrada.delete(0, END)
		messagebox.showwarning("CUIDADO", "INCORRECTO")

def abrir_ventana2():
	ventana1.withdraw()
	ventana2=Toplevel()
	ventana2.title("VENTANA 2")
	ventana2.geometry("200x70+400+200")
	Label(ventana2, text="Password validado!!").pack()
	Button(ventana2, text="OK", command=ventana2.destroy).pack()

ventana1=Tk()
ventana1.title("VENTANA 1")
ventana1.geometry("200x100+200+200")
Label(ventana1, text="PASSWORD: ").pack()
entrada=Entry(ventana1, show="*", justify="right")
entrada.pack()
ventana1.bind('<Return>', lambda event: validar())
Button(ventana1, text="VALIDAR", command=validar).pack()
entrada.focus_set()

ventana1.mainloop()
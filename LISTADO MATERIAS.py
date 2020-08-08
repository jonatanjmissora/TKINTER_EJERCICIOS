from tkinter import *
from tkinter.ttk import Combobox

def combo_values():
	return [j+1 for j in range(len(lista.get(0, END))+1)]

def agregar():
	if texto.get() != "":
		lista.insert(int(combo.get())-1, texto.get())
		combo["values"]=combo_values()
		combo.current(len(combo["values"])-1)
		entrada.delete(0,END)

def borrar():
	try:
		for x in lista.curselection(): 
			lista.delete(x)
		combo["values"]=combo_values()
		combo.current(len(combo["values"])-1)
	except:
		None

def grabar():
	lista_final=lista.get(0, END)
	for x in lista_final:
		print(x)

win=Tk()
win.geometry("300x300+1000+100")
win.title("LISTADO")
win.resizable(False, False)

f1=Frame(win, width=210, height=70, bg="#b3ccff")
f1.pack(fill=X, padx=5, pady=5)

listado=Label(win, text="Listado:", bg="#b3ccff")
texto=StringVar()
entrada=Entry(win, textvariable=texto, width=36)
entrada.focus_set()
entrada.bind("<Return>", lambda event: agregar())
indice=Label(win, text="indice:", bg="#b3ccff")
combo=Combobox(win, state="readonly", width=4)
boton1=Button(win, text="Agregar", command=agregar)

#		POSICIONES FRAME1
listado.place(x=5, y=5)
entrada.place(x=60, y=7)
indice.place(x=100, y=38)
combo.place(x=150, y=38)
boton1.place(x=225, y=34)

indices=Label(win, text=" 1:\n 2:\n 3:\n 4:\n 5:\n 6:\n 7:\n 8:\n 9:\n10:\n")
lista=Listbox(win, width=37, activestyle="none", selectmode=EXTENDED)
lista.insert(0,"Matematica")
lista.insert(1,"Historia")		#si quiero insertar o eliminar elementos por codigo
lista.insert(2,"Lengua")		#debo hacerlos antes del pack, place, o grid
lista.bind("<Delete>", lambda event: borrar())
boton2=Button(win, text="Quitar", command=borrar, width=15)
boton3=Button(win, text="Grabar", command=grabar, width=10)

combo["values"]=combo_values()
combo.current(len(combo["values"])-1)

#		POSICIONES FRAME2
indices.place(x=20, y=82)
lista.place(x=45, y=83)
boton2.place(x=70, y=260)
boton3.place(x=200, y=260)

win.mainloop()
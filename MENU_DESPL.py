from tkinter import *

win=Tk()
win.title("Menu Desplegable")
win.geometry("200x200+200+200")
color=StringVar()
colores=["red", "yellow", "blue", "black", "white"]
color.set(colores[0])

def go(x):
	L.config(bg=x)

menu=OptionMenu(win, color, *colores, command=go)
menu.config(width=20)
menu.pack()
L=Label(win, textvariable=color, bg="red")
L.pack()



win.mainloop()
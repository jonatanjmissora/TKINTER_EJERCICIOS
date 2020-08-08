from tkinter import *

lastx, lasty = 0, 0
color="black"

def paleta_colores():
	id1 = canvas.create_rectangle((10, 10, 30, 30), fill="red")
	canvas.tag_bind(id1, "<Button-1>", lambda x: setColor("red"))
	id2 = canvas.create_rectangle((10, 35, 30, 55), fill="blue")
	canvas.tag_bind(id2, "<Button-1>", lambda x: setColor("blue"))
	id3 = canvas.create_rectangle((10, 60, 30, 80), fill="black")
	canvas.tag_bind(id3, "<Button-1>", lambda x: setColor("black"))

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line(lastx, lasty, event.x, event.y, width=2, fill=color, tag="dibu")
    lastx, lasty = event.x, event.y

def setColor(c):
	global color
	color=c

def borrar():
	canvas.delete("dibu")

root = Tk()
canvas = Canvas(root)
canvas.grid(column=0, row=0, columnspan=4, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

paleta_colores()

b1=Button(root, text="AZUL", command= lambda : setColor("blue"))
b1.grid(column=0, row=1)
b2=Button(root, text="ROJO", command= lambda : setColor("red"))
b2.grid(column=1, row=1)
b2=Button(root, text="VERDE", command= lambda : setColor("green"))
b2.grid(column=2, row=1)
b3=Button(root, text="BORRA", command=borrar)
b3.grid(column=3, row=1)
print(canvas.find_all())

mainloop()
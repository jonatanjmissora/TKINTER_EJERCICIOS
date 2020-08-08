from tkinter import *
from tkinter import ttk


#===================  PACK  ======================================
win=Tk()
win.geometry("300x85+100+100")
win.config(bg="blue", padx=4, pady=5) # pad separacion externa que me deja ver azul

fr1=Frame(win, bg="red")
fr1.pack(side=LEFT, padx=1)	

fr11=Frame(fr1, bg="yellow")
fr11.pack(side=TOP, ipadx=55)	# ipad le da el tamaño del amarillo fr11

fr12=Frame(fr1, bg="green")
fr12.pack(side=TOP, ipadx=55)

fr13=Frame(fr1, bg="cyan")
fr13.pack(side=TOP, ipadx=65)

lb111=Label(fr11, text="hola1")
lb111.pack(side=LEFT, fill=X, expand=1)
lb112=Entry(fr11, width=5)
lb112.pack(side=LEFT, fill=X, expand=1)
#	fill y expand van juntas si queremos que ocupe todo el ancho

lb112=Label(fr12, text="hola1")
lb112.pack(side=LEFT, fill=X, expand=1)
lb122=Entry(fr12, width=5)
lb122.pack(side=LEFT, fill=X, expand=1)

bt123=Button(fr13, text="buton1")
bt123.pack(fill=X, expand=1)


fr2=Frame(win, bg="red")
fr2.pack(side=LEFT, padx=1)

fr21=Frame(fr2, bg="yellow")
fr21.pack(side=TOP, ipadx=72, ipady=11)	

fr23=Frame(fr2, bg="cyan")
fr23.pack(side=TOP, ipadx=41)

lb211=Label(fr21, text="hola1")
lb211.pack(side=LEFT, fill=BOTH, expand=1)

bt223=Button(fr23, text="buton2")
bt223.pack(side=LEFT, fill=X, expand=1)

bt224=Button(fr23, text="buton3")
bt224.pack(side=RIGHT, fill=X, expand=1)

#===================  GRID  ======================================

win2=Tk()
win2.geometry("299x80+400+100")
win2.config(bg="blue", padx=5, pady=5) # pad separacion externa que me deja ver azul

lb00=Label(win2, text="hola1", width=10)
lb00.grid()

lb01=Entry(win2, width=10)
lb01.grid(row=0, column=1)

lb10=Label(win2, text="hola1", width=10)
lb10.grid(row=1, column=0)
lb11=Entry(win2, width=10)
lb11.grid(row=1, column=1)
bt20=Button(win2, text="buton1", width=19)
bt20.grid(row=2, column=0, columnspan=2)

lb03=Label(win2, text="hola1", width=19, height=2)
lb03.grid(row=0, column=3, rowspan=2, columnspan=2)
bt23=Button(win2, text="buton2", width=9)
bt23.grid(row=2, column=3)
bt24=Button(win2, text="buton3", width=9)
bt24.grid(row=2, column=4)

#===================  PLACE ======================================
win3=Tk()
win3.geometry("300x80+700+100")
win3.config(bg="blue", padx=5, pady=5) # pad separacion externa que me deja ver azul

lb00=Label(win3, text="hola1", width=10)
lb00.place(x=2, y=2)

lb01=Entry(win3, width=10)
lb01.place(x=80, y=2)

lb10=Label(win3, text="hola1", width=10)
lb10.place(x=2, y=22)
lb11=Entry(win3, width=10)
lb11.place(x=80, y=22)
bt20=Button(win3, text="buton1", width=19)
bt20.place(x=2, y=44)

lb03=Label(win3, text="hola1", width=19, height=2)
lb03.place(x=148, y=4)
bt23=Button(win3, text="buton2", width=9)
bt23.place(x=145, y=44)
bt24=Button(win3, text="buton3", width=9)
bt24.place(x=218, y=44)

mainloop()


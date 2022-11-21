from tkinter import *
from tkinter import ttk

def f(event):
    root.destroy()




root = Tk()
can = Canvas(bg = "white")
can.pack()

def g(event):
    print('Hello world')
    img = PhotoImage(file='switch.png')
    can.create_image(10,10, image= img)
    
def clic(event):
    x=event.x
    y=event.y
    t=cnv.find_closest(x, y)
    if t:
        can.delete(t[0])
def prop(event):
    x=event.x
    y=event.y
    t=can.find_closet(x,y)
    if t:
        Label()
root.bind("<Key-c>", f)
root.bind("<Key-m>",g)
root.binf ("Button-3",clic)
root.mainloop()
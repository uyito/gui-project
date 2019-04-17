from tkinter import *


root = Tk()


top = Frame(root)
top.pack()
down = Frame(root)
down.pack(side=BOTTOM)


button1 = Button(top, text="click me", fg="red")
button2 = Button(top, text="click me", fg="green")
button3 = Button(down, text="click me", fg="blue")
button4 = Button(down, text="click me", fg="yellow")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)


root.mainloop()

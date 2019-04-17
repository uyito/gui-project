from tkinter import *

root = Tk()

x = Label(root, text="Name")
y = Label(root, text="passowrd")
x1 = Entry(root)
x2 = Entry(root)

x.grid(row=0, sticky=E)
y.grid(row=1, sticky=E)

x1.grid(row=0, column=1)
x2.grid(row=1, column=1)

c = Checkbutton(root, text= "Keep me logged in")
c.grid(columnspan=2)

root.mainloop()


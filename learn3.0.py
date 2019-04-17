from tkinter import *

root = Tk()


def printname(event):
    print("hello my name is uyi")


B = Button(root, text="print")
B.bind("<Button-1>", printname)
B.pack()

root.mainloop()
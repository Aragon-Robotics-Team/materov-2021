from tkinter import *

top = Tk()

def asdf():
    print("hello")

btn = Button(top, text = "hello", command = asdf)
btn.pack()

top.mainloop()

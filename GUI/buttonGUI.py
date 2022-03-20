import tkinter as tk
from tkinter import *
import time
import sys
import os
import tkinter.font as font
from time import sleep

##GUI CODE
root = tk.Tk()

canvas = Canvas(root,height=200,width=200,bg="#fff")

canvas.pack()

rec1 = canvas.create_rectangle(30, 30, 180, 120,outline="#fb0",fill="#fb0")

button1status = False

def button1():
    print("checking")
    if button1status == True:
        canvas.itemconfig(rec1, fill='green')
    if button1status == False:
        canvas.itemconfig(rec1, fill='yellow')
    canvas.after(20, button1)
# button1()

def green(): #if button pressed down
    global button1status
    button1status = True
    print("true")

def yellow(): #if button pressed up
    global button1status
    button1status = False
    print("false")

Button(root, text="Green", command=green).pack()
Button(root, text="Yellow", command=yellow).pack()

button1()
while True:
    root.update()
# root.mainloop()

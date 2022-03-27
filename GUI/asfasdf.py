import tkinter as tk
from tkinter import *
import time
import sys
import os
import tkinter.font as font
from time import sleep
import pygame

##GUI CODE
root = tk.Tk()
timercanvas = Canvas(root, height = 250, width = 250, bg = "#fff")
timercanvas.pack()

minute=StringVar()
second=StringVar()
hours=StringVar()

sec = StringVar()
mins= StringVar()
hrs= StringVar()

# #  # #

Entry(timercanvas, textvariable = sec, width = 2, font = 'arial 12').place(x=70, y=30) # Seconds
Entry(timercanvas, textvariable = mins, width =2, font = 'arial 12').place(x=45, y=30) # Mins
Entry(timercanvas, textvariable = hrs, width =2, font = 'arial 12').place(x=20, y=30) # Hours

# #  # #

minute.set('00')
second.set('00')
hours.set('00')

sec.set('00')
mins.set('00')
hrs.set('00')
times = 0

# #  # #

def countdown():
    global times
    print("hello") #testing, working but code not working
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > 0:
        minute,second = (times // 60 , times % 60)

        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)
        times -= 1
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
            return

Button(timercanvas, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold').place(x=15, y=70)


def stop():
    global times
    minute.set('00')
    second.set('00')
    hours.set('00')
    sec.set('00')
    mins.set('00')
    hrs.set('00')
    times = 0
    #root.destroy()
    #python = sys.executable
    #os.execl(python, python, * sys.argv)



Button(timercanvas, text='STOP', bd ='5', command = stop, bg = 'white', font = 'arial 10 bold').place(x=15, y=100)

root.mainloop()

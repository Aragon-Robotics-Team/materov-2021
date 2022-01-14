#!/usr/bin/python
#python3 /Users/valeriefan/github/test-materov-2021/GUI/GUI.py
import tkinter as tk
import time
import sys
import os
import pygame
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar

########################
root = tk.Tk()
root.geometry("1920x1080")
root.resizable(0,0)
root.config(bg ='gray')
root.title("Countdown Timer Verision 0.0.1")
# #  # #

minute=StringVar()
second=StringVar()
hours=StringVar()

sec = StringVar()
mins= StringVar()
hrs= StringVar()

# #  # #

tk.Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=200, y=155) # Seconds
tk.Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=175, y=155) # Mins
tk.Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=150, y=155) # Hours

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


tk.Button(root, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold').place(x=150, y=210)
# #  # #

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



tk.Button(root, text='STOP', bd ='5', command = stop, bg = 'white', font = 'arial 10 bold').place(x=150, y=250)
##############################################################

def button1():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(root, text ="Hello", command = button1, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=1050, y=100)

def button2():
   tk.messagebox.showinfo( "Hello Python2", "Hello World2")

Bu = tk.Button(root, text ="Hello2", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=1050, y=150)

def button3():
   tk.messagebox.showinfo( "Hello Python3", "Hello World3")

Bu = tk.Button(root, text ="Hello3", command = button3, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=1050, y=200)

def button4():
   tk.messagebox.showinfo( "Hello Python4", "Hello World4")

Bu = tk.Button(root, text ="Hello4", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=1050, y=250)

def button5():
   tk.messagebox.showinfo( "Hello Python5", "Hello World5")

Bu = tk.Button(root, text ="Hello5", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=1050, y=300)

def button6():
   tk.messagebox.showinfo( "Hello Python6", "Hello World6")

Bu = tk.Button(root, text ="Hello6", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 10).place(x=1050, y=350)

def button6():
   tk.messagebox.showinfo( "Hello Python6", "Hello World6")

Bu = tk.Button(root, text ="Hello6", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 10).place(x=1150, y=350)
videoplay = cv2.VideoCapture(0)
##############
root.mainloop()
##############

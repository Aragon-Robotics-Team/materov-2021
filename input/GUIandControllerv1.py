import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
from threading import *
from time import sleep
import pygame

########################
root = tk.Tk()
root.geometry("400x400")
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
   print("Hello World")

B = tk.Button(root, text ="Hello", command = button1, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=150, y=50)

def button2():
   print("Hello World")

Bu = tk.Button(root, text ="Hello2", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,
          width = 20).place(x=150, y=100)

def threading():
    t1 = Thread(target = joystick)
    t1.start()

def joystick():
    import pygame
    from time import sleep
    pygame.init()
    joysticks = []
    clock = pygame.time.Clock()
    deadband = 0.1
    keepPlaying = True
    print("example4")

    myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
    myjoystick.init()

    while keepPlaying:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                        print("Select Has Been Pressed")
                    if event.button == 1:
                        print("Left Joystick button has been pressed")
                    if event.button == 2:
                        print("Right Joystick button has been pressed")
                    if event.button == 3:
                        print("Start has been pressed")
                    if event.button == 4:
                        print("Surface top button has been pressed")
                    if event.button == 5:
                        print("Surface right button has been pressed")
                    if event.button == 6:
                        print("Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print("Surface left button has been pressed")
                    if event.button == 8:
                        print("Left 2 has been pressed")
                    if event.button == 9:
                        print("Right 2 has been pressed")
                    if event.button == 10:
                        print("Left 1 has been pressed")
                    if event.button == 11:
                        print("Right 1 has been pressed")
                    if event.button == 12: # event.type == pygame.JOYBUTTONUP:
                        print("Triangle Has Been Pressed")
                    if event.button == 13:
                        print("Circle has been pressed")
                    if event.button == 14:
                        print("X has been pressed")
                    if event.button == 15:
                        print("Square has been pressed")
                    if event.button == 16:
                        print("Center PS has been pressed")
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(myjoystick.get_axis(0))> deadband:
                    one = myjoystick.get_axis(0)
                    print('1 has been moved ' + str(one))
                if event.axis == 1 and abs(myjoystick.get_axis(1))> deadband:
                    two = myjoystick.get_axis(1)
                    print('2 has been moved ' + str(two))
                if event.axis == 2 and abs(myjoystick.get_axis(2))> deadband:
                    three = myjoystick.get_axis(2)
                    print('3 has been moved ' + str(three))
                if event.axis == 3 and abs(myjoystick.get_axis(3))> deadband:
                    four = myjoystick.get_axis(3)
                    print('4 has been moved ' + str(four))

Bu = tk.Button(root, text="Start Controller input", command = threading).place(x=150, y=10)
##############
root.mainloop()
##############

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

joystickcanvas = Canvas(root,height=200,width=400,bg="#fff")

joystickcanvas.pack()

topx = 50
topy = 10
width = 80
height = 10
bottomx = topx + width
bottomy = topy + height

j1xrow = 0
j1yrow = 1
j2xrow = 2
j2yrow = 3
space = 20

center = width/2
joy1xstatus = center

joystickcanvas.create_rectangle(topx, topy + space * j1xrow, bottomx, bottomy + space * j1xrow, outline = "gray", fill = "gray")
joy1xrec = joystickcanvas.create_rectangle(topx, topy + space * j1xrow, topx + joy1xstatus, bottomy + space * j1xrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j1xrow, text="Joy 1 X Axis", fill="dark gray", font=('Helvetica 10 bold'))

joy1ystatus = center

joystickcanvas.create_rectangle(topx, topy + space * j1yrow, bottomx, bottomy + space * j1yrow, outline = "gray", fill = "gray")
joy1yrec = joystickcanvas.create_rectangle(topx, topy + space * j1yrow, topx + joy1ystatus, bottomy + space * j1yrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j1yrow, text="Joy 1 Y Axis", fill="dark gray", font=('Helvetica 10 bold'))

joy2xstatus = center

joystickcanvas.create_rectangle(topx, topy + space * j2xrow, bottomx, bottomy + space * j2xrow, outline = "gray", fill = "gray")
joy2xrec = joystickcanvas.create_rectangle(topx, topy + space * j2xrow, topx + joy2xstatus, bottomy + space * j2xrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j2xrow, text="Joy 2 X Axis", fill="dark gray", font=('Helvetica 10 bold'))

joy2ystatus = center

joystickcanvas.create_rectangle(topx, topy + space * j2yrow, bottomx, bottomy + space * j2yrow, outline = "gray", fill = "gray")
joy2yrec = joystickcanvas.create_rectangle(topx, topy + space * j2yrow, topx + joy2ystatus, bottomy + space * j2yrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j2yrow, text="Joy 2 Y Axis", fill="dark gray", font=('Helvetica 10 bold'))


def joystickgraphic():
    print("Asdfasdf")
    print(joy1xstatus)
    #joystickcanvas.itemconfig(joy1xrec, x1 = topx + center + joy1xstatus)
    joystickcanvas.coords(joy1xrec, topx, topy + space * j1xrow, topx + joy1xstatus, bottomy + space * j1xrow)
    joystickcanvas.coords(joy1yrec, topx, topy + space * j1yrow, topx + joy1ystatus, bottomy + space * j1yrow)
    joystickcanvas.coords(joy2xrec, topx, topy + space * j2xrow, topx + joy2xstatus, bottomy + space * j2xrow)
    joystickcanvas.coords(joy2yrec, topx, topy + space * j2yrow, topx + joy2ystatus, bottomy + space * j2yrow)
    joystickcanvas.after(20, joystickgraphic)


joystickgraphic()
def joytests():
    global joy1xstatus
    global joy1ystatus
    global joy2xstatus
    global joy2ystatus
    #print("Asdfasdf")
    sleep(0.1)
    for event in pygame.event.get():
        #print("Asfadsf")
        # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                zero = myjoystick.get_axis(0)
                joy1xstatus = center + zero*width/2
                #print('1 has been moved ' + str(zero))
            if event.axis == 1:
                one = myjoystick.get_axis(1)
                joy1ystatus = center + one*width/2
                #print('2 has been moved ' + str(one))
            if event.axis == 2:
                two = myjoystick.get_axis(2)
                joy2xstatus = center + two*width/2
                #print('3 has been moved ' + str(two))
            if event.axis == 3:
                three = myjoystick.get_axis(3)
                joy2ystatus = center + three*width/2
            #    print('4 has been moved ' + str(three))


pygame.init()
keepPlaying = True
print("example4")

myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
myjoystick.init()

while True:
    joytests()
    root.update()

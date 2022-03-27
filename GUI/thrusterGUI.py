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

thrustercanvas = Canvas(root,height=200,width=400,bg="#fff")

thrustercanvas.pack()


topx = 30 #this is also the center of the top left rectangle
topy = 30
width = 100
height = 120
bottomx = topx + width
bottomy = topy + height

centerx = topx + width/2
centery = topy + height/2

thrustercanvas.create_rectangle(topx, topy, bottomx, bottomy, width = 5, outline = "light gray")

t_height = 24
t_width = 15
center = t_height

#y0 is what changes
#left
#background
thrustercanvas.create_rectangle(centerx - t_width - width/2, centery - t_height, centerx + t_width - width/2, centery + t_height, fill = "dark gray", outline = "dark gray")
#status
t1status = t_height
t1 = thrustercanvas.create_rectangle(centerx - t_width - width/2, centery - t_height + t1status, centerx + t_width - width/2, centery + t_height, fill = "green", outline = "green")

thrustercanvas.create_text(centerx - width/2, centery, text = "1", fill="black", font=('Helvetica 15 bold'))

#right
#background
thrustercanvas.create_rectangle(centerx - t_width + width/2, centery - t_height, centerx + t_width + width/2, centery + t_height, fill = "dark gray", outline = "dark gray")
#status
t2status = center
t2 = thrustercanvas.create_rectangle(centerx - t_width + width/2, centery - t_height + t2status, centerx + t_width + width/2, centery + t_height, fill = "green", outline = "green")

thrustercanvas.create_text(centerx + width/2, centery, text = "2", fill="black", font=('Helvetica 15 bold'))

#top
#background
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height - height/2, centerx + t_width, centery + t_height - height/2, fill = "dark gray", outline = "dark gray")
#status
t3status = center
t3 = thrustercanvas.create_rectangle(centerx - t_width, centery - t_height - height/2 + t3status, centerx + t_width, centery + t_height - height/2, fill = "green", outline = "green")

thrustercanvas.create_text(centerx, centery - height/2, text = "3", fill="black", font=('Helvetica 15 bold'))

#bottom
#background
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2, centerx + t_width, centery + t_height + height/2, fill = "dark gray", outline = "dark gray")
#status
t4status = center
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2, centerx + t_width, centery + t_height + height/2, fill = "dark gray", outline = "dark gray")
t4 = thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2 + t4status, centerx + t_width, centery + t_height + height/2, fill = "green", outline = "green")

thrustercanvas.create_text(centerx, centery + height/2, text = "4", fill="black", font=('Helvetica 15 bold'))

def thrustergraphic():
    thrustercanvas.coords(t1, centerx - t_width - width/2, centery - t_height + t1status, centerx + t_width - width/2, centery + t_height)
    thrustercanvas.coords(t2, centerx - t_width + width/2, centery - t_height + t2status, centerx + t_width + width/2, centery + t_height)
    thrustercanvas.coords(t3, centerx - t_width, centery - t_height - height/2 + t3status, centerx + t_width, centery + t_height - height/2)
    thrustercanvas.coords(t4,centerx - t_width, centery - t_height + height/2 + t4status, centerx + t_width, centery + t_height + height/2)
    thrustercanvas.after(20, thrustergraphic)

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
    # joytests()
    root.update()

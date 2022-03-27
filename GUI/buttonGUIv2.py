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

buttoncanvas = Canvas(root,height=200,width=400,bg="#fff")

buttoncanvas.pack()

centx = 200 #x coord of center point of buttons
centy = 50 #y coord of center point of buttons
bsx = 10 #x span of button
bsy = 10 #y span of buttons
bspace = 30 #space between buttons

#Variables for button statuses and creating corresponding circle and square objects
buttonAstatus = False
Acirc = buttoncanvas.create_oval(centx - bsx, centy - bsy - bspace, centx + bsx, centy + bsy - bspace)
buttonBstatus = False
Bcirc = buttoncanvas.create_oval(centx - bsx + bspace, centy - bsy,  centx + bsx + bspace, centy + bsy)
buttonXstatus = False
Xcirc = buttoncanvas.create_oval(centx - bsx - bspace, centy - bsy,  centx + bsx - bspace, centy + bsy)
buttonYstatus = False
Ycirc = buttoncanvas.create_oval(centx - bsx, centy - bsy + bspace, centx + bsx, centy + bsy + bspace)

Acentx = 75
Acenty = 50

leftstatus = False
leftSquare = buttoncanvas.create_rectangle(Acentx - bsx - bspace, Acenty - bsy,  Acentx + bsx - bspace, Acenty + bsy)
rightstatus = False
rightSquare = buttoncanvas.create_rectangle(Acentx - bsx + bspace, Acenty - bsy,  Acentx + bsx + bspace, Acenty + bsy)
upstatus = False
upSquare = buttoncanvas.create_rectangle(Acentx - bsx, Acenty - bsy + bspace, Acentx + bsx, centy + bsy + bspace)
downstatus = False
downSquare = buttoncanvas.create_rectangle(Acentx - bsx, Acenty - bsy - bspace, Acentx + bsx, Acenty + bsy - bspace)

#adfasdfadfadf need to do this part
LTstatus = False
LBstatus = False
RTstatus = False

#changes the button color when pressed
def buttons():
    global buttonAstatus
    global buttonBstatus
    global buttonXstatus
    global buttonYstatus

    global leftstatus
    global rightstatus
    global upstatus
    global downstatus
    #a
    if buttonAstatus == True:
        buttoncanvas.itemconfig(Acirc, fill='green')
    if buttonAstatus == False:
        buttoncanvas.itemconfig(Acirc, fill='dark gray')
    #b
    if buttonBstatus == True:
        buttoncanvas.itemconfig(Bcirc, fill='green')
    if buttonBstatus == False:
        buttoncanvas.itemconfig(Bcirc, fill='dark gray')
    #x
    if buttonXstatus == True:
        buttoncanvas.itemconfig(Xcirc, fill='green')
    if buttonXstatus == False:
        buttoncanvas.itemconfig(Xcirc, fill='dark gray')
    #y
    if buttonYstatus == True:
        buttoncanvas.itemconfig(Ycirc, fill='green')
    if buttonYstatus == False:
        buttoncanvas.itemconfig(Ycirc, fill='dark gray')
    #NO BUTTON EVENTS FOR THESE YET
    #left arrow
    if leftstatus == True:
        buttoncanvas.itemconfig(leftSquare, fill='gray')
    if leftstatus == False:
        buttoncanvas.itemconfig(leftSquare, fill='white')
    #right arrow
    if rightstatus == True:
        buttoncanvas.itemconfig(rightSquare, fill='gray')
    if rightstatus == False:
        buttoncanvas.itemconfig(rightSquare, fill='white')
    #up arrow
    if upstatus == True:
        buttoncanvas.itemconfig(upSquare, fill='gray')
    if upstatus == False:
        buttoncanvas.itemconfig(upSquare, fill='white')
    #down arrow
    if downstatus == True:
        buttoncanvas.itemconfig(downSquare, fill='gray')
    if downstatus == False:
        buttoncanvas.itemconfig(downSquare, fill='white')
    buttoncanvas.after(20, buttons)


#checks for joystick input
def joytests():
    global buttonAstatus
    global buttonBstatus
    global buttonXstatus
    global buttonYstatus
    #print("Asdfasdf")
    sleep(0.1)
    for event in pygame.event.get():
        #print("Asfadsf")
        # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
        if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                    print("A Has Been Pressed")
                    buttonAstatus = True
                if event.button == 1: # event.type == pygame.JOYBUTTONUP:
                    print("B Has Been Pressed")
                    buttonBstatus = True
                if event.button == 2: # event.type == pygame.JOYBUTTONUP:
                    print("X Has Been Pressed")
                    buttonXstatus = True
                if event.button == 3: # event.type == pygame.JOYBUTTONUP:
                    print("Y Has Been Pressed")
                    buttonYstatus = True
                # if event.button == 4:
                #     print("Surface top button has been pressed")
                #     upstatus = True
                # if event.button == 5:
                #     print("Surface right button has been pressed")
                #     rightstatus = True
                # if event.button == 6:
                #     print("Surface Bottom Has Been Pressed")
                #     downstatus = True
                # if event.button == 7:
                #     print("Surface left button has been pressed")
                #     leftstatus = True
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                print("A Has Been Released")
                buttonAstatus = False
            if event.button == 1: # event.type == pygame.JOYBUTTONUP:
                print("B Has Been Released")
                buttonBstatus = False
            if event.button == 2: # event.type == pygame.JOYBUTTONUP:
                print("X Has Been Released")
                buttonXstatus = False
            if event.button == 3: # event.type == pygame.JOYBUTTONUP:
                print("Y Has Been Released")
                buttonYstatus = False
            # if event.button == 4:
            #     print("Surface top button has been released")
            #     upstatus = False
            # if event.button == 5:
            #     print("Surface right button has been released")
            #     rightstatus = False
            # if event.button == 6:
            #     print("Surface bottom has been released")
            #     downstatus = False
            # if event.button == 7:
            #     print("Surface left button has been released")
            #     leftstatus = False

pygame.init()
deadband = 0.1
keepPlaying = True
print("example4")

myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
myjoystick.init()

buttons()
while True:
    joytests()
    root.update()
# root.mainloop()

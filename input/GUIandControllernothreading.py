#Another method of making our GUI and Controller input run together: Instead of running the two programs simultaenousl
#we switch between the controller input and the gui every 0.1 seconds. This way, both pygame and tkinter are
#on the main loop. Originally, the controller input loop also had a delay of 0.1 seconds, but I moved the delay in between
#the GUI and controller loop instead.

import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import pygame
from time import sleep


root = tk.Tk()
root.config(bg ='gray')

pygame.init()
joysticks = []
clock = pygame.time.Clock()
deadband = 0.1
keepPlaying = True
print("example4")

myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
myjoystick.init()

def controller():

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

def loop():
    print("loop")

def helloWorld():
    print("helloWorld")

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()

Result = True
while Result:
    controller()
    #sleep(0.1)
    root.update()

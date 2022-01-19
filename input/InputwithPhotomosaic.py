#i deleted the photomosaic

import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import pygame
from time import sleep
import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time
from threading import *

root = tk.Tk()
root.config(bg ='gray')

videoCaptureObject = cv2.VideoCapture(0)

pygame.init()
joysticks = []
clock = pygame.time.Clock()
deadband = 0.1
keepPlaying = True
print("Controller Input Begun")

global quit
quit = False

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

def quitStatus():
    print(quit)

def loopThreading():
    t1 = Thread(target = loop)
    t1.start()

def loop():
    Result = True
    count = 0
    while count < 2:
        print("s")
        count = count + 1
        sleep(0.5)

Bu = tk.Button(root, text = "Threading loop", command = loopThreading).pack()

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()
###############
def quitVideo():
    print("quit video")
    global quit
    videoCaptureObject.release()
    quit = True

Bu = tk.Button(root, text="Quit Video", command = quitVideo).pack()

# def photomosaicThread():
#     t2 = Thread(target = photomosaic)
#     t2.start()

Bu = tk.Button(root, text="Photomosaic Snapshot", command = photomosaic).pack()

Result = True
while Result:
    #quitStatus()
    controller()
    showVideo()
    root.update()

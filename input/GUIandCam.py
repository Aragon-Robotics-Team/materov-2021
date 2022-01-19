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

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()

videoCaptureObject = cv2.VideoCapture(0)

def video():
    ret,frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video",frame)
    #deletes every frame as the next one comes on, closes all windows when q is pressed
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()

while True:
    root.update()
    video()

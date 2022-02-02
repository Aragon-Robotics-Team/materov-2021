import cv2
import threading
import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import queue
from time import sleep
import math
import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import queue
import numpy as np

root = tk.Tk()
root.config(bg ='gray')
#q = queue.Queue()

fishCoords = [[0,0],[0,0],[0,0],[0,0]]
fishLengths = [0,0,0]
#[laserX1, laserY1],
#[laserX2, laserY2],
#[fishX1, fishY1],
#[fishX2, fishY2]
measureFishieClick = False
#measureFishieStart = False
measureFishieCalc = False
countFishCoords = 0
fishImg = ""

print("asfasdf")

fishPictureCount = 0
allFishLengths = [0,0,0]

def click_event(event, x, y, flags, params):
    global image
    global countFishCoords
    global measureFishieClick
    # checking for left mouse clicks for laser points
    if measureFishieClick==True:
        if fishPictureCount < 3:
            #print("click event")
            #print("MeasureFishieClick is true in click event")
            if countFishCoords < 4:
                if event == cv2.EVENT_LBUTTONDOWN:
                    #print("Button is clicked is true in click event")
                    # displaying the coordinates on the Shell
                    fishCoords[countFishCoords][0] = x
                    fishCoords[countFishCoords][1] = y
                    countFishCoords = countFishCoords + 1
                    # xcoords[countFishCoords-1] = x
                    # ycoords[countFishCoords-1] = y
                    print(x, ' ', y)

                    # displaying the coordinates
                    # on the image window
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(fishImg, str(x) + ',' +
                                str(y), (x,y), font,
                                1, (255, 0, 0), 2)
                    #q.put(fishImg)
                    cv2.imshow('Fish', fishImg)
                    #countFishCoords = countFishCoords + 1
            else:
                measureFishieClick = False
                #print("starting fish calculations")
                measureFishieCalculations()
                cv2.destroyAllWindows()

def measureFishieCalculations():
    global fishPictureCount
    global countFishCoords
    global measureFishieClick
    global fishCoords

    #finding distances
    laserPixels = math.sqrt(((fishCoords[0][0]-fishCoords[1][0])**2) + ((fishCoords[0][1]-fishCoords[1][1]) **2))
    print("Laser Pixels per inch: " + str(laserPixels))
    fishPixels = math.sqrt(((fishCoords[2][0]-fishCoords[3][0])**2) + ((fishCoords[2][1]-fishCoords[3][1]) **2))
    print("Total Fish Pixels: " + str(fishPixels))
    fishLength = fishPixels / laserPixels
    print("Fish Length in inches: " + str(fishLength))
    allFishLengths[fishPictureCount] = fishLength
    fishPictureCount = fishPictureCount + 1

def measureFishie():
    #reset variables for new image
    global countFishCoords
    global measureFishieClick
    global fishCoords
    global fishImg
    countFishCoords = 0
    measureFishieClick = True

    if fishPictureCount < 3:
        #show image and read coordinates
        print("Fish #: " + str(fishPictureCount + 1))
        ret, frame = videoCaptureObject.read()
        fishImg = frame
        cv2.imshow("Fish", fishImg)
        cv2.setMouseCallback("Fish", click_event)
    else:
        print("Fish Lengths: " + str(allFishLengths))

Bu = tk.Button(root, text="Measure Fish", command = measureFishie).pack()

def resetMeasureFish():
    print("Measuring Fish Task Reset")
    global allFishLengths
    global fishPictureCount
    global countFishCoords
    allFishLengths = [0,0,0]
    countFishCoords = 0
    fishPictureCount = 0

Bu = tk.Button(root, text="Reset Fish Measuring", command = resetMeasureFish).pack()

#DON"T NEED TO CHANGE WHEN ADDED INTO THE MAIN PROGRAM
videoCaptureObject = cv2.VideoCapture(0)
photomosaicCount = 0
#BM: Video Feed
def videoCapture():
    global photomosaicVideo
    global photomosaicStart
    global photomosaicCount
    ret, frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video", frame)
    # deletes every frame as the next one comes on, closes all windows when q is pressed
    if cv2.waitKey(1) == ord('q'):
        videoCaptureObject.release()
        cv2.destroyAllWindows()

#TODO: Add equation to calculate average length, then average mass of the  cohort of fish
#Integrate into main program

while True:
    queue()
    videoCapture()
    root.update()

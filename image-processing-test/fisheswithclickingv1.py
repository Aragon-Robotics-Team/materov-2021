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

def click_event(event, x, y, flags, params):
    global image
    global countFishCoords
    global measureFishieClick
    # checking for left mouse clicks for laser points
    if measureFishieClick==True:
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
                cv2.imshow('image', fishImg)
                #countFishCoords = countFishCoords + 1
        else:
            measureFishieClick = False
            #print("starting fish calculations")
            measureFishieCalculations()

def measureFishieCalculations():
    # global countFishCoords
    # global measureFishieClick
    # global fishCoords
    # #fishCoords = [[0,0],[0,0],[0,0],[0,0]]
    # countFishCoords = 0
    # measureFishieClick = True

    # while measureFishieCalc == False:
    #     sleep(0.1)

    #finding distances
    laserPixels = math.sqrt(((fishCoords[0][0]-fishCoords[1][0])**2) + ((fishCoords[0][1]-fishCoords[1][1]) **2))
    print("Laser Pixels per inch: " + str(laserPixels))
    fishPixels = math.sqrt(((fishCoords[2][0]-fishCoords[3][0])**2) + ((fishCoords[2][1]-fishCoords[3][1]) **2))
    print("Total Fish Pixels: " + str(fishPixels))
    fishLength = fishPixels / laserPixels
    print("Fish Length in inches: " + str(fishLength))

def measureFishie():
    #reset variables for new image
    # global countFishCoords
    # global measureFishieClick
    # global fishCoords
    # fishCoords = [[0,0],[0,0],[0,0],[0,0]]
    # countFishCoords = 0
    # measureFishieClick = True

    #show image and read coordinates
    global countFishCoords
    global measureFishieClick
    global fishCoords
    global fishImg
    #fishCoords = [[0,0],[0,0],[0,0],[0,0]]
    countFishCoords = 0
    measureFishieClick = True
    #print("measurefishieclick is true, count fish coords = 0")

    fishImg = cv2.imread('/Users/valeriefan/Desktop/thin-red-line-flag-united-states-america-country-police-thin-red-line-flag-137248115.jpg')
    cv2.imshow('image', fishImg)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    #Wait for coordinates to all be determined and then make calculations
    # while measureFishieCalc == False:
    #     sleep(0.1)
    #measureFishieCalculations()

measureFishie()
cv2.waitKey(0)
cv2.destroyAllWindows()

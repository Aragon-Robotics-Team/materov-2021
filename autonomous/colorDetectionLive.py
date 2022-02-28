
#Button -> Takes the snapshot -> Mouse clicks on a pixel and it reads the pixel value
#-> We take that pixel value and track the color in our entire video
import cv2
import numpy as np
import argparse

from skimage.transform import (hough_line, hough_line_peaks)
import math
from time import sleep

import tkinter as tk
import time
import sys
import os
import tkinter.font as font
import cv2
from tkinter import messagebox, RIGHT, LEFT, StringVar

videoCaptureObject = cv2.VideoCapture(0)
result = True

autoInitCompleted = False

##GUI SET UP
root = tk.Tk()
root.geometry("1000x1200")
root.resizable(0,0)

def videoCapture():
    ret,frame = videoCaptureObject.read()
    image = cv2.imwrite("/Users/valeriefan/Desktop/videoCapture.jpg", frame)
    cv2.imshow("Capturing Video",frame)

color_explore = np.zeros((150,150,3), np.uint8)
color_selected = np.zeros((150,150,3), np.uint8)

# red = 0
# blue = 0
# green = 0
findColor = False
blueLow = 0
greenLow = 0
redLow = 0
blueHigh = 0
greenHigh = 0
redHigh = 0

def show_color(event,x,y,flags,param):
    # global red
    # global blue
    # global green
    #global findColor

    B=param[y,x][0]
    G=param[y,x][1]
    R=param[y,x][2]
    color_explore [:] = (B,G,R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected [:] = (B,G,R)
        B=color_selected[10,10][0]
        G=color_selected[10,10][1]
        R=color_selected[10,10][2]
        print(R,G,B)
        #write_to_file(R,G,B)
        print(hex(R),hex(G),hex(B))
        red = R
        blue = B
        green = G
        # findColor = False
        print("About to set color")
        setColor(R, B, G)

autoInitCompleted = False

def setColor(red, blue, green):
    print("In Set Color")
    global blueLow
    global greenLow
    global redLow
    global blueHigh
    global greenHigh
    global redHigh
    global autoInitCompleted
    # global blue
    # global red
    # global green

    print("Setting lows and highs")
    blueLow = blue - 50
    greenLow = green - 50
    redLow = red - 50
    #lower = np.array([blueLow, greenLow, redLow])

    blueHigh = blue + 50
    greenHigh = green + 50
    redHigh = red + 50
    #high = np.array([blueHigh, greenHigh, redHigh]

    print("Setting autoInitCompleted to true")
    autoInitCompleted = True
    print("autoInitCompleted: " + str(autoInitCompleted))

    print("Closing Windows")
    #cv2.destroyWindow('image')
    print("Done")

def autonomousLineInitialization():
    global autoInitCompleted
    autoInitCompleted = False
    ret, frame = videoCaptureObject.read()
    lineImg = frame
    cv2.imshow('image', lineImg)
    cv2.imshow('color_explore', color_explore)
    cv2.imshow('color_selected', color_selected)
    cv2.setMouseCallback('image', show_color, param = lineImg)
    #cv2.destroyAllWindows()
    #wait until the image is clicked
    # while findColor == True:
    #     sleep(0.1)
    # global blueLow
    # global greenLow
    # global redLow
    # global blueHigh
    # global greenHigh
    # global redHigh
    # global blue
    # global red
    # global green
    #
    # blueLow = blue - 50
    # greenLow = green - 50
    # redLow = red - 50
    # #lower = np.array([blueLow, greenLow, redLow])
    #
    # blueHigh = blue + 50
    # greenHigh = green + 50
    # redHigh = red + 50
    # #high = np.array([blueHigh, greenHigh, redHigh])
    # autoInitCompleted = True

def midpoint(videoImg): #Find the center of the two lines
    image = cv2.imread(videoImg)

    result = image.copy()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    #set the low and high tuples based on the chosen color

    low = np.array([blueLow, greenLow, redLow])
    high = np.array([blueHigh, greenHigh, redHigh])
    #mask everything but the red
    mask = cv2.inRange(image, low, high)
    # mask2 = cv2.inRange(image, (175, 50, 20), (180, 255, 255))
    #cv2.waitKey()
    output = cv2.bitwise_and(image, image, mask = mask)
    # cv2.imshow("mask", output)
    # cv2.waitKey(0)

    # create more contrast between light blue background and red line, and replace green netting with light blue

    edges = cv2.Canny(output, 50, 150)

    #find and draw lines on images
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength = 30, maxLineGap = 30)

    #draw line on the original image
    i = 0

    for leftx1, lefty1, leftx2, lefty2 in lines[0]:
        cv2.line(result, (leftx1, lefty1), (leftx2, lefty2), (255, 255, 255), 10)
        #cv2.imshow('',result) #bm: threading

        if lefty1 > lefty2:
            leftTopX = leftx2
            print("left circle")
            #cv2.circle(image, center_coordinates, radius, color, thickness)
            cv2.circle(result, (leftx2, lefty2), 3, (5, 255, 255), 3)
        else:
            print("left circle")
            leftTopX = leftx1
            cv2.circle(result, (leftx1, lefty1), 3, (5, 255, 255), 3)

    for rightx1, righty1, rightx2, righty2 in lines[1]:
        #If the lines are too close together (the detected lines are on the same line)
        if abs(rightx1 - leftx1) < 100:
            print("Line is too close")
            i+=2
        else:
            cv2.line(result, (rightx1, righty1), (rightx2, righty2), (255, 255, 255), 10)
            #cv2.imshow('', result) #bm: threading
            if righty1 > righty2:
                print("right circle")
                rightTopX = rightx2
                cv2.circle(result, (rightx2, righty2), 3, (5, 255, 255), 3)
            else:
                print("right circle")
                rightTopX = rightx1
                cv2.circle(result, (rightx1, righty1), 3, (5, 255, 255), 3)

    while i > 1:
        print("Checking next line")
        if len(lines) <i:
            i = 0
        else:
            for rightx1, righty1, rightx2, righty2 in lines[i]:
                if abs(rightx1 - leftx1) < 100:
                    i+=1
                else:
                    cv2.line(result, (rightx1, righty1), (rightx2, righty2), (255, 255, 255), 10)
                    #cv2.imshow('', result) #bm: threading
                    if righty1 > righty2:
                        print("right circle")
                        rightTopX = rightx2
                        cv2.circle(result, (rightx2, righty2), 3, (5, 255, 255), 3)
                    else:
                        print("right circle")
                        rightTopX = rightx1
                        cv2.circle(result, (rightx1, righty1), 3, (5, 255, 255), 3)
                    i = 0


    midpointX = (int)((leftTopX + rightTopX) / 2) #account for the rounding when we're checking it against the center value
    cv2.circle(result, (midpointX, 10), 3, (5, 255, 255), 3)
    cv2.imshow('', result)

    return midpointX

autoInitCompleted = False
startLFPWM = False

def StraightLFPWMOutput():
    global autoInitCompleted
    global startLFPWM
    #print("autoInitCompleted: " + str(autoInitCompleted))
    if startLFPWM == True:
        if autoInitCompleted == True:
            videoImg = "/Users/valeriefan/Desktop/videoCapture.jpg"
            midpointX = midpoint(videoImg)
            midpointY = 0

            image = cv2.imread(videoImg)
            centerX = image.shape[1]/2

            angleToAdjust = math.atan(abs(centerX - midpointX)/image.shape[0])
            speed = 1
            if (midpointX < centerX):
                joyX = speed * (math.sin(angleToAdjust)) * -1 #incorrect calculation
            elif midpointX >= centerX:
                joyX = speed * (math.sin(angleToAdjust)) #incorrect calculation
            joyY = speed * (math.cos(angleToAdjust))
            print("Joystick Coords:")
            print("X: " + str(joyX))
            print("Y: " + str(joyY))

def startStraightLFPWMOutput():
    global startLFPWM
    if autoInitCompleted == False:
        print("Complete auto initialization first!")
    else:
        startLFPWM = True

Bu = tk.Button(root, text = "Initialize Autonomous", command = autonomousLineInitialization).pack()
Bu = tk.Button(root, text = "Autonomous Line Follower", command = startStraightLFPWMOutput).pack()

while True:
    StraightLFPWMOutput()
    videoCapture()
    root.update()

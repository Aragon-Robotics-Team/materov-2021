
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

from matplotlib import pyplot as plt

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


# img = cv2.imread('die.png')
#
# dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
#
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()

def midpoint(videoImg): #Find the center of the two lines
    image = cv2.imread(videoImg)

    result = image.copy()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    #dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    #
    # plt.subplot(121),plt.imshow(image)
    # plt.subplot(122),plt.imshow(dst)
    # plt.show()

    #ljkasklhKSJDHFLHSDLKFHKJSDHLFHDSF
    # path to input image specified and
    # image is loaded with imread command
    # convert the input image into
    # grayscale color space
    # # Reverting back to the original image,
    # # with optimal threshold value
    # result[dest > 0.01 * dest.max()]=[255, 255, 255]
    #
    # #AKJSHDKHSKDLJFHKLSDHKFJHjkldf

    #set the low and high tuples based on the chosen color
    blurred = cv2.bilateralFilter(result, 9, 75, 75)

    low = np.array([blueLow, greenLow, redLow])
    high = np.array([blueHigh, greenHigh, redHigh])
    #mask everything but the red
    mask = cv2.inRange(blurred, low, high)
    # mask2 = cv2.inRange(image, (175, 50, 20), (180, 255, 255))
    #cv2.waitKey()
    output = cv2.bitwise_and(blurred, blurred, mask = mask)

    #denoise the mask
    denoise_1 = cv2.fastNlMeansDenoisingColored(output,None,3,3,7,21)
    cv2.imshow("1",denoise_1)
    cv2.waitKey(0)

    #Find the contours in the mask
    gray = cv2.cvtColor(denoise_1, cv2.COLOR_BGR2GRAY)

    #threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

    rectangles = []

    i = 0
    for contour in contours:

        # here we are ignoring first counter because
        # find contour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        # cv2.approxPloyDP() function to approximate the shape
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

        # finding center point of shape
        # M = cv2.moments(contour)
        # if M['m00'] != 0.0:
        #     x = int(M['m10']/M['m00'])
        #     y = int(M['m01']/M['m00'])

        cv2.drawContours(denoise_1, contour, 0, (255, 255, 255), 5)

        if len(approx) == 4:
            print("found rectangle oohhhoohoh")
            rectangles.append(approx)

    max = 0
    #find the biggest area
    for i in range(len(rectangles)):
        area = cv2.contourArea(rectangles[i])
        if area > cv2.contourArea(rectangles[max]):
            max = i

    #find center of mass of the largest contour
    # M = cv2.moments(rectangles[max])
    # if M['m00'] != 0.0:
    #     x = int(M['m10']/M['m00'])
    #     y = int(M['m01']/M['m00'])

    #draw the largest contour onto the image
    # cv2.putText(denoise_1, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    # using drawContours() function
    #cv2.drawContours(denoise_1, [rectangles[max]], 0, (255, 255, 255), 5)
    cv2.imshow("denoise_1", denoise_1)



    # blurred2 = cv2.bilateralFilter(denoise_1, 9, 75, 75)
    # cv2.imshow("mask", output)
    # cv2.waitKey(0)
    #
    # operatedImage = cv2.cvtColor(denoise_1, cv2.COLOR_BGR2GRAY)
    #
    # # modify the data type
    # # setting to 32-bit floating point
    # operatedImage = np.float32(operatedImage)
    #
    # # apply the cv2.cornerHarris method
    # # to detect the corners with appropriate
    # # values as input parameters
    # dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
    #
    # # Results are marked through the dilated corners
    # dest = cv2.dilate(dest, None)
    # cv2.imshow("denoise_1", denoise_1)
    # cv2.imshow("dest",dest)
    cv2.waitKey(0)
    #

    # create more contrast between light blue background and red line, and replace green netting with light blue

    # edges = cv2.Canny(blurred2, 50, 150)
    #cv2.imshow("edges", edges);
    #Find corners of lines
    #ljkasklhKSJDHFLHSDLKFHKJSDHLFHDSF
    # path to input image specified and
    # image is loaded with imread command
    # convert the input image into
    # grayscale color space
    # operatedImage = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    #
    # # modify the data type
    # # setting to 32-bit floating point
    # operatedImage = np.float32(operatedImage)
    #
    # #edges = np.float32(edges)
    #
    # # apply the cv2.cornerHarris method
    # # to detect the corners with appropriate
    # # values as input parameters
    # dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
    #
    # # Results are marked through the dilated corners
    # dest = cv2.dilate(output, None)
    #
    # # Reverting back to the original image,
    # # with optimal threshold value
    # output[dest > 0.01 * dest.max()]=[0, 0, 255]
    # cv2.imshow("output", output);
    # #AKJSHDKHSKDLJFHKLSDHKFJHjkldf
    # #
    # # midpointX = (int)((leftTopX + rightTopX) / 2) #account for the rounding when we're checking it against the center value
    # cv2.circle(result, (midpointX, 10), 3, (5, 255, 255), 3)
    # #cv2.imshow('', result)
    # #cv2.imshow("mask", output)
    midpointX= 0
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

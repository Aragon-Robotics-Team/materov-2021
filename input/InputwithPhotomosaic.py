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

#PHOTOMOSAIC-----------------------------------------------------------------------------------------------
global i
i = 0
def showVideo():
    if quit == False:
        ret, frame = videoCaptureObject.read()
        cv2.imshow("Capturing Video", frame)
        # deletes every frame as the next one comes on, closes all windows when q is pressed
        #if cv2.waitKey(1) == ord('q'):
    if quit == True:
        videoCaptureObject.release()
        cv2.destroyAllWindows()

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

#---------crop and resize the image to a height of 250 pixels-----------
def cropping(image):
    image = cv2.imread(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 300, cv2.THRESH_BINARY_INV)[1]
    #cv2.imshow("Thresh", thresh)
    #cv2.waitKey(0)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    output = image.copy()
    cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    (x, y, w, h) = cv2.boundingRect(c)
    text = "original, num_pts = {}".format(len(c))
    cv2.putText(output, text, (x,y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    #Crop the image based on the points of the bounding box, show the cropped image
    cropped = image[y:y+h, x:x+w]
    file = snapshots[i]
    cv2.imwrite(file, cropped)
    #cv2.imshow("Cropped Image", cropped)
    #cv2.waitKey(0)

    ratio = 250/cropped.shape[0]
    resizeimage[i] = resize_image(cropped, ratio, ratio)
    cv2.imwrite(resizedimages[i], resizeimage[i])
    #cv2.imshow("Resized Cropped", resizeimage[i])
    #cv2.waitKey(0)

    #cv2.destroyAllWindows()

center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

centerResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/centerResize.png", blank)
topResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topResize.png", topResize)
bottomResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomResize.png", bottomResize)
leftResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/leftResize.png", leftResize)
rightResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/rightResize.png", rightResize)
blankTopResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankTopResize.png", blankTopResize)
blankBottomResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankBottomResize.png", blankBottomResize)

resizedimages = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/centerResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/leftResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/rightResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankResize.png"
]

resizeimage = [
    centerResize,
    topResize,
    bottomResize,
    leftResize,
    rightResize]

snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]

# def photomosaicThreading():
#     t1 = Thread(target = photomosaic)
#     t1.start()

def photomosaic():
    global i
    i = 0
    print("Running Photomosaic")
    snap = True
    while snap:
        ret, frame = videoCaptureObject.read()
        #cv2.imshow("Photomosaic Video", frame)
        # deletes every frame as the next one comes on, closes all windows when q is pressed
        if cv2.waitKey(1) == ord('q'):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
        # when s is pressed
        if keyboard.is_pressed('s'):
            # and the index is less than the length of the snapshot list
            if i < len(snapshots):
                # take as snapshot, save it, show it
                cv2.imwrite(snapshots[i], frame)
                #cv2.imshow(snapshots[i], frame)
                cropping(snapshots[i])
                resizeimage[i] = cv2.imread(resizedimages[i])
                time.sleep(1)
                i += 1
            else:
                snap = False

    center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
    top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
    bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
    left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
    right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
    blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

    #---------saving the resized versions of the images to variables-----------
    centerResize = cv2.imread(resizedimages[0])
    topResize = cv2.imread(resizedimages[1])
    bottomResize = cv2.imread(resizedimages[2])
    leftResize = cv2.imread(resizedimages[3])
    rightResize = cv2.imread(resizedimages[4])

    #----------------------concat middle tile------------------------
    middleTileLeft = cv2.hconcat([leftResize, centerResize])
    cv2.imshow("Middle Tile Left", middleTileLeft)
    cv2.waitKey(0)
    middleTile = cv2.hconcat([middleTileLeft, rightResize])
    cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/middleTile.png", middleTile)
    cv2.imshow("MiddleTile", middleTile)
    cv2.waitKey(0)
    print("Middle Tile Length:")
    print(middleTile.shape[1])

    #--------calculate the size of the blank images to make up for the size difference in the tiles------------
    heightratio = 250/blank.shape[0]
    topwidth = (middleTile.shape[1] - topResize.shape[1])/2
    #print(topResize.shape[1])
    print("Top Image Length:")
    print(topwidth)
    topwidthratio = topwidth/blank.shape[1]
    bottomwidth = (middleTile.shape[1] - bottomResize.shape[1])/2
    #print(bottomResize.shape[1])
    print("Bottom Image Length:")
    print(bottomwidth)
    bottomwidthratio = bottomwidth/blank.shape[1]
    blankTopResize = resize_image(blank, topwidthratio, heightratio)
    print("Blank Top Tile Length")
    print(blankTopResize.shape[1])
    blankBottomResize = resize_image(blank, bottomwidthratio, heightratio)
    print("Blank Bottom Tile Length:")
    print(blankBottomResize.shape[1])

    #----------concat top tile-----------------
    topTileLeft = cv2.hconcat([blankTopResize, topResize])
    topTile = cv2.hconcat([topTileLeft, blankTopResize])
    cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topTile.png", topTile)
    cv2.imshow("Top Tile", topTile)
    cv2.waitKey(0)
    print("Top Tile Length:")
    print(topTile.shape[1])

    #-------------concat bottom tile--------------
    bottomTileLeft = cv2.hconcat([blankBottomResize, bottomResize])
    bottomTile = cv2.hconcat([bottomTileLeft, blankBottomResize])
    cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomTile.png", bottomTile)
    cv2.imshow("Bottom Tile", bottomTile)
    cv2.waitKey(0)
    print("Bottom Tile Length")
    print(bottomTile.shape[1])


    #------------resize again if it doesn't work for some reason -.- -------------
    if bottomTile.shape[1] != middleTile.shape[1]:
        bottomTile = resize_image(bottomTile, middleTile.shape[1]/bottomTile.shape[1], 1)
        print("resizing bottomTile")
        print(bottomTile.shape[1])

    if topTile.shape[1] != middleTile.shape[1]:
        topTile = resize_image(topTile, middleTile.shape[1]/topTile.shape[1], 1)
        print("resizing top tile")
        print(topTile.shape[1])


    #---------stitch together all the tiles-----------
    topSection = cv2.vconcat([topTile, middleTile])
    photomosaic = cv2.vconcat([topSection, bottomTile])
    cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/photomosaic.png", photomosaic)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("PHOTOMOSAIC", photomosaic)
    cv2.waitKey(0)

Bu = tk.Button(root, text = "Photomosaic", command = photomosaic).pack()


Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()
###############
def quitVideo():
    print("quit video")
    global quit
    quit = True

Bu = tk.Button(root, text="Quit Video", command = quitVideo).pack()

Bu = tk.Button(root, text="Quit GUI", command = root.destroy).pack()

#Bu = tk.Button(root, text="Photomosaic Snapshot", command = photomosaic).pack()

Result = True
while Result:
    #quitStatus()
    controller()
    showVideo()
    root.update()

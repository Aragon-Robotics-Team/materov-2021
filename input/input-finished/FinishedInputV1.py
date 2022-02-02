#To find specific sections, search up BM: "*insert name*"
#Current Bookmarks:
#BM: GUI set up
#BM: Controller input Setup
#BM: Image Processing
    #BM: Photomosaic
#BM: General Setup
    #BM: Video Feed
    #BM: Queue for threading
    #BM: Testing Buttons with Hello World
#BM: Main Loop

#GUI Imports
import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import queue

#Pygame imports
import pygame
from time import sleep

#Image Processing imports
import numpy as np
import threading
import cv2
import imutils
import keyboard


photomosaicVideo = False
photomosaicStart = False

#BM: GUI set up --------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.config(bg ='gray')
q = queue.Queue()
#BM: Controller input Setup --------------------------------------------------------------------------------------------------------------------
# pygame.init()
# joysticks = []
# clock = pygame.time.Clock()
# deadband = 0.1
# keepPlaying = True
# print("Controller Input Begun")
#
# myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
# myjoystick.init()

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


#BM: Image Processing --------------------------------------------------------------------------------------------------------
#BM: Photomosaic --------------------------------------------------------------------------------------------------------

def photomosaicThreading():
    global photomosaicStart
    photomosaicStart = True
    threading.Thread(target=photomosaic).start()

center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_h), int(img.shape[0]*scale_w)))

def cropping(image):
    image = cv2.imread(image)
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 300, cv2.THRESH_BINARY_INV)[1]

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

photomosaicCount = 0
photomosaicStart = False
def photomosaic():
    print("Starting photomosaic")
    global photomosaicCount
    photomosaicCount = 0
    global photomosaicVideo
    photomosaicVideo = True
    global photomosaicStart
    photomosaicStart = False
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True

    while photomosaicStart == False:
        sleep(0.1)
    if photomosaicStart == True:
        print("Starting Photomosaic Process")
        #---------rereading the original images from the snapshots-----------
        center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
        top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
        bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
        left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
        right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
        blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

        # #--------calculate the size of the blank images to make up for the size difference in the tiles------------
        print("Resizing Images")
        topLeftHeightRatio = cv2.imread(snapshots[1]).shape[1]/blank.shape[1]
        topLeftWidthRatio = cv2.imread(snapshots[3]).shape[0]/blank.shape[0]
        topLeftBlank = resize_image(blank, topLeftWidthRatio, topLeftHeightRatio)
        bottomLeftHeightRatio = cv2.imread(snapshots[2]).shape[1]/blank.shape[1]
        bottomLeftWidthRatio = cv2.imread(snapshots[3]).shape[0]/blank.shape[0]
        bottomLeftBlank = resize_image(blank, bottomLeftWidthRatio, bottomLeftHeightRatio)
        topRightHeightRatio = cv2.imread(snapshots[1]).shape[1]/blank.shape[1]
        topRightWidthRatio = cv2.imread(snapshots[4]).shape[0]/blank.shape[0]
        topRightBlank = resize_image(blank, topRightWidthRatio, topRightHeightRatio)
        bottomRightHeightRatio = cv2.imread(snapshots[2]).shape[1]/blank.shape[1]
        bottomRightWidthRatio = cv2.imread(snapshots[4]).shape[0]/blank.shape[0]
        bottomRightBlank = resize_image(blank, bottomRightWidthRatio, bottomRightHeightRatio)

        #----------------------concat middle tile------------------------
        print("Concat Middle Tile")
        middleTileLeft = cv2.hconcat([cv2.imread(snapshots[3]), cv2.imread(snapshots[0])])
        middleTile = cv2.hconcat([middleTileLeft, cv2.imread(snapshots[4])])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/middleTile.png", middleTile)

        #----------concat top tile-----------------
        print("Concat Top Tile")
        topTileLeft = cv2.hconcat([topLeftBlank, cv2.imread(snapshots[1])])
        topTile = cv2.hconcat([topTileLeft, topRightBlank])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topTile.png", topTile)

        #-------------concat bottom tile--------------
        print("Concat Bottom Tile")
        bottomTileLeft = cv2.hconcat([bottomLeftBlank, cv2.imread(snapshots[4])])
        bottomTile = cv2.hconcat([bottomTileLeft, bottomRightBlank])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomTile.png", bottomTile)

        #---------stitch together all the tiles-----------
        print("Stitch together all the tiles")
        topSection = cv2.vconcat([topTile, middleTile])
        photomosaic = cv2.vconcat([topSection, bottomTile])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/photomosaic.png", photomosaic)
        print("Sending Photomosaic Image to main thread")
        q.put(photomosaic)
        #cv2.imshow("PHOTOMOSAIC", photomosaic)
        cv2.waitKey(0)

        #definitely have to add this back in later
        #global photomosaicStart
        photomosaicStart = False


Bu  = tk.Button(root, text = "Photomosaic", command = photomosaicThreading).pack()

#BM: General Setup --------------------------------------------------------------------------------------------------------
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
    if photomosaicVideo == True:
        #print("photomosaic true")
        if keyboard.is_pressed('s'):
            # and the index is less than the length of the snapshot list
            if photomosaicCount < len(snapshots):
                cv2.imwrite(snapshots[photomosaicCount], frame)
                cropping(snapshots[photomosaicCount])
                center_height = cv2.imread(snapshots[0]).shape[0]
                center_width = cv2.imread(snapshots[0]).shape[1]
                width_ratio = center_width/cv2.imread(snapshots[photomosaicCount]).shape[1]
                height_ratio = center_height/cv2.imread(snapshots[photomosaicCount]).shape[0]
                if photomosaicCount < 3:
                    resized = resize_image(cv2.imread(snapshots[photomosaicCount]), width_ratio, width_ratio)
                else:
                    resized = resize_image(cv2.imread(snapshots[photomosaicCount]), height_ratio, height_ratio)

                cv2.imwrite(snapshots[photomosaicCount], resized)
                print("Snapshot #" + str(photomosaicCount) + " taken")
                #cv2.imshow(snapshots[i], frame)
                time.sleep(1)
                photomosaicCount += 1
            else:
                print("PhotomosaicStart true")
                photomosaicVideo = False
                photomosaicStart = True
        # when s is pressed

#BM: Queue for threading
def queue(): #Needs forever loop, therefore can't use root.mainloop()
    if q.empty() == False:
        item = q.get()
        print(type(item))
        if (type(item) == np.ndarray):
            print("Input Type : Image Path")
            cv2.imshow("Threading Image", item)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        q.task_done()

#BM: Testing Buttons with Hello World
def helloWorld():
    print("helloWorld")

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()
#BM: Main Loop --------------------------------------------------------------------------------------------------------
Result = True
while Result:
    #controller()
    #sleep(0.1)
    videoCapture()
    queue()
    root.update()

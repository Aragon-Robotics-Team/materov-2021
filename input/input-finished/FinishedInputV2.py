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
#BM: GUI Features:
    #BM: Timer
    #BM: Task Display
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
import math


photomosaicVideo = False
photomosaicStart = False

#BM: GUI set up --------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.config(bg ='gray')
root.geometry("1000x1200")
root.title("MATE ROV GUI Version 1.0")
root.resizable(True, True)
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
    print("Type s 4 times to take snapshots, and one more time to construct the photomosaic")
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


Bu  = tk.Button(root, text = "Photomosaic", command = photomosaicThreading).place(x=10, y=15)
#BM: Measure Fish --------------------------------------------------------------------------------------------------------
fishCoords = [[0,0],[0,0],[0,0],[0,0]]
#[laserX1, laserY1],
#[laserX2, laserY2],
#[fishX1, fishY1],
#[fishX2, fishY2]
measureFishieClick = False
measureFishieCalc = False
countFishCoords = 0
fishImg = ""

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

    #take 3photos and measure
    if fishPictureCount < 3:
        #show image and read coordinates
        print("Fish #: " + str(fishPictureCount + 1))
        ret, frame = videoCaptureObject.read()
        fishImg = frame
        cv2.imshow("Fish", fishImg)
        cv2.setMouseCallback("Fish", click_event)
    else:
        #print all the measured fish lengths, input N, a, and b, and calculate the biomass of the cohort
        print("Fish Lengths: " + str(allFishLengths))
        averageFishLength = (allFishLengths[0]+allFishLengths[1]+allFishLengths[2])/3
        print("Average Fish Length: " + str(averageFishLength))

        askForValues = True
        while askForValues:
            #ask for the values
            numFish = int(input("Enter the number of fish (N): "))
            print("Number of Fish: " + str(numFish))

            numA = int(input("Enter the value of A: "))
            print("Value of A: " + str(numA))

            numB = int(input("Enter the value of B: "))
            print("Value of B: " + str(numB))

            askForValuesInput = input("Are these values correct? Type Y or N: ")

            if askForValuesInput == "Y":
                #calculate the biomass of the cohort
                askForValues = False
                print("Calculating biomass of the cohort using the equation M = N * a * L^b")
                fishMass = numFish * numA * ((averageFishLength)**numB)
                print("Biomass of the Cohort: " + str(fishMass))
            elif askForValuesInput == "N":
                #if these values are wrong, as for them again
                askForValues = True
            else:
                print("You're kind of stupid for not even typing Y or N, enter all the values in again")
                askForValues = True

Bu = tk.Button(root, text="Measure Fish (Click to 3 times to take photos and calculate)", command = measureFishie).place(x=10, y=50)
#if measure fishies doesn't work out, reset and restart
def resetMeasureFish():
    print("Measuring Fish Task Reset")
    global allFishLengths
    global fishPictureCount
    global countFishCoords
    allFishLengths = [0,0,0]
    countFishCoords = 0
    fishPictureCount = 0

Bu = tk.Button(root, text="Reset Fish Measuring", command = resetMeasureFish).place(x=10, y=85)

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

#GUI FEATURES --------------------------------------------------------------------------------------------------------
#BM: Timer

minute=StringVar()
second=StringVar()
hours=StringVar()

sec = StringVar()
mins= StringVar()
hrs= StringVar()

tk.Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=875, y=10) # Seconds
tk.Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=910, y=10) # Mins
tk.Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=945, y=10) # Hours

minute.set('00')
second.set('00')
hours.set('00')
sec.set('00')
mins.set('00')
hrs.set('00')
times = 0

def countdown():
    global times
    print("hello") #testing, working but code not working
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > 0:
        minute,second = (times // 60 , times % 60)

        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)
        times -= 1
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
            return

def stop():
    global times
    minute.set('00')
    second.set('00')
    hours.set('00')
    sec.set('00')
    mins.set('00')
    hrs.set('00')
    times = 0

tk.Button(root, text='START', bd ='1', command = countdown, height= 1, width= 5, bg = 'white', font = 'arial 10 bold').place(x=874, y=35)
tk.Button(root, text='STOP', bd ='1', command = stop, height= 1, width= 5, bg = 'white', font = 'arial 10 bold').place(x=922, y=35)

#BM: Task Display

def button1():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(root, text ="Hello", command = button1, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 20).place(x=700, y=100)

def button2():
   tk.messagebox.showinfo( "Hello Python2", "Hello World2")

Bu = tk.Button(root, text ="Hello2", command = button2, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 20).place(x=700, y=150)

def button3():
   tk.messagebox.showinfo( "Hello Python3", "Hello World3")

Bu = tk.Button(root, text ="Hello3", command = button3, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 20).place(x=700, y=200)

def button4():
   tk.messagebox.showinfo( "Hello Python4", "Hello World4")

Bu = tk.Button(root, text ="Hello4", command = button2, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 20).place(x=700, y=250)

def button5():
   tk.messagebox.showinfo( "Hello Python5", "Hello World5")

Bu = tk.Button(root, text ="Hello5", command = button2, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 20).place(x=700, y=300)

def button6():
   tk.messagebox.showinfo( "Hello Python6", "Hello World6")

Bu = tk.Button(root, text ="Hello6", command = button2, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 10).place(x=700, y=350)

def task1():
    print("hi")

Bu = tk.Button(root, text ="Hello6", command = task1, font = 'Roboto', borderwidth = 1, bg = 'dark gray', height = 1,width = 10).place(x=700, y=350)

labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="Inside the LabelFrame")
left.pack()

#BM: Main Loop --------------------------------------------------------------------------------------------------------
Result = True
while Result:
    #controller() <-- If autonomous, replace controller thruster input with autonomous thruster input
    videoCapture()
    queue()
    root.update()

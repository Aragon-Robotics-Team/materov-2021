from tkinter import *
import glob
from img_proc.measure_fishes import measureFish
from img_proc.measure_fishes import averageLength

from img_proc.measure_fishes import ValuesAndCalc

import cv2
import multiprocessing

from img_proc.photomosaic import cropping
from img_proc.photomosaic import resize_image
from img_proc.photomosaic import stitch
import time

cap = cv2.VideoCapture(0)

#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1300x750")

#TEST ------------------------------------------------------------------------------------------------------
def asdf():
    print("hello")

btn = Button(root, text = "hello", command = asdf)
btn.grid(row = 0, column = 1, sticky = 'e')

#PHOTOMOSAIC ------------------------------------------------------------------------------------------------------
# def startPhotomosaic():
#     print("asdf")
#     glob.photomosaicCount = 0
#     print("Starting photomosaic")
#     print("Type s 4 times to take snapshots, and one more time to construct the photomosaic")
#     print("Type q to quit the photomosaic")
#     glob.photomosaicVideo = True #switches video feed to photomosaic Video
#
# btn = Button(root, text = "Start Photomosaic", command = startPhotomosaic)
# btn.grid(row = 1,column = 1, sticky = 'e')
#
startPhotomosaic = False
photomosaicCount = 0

def beginPhotomosaic():
    global startPhotomosaic
    print("Photomosaic begun")
    print("Click take photomosaic button to take each snapshot")
    startPhotomosaic = True
    photomosaicCount = 0

btn = Button(root, text = "Start Photomosaic", command = beginPhotomosaic)
btn.grid(row = 1, column = 1, sticky = 'e')

def takePhotomosaicPhoto():
    global startPhotomosaic
    global photomosaicCount
    if startPhotomosaic == True:
        if photomosaicCount < len(glob.snapshots):
            ret, frame = cap.read()
            cv2.imwrite(glob.snapshots[glob.photomosaicCount], frame)
            cropping(glob.snapshots[glob.photomosaicCount])
            center_height = cv2.imread(glob.snapshots[0]).shape[0]
            center_width = cv2.imread(glob.snapshots[0]).shape[1]
            width_ratio = center_width/cv2.imread(glob.snapshots[glob.photomosaicCount]).shape[1]
            height_ratio = center_height/cv2.imread(glob.snapshots[glob.photomosaicCount]).shape[0]
            if photomosaicCount < 3:
                resized = resize_image(cv2.imread(glob.snapshots[glob.photomosaicCount]), width_ratio, width_ratio)
            else:
                resized = resize_image(cv2.imread(glob.snapshots[glob.photomosaicCount]), height_ratio, height_ratio)

            cv2.imwrite(glob.snapshots[photomosaicCount], resized)
            print("Snapshot #" + str(photomosaicCount) + " taken")
            #cv2.imshow(glob.snapshots[i], frame)
            time.sleep(1)
            photomosaicCount += 1
        else:
            print("All photomosaic snapshots taken")
            stitch()
            startPhotomosaic = False
    else:
        print("Photomosaic has not been started yet")

btn = Button(root, text = "Take Photomosaic Snapshot", command = takePhotomosaicPhoto)
btn.grid(row = 2, column = 1, sticky = 'e')

def resetPhotomosaic():
    global startPhotomosaic
    global photomosaicCount
    startPhotomosaic = False
    photomosaicCount = 0

btn = Button(root, text = "Reset Photomosaic Snapshot", command = resetPhotomosaic)
btn.grid(row = 3, column = 1, sticky = 'e')


#MEASURE FISHIES ------------------------------------------------------------------------------------------------------
fishCount = 0
def start_measure_fish():
    global fishCount
    ret, frame = cap.read()
    if fishCount < 3:
        measureFish(frame)
        fishCount = fishCount + 1
    else:
        averageFishLength = averageLength()
        ValuesAndCalc(averageFishLength)

label = Label(root, text = "(Click to 3 times to take photos and calculate)", font = 10)
label.grid(row = 5, column = 1, sticky = 'n')

btn = Button(root, text="Measure Fish", command = start_measure_fish)
btn.grid(row = 4,column = 1, sticky = 'e')

def resetMeasureFish():
    print("Measuring Fish Task Reset")
    glob.allFishLengths = [0,0,0]
    glob.countfishCoords = 0
    glob.fishPictureCount = 0

btn = Button(root, text="Reset Fish Measuring", command = resetMeasureFish)
btn.grid(row = 6, column = 1, sticky = 'e')

#DRIFT
from misc.drift import floatLocation
btn = Button(root, text = "Calculate Float Location", command = floatLocation)
btn.grid(row = 7, column = 1, sticky = 'e')

#VIDEO FEED ------------------------------------------------------------------------------------------------------
#pretty much the same lag as when the video feed is in the loop
from PIL import Image, ImageTk

# Create a Label to capture the Video frames
label = Label(root, height = 700, width = 1000)
label.grid(row = 0, column = 0, rowspan = 30)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

show_frames()

def updateGUI():
    while True:
        root.update()

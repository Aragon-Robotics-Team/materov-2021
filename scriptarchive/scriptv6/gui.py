from tkinter import *
import glob
from img_proc.measure_fishes import measureFish
from img_proc.measure_fishes import averageLength

from img_proc.measure_fishes import ValuesAndCalc

import cv2
import multiprocessing

from img_proc.docking import dockpic
from img_proc.docking import dockCalculate

cap = cv2.VideoCapture(0)
#cap1 = cv2.VideoCapture(1) <-- Second Camera


#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1300x750")

#TEST ------------------------------------------------------------------------------------------------------
def asdf():
    print("hello")

btn = Button(root, text = "hello", command = asdf)
btn.grid(row = 0, column = 1, sticky = 'e')

#PHOTOMOSAIC ------------------------------------------------------------------------------------------------------
def startPhotomosaic():
    print("asdf")
    glob.photomosaicCount = 0
    print("Starting photomosaic")
    print("Type s 4 times to take snapshots, and one more time to construct the photomosaic")
    print("Type q to quit the photomosaic")
    glob.photomosaicVideo = True #switches video feed to photomosaic Video

btn = Button(root, text = "Start Photomosaic", command = startPhotomosaic)
btn.grid(row = 1,column = 1, sticky = 'e')

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
label.grid(row = 3, column = 1, sticky = 'n')

btn = Button(root, text="Measure Fish", command = start_measure_fish)
btn.grid(row = 2,column = 1, sticky = 'e')

def resetMeasureFish():
    print("Measuring Fish Task Reset")
    glob.allFishLengths = [0,0,0]
    glob.countfishCoords = 0
    glob.fishPictureCount = 0

btn = Button(root, text="Reset Fish Measuring", command = resetMeasureFish)
btn.grid(row = 4, column = 1, sticky = 'e')

#DRIFT
from misc.drift import floatLocation
btn = Button(root, text = "Calculate Float Location", command = floatLocation)
btn.grid(row = 5, column = 1, sticky = 'e')

#DOCKING
dockCount = 0
def docking():
    global dockCount
    ret, frame = cap.read()
    if dockCount == 0:
        dockpic(frame)
        dockCount = dockCount + 1
    else:
        cv2.destroyAllWindows()
        dockCalculate()


btn = Button(root, text = "Autonomous Docking Calibration", command = docking)
btn.grid(row = 6, column = 1, sticky = 'e')

#VIDEO FEED ------------------------------------------------------------------------------------------------------
#pretty much the same lag as when the video feed is in the loop
from PIL import Image, ImageTk

# Create a Label to capture the Video frames
label = Label(root, height = 700, width = 1000)
label.grid(row = 0, column = 0, rowspan = 30)

camera = 0 #specifies the camera object to use


# Define function to show frame
def show_frames():
    #To Change the cameras
    # if camera = 0:
    #     cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    # elif camera = 1:
    #     cv2image= cv2.cvtColor(cap1.read()[1],cv2.COLOR_BGR2RGB)

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

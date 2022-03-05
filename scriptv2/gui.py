from tkinter import *
import glob

#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1400x2000")

#TEST ------------------------------------------------------------------------------------------------------
def asdf():
    print("hello")

btn = Button(root, text = "hello", command = asdf)
btn.pack()

#PHOTOMOSAIC ------------------------------------------------------------------------------------------------------
def startPhotomosaic():
    print("asdf")
    glob.photomosaicCount = 0
    print("Starting photomosaic")
    print("Type s 4 times to take snapshots, and one more time to construct the photomosaic")
    print("Type q to quit the photomosaic")
    glob.photomosaicVideo = True #switches video feed to photomosaic Video

btn = Button(root, text = "Start Photomosaic", command = startPhotomosaic)
btn.pack()

#MEASURE FISHIES ------------------------------------------------------------------------------------------------------
from img_proc.measure_fishes import measureFishie
import cv2

def start_measure_fish():
    measureFishie()

Bu = Button(root, text="Measure Fish (Click to 3 times to take photos and calculate)", command = start_measure_fish).pack()

def resetMeasureFish():
    print("Measuring Fish Task Reset")
    glob.allFishLengths = [0,0,0]
    glob.countfishCoords = 0
    glob.fishPictureCount = 0

Bu = Button(root, text="Reset Fish Measuring", command = resetMeasureFish).pack()

#VIDEO FEED ------------------------------------------------------------------------------------------------------
#pretty much the same lag as when the video feed is in the loop
from PIL import Image, ImageTk

root.geometry("1400x2000")

# Create a Label to capture the Video frames
label = Label(root, height = 700, width = 700)
label.place(x = 700,y = 0)
cap = cv2.VideoCapture(0)

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

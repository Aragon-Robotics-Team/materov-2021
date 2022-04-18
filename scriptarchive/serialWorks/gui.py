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

#BUTTON GRAPHICS------------------------------------------------------------------------------------------------------

buttoncanvas = Canvas(root,height=120,width=250,bg="#fff")

buttoncanvas.grid(row = 7, column = 1, sticky = 'e')

buttoncanvas.create_line(10, 10, 240, 10, fill = "black")

centx = 200 #x coord of center point of buttons
centy = 75 #y coord of center point of buttons
bsx = 10 #x span of button
bsy = 10 #y span of buttons
bspace = 30 #space between buttons

#Variables for button statuses and creating corresponding circle and square objects
buttonAstatus = False
Acirc = buttoncanvas.create_oval(centx - bsx, centy - bsy - bspace, centx + bsx, centy + bsy - bspace)
buttonBstatus = False
Bcirc = buttoncanvas.create_oval(centx - bsx + bspace, centy - bsy,  centx + bsx + bspace, centy + bsy)
buttonXstatus = False
Xcirc = buttoncanvas.create_oval(centx - bsx - bspace, centy - bsy,  centx + bsx - bspace, centy + bsy)
buttonYstatus = False
Ycirc = buttoncanvas.create_oval(centx - bsx, centy - bsy + bspace, centx + bsx, centy + bsy + bspace)

Acentx = 75
Acenty = 75

leftstatus = False
leftSquare = buttoncanvas.create_rectangle(Acentx - bsx - bspace, Acenty - bsy,  Acentx + bsx - bspace, Acenty + bsy)
rightstatus = False
rightSquare = buttoncanvas.create_rectangle(Acentx - bsx + bspace, Acenty - bsy,  Acentx + bsx + bspace, Acenty + bsy)
upstatus = False
upSquare = buttoncanvas.create_rectangle(Acentx - bsx, Acenty - bsy + bspace, Acentx + bsx, Acenty + bsy + bspace)
downstatus = False
downSquare = buttoncanvas.create_rectangle(Acentx - bsx, Acenty - bsy - bspace, Acentx + bsx, Acenty + bsy - bspace)

#adfasdfadfadf need to do this part
LTstatus = False
LBstatus = False
RTstatus = False

#JOYSTICK GRAPHICS

joystickcanvas = Canvas(root,height=250,width=250,bg="#fff")

joystickcanvas.grid(row = 8, column = 1, sticky = 'e')

joystickcanvas.create_line(10, 10, 240, 10, fill = "black")
topx = 50
topy = 50
width = 160
height = 20
bottomx = topx + width
bottomy = topy + height

j1xrow = 0
j1yrow = 1
j2xrow = 2
j2yrow = 3
space = 50

center = width/2
joy1xstatus = center

joystickcanvas.create_rectangle(topx, topy + space * j1xrow, bottomx, bottomy + space * j1xrow, outline = "gray", fill = "gray")
joy1xrec = joystickcanvas.create_rectangle(topx, topy + space * j1xrow, topx + joy1xstatus, bottomy + space * j1xrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j1xrow, text="Joy 1 X Axis", fill="dark gray", font=('Helvetica 10 bold'))

joy1ystatus = center

joystickcanvas.create_rectangle(topx, topy + space * j1yrow, bottomx, bottomy + space * j1yrow, outline = "gray", fill = "gray")
joy1yrec = joystickcanvas.create_rectangle(topx, topy + space * j1yrow, topx + joy1ystatus, bottomy + space * j1yrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j1yrow, text="Joy 1 Y Axis", fill="dark gray", font=('Helvetica 10 bold'))

joy2xstatus = center

joystickcanvas.create_rectangle(topx, topy + space * j2xrow, bottomx, bottomy + space * j2xrow, outline = "gray", fill = "gray")
joy2xrec = joystickcanvas.create_rectangle(topx, topy + space * j2xrow, topx + joy2xstatus, bottomy + space * j2xrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j2xrow, text="Joy 2 X Axis", fill="dark gray", font=('Helvetica 10 bold'))

joy2ystatus = center

joystickcanvas.create_rectangle(topx, topy + space * j2yrow, bottomx, bottomy + space * j2yrow, outline = "gray", fill = "gray")
joy2yrec = joystickcanvas.create_rectangle(topx, topy + space * j2yrow, topx + joy2ystatus, bottomy + space * j2yrow, outline = "green", fill = "green")
joystickcanvas.create_text(topx + width/2, topy + height/2 + space * j2yrow, text="Joy 2 Y Axis", fill="dark gray", font=('Helvetica 10 bold'))




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

if __name__ == "__main__":
    root.mainloop()

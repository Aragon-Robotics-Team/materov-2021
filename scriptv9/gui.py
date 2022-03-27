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

from img_proc.photomosaic import cropping
from img_proc.photomosaic import resize_image
from img_proc.photomosaic import stitch
import time

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
            # frame = PiRGBArray(camera)
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
label.grid(row = 4, column = 1, sticky = 'n')

btn = Button(root, text="Measure Fish", command = start_measure_fish)
btn.grid(row = 5 ,column = 1, sticky = 'e')

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
btn.grid(row = 8, column = 1, sticky = 'e')

#BUTTON GRAPHICS------------------------------------------------------------------------------------------------------
buttoncanvas = Canvas(root,height=120,width=250,bg="#fff")

buttoncanvas.grid(row = 9, column = 1, sticky = 'e')

buttoncanvas.create_line(10, 10, 240, 10, fill = "black", width = 5)

centx = 200 #x coord of center point of buttons
centy = 75 #y coord of center point of buttons
bsx = 10 #x span of button
bsy = 10 #y span of buttons
bspace = 30 #space between buttons

#Variables for button statuses and creating corresponding circle and square objects
buttonAstatus = False
Acirc = buttoncanvas.create_oval(centx - bsx, centy - bsy - bspace, centx + bsx, centy + bsy - bspace, fill = "dark gray", outline = "dark gray")
buttoncanvas.create_text(centx, centy - bspace, text = "A", font =('Helvetica 15 bold'))
buttonBstatus = False

Bcirc = buttoncanvas.create_oval(centx - bsx + bspace, centy - bsy,  centx + bsx + bspace, centy + bsy, fill = "dark gray", outline = "dark gray")
buttoncanvas.create_text(centx + bspace, centy, text = "B", font = 'Helvetica 15 bold')
buttonXstatus = False

Xcirc = buttoncanvas.create_oval(centx - bsx - bspace, centy - bsy,  centx + bsx - bspace, centy + bsy, fill = "dark gray", outline = "dark gray")
buttoncanvas.create_text(centx - bspace, centy, text = "X", font = 'Helvetica 15 bold')
buttonYstatus = False

Ycirc = buttoncanvas.create_oval(centx - bsx, centy - bsy + bspace, centx + bsx, centy + bsy + bspace, fill = "dark gray", outline = "dark gray")
buttoncanvas.create_text(centx, centy + bspace, text = "Y", font = 'Helvetica 15 bold')

indleftx = 30
indlefty = 55
ind_height = 20
ind_width = 110
ind_space = 40

teleopInd = buttoncanvas.create_rectangle(indleftx, indlefty, indleftx + ind_width, indlefty + ind_height, fill = "dark gray", outline = "dark gray")
teleopStatus = False
buttoncanvas.create_text(indleftx + ind_width/2, indlefty + ind_height/2, text = "TELEOP STATUS", font = 'Helvetica 10 bold', fill = "black")

nonlinInd = buttoncanvas.create_rectangle(indleftx, indlefty + ind_space, indleftx + ind_width, indlefty + ind_height + ind_space, fill = "dark gray", outline = "dark gray")
nonlinStatus = False
buttoncanvas.create_text(indleftx + ind_width/2 + 2, indlefty + ind_height/2 + ind_space, text = "NONLINEAR MODE", font = 'Helvetica 10 bold', fill = "black")

# from glob import statuses

statuses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def buttonstatus():
    global buttonXstatus
    global buttonYstatus
    global buttonAstatus
    global buttonBstatus
    global teleopStatus
    global nonlinStatus
    buttonAstatus = statuses[4]
    buttonBstatus = statuses[5]
    buttonXstatus = statuses[6]
    buttonYstatus = statuses[7]
    teleopStatus = statuses[8]
    nonlineStatus = statuses[9]

    # print(statuses)

    if buttonAstatus == 1:
        print("buttonA is 1")
        buttoncanvas.itemconfig(Acirc, fill='green')
    if buttonAstatus == 0:
        buttoncanvas.itemconfig(Acirc, fill='dark gray')
    #b
    if buttonBstatus == 1:
        buttoncanvas.itemconfig(Bcirc, fill='green')
    if buttonBstatus == 0:
        buttoncanvas.itemconfig(Bcirc, fill='dark gray')
    #x
    if buttonXstatus == 1:
        buttoncanvas.itemconfig(Xcirc, fill='green')
    if buttonXstatus == 0:
        buttoncanvas.itemconfig(Xcirc, fill='dark gray')
    #y
    if buttonYstatus == 1:
        buttoncanvas.itemconfig(Ycirc, fill='green')
    if buttonYstatus == 0:
        buttoncanvas.itemconfig(Ycirc, fill='dark gray')
    #teleop status
    if teleopStatus == 1:
        buttoncanvas.itemconfig(teleopInd, fill='green')
    if teleopStatus == 0:
        buttoncanvas.itemconfig(teleopInd, fill='dark gray')
    #non
    if nonlinStatus == 1:
        buttoncanvas.itemconfig(nonlinInd, fill='green')
    if nonlinStatus == 0:
        buttoncanvas.itemconfig(nonlinInd, fill='dark gray')

    buttoncanvas.after(20, buttonstatus)

buttonstatus()
#THRUSTER GRAPHICS ------------------------------------------------------------------------------------------------------
thrustercanvas = Canvas(root,height=200,width=250,bg="#fff")

thrustercanvas.grid(row = 10, column = 1, sticky = 'e')


topx = 75 #this is also the center of the top left rectangle
topy = 50
width = 100
height = 120
bottomx = topx + width
bottomy = topy + height

centerx = topx + width/2
centery = topy + height/2


thrustercanvas.create_rectangle(topx, topy, bottomx, bottomy, width = 5, outline = "light gray")

t_height = 24
t_width = 15
center = t_height

#y0 is what changes
#left
#background
thrustercanvas.create_rectangle(centerx - t_width - width/2, centery - t_height, centerx + t_width - width/2, centery + t_height, fill = "dark gray", outline = "dark gray")
#status
t0status = t_height
t0 = thrustercanvas.create_rectangle(centerx - t_width - width/2, centery - t_height + t0status, centerx + t_width - width/2, centery + t_height, fill = "green", outline = "green")

thrustercanvas.create_text(centerx - width/2, centery, text = "0", fill="black", font=('Helvetica 15 bold'))

#right
#background
thrustercanvas.create_rectangle(centerx - t_width + width/2, centery - t_height, centerx + t_width + width/2, centery + t_height, fill = "dark gray", outline = "dark gray")
#status
t1status = center
t1 = thrustercanvas.create_rectangle(centerx - t_width + width/2, centery - t_height + t1status, centerx + t_width + width/2, centery + t_height, fill = "green", outline = "green")

thrustercanvas.create_text(centerx + width/2, centery, text = "1", fill="black", font=('Helvetica 15 bold'))

#top
#background
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height - height/2, centerx + t_width, centery + t_height - height/2, fill = "dark gray", outline = "dark gray")
#status
t2status = center
t2 = thrustercanvas.create_rectangle(centerx - t_width, centery - t_height - height/2 + t2status, centerx + t_width, centery + t_height - height/2, fill = "green", outline = "green")

thrustercanvas.create_text(centerx, centery - height/2, text = "2", fill="black", font=('Helvetica 15 bold'))

#bottom
#background
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2, centerx + t_width, centery + t_height + height/2, fill = "dark gray", outline = "dark gray")
#status
t3status = center
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2, centerx + t_width, centery + t_height + height/2, fill = "dark gray", outline = "dark gray")
t3 = thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2 + t3status, centerx + t_width, centery + t_height + height/2, fill = "green", outline = "green")

thrustercanvas.create_text(centerx, centery + height/2, text = "3", fill="black", font=('Helvetica 15 bold'))

def thrustergraphic():
    global t0status
    global t1status
    global t2status
    global t3status

    #get raw thruster values in pwm and convert to values for the gui
    t0status = (statuses[0] - 1500) * height / 2000
    t1status = (statuses[1] - 1500) * height / 2000
    t2status = (statuses[2] - 1500) * height / 2000
    t3status = (statuses[3] - 1500) * height / 2000

    thrustercanvas.coords(t0, centerx - t_width - width/2, centery - t_height + t0status, centerx + t_width - width/2, centery + t_height)
    thrustercanvas.coords(t1, centerx - t_width + width/2, centery - t_height + t1status, centerx + t_width + width/2, centery + t_height)
    thrustercanvas.coords(t2, centerx - t_width, centery - t_height - height/2 + t2status, centerx + t_width, centery + t_height - height/2)
    thrustercanvas.coords(t3,centerx - t_width, centery - t_height + height/2 + t3status, centerx + t_width, centery + t_height + height/2)
    thrustercanvas.after(20, thrustergraphic)

#QUEUE ------------------------------------------------------------------------------------------------------

def queue(out_queue):
    global output_queue
    output_queue = out_queue
    queuerecieve()

def queuerecieve():
    global statuses
    if output_queue.empty() == False:
        statuses = output_queue.get()
        #print("recieved from queue")
    root.after(10, queuerecieve)

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
    root.update()

if __name__ == "__main__":
    root.mainloop()

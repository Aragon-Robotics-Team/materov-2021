from tkinter import *
from tkinter import ttk
# from tkinter.tkk import Style
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
#cap2 = cv2.VideoCapture(2)

#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1300x1000")
#change to 1000x500

style =  ttk.Style()

style.theme_create( "button-center", parent="alt", settings={
        "TButton": {"configure": {"anchor": "center"}}} )

style.configure('TButton', font = ('Helvetica', 13), width = 25)

#TEST ------------------------------------------------------------------------------------------------------
vcol = 3

def asdf():
    print("hello")

# btn = Button(root, text = "hello", command = asdf)
btn = ttk.Button(root, text = "Testing", command = asdf, style = "TButton")
btn.grid(row = 0, column = vcol + 1, sticky = 'e', pady=(10, 0))

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

from img_proc.photomosaic import resize_image
from img_proc.photomosaic import stitch
import time

startPhotomosaic = False
photomosaicCount = 0

# def beginPhotomosaic():
#     global startPhotomosaic
#     print("Photomosaic begun")
#     print("Click take photomosaic button to take each snapshot")
#     startPhotomosaic = True
#     photomosaicCount = 0
#
# btn = ttk.Button(root, text = "Start Photomosaic", command = beginPhotomosaic)
# btn.grid(row = 1, column = vcol + 1, sticky = 'e')

def takePhotomosaicPhoto():
    global startPhotomosaic
    global photomosaicCount
    # if startPhotomosaic == True:
    if photomosaicCount < len(glob.snapshots):
        ret, frame = cap.read()
        # frame = PiRGBArray(camera)
        cv2.imwrite(glob.snapshots[photomosaicCount], frame)
        resized = resize_image(cv2.imread(glob.snapshots[photomosaicCount]), 0.75, 0.75)
        cv2.imwrite(glob.snapshots[photomosaicCount], resized)
        time.sleep(1)
        print("Snapshot #" + str(photomosaicCount) + " taken")
        #cv2.imshow(glob.snapshots[i], frame)
        time.sleep(1)
        photomosaicCount += 1
    else:
        print("All photomosaic snapshots taken")
        stitch()
        # startPhotomosaic = False
    # else:
    #     print("Photomosaic has not been started yet")

btn = ttk.Button(root, text = "Take Photomosaic Snapshot", command = takePhotomosaicPhoto)
btn.grid(row = 2, column = vcol + 1, sticky = 'e', pady = (25, 0))

def resetPhotomosaic():
    global startPhotomosaic
    global photomosaicCount
    startPhotomosaic = False
    photomosaicCount = 0

btn = ttk.Button(root, text = "Reset Photomosaic Snapshot", command = resetPhotomosaic)
btn.grid(row = 3, column = vcol + 1, sticky = 'e')



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

label = Label(root, text = "(Click to 3 times to take photos and calculate)", font = ('Helvetica', 10))
label.grid(row = 4, column = vcol + 1, sticky = 'e', pady = (25, 0))

btn = ttk.Button(root, text="Measure Fish", command = start_measure_fish)
btn.grid(row = 5 ,column = vcol + 1, sticky = 'e')

def resetMeasureFish():
    print("Measuring Fish Task Reset")
    glob.allFishLengths = [0,0,0]
    glob.countfishCoords = 0
    glob.fishPictureCount = 0

btn = ttk.Button(root, text="Reset Fish Measuring", command = resetMeasureFish)
btn.grid(row = 6, column = vcol + 1, sticky = 'e')

#DRIFT -----------------------------------------------------------------------------------------
from misc.drift import floatLocation
btn = ttk.Button(root, text = "Calculate Float Location", command = floatLocation)
btn.grid(row = 7, column = vcol + 1, sticky = 'e', pady = (25, 0))

#DOCKING ------------------------------------------------------------------
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


btn = ttk.Button(root, text = "Autonomous Docking Calibration", command = docking)
btn.grid(row = 8, column = vcol + 1, sticky = 'e', pady = (25, 0))

def startDocking():
    print("haha this has not been done yet")

btn = ttk.Button(root, text = "Start Autonomous Docking", command = startDocking)
btn.grid(row = 9, column = vcol + 1, sticky = 'e')

#MEASURING THE LENGTH OF THE WRECK ---------------------------------------------------------------------------------------------------------------
def measureWreck():
    print("haha this has not been completed yet")

btn = ttk.Button(root, text = "Measure Wreck", command = measureWreck)
btn.grid(row = 10, column = vcol + 1, sticky = 'e', pady = (25, 0))

#LASERS ---------------------------------------------------------------------------------------------------------------
#
# def lasersOn():
#     print("haha this has not been done yet")
#
# btn = ttk.Button(root, text = "Turn Lasers On", command = lasersOn)
# btn.grid(row = 10, column = vcol + 1, sticky = 'e', pady = (25, 0))
#
# def lasersOff():
#     print("haha this has not been done yet")
#
# btn = ttk.Button(root, text = "Turn Lasers Off", command = lasersOff)
# btn.grid(row = 11, column = vcol + 1, sticky = 'e')

#BUTTON GRAPHICS------------------------------------------------------------------------------------------------------
buttoncanvas = Canvas(root,height=120,width=250,bg="#fff")

buttoncanvas.grid(row = 12, column = vcol + 1, sticky = 'e')

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

statuses = [1500, 1500, 1500, 1500, 0, 0, 0, 0, 0, 0]
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
    print(statuses)

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
thrustercanvas = Canvas(root,height=240,width=250,bg="#fff")

thrustercanvas.grid(row = 13, column = vcol + 1, sticky = 'e')


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
t0status = 0
t0 = thrustercanvas.create_rectangle(centerx - t_width - width/2, centery - t0status, centerx + t_width - width/2, centery + t_height, fill = "green", outline = "green")
#t0 = thrustercanvas.create_rectangle(centerx - t_width - width/2, centery - t_height - t0status, centerx + t_width - width/2, centery + t_height, fill = "green", outline = "green")

thrustercanvas.create_text(centerx - width/2, centery, text = "0", fill="black", font=('Helvetica 15 bold'))

#right
#background
thrustercanvas.create_rectangle(centerx - t_width + width/2, centery - t_height, centerx + t_width + width/2, centery + t_height, fill = "dark gray", outline = "dark gray")
#status
t1status = 0
t1 = thrustercanvas.create_rectangle(centerx - t_width + width/2, centery - t1status, centerx + t_width + width/2, centery + t_height, fill = "green", outline = "green")

thrustercanvas.create_text(centerx + width/2, centery, text = "1", fill="black", font=('Helvetica 15 bold'))

#top
#background
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height - height/2, centerx + t_width, centery + t_height - height/2, fill = "dark gray", outline = "dark gray")
#status
t2status = 0
t2 = thrustercanvas.create_rectangle(centerx - t_width, centery - height/2 - t2status, centerx + t_width, centery + t_height - height/2, fill = "green", outline = "green")

thrustercanvas.create_text(centerx, centery - height/2, text = "2", fill="black", font=('Helvetica 15 bold'))

#bottom
#background
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2, centerx + t_width, centery + t_height + height/2, fill = "dark gray", outline = "dark gray")
#status
t3status = 0
thrustercanvas.create_rectangle(centerx - t_width, centery - t_height + height/2, centerx + t_width, centery + t_height + height/2, fill = "dark gray", outline = "dark gray")
t3 = thrustercanvas.create_rectangle(centerx - t_width, centery  + height/2 - t3status, centerx + t_width, centery + t_height + height/2, fill = "green", outline = "green")

thrustercanvas.create_text(centerx, centery + height/2, text = "3", fill="black", font=('Helvetica 15 bold'))


thrustercanvas.create_line(10, 220, 240, 220, fill = "black", width = 5)


def thrustergraphic():
    global t0status
    global t1status
    global t2status
    global t3status

    # print(statuses)
    #get raw thruster values in pwm and convert to values for the gui
    t0status = (statuses[0] - 1500) * height / 2000
    t1status = (statuses[1] - 1500) * height / 2000
    t2status = (statuses[2] - 1500) * height / 2000
    t3status = (statuses[3] - 1500) * height / 2000
    # print(str(t0status) + ", " + str(t1status) + ", " + str(t2status) + ", " + str(t3status))


    thrustercanvas.coords(t0, centerx - t_width - width/2, centery - t0status, centerx + t_width - width/2, centery + t_height)
    thrustercanvas.coords(t1, centerx - t_width + width/2, centery - t1status, centerx + t_width + width/2, centery + t_height)
    thrustercanvas.coords(t2, centerx - t_width, centery - height/2 - t2status, centerx + t_width, centery + t_height - height/2)
    thrustercanvas.coords(t3, centerx - t_width, centery  + height/2 - t3status, centerx + t_width, centery + t_height + height/2)
    thrustercanvas.after(20, thrustergraphic)

thrustergraphic()

#QUEUE ------------------------------------------------------------------------------------------------------

def queue(in_queue, out_queue):
    global output_queue
    global input_queue
    input_queue = out_queue
    output_queue = in_queue
    queuerecieve()

def queuerecieve():
    global statuses
    if input_queue.empty() == False:
        statuses = input_queue.get()
        #print("recieved from queue")
    root.after(10, queuerecieve)
#
# def endthrusterprocess():
#     output_queue.put(False)
#     print("Sent through process")
#
#
# btn = Button(root, text = "End Thruster Process", command = endthrusterprocess)
# btn.grid(row = 9, column = vcol + 1, sticky = 'e')
#

#TIMER ------------------------------------------------------------------------------------------------------
timercanvas = Canvas(root, height = 140, width = 250, background = "#fff")
timercanvas.grid(row = 14, column = vcol + 1, sticky = 'e')

minute=StringVar()
second=StringVar()
hours=StringVar()

sec = StringVar()
mins= StringVar()
hrs= StringVar()

# #  # #
spacing = 25
totalEntryLength = spacing * 3
startingx = (250 - totalEntryLength)/2
print(startingx)


Entry(timercanvas, textvariable = sec, width = 2, font = 'arial 12').place(x=startingx, y=10) # Seconds
Entry(timercanvas, textvariable = mins, width = 2, font = 'arial 12').place(x=startingx + spacing, y=10) # Mins
Entry(timercanvas, textvariable = hrs, width = 2, font = 'arial 12').place(x=startingx + spacing * 2, y=10) # Hours

# #  # #

minute.set('00')
second.set('00')
hours.set('00')

sec.set('00')
mins.set('00')
hrs.set('00')
times = 0

# #  # #

def countdown():
    global times
    print("hello") #testing, working but code not working
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())


    if times > 0:
        minute,second = (times // 60 , times % 60)
        timercanvas.after(1000, countdown)

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

#set the time
#instead of times > 0, do if time > 0, and have an after function at the end of the if statement


#time = 2
#is time > 0?
    #change the timer graphic
    #time--
    #timercanvas.after(1000, countdown)
#is time == 0?
    #reset everything

Button(timercanvas, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold', width = 15).place(x=80, y=50)


def stop():
    global times
    minute.set('00')
    second.set('00')
    hours.set('00')
    sec.set('00')
    mins.set('00')
    hrs.set('00')
    times = 0
    #root.destroy()
    #python = sys.executable
    #os.execl(python, python, * sys.argv)



Button(timercanvas, text='STOP', bd ='5', command = stop, bg = 'white', font = 'arial 10 bold', width = 15).place(x=80.5, y=75)

timercanvas.create_line(10, 130, 240, 130, fill = "black", width = 5)

#VIDEO FEED ------------------------------------------------------------------------------------------------------
#pretty much the same lag as when the video feed is in the loop
from PIL import Image, ImageTk

# Create a Label to capture the Video frames
label = Label(root, height = 800, width = 1000)
label.grid(row = 1, column = 0, rowspan = 20, columnspan = vcol, sticky = 'n')

camera = 0 #specifies the camera object to use

# Define function to show frame
def show_frames():
    #To Change the cameras
    # if camera = 0:
    #     cv2image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    # elif camera = 1:
    #     cv2image = cv2.cvtColor(cap1.read()[1],cv2.COLOR_BGR2RGB)
    # elif camera = 2:
    #     cv2image = cv2.cvtColor(cap2.read()[1],cv2.COLOR_BGR2RGB)

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

def cam0():
    global camera
    camera = 0

ttk.Button(root, text = "CAMERA 0", command = cam0).grid(row = 0,column = 0)

def cam1():
    global camera
    camera = 1

ttk.Button(root, text = "CAMERA 1", command = cam1).grid(row = 0, column = 1)

def cam2():
    global camera
    camera = 2

ttk.Button(root, text = "CAMERA 2", command = cam2).grid(row = 0, column = 2)

#EMERGENCY HALT ------------------------------------------------------------------------------------------------------------
def enableBot():
    print ("haha this has not been done yet")

btn = Button(root, text = "Enable Bot", command = enableBot, width = 30, height = 3, fg = 'red', bg = 'dark gray')
btn.grid(row = 14, column = 0, sticky = 'w', pady = (75, 0), padx = (50, 0))

def disableBot():
    print("haha this has not been done yet")
#
# btn = Button(root, text = "EMERGENCY HALT", command = emergencyHalt, height = 25, width = 200, fg = 'red')
btn = Button(root, text = "Disable Bot (Emergency Halt)", command = disableBot, width = 30, height = 3, fg = 'red')
btn.grid(row = 14, column = 1, sticky = 'w', pady = (75, 0), padx = (50, 0))


def updateGUI():
    root.update()

if __name__ == "__main__":
    root.mainloop()

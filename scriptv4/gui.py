from tkinter import *
import glob
from img_proc.measure_fishes import measureFishie
import cv2
import multiprocessing

#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1300x750")
hello = "hello"

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

def start_measure_fish():
    measureFishie()

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

#VIDEO FEED ------------------------------------------------------------------------------------------------------
#pretty much the same lag as when the video feed is in the loop
from PIL import Image, ImageTk

# Create a Label to capture the Video frames
label = Label(root, height = 700, width = 1000)
label.grid(row = 0, column = 0, rowspan = 30)
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

#Thruster -----------------------------------------------------------------------------------------------------------

from nav.controller import joy_init
from nav.controller import joytests
import psutil

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

auto_queue = multiprocessing.Queue()

def startThrusterProcess():
    global auto_queue
    proc_running = False
    if proc_running == False:
        print("starting thruster process")
        multiprocessing.set_start_method('spawn')
        thruster_proc = multiprocessing.Process(target = thrusterProcess)
        auto_queue = multiprocessing.Queue()
        proc_running = True
        thruster_proc.start()
    elif proc_running == True:
        thruster_proc.terminate()
        print("Thruster Process Terminated")


def thrusterProcess():
    global auto_queue
    joy_init()
    print("Starting joy tests")
    teleop = True
    autonomous = True
    automode = ""
    while True:
        if teleop == True:
            joytests()
        if autonomous == True:
            print(automode)
        if auto_queue.size() > 0:
            automode = auto_queue.get()
            if automode == "Start Autonomous":
                teleop = False
                autnomous = True
            if automode == "End Autonomous":
                teleop = True
                autonomous = False


btn = Button(root, text = "Start thruster", command = startThrusterProcess)
btn.grid(row = 6, column = 1, sticky = 'e')
#
# btn = Button(root, text = "Start Autonomous", command = auto_queue.put("Start Autonomous"))
# btn.grid(row = 7, column = 1, sticky = 'e')
#
# btn = Button(root, text = "End Autonomous", command = auto_queue.put("End Autonomous"))
# btn.grid(row = 8, column = 1, sticky = 'e')

def end_prog():
    startThrusterProcess()
    root.destroy()

btn = Button(root, text = "Close Window and End Processes", command = end_prog)
btn.grid(row = 9, column = 1, sticky = 'e')



def updateGUI():
    root.update()

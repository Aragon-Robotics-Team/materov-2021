from tkinter import *
import glob
from img_proc.measure_fishes import measureFishie
import cv2

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

#VIDEO FEED & BUTTONS ------------------------------------------------------------------------------------------------------
#pretty much the same lag as when the video feed is in the loop
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
   label.configure(image=Imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)


########################
import tkinter as tk
import time
import tkinter.font as font
import cv2
from tkinter import messagebox, RIGHT, LEFT, StringVar
########################

text = tk.StringVar()
text.set("Test")
label = tk.Label(root, textvariable=text).place(x=500, y=450)

def changeText():
    text.set("dwliouhwihdwhiwdhiodwhidwohiwdhiodhowohidwdhowhodhodwwahiihdwphpdpodwdpwdpodpowdopupuopoudwupowdopudopdpojwdjpowdjpowdjopwdjodwpjdwjowpdjwdpwdjopjodpodjpdjopwdjopwdjopwdjopdowjwdjowdojwdjwdojpwdjopdwjop")

button = tk.Button(root, text="Click to change text below",command=changeText).place(x=500, y=500)

########################

minute=StringVar()
second=StringVar()
hours=StringVar()

sec = StringVar()
mins= StringVar()
hrs= StringVar()

# #  # #

tk.Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=200, y=155) # Seconds
tk.Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=175, y=155) # Mins
tk.Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=150, y=155) # Hours

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


tk.Button(root, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold').place(x=150, y=210)
# #  # #

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



tk.Button(root, text='STOP', bd ='5', command = stop, bg = 'white', font = 'arial 10 bold').place(x=150, y=250)
##############################################################

def button1():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(root, text ="Hello", command = button1, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 20).place(x=700, y=100)

def button2():
   tk.messagebox.showinfo( "Hello Python2", "Hello World2")

Bu = tk.Button(root, text ="Hello2", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 20).place(x=700, y=150)

def button3():
   tk.messagebox.showinfo( "Hello Python3", "Hello World3")

Bu = tk.Button(root, text ="Hello3", command = button3, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 20).place(x=700, y=200)

def button4():
   tk.messagebox.showinfo( "Hello Python4", "Hello World4")

Bu = tk.Button(root, text ="Hello4", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 20).place(x=700, y=250)

def button5():
   tk.messagebox.showinfo( "Hello Python5", "Hello World5")

Bu = tk.Button(root, text ="Hello5", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 20).place(x=700, y=300)

def button6():
   tk.messagebox.showinfo( "Hello Python6", "Hello World6")

Bu = tk.Button(root, text ="Hello6", command = button2, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 10).place(x=700, y=350)

def task1():
    print("hi")

Bu = tk.Button(root, text ="Hello6", command = task1, font = 'Roboto', borderwidth = 0, bg = 'dark gray', height = 1,width = 10).place(x=700, y=350)

show_frames()
root.mainloop()

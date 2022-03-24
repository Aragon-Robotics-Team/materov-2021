# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2

# Create an instance of TKinter Window or frame
win = Tk()

# Set the size of the window
win.geometry("1400x2000")

# Create a Label to capture the Video frames
label = Label(win, height = 700, width = 700)
label.place(x = 700,y = 0)
cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

camera = 0

# Define function to show frame
def show_frames():
    if camera == 0:
        cv2image = cv2.cvtColor(cap0.read()[1],cv2.COLOR_BGR2RGB)
    if camera == 1:
        cv2image = cv2.cvtColor(cap1.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)

show_frames()

def cam0():
    camera = 0

def cam1():
    camera = 1

button = Button(win, text="Camera 0",command=cam0).place(x=10, y=10)
button = Button(win, text="Camera 1",command=cam1).place(x = 10, y = 30)

while True:
    win.update()

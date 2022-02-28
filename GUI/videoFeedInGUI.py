#Import the required library
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import threading
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("750x400")
#Create a canvas and add the image into it
canvas= Canvas(win, width=650, height= 350)
canvas.pack()
#Create a button to update the canvas image


videoCaptureObject = cv2.VideoCapture(0)
ret, frame = videoCaptureObject.read()
img1 = cv2.imwrite("/Users/valeriefan/Desktop/videoCapture.jpg", frame)

#Open an Image in a Variable
#Image.open("bll.jpg")
#img1= PhotoImage(file="/Users/valeriefan/Desktop/videoCapture.jpg")
img1 = PhotoImage(Image.open("/Users/valeriefan/Desktop/videoCapture.jpg"))
img = "/Users/valeriefan/Desktop/videoCapture.jpg"
#Add image to the canvas

#ret, frame = #read camera what else we need to do xd smiley face i like men
#cv2.imwrite(img1, frame)

#image_container = canvas.create_image(0,0, anchor="nw",image=img1)
image_container = canvas.create_image(10,10, anchor="nw",image=img1)
#Define function to update the image

def videoCapture():
    while True:
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("/Users/valeriefan/Desktop/videoCapture.jpg", frame)
        img1= PhotoImage(file="/Users/valeriefan/Desktop/videoCapture.jpg")
        canvas.itemconfig(image_container,image=img1)

thread = threading.Thread(target=videoCapture)
thread.daemon = 1
thread.start()

while True:
    win.update()

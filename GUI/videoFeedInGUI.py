
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

# videoCaptureObject = cv2.VideoCapture(0)
# ret, frame = videoCaptureObject.read()
img = "/Users/valeriefan/Desktop/lines2.jpg"
#cv2.imwrite(img, frame)

#Open an Image in a Variable
#Image.open("bll.jpg")
#img1= PhotoImage(file="/Users/valeriefan/Desktop/videoCapture.jpg")
# filename = PhotoImage(file = "sunshine.gif")
# image = canvas.create_image(50, 50, anchor=NE, image=filename)
filename = PhotoImage(Image.open(img))
image_container = canvas.create_image(0, 0, anchor = NE, image = filename)

#ret, frame = #read camera what else we need to do xd smiley face i like men
#cv2.imwrite(img1, frame)

# image_container = canvas.create_image(0,0, anchor=NW, image=img1)
#
# #Define function to update the image
# videoCaptureObject = cv2.VideoCapture(0)
# #image = cv2.imread("C:\Users\mz141\Downloads\VideoInput.png")
#
# def videoCapture():
#     global img1
#     while True:
#         ret, frame = videoCaptureObject.read()
#         cv2.imwrite("/Users/valeriefan/Desktop/VideoInput.jpg", frame)
#         img1= PhotoImage(file="/Users/valeriefan/Desktop/VideoInput.jpg")
#         canvas.itemconfig(image_container,image=img1)
#
while True:
#     #videoCapture()
    win.update()
# win.mainloop()

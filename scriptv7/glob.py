#INCLUDE ANY VARIABLES THAT ARE USED IN MULTIPLE FILES HERE

#VIDEO
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
# videoCaptureObject = cv2.VideoCapture(0)
# ret, frame = videoCaptureObject.read()

camera = PiCamera()
frame = PiRGBArray(camera)
#Photomosaic ------------------------------------------------------------------------------------------------------
photomosaicVideo = False #used in main.py and gui.py to determine whether or not the program should use the photomosaic video feed
photomosaicCount = 0 #used in video.py and gui.py to keep track of the number of snapshots that are taken

#Replace "/home/pi/Pictures/Photomosaic/" with the file path you want the files to go
#no need to create the file, the program will create it for you if it does not already exist
snapshots = ["/home/pi/Pictures/Photomosaic/center.png",
    "/home/pi/Pictures/Photomosaic/top.png",
    "/home/pi/Pictures/Photomosaic/bottom.png",
    "/home/pi/Pictures/Photomosaic/left.png",
    "/home/pi/Pictures/Photomosaic/right.png"]
    #file paths for photomosaic snapshots, used in photomosaic.py and video.py

blankFile = "/home/pi/Pictures/Photomosaic/blank.png"
middleTileFile = "/home/pi/Pictures/Photomosaic/middleTile.png"
topTileFile = "/home/pi/Pictures/Photomosaic/topTile.png"
bottomTileFile = "/home/pi/Pictures/Photomosaic/bottomTile.png"
photomosaicFile = "/home/pi/Pictures/Photomosaic/photomosaic.png"

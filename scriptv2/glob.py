
#INCLUDE ANY VARIABLES THAT ARE USED IN MULTIPLE FILES HERE

#VIDEO
import cv2
videoCaptureObject = cv2.VideoCapture(0)

#Photomosaic ------------------------------------------------------------------------------------------------------
photomosaicVideo = False #used in main.py and gui.py to determine whether or not the program should use the photomosaic video feed
photomosaicCount = 0 #used in video.py and gui.py to keep track of the number of snapshots that are taken
snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]
    #file paths for photomosaic snapshots, used in photomosaic.py and video.py

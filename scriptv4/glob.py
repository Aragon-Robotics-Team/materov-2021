#INCLUDE ANY VARIABLES THAT ARE USED IN MULTIPLE FILES HERE

#VIDEO
import cv2
videoCaptureObject = cv2.VideoCapture(0)
ret, frame = videoCaptureObject.read()

#Photomosaic ------------------------------------------------------------------------------------------------------
photomosaicVideo = False #used in teleop.py and gui.py to determine whether or not the program should use the photomosaic video feed
photomosaicCount = 0 #used in video.py and gui.py to keep track of the number of snapshots that are taken

#Replace "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/" with the file path you want the files to go
#no need to create the file, the program will create it for you if it does not already exist
snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]
    #file paths for photomosaic snapshots, used in photomosaic.py and video.py

blankFile = "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png"
middleTileFile = "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/middleTile.png"
topTileFile = "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topTile.png"
bottomTileFile = "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomTile.png"
photomosaicFile = "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/photomosaic.png"

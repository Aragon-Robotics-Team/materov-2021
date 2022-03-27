import numpy as np
import threading
import cv2
import imutils
import keyboard
import math

from time import sleep
photomosaicVideo = False
photomosaicStart = False

def photomosaicThreading():
    global photomosaicStart
    photomosaicStart = True
    threading.Thread(target=photomosaic).start()

center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_h), int(img.shape[0]*scale_w)))

def cropping(image):
    image = cv2.imread(image)
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 300, cv2.THRESH_BINARY_INV)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    output = image.copy()
    cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    (x, y, w, h) = cv2.boundingRect(c)
    text = "original, num_pts = {}".format(len(c))
    cv2.putText(output, text, (x,y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    #Crop the image based on the points of the bounding box, show the cropped image
    cropped = image[y:y+h, x:x+w]

photomosaicCount = 0
photomosaicStart = False
def photomosaic():
    print("Starting photomosaic")
    print("Type s 4 times to take snapshots, and one more time to construct the photomosaic")
    global photomosaicCount
    photomosaicCount = 0
    global photomosaicVideo
    photomosaicVideo = True
    global photomosaicStart
    photomosaicStart = False
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True

    while photomosaicStart == False:
        sleep(0.1)
    if photomosaicStart == True:
        print("Starting Photomosaic Process")
        #---------rereading the original images from the snapshots-----------
        center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
        top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
        bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
        left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
        right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
        blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

        # #--------calculate the size of the blank images to make up for the size difference in the tiles------------
        print("Resizing Images")
        topLeftHeightRatio = cv2.imread(snapshots[1]).shape[1]/blank.shape[1]
        topLeftWidthRatio = cv2.imread(snapshots[3]).shape[0]/blank.shape[0]
        topLeftBlank = resize_image(blank, topLeftWidthRatio, topLeftHeightRatio)
        bottomLeftHeightRatio = cv2.imread(snapshots[2]).shape[1]/blank.shape[1]
        bottomLeftWidthRatio = cv2.imread(snapshots[3]).shape[0]/blank.shape[0]
        bottomLeftBlank = resize_image(blank, bottomLeftWidthRatio, bottomLeftHeightRatio)
        topRightHeightRatio = cv2.imread(snapshots[1]).shape[1]/blank.shape[1]
        topRightWidthRatio = cv2.imread(snapshots[4]).shape[0]/blank.shape[0]
        topRightBlank = resize_image(blank, topRightWidthRatio, topRightHeightRatio)
        bottomRightHeightRatio = cv2.imread(snapshots[2]).shape[1]/blank.shape[1]
        bottomRightWidthRatio = cv2.imread(snapshots[4]).shape[0]/blank.shape[0]
        bottomRightBlank = resize_image(blank, bottomRightWidthRatio, bottomRightHeightRatio)

        #----------------------concat middle tile------------------------
        print("Concat Middle Tile")
        middleTileLeft = cv2.hconcat([cv2.imread(snapshots[3]), cv2.imread(snapshots[0])])
        middleTile = cv2.hconcat([middleTileLeft, cv2.imread(snapshots[4])])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/middleTile.png", middleTile)

        #----------concat top tile-----------------
        print("Concat Top Tile")
        topTileLeft = cv2.hconcat([topLeftBlank, cv2.imread(snapshots[1])])
        topTile = cv2.hconcat([topTileLeft, topRightBlank])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topTile.png", topTile)

        #-------------concat bottom tile--------------
        print("Concat Bottom Tile")
        bottomTileLeft = cv2.hconcat([bottomLeftBlank, cv2.imread(snapshots[4])])
        bottomTile = cv2.hconcat([bottomTileLeft, bottomRightBlank])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomTile.png", bottomTile)

        #---------stitch together all the tiles-----------
        print("Stitch together all the tiles")
        topSection = cv2.vconcat([topTile, middleTile])
        photomosaic = cv2.vconcat([topSection, bottomTile])
        cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/photomosaic.png", photomosaic)
        print("Sending Photomosaic Image to main thread")
        q.put(photomosaic)
        #cv2.imshow("PHOTOMOSAIC", photomosaic)
        cv2.waitKey(0)

        #definitely have to add this back in later
        #global photomosaicStart
        photomosaicStart = False

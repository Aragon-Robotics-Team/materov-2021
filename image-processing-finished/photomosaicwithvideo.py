#sudo python3 /Users/valeriefan/github/test-materov-2021/image-processing-finished/photomosaicwithvideo.py

import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time

i = 0

center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")

centerResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/centerResize.png", blank)
topResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topResize.png", topResize)
bottomResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomResize.png", bottomResize)
leftResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/leftResize.png", leftResize)
rightResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/rightResize.png", rightResize)
blankTopResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankTopResize.png", blankTopResize)
blankBottomResize = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankBottomResize.png", blankBottomResize)

resizedimages = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/centerResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/leftResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/rightResize.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankResize.png"
]

resizeimage = [
    centerResize,
    topResize,
    bottomResize,
    leftResize,
    rightResize]


def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

#---------crop and resize the image to a height of 250 pixels-----------
def cropping(image):
    image = cv2.imread(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 300, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Thresh", thresh)
    cv2.waitKey(0)

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
    file = snapshots[i]
    cv2.imwrite(file, cropped)
    #cv2.imshow("Cropped Image", cropped)
    #cv2.waitKey(0)

    ratio = 250/cropped.shape[0]
    resizeimage[i] = resize_image(cropped, ratio, ratio)
    cv2.imwrite(resizedimages[i], resizeimage[i])
    #cv2.imshow("Resized Cropped", resizeimage[i])
    #cv2.waitKey(0)

    cv2.destroyAllWindows

videoCaptureObject = cv2.VideoCapture(0)
result = True

snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]

#---------capture images and save them to the files-----------
videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
result = True
i = 0
while result:
    ret, frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video", frame)
    # deletes every frame as the next one comes on, closes all windows when q is pressed
    if cv2.waitKey(1) == ord('q'):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    # when s is pressed
    if keyboard.is_pressed('s'):
        # and the index is less than the length of the snapshot list
        if i < len(snapshots):
            # take as snapshot, save it, show it
            cv2.imwrite(snapshots[i], frame)
            cv2.imshow(snapshots[i], frame)
            cropping(snapshots[i])
            resizeimage[i] = cv2.imread(resizedimages[i])
            time.sleep(1)
            i += 1
        else:
            result = False

#---------rereading the original images from the snapshots-----------
center = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png")
top = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png")
bottom = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png")
left = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png")
right = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png")
blank = cv2.imread("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blank.png")


#---------saving the resized versions of the images to variables-----------
centerResize = cv2.imread(resizedimages[0])
#cv2.imshow("centerResize", centerResize)
#cv2.waitKey(0)

topResize = cv2.imread(resizedimages[1])
#cv2.imshow("leftResize", leftResize)
#cv2.waitKey(0)

bottomResize = cv2.imread(resizedimages[2])
#cv2.imshow("rightResize", rightResize)
#cv2.waitKey(0)

leftResize = cv2.imread(resizedimages[3])
#cv2.imshow("topResize", topResize)
#cv2.waitKey(0)

rightResize = cv2.imread(resizedimages[4])
#cv2.imshow("bottomResize", bottomResize)
#cv2.waitKey(0)

#----------------------concat middle tile------------------------
middleTileLeft = cv2.hconcat([leftResize, centerResize])
cv2.imshow("Middle Tile Left", middleTileLeft)
cv2.waitKey(0)
middleTile = cv2.hconcat([middleTileLeft, rightResize])
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/middleTile.png", middleTile)
cv2.imshow("MiddleTile", middleTile)
cv2.waitKey(0)
print("Middle Tile Length:")
print(middleTile.shape[1])

#--------calculate the size of the blank images to make up for the size difference in the tiles------------
heightratio = 250/blank.shape[0]
topwidth = (middleTile.shape[1] - topResize.shape[1])/2
#print(topResize.shape[1])
print("Top Image Length:")
print(topwidth)
topwidthratio = topwidth/blank.shape[1]
bottomwidth = (middleTile.shape[1] - bottomResize.shape[1])/2
#print(bottomResize.shape[1])
print("Bottom Image Length:")
print(bottomwidth)
bottomwidthratio = bottomwidth/blank.shape[1]
blankTopResize = resize_image(blank, topwidthratio, heightratio)
print("Blank Top Tile Length")
print(blankTopResize.shape[1])
blankBottomResize = resize_image(blank, bottomwidthratio, heightratio)
print("Blank Bottom Tile Length:")
print(blankBottomResize.shape[1])

#----------concat top tile-----------------
topTileLeft = cv2.hconcat([blankTopResize, topResize])
topTile = cv2.hconcat([topTileLeft, blankTopResize])
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/topTile.png", topTile)
cv2.imshow("Top Tile", topTile)
cv2.waitKey(0)
print("Top Tile Length:")
print(topTile.shape[1])

#-------------concat bottom tile--------------
bottomTileLeft = cv2.hconcat([blankBottomResize, bottomResize])
bottomTile = cv2.hconcat([bottomTileLeft, blankBottomResize])
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottomTile.png", bottomTile)
cv2.imshow("Bottom Tile", bottomTile)
cv2.waitKey(0)
print("Bottom Tile Length")
print(bottomTile.shape[1])


#------------resize again if it doesn't work for some reason -.- -------------
if bottomTile.shape[1] != middleTile.shape[1]:
    bottomTile = resize_image(bottomTile, middleTile.shape[1]/bottomTile.shape[1], 1)
    print("resizing bottomTile")
    print(bottomTile.shape[1])

if topTile.shape[1] != middleTile.shape[1]:
    topTile = resize_image(topTile, middleTile.shape[1]/topTile.shape[1], 1)
    print("resizing top tile")
    print(topTile.shape[1])


#---------stitch together all the tiles-----------
topSection = cv2.vconcat([topTile, middleTile])
photomosaic = cv2.vconcat([topSection, bottomTile])
cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/photomosaic.png", photomosaic)
cv2.imshow("PHOTOMOSAIC", photomosaic)
cv2.waitKey(0)

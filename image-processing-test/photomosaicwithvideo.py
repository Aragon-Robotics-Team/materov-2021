#sudo python3 /Users/valeriefan/github/test-materov-2021/image-processing-test/photomosaicwithvideo.py

import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time


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

def resize_blank(image):
    heightratio = 250/image.shape[0]
    widthratio = 249/image.shape[1]
    blankResize = resize_image(image, widthratio, heightratio)
    cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/blankResize.png", blankResize)

def resize_tile(image):
    ratio = 750/image.shape[1]
    resizeimage[i] = resize_image(image, ratio, ratio)

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
    #image = cropped
    file = snapshots[i]
    cv2.imwrite(file, cropped)
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)

    ratio = 250/cropped.shape[0]
    resizeimage[i] = resize_image(cropped, ratio, ratio)
    cv2.imwrite(resizedimages[i], resizeimage[i])
    cv2.imshow("Resized Cropped", resizeimage[i])
    cv2.waitKey(0)

    cv2.destroyAllWindows

videoCaptureObject = cv2.VideoCapture(0)
result = True

snapshots = ["/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/center.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/top.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/bottom.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/left.png",
    "/Users/valeriefan/Desktop/MATE-ROV-IP/Photomosaic/right.png"]

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

#crop the center
#cropping(center)
centerResize = cv2.imread(resizedimages[i])
cv2.imshow("centerResize", centerResize)
cv2.waitKey(0)

i = 1
#cropping(left)
leftResize = cv2.imread(resizedimages[i])
#cv2.imshow("leftResize", leftResize)
#cv2.waitKey(0)

i = 2
#cropping(right)
rightResize = cv2.imread(resizedimages[i])
#cv2.imshow("rightResize", rightResize)
#cv2.waitKey(0)

i = 3
#cropping(top)
topResize = cv2.imread(resizedimages[i])

#cv2.imshow("topResize", topResize)
#cv2.waitKey(0)

i = 4
#cropping(bottom)
bottomResize = cv2.imread(resizedimages[i])

#cv2.imshow("bottomResize", bottomResize)
#cv2.waitKey(0)

middleTileLeft = cv2.hconcat([leftResize, centerResize])
cv2.imshow("Middle Tile Left", middleTileLeft)
cv2.waitKey(0)
middleTile = cv2.hconcat([middleTileLeft, rightResize])
cv2.imshow("MiddleTile", middleTile)
cv2.waitKey(0)
#resize_tile(middleTile)
print(middleTile.shape[1])

heightratio = 250/blank.shape[0]
topwidth = (middleTile.shape[1] - topResize.shape[1])/2
print("Top Width: " + topwidth)
topwidthratio = topwidth/blank.shape[1]
bottomwidth = (middleTile.shape[1] - bottomResize.shape[1])/2
print("Bottom Width: " + bottomwidth)
bottomwidthratio = bottomwidth/blank.shape[1]
blankTopResize = resize_image(blank, topwidthratio, heightratio)
blankTopResize = resize_image(blank, bottomwidthratio, heightratio)

topTileLeft = cv2.hconcat([blankTopResize, topResize])
topTile = cv2.hconcat([topTileLeft, blankTopResize])
cv2.imshow("Top Tile", topTile)
cv2.waitKey(0)
#resize_tile(topTile)
print(topTile.shape[1])

bottomTileLeft = cv2.hconcat([blankBottomResize, bottomResize])
bottomTile = cv2.hconcat([bottomTileLeft, blankBottomResize])
cv2.imshow("Bottom Tile", bottomTile)
cv2.waitKey(0)
#resize_tile(bottomTile)
print(bottomTile.shape[1])

topSection = cv2.vconcat([topTile, middleTile])
photomosaic = cv2.vconcat([topSection, bottomTile])
cv2.imshow("PHOTOMOSAIC", photomosaic)
cv2.waitKey(0)

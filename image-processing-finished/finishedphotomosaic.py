import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time

center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\center.png")
top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
bottom = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

snapshots = ["C:\\Users\\alexa\\Desktop\\photomosaic\\center.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\top.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\left.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\right.png"]

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_h), int(img.shape[0]*scale_w)))

#---------crop and resize the image to a height of 250 pixels-----------
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

def photomosaic():
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
                cv2.imwrite(snapshots[i], frame)
                cropping(snapshots[i])
                center_height = cv2.imread(snapshots[0]).shape[0]
                center_width = cv2.imread(snapshots[0]).shape[1]
                width_ratio = center_width/cv2.imread(snapshots[i]).shape[1]
                height_ratio = center_height/cv2.imread(snapshots[i]).shape[0]
                if i < 3:
                    resized = resize_image(cv2.imread(snapshots[i]), width_ratio, width_ratio)
                else:
                    resized = resize_image(cv2.imread(snapshots[i]), height_ratio, height_ratio)

                cv2.imwrite(snapshots[i], resized)
                cv2.imshow(snapshots[i], frame)
                time.sleep(1)
                i += 1
            else:
                result = False

    #---------rereading the original images from the snapshots-----------
    center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\center.png")
    top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
    bottom = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
    left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
    right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
    blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

    # #--------calculate the size of the blank images to make up for the size difference in the tiles------------
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
    middleTileLeft = cv2.hconcat([cv2.imread(snapshots[3]), cv2.imread(snapshots[0])])
    middleTile = cv2.hconcat([middleTileLeft, cv2.imread(snapshots[4])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\middleTile.png", middleTile)

    #----------concat top tile-----------------
    topTileLeft = cv2.hconcat([topLeftBlank, cv2.imread(snapshots[1])])
    topTile = cv2.hconcat([topTileLeft, topRightBlank])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topTile.png", topTile)

    #-------------concat bottom tile--------------
    bottomTileLeft = cv2.hconcat([bottomLeftBlank, cv2.imread(snapshots[4])])
    bottomTile = cv2.hconcat([bottomTileLeft, bottomRightBlank])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomTile.png", bottomTile)

    #---------stitch together all the tiles-----------
    topSection = cv2.vconcat([topTile, middleTile])
    photomosaic = cv2.vconcat([topSection, bottomTile])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\photomosaic.png", photomosaic)
    cv2.imshow("PHOTOMOSAIC", photomosaic)
    cv2.waitKey(0)

photomosaic()

import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time
import glob

top1 = cv2.imread(glob.snapshots[0])
top2 = cv2.imread(glob.snapshots[1])
top3 = cv2.imread(glob.snapshots[2])
top4 = cv2.imread(glob.snapshots[3])
bottom1 = cv2.imread(glob.snapshots[4])
bottom2 = cv2.imread(glob.snapshots[5])
bottom3 = cv2.imread(glob.snapshots[6])
bottom4 = cv2.imread(glob.snapshots[7])

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_h), int(img.shape[0]*scale_w)))

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
            if i < len(glob.snapshots):
                cv2.imwrite(glob.snapshots[i], frame)
                resized = resize_image(cv2.imread(glob.snapshots[i]), 0.75, 0.75)
                cv2.imwrite(glob.snapshots[i], resized)
                time.sleep(1)
                i += 1
            else:
                result = False

    #----------------------concat top two------------------------
    topLeft = cv2.hconcat([cv2.imread(glob.snapshots[0]), cv2.imread(glob.snapshots[1])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topLeft.png", topLeft)

    #----------concat second top two-----------------
    topRight = cv2.hconcat([cv2.imread(glob.snapshots[2]), cv2.imread(glob.snapshots[3])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topRight.png", topRight)

    topTile = cv2.hconcat([topLeft, topRight])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topTile.png", topTile)

    #-------------concat bottom two--------------
    bottomLeft = cv2.hconcat([cv2.imread(glob.snapshots[4]), cv2.imread(glob.snapshots[5])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomLeft.png", bottomLeft)

    #------------concat second bottom two----------
    bottomRight = cv2.hconcat([cv2.imread(glob.snapshots[6]), cv2.imread(glob.snapshots[7])])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomLeft.png", bottomLeft)

    bottomTile = cv2.hconcat([bottomLeft, bottomRight])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomTile.png", bottomTile)w

    #---------stitch together all the tiles-----------
    photomosaic = cv2.vconcat([topTile, bottomTile])
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\photomosaic.png", photomosaic)
    cv2.imshow("PHOTOMOSAIC", photomosaic)
    cv2.waitKey(0)

photomosaic()

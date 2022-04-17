import numpy as np
import argparse
import imutils
import cv2
# import keyboard
import time
import glob
import math

videoCaptureObject = cv2.VideoCapture(0)#, cv2.CAP_DSHOW)

dockImg = ""

def dockpic(videoImg):
    global laserCoords
    global docklaser
    global countLaserCoords
    global dockImg
    global dockClick
    laserCoords = [[0,0],[0,0]]
    docklaser = 0
    countLaserCoords = 0
    result = True
    dockImg = videoImg
    cv2.imshow("docking", dockImg)
    dockClick=True
    cv2.setMouseCallback("docking", click_event)

    #
    #
    # while result:
    #   ret, frame = videoCaptureObject.read()
    #   cv2.imshow("Capturing Video", frame)
    #   if cv2.waitKey(1) == ord('q'):
    #       videoCaptureObject.release()
    #       cv2.destroyAllWindows()
    #   if keyboard.is_pressed('s'):
    #       cv2.imwrite("/Users/valeriefan/Desktop/MATE-ROV-IP/docking.png", frame)
    #       cv2.imshow("docking", frame)
    #       dockImg = frame
    #       cv2.setMouseCallback("docking", click_event)

def dockCalculate():
    idealPixel = 39
    #idealPixelHigh
    #idealPixelLow
    laserPixels = math.sqrt(((laserCoords[0][0]-laserCoords[1][0])**2) + ((laserCoords[0][1]-laserCoords[1][1]) **2))
    print("Laser Pixels per inch: " + str(laserPixels))
    #return laserPixels
    print("Number of pixels: " + str(laserPixels))
    print("Ideal number of pixels: " + str(idealPixel)) #In the future, insert a range that we can be in
    if laserPixels < idealPixel:
        #replace 39 with more accurate number from real cam later
        print("Move forward!")
        #DO NOT ENTER AUTONOMOUS IF THIS IS SHOWN
    if laserPixels > idealPixel:
        print("Move backward!")
    # cv2.destroyAllWindows()

laserCoords = [[0,0],[0,0]]
docklaser = 0
countLaserCoords = 0
#dockImg = ""
def click_event(event, x, y, flags, params):
    global image
    global laserCoords
    global dockClick
    global countLaserCoords
    global dockImg
    # dockClick=True
    if dockClick==True:
        if countLaserCoords < 2:
            if event == cv2.EVENT_LBUTTONDOWN:
                print(countLaserCoords)
                laserCoords[countLaserCoords][0] = x
                laserCoords[countLaserCoords][1] = y
                countLaserCoords = countLaserCoords + 1
                print(x, ' ', y)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.circle(dockImg, (x, y), 3, (0, 0, 255), 3)
                #cv2.putText(dockImg, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
                cv2.imshow('docking', dockImg)
        else:
            dockClick = False
            print("Dock Click Ended")
            #dockCalculate()
        # else:
        #     dockClick = False
        #     print("Dock Click Ended")
        #     laserPixels = dockCalculate()
        #     print("Number of pixels: " + str(laserPixels))
        #     print("Ideal number of pixels: 39") #In the future, insert a range that we can be in
        #     if laserPixels > 39:
        #         #replace 39 with more accurate number from real cam later
        #         print("Move forward! (Not Accurate Check for Yourself)")
        #         #DO NOT ENTER AUTONOMOUS IF THIS IS SHOWN

if __name__ == "__main__":
    dockpic()

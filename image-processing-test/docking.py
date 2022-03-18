import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time
import glob


def dockpic():
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
      result = True
      i = 0
      while result:
          ret, frame = videoCaptureObject.read()
          cv2.imshow("Capturing Video", frame)
          if cv2.waitKey(1) == ord('q'):
              videoCaptureObject.release()
              cv2.destroyAllWindows()
          if keyboard.is_pressed('s'):
              if i < 1:
                  cv2.imwrite(glob.dock, frame)
                  i += 1
              else:
                  result = False

def dockCalculate():
    laserPixels = math.sqrt(((laserCoords[0][0]-laserCoords[1][0])**2) + ((laserCoords[0][1]-laserCoords[1][1]) **2))
    print("Laser Pixels per inch: " + str(laserPixels))


laserCoords = [[0,0],[0,0]]
docklaser = 0
countLaserCoords = 0
dockImg = ""
def click_event(event, x, y, flags, params):
    global image
    global laserCoords
    global dockClick
    dockClick=True
    if dockClick==True:
        if fishPictureCount < 1:
            if countLaserCoords < 2:
                if event == cv2.EVENT_LBUTTONDOWN:
                    laserCoords[countLaserCoords][0] = x
                    laserCoords[countLaserCoords][1] = y
                    countLaserCoords = countLaserCoords + 1
                    print(x, ' ', y)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(dockImg, str(x) + ',' +
                                str(y), (x,y), font,
                                1, (255, 0, 0), 2)
                    cv2.imshow('Laser', dockImg)
            else:
                dockClick = False
                dockCalculate()
                if laserPixels > 39:
                    #replace 39 with more accurate number from real cam later
                    print("Move forward!")
                    #DO NOT ENTER AUTONOMOUS IF THIS IS SHOWN
                else:
                    #move forward ~ 0.5 meter
                cv2.destroyAllWindows()

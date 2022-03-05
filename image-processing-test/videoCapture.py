#shows video feed and takes snapshots (+ saves them to prenamed files)

import numpy as np
import imutils
import cv2
import keyboard
import time

videoCaptureObject = cv2.VideoCapture(0)
result = True

snapshots = ["front.jpg", "back.jpg", "top.jpg", "left.jpg", "right.jpg"]
i = 0;
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video",frame)
    #deletes every frame as the next one comes on, closes all windows when q is pressed
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    #when s is pressed
    if keyboard.is_pressed('s'):
        #and the index is less than the length of the snapshot list
        if i < len(snapshots):
            #take as snapshot, save it, show it
            cv2.imwrite(snapshots[i],frame)
            cv2.imshow(snapshots[i], frame)
            i += 1
            time.sleep(1)
        else:
            result=False

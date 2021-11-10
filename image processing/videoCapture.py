import numpy as np
import argparse
import imutils
import cv2
import keyboard


videoCaptureObject = cv2.VideoCapture(0)
#if we want cam on
result = True
snapshots = ["front.jpg", "back.jpg", "top.jpg", "left.jpg", "right.jpg"]
i = 0;
#for name in snapshots:
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imshow("Capturing Video",frame)
        result = False
        if keyboard.is_pressed("q"):
            if i < len(snapshots)
            cv2.imwrite(snapshots[i],frame)
            cv2.imshow(snapshots[i], frame)
            i++


    videoCaptureObject.release()
    cv2.waitKey(0)
    while(result):
        cv2.waitKey(0)
        ret,frame = videoCaptureObject.read()
        cv2.imwrite(name,frame)
        result = False
    videoCaptureObject.release()

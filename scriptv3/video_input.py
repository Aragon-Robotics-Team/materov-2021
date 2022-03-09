import glob

import keyboard

from img_proc.photomosaic import cropping #import functions directly so we don't have to change code that much
from img_proc.photomosaic import resize_image
from img_proc.photomosaic import stitch
import cv2
import imutils
import time

#videoCaptureObject = cv2.VideoCapture(0)
def general_video():
    ret, frame = glob.videoCaptureObject.read()
    # cv2.imshow("Capturing Video", frame)
    #may need to change so that the video shows in the GUI
    #in which case, cv2.imwrite() to the image file that we will be showing for the video feed

def photomosaic():
    ret, frame = glob.videoCaptureObject.read()
    # cv2.imshow("Photomosaic Capturing Video", frame)
    if keyboard.is_pressed('s'):
        # and the index is less than the length of the snapshot list
        if glob.photomosaicCount < len(glob.snapshots):
            cv2.imwrite(glob.snapshots[glob.photomosaicCount], frame)
            cropping(glob.snapshots[glob.photomosaicCount])
            center_height = cv2.imread(glob.snapshots[0]).shape[0]
            center_width = cv2.imread(glob.snapshots[0]).shape[1]
            width_ratio = center_width/cv2.imread(glob.snapshots[glob.photomosaicCount]).shape[1]
            height_ratio = center_height/cv2.imread(glob.snapshots[glob.photomosaicCount]).shape[0]
            if glob.photomosaicCount < 3:
                resized = resize_image(cv2.imread(glob.snapshots[glob.photomosaicCount]), width_ratio, width_ratio)
            else:
                resized = resize_image(cv2.imread(glob.snapshots[glob.photomosaicCount]), height_ratio, height_ratio)

            cv2.imwrite(glob.snapshots[glob.photomosaicCount], resized)
            print("Snapshot #" + str(glob.photomosaicCount) + " taken")
            #cv2.imshow(glob.snapshots[i], frame)
            time.sleep(1)
            glob.photomosaicCount += 1
        else:
            print("PhotomosaicStart true")
            glob.photomosaicVideo = False
            stitch()
    if keyboard.is_pressed('q'):
        glob.photomosaicVideo = False
        # cv2.destroyAllWindows()

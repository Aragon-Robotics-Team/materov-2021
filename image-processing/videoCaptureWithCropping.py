# shows video, takes snapshots, crops them and saves
#valerie run: python3 /Users/valeriefan/github/test-materov-2021/image-processing/videoCaptureWithCropping.py
import numpy as np
import argparse
import imutils
import cv2
import keyboard
import time

def crop(image_name):
    # Load image and display (convert to grayscale and threshold it)
    image = cv2.imread(image_name)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("Thresh", thresh)

    cnts = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)

    output = image.copy()
    cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    (x, y, w, h) = cv2.boundingRect(c)
    text = "original, num_pts = {}".format(len(c))
    cv2.putText(output, text, (x, y - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Crop the image based on the points of the bounding box, show the cropped image
    cropped = image[y:y+h, x:x+w]
    cv2.imwrite(image_name, cropped)
    cv2.imshow(image_name, cropped)
    cv2.waitKey(0)


#############
videoCaptureObject = cv2.VideoCapture(0)
result = True

snapshots = ["front.jpg", "back.jpg", "top.jpg", "left.jpg", "right.jpg"]
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
            crop(snapshots[i])
            time.sleep(1)
            i += 1
        else:
            result = False

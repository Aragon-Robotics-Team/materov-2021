import numpy as np
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="shape.png", help = "path to input image")
args = vars(ap.parse_args())

#Load image and display (convert to grayscale and threshold it)
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)[1]
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
cv2.imwrite('cropped_image.png', cropped)
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)

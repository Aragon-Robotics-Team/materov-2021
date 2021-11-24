import numpy as np
import argparse
import cv2
import matplotlib
import imutils

count = 1

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

def cropping(image):
    #image = cv2.imread(image)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 300, cv2.THRESH_BINARY)[1]
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
    file = images[count]
    count == count + 1
    cv2.imwrite(file, cropped)
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)

    ratio = 500/cropped.shape[0]
    resizeimage[count] = resize_image(cropped, 430.5/563, 430.5/563)
    cv2.imwrite(image[count], resizeimage[count])
    cv2.imshow("Resized Cropped", resizeimage[count])

rightresize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

images = {
    1: "C:\\Users\\alexa\\Desktop\\photomosaic\\rightcropped.png"
}

resizeimage = {
    1: rightresize
}

center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

cropping(right)

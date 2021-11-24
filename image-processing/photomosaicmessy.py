import numpy as np
import argparse
import cv2
import matplotlib
import imutils

count = 1

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



def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

#gotta fix center because we accidentally overwrote it
center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
print(center.shape)
centerresized = resize_image(center, 430.5/563, 430.5/563)
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\centerresized.png", centerresized)
cv2.imshow("Center resize", centerresized)
cv2.imshow("Center", center)
print(centerresized.shape)
cv2.waitKey(0)
left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
cv2.imshow("Left", left)
print(left.shape)
cv2.waitKey(0)
right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
cv2.imshow("Right", right)
top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

shape = cv2.imread("C:\\Users\\alexa\\Desktop\\shape3.png")
#testing to show
#cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\center.png", center)
#cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png", left)
#cv2.imshow("left", left)
#cv2.imshow("Center", center)
#cv2.waitKey(0)

rightresize = blank

images = {
    1: "C:\\Users\\alexa\\Desktop\\photomosaic\\rightcropped.png"
}

resizeimage {
    1: rightresize
}

#crop each images
cropping(right)
#cropping(left)
#cropping(right)
#cropping(top)
#stitch together the images (tile?)
#im_tile = concat_tile([[blank, top, blank],
                        #[left, center, right]])
#show the image tile
#im_tile = cv2.hconcat([right, centerresized])
#cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\hconcat.png", im_tile)
#cv2.imshow("Tile", im_tile)
#cv2.waitKey(0)

import numpy as np
import argparse
import cv2
import matplotlib
import imutils

#replace this
center = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
left = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\left.png")
right = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\right.png")
top = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\top.png")
bottom = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\bottom.png")
blank = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")

centerResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\centerResize.png", blank)
leftResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\leftResize.png", leftResize)
rightResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\rightResize.png", rightResize)
topResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\topResize.png", topResize)
bottomResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\bottomResize.png", bottomResize)
blankResize = cv2.imread("C:\\Users\\alexa\\Desktop\\photomosaic\\blank.png")
cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\blankResize.png", blankResize)

images = ["C:\\Users\\alexa\\Desktop\\photomosaic\\centercropped.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\leftcropped.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\rightcropped.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\topcropped.png",
     "C:\\Users\\alexa\\Desktop\\photomosaic\\bottomcropped.png",
     "C:\\Users\\alexa\\Desktop\\photomosaic\\blankcropped.png"]

resizedimages = ["C:\\Users\\alexa\\Desktop\\photomosaic\\centerResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\leftResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\rightResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\topResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\bottomResize.png",
    "C:\\Users\\alexa\\Desktop\\photomosaic\\blankResize.png"
]

resizeimage = [
    centerResize,
    leftResize,
    rightResize,
    topResize,
    bottomResize,
    blankResize]



def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

def resize_blank(image):
    heightratio = 250/image.shape[0]
    widthratio = 249/image.shape[1]
    blankResize = resize_image(image, widthratio, heightratio)
    cv2.imwrite("C:\\Users\\alexa\\Desktop\\photomosaic\\blankResize.png", blankResize)

def resize_tile(image):
    ratio = 750/image.shape[1]
    resizeimage[i] = resize_image(image, ratio, ratio)

i = 0
def cropping(image):
    #image = cv2.imread(image)
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 300, cv2.THRESH_BINARY)[1]
    #cv2.imshow("Thresh", thresh)
    #cv2.waitKey(0)

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
    file = images[i]
    cv2.imwrite(file, cropped)
    #cv2.imshow("Cropped Image", cropped)
    #cv2.waitKey(0)

    ratio = 250/cropped.shape[0]
    resizeimage[i] = resize_image(cropped, ratio, ratio)
    cv2.imwrite(resizedimages[i], resizeimage[i])
    #cv2.imshow("Resized Cropped", resizeimage[i])

    #cv2.waitKey(0)

cropping(center)
centerResize = cv2.imread(resizedimages[i])
cv2.imshow("centerResize", centerResize)
cv2.waitKey(0)

i = 1
cropping(left)
leftResize = cv2.imread(resizedimages[i])
cv2.imshow("leftResize", leftResize)
cv2.waitKey(0)

i = 2
cropping(right)
rightResize = cv2.imread(resizedimages[i])
cv2.imshow("rightResize", rightResize)
cv2.waitKey(0)

i = 3
cropping(top)
topResize = cv2.imread(resizedimages[i])
cv2.imshow("topResize", topResize)
cv2.waitKey(0)

i = 4
cropping(bottom)
bottomResize = cv2.imread(resizedimages[i])
cv2.imshow("bottomResize", bottomResize)
cv2.waitKey(0)

heightratio = 250/blank.shape[0]
widthratio = 249/blank.shape[1]
blankResize = resize_image(blank, widthratio, heightratio)

# i = 2
# cropping(left)
# i = 3
# cropping(right)

middleTileLeft = cv2.hconcat([leftResize, centerResize])
cv2.imshow("Middle Tile Left", middleTileLeft)
cv2.waitKey(0)
middleTile = cv2.hconcat([middleTileLeft, rightResize])
cv2.imshow("MiddleTile", middleTile)
cv2.waitKey(0)
#resize_tile(middleTile)
print(middleTile.shape[1])

topTileLeft = cv2.hconcat([blankResize, topResize])
topTile = cv2.hconcat([topTileLeft, blankResize])
cv2.imshow("Top Tile", topTile)
cv2.waitKey(0)
#resize_tile(topTile)
print(topTile.shape[1])

bottomTileLeft = cv2.hconcat([blankResize, bottomResize])
bottomTile = cv2.hconcat([bottomTileLeft, blankResize])
cv2.imshow("Bottom Tile", bottomTile)
cv2.waitKey(0)
#resize_tile(bottomTile)
print(bottomTile.shape[1])

topSection = cv2.vconcat([topTile, middleTile])
photomosaic = cv2.vconcat([topSection, bottomTile])
cv2.imshow("PHOTOMOSAIC", photomosaic)
cv2.waitKey(0)

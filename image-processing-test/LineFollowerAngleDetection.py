import cv2
import numpy as np
import numpy as np
import argparse
import imutils
from skimage.transform import (hough_line, hough_line_peaks)

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

image = cv2.imread('/Users/valeriefan/Desktop/angledRedLine.jpg')
result = image.copy()
cv2.imshow("Image", image)
cv2.waitKey()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

mask1 = cv2.inRange(image, (0, 50, 20), (5, 255, 255))
mask2 = cv2.inRange(image, (175, 50, 20), (180, 255, 255))
cv2.waitKey()

mask = cv2.bitwise_or(mask1, mask2)

cv2.imshow("mask", mask)
cv2.waitKey()


#find edges
edges = cv2.Canny(mask, 50, 150)
cv2.imshow("edges", edges)
cv2.waitKey()

#find and draw lines on images
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength = 30, maxLineGap = 30)

black = cv2.imread('/Users/valeriefan/Desktop/download.jpg')
scale_w = image.shape[1]/black.shape[1]
scale_h = image.shape[0]/black.shape[0]
black = resize_image(black, scale_w, scale_h)

lineImage = black.copy()

i = 0
for x1, y1, x2, y2 in lines[0]:
    i+=1
    cv2.line(result, (x1, y1), (x2, y2), (255, 255, 255), 10)
    cv2.line(lineImage, (x1, y1), (x2, y2), (255, 255, 255), 5)
print(i)

center_width = black.shape[0]/2
center_height = black.shape[1]

#259 × 194 pixels
cv2.line(lineImage, ((int(center_width)), 0), ((int(center_width)), (int(center_height))), (0, 100, 50), 5)

cv2.imshow("res", result)
cv2.imshow("LineImage", lineImage)
cv2.waitKey(0)

grayLineImage = lineImage.sum(-1)

##detect angle
hspace, angles, distances = hough_line(grayLineImage)

angle = []
for _, a, distances in zip(*hough_line_peaks(hspace, angles, distances)):
    angle.append(a)

angles = [a*180/np.pi for a in angle]
angle_difference = np.max(angles) - np.min(angles)
print(angle_difference)

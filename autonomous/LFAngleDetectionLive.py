import cv2
import numpy as np
import argparse
import imutils
from skimage.transform import (hough_line, hough_line_peaks)
import math

def resize_image(img, scale_w, scale_h):
    return cv2.resize(img, (int(img.shape[1]*scale_w), int(img.shape[0]*scale_h)))

def angleBetweenLines(x1, y1, x2, y2, x3, y3): #given 3 points, where x1,y1 is the shared point
    v1 = (x2-x1, y2-y1)
    v2 = (x3-x1, y3-y1)
    dot = np.dot(v1, v2)
    magv1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magv2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cosAngle = dot/(magv1*magv2)
    angle = math.acos(cosAngle) #in radians
    print("x1: " + str(x1))
    print("x2:" + str(x2))
    print("x3: " + str(x3))
    if x2 <= x1:
        print("Positive")
        angle = math.pi-angle
        if y2 == y1:
            angle = abs(angle)
        return angle
    if x2 > x1:
        print("Negative")
        return (math.pi - angle) * -1


def LineFollowerAngleDetection(videoImg):
    image = cv2.imread(videoImg)
    #image = videoImg
    result = image.copy()
    #cv2.imshow("Image", image)
    #cv2.waitKey()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    #mask everything but the red
    mask1 = cv2.inRange(image, (0, 50, 20), (5, 255, 255))
    mask2 = cv2.inRange(image, (175, 50, 20), (180, 255, 255))
    #cv2.waitKey()
    mask = cv2.bitwise_or(mask1, mask2)
    #cv2.imshow("mask", mask)
    #cv2.waitKey()

    #find edges
    edges = cv2.Canny(mask, 50, 150)
    #cv2.imshow("edges", edges)
    #cv2.waitKey()

    #find and draw lines on images
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength = 30, maxLineGap = 30)

    #create a black background to put lines on - resize to the size of the original image
    black = cv2.imread('/Users/valeriefan/Desktop/download.jpg')
    scale_w = image.shape[1]/black.shape[1]
    scale_h = image.shape[0]/black.shape[0]
    black = resize_image(black, scale_w, scale_h)

    lineImage = black.copy()

    #calculate the bottom center point of the image
    center_width = black.shape[0]/2
    height = black.shape[1]

    i = 0
    for x1, y1, x2, y2 in lines[0]:
        i+=1
        cv2.line(result, (x1, y1), (x2, y2), (255, 255, 255), 10)
        #original placement of line
        cv2.line(lineImage, (x1, y1), (x2, y2), (142, 0, 24), 5)
        #line moved to center
        cv2.line(lineImage, (int(center_width), int(height)), (x2+(int(center_width)-x1), y2+(int(height))-y1), (255, 255, 255), 10)
    print(i)

    #259 × 194 pixels
    cv2.line(lineImage, ((int(center_width)), 0), ((int(center_width)), (int(height))), (0, 100, 50), 5)

    #cv2.imshow("res", result)
    #cv2.imshow("LineImage", lineImage)
    #cv2.waitKey(0)

    grayLineImage = lineImage.sum(-1)

    #calculate angle between lines
    for x1, y1, x2, y2 in lines[0]:
        #error: top coordinate is always 1, bottom coordinate is always 2
        print("original 1: " + str(x1) + ", " + str(y1) + " 2: " + str(x2) + ", " + str(y2))
        if y2 <= y1:
            filler = y1
            y1 = y2
            y2 = filler
            filler = x1
            x1 = x2
            x2 = filler
        angle = angleBetweenLines((int(center_width)), (int(height)), x2+(int(center_width))-x1, y2+(int(height))-y1, (int(center_width)), 0)
        #angle = angleBetweenLines(x1+(int(center_width))-x2, y1+(int(height))-y2, (int(center_width)), (int(height)), (int(center_width)), 0)
        #print(math.degrees(angle))
        #cv2.line(result, (0,0), (0,int(height)), (0, 0, 0), 10)

        cv2.putText(result, str(math.degrees(angle)), (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
        #cv2.putText(result, str(center_width) + ", " str(height), (center_width, height), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
        #cv2.putText(result, str(center_width) + ", " str(height), (center_width, height), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("LF", result)
        return angle

def ThrusterValue(videoImg):
    angle = LineFollowerAngleDetection(videoImg)
    speed = 1

videoCaptureObject = cv2.VideoCapture(0)
result = True
LF = False
while result:
    ret, frame = videoCaptureObject.read()
    if LF == False:
        cv2.imshow("Capturing Video", frame)
    if LF == True:
        videoImage = "/Users/valeriefan/Desktop/MATE-ROV-IP/Autonomous/videoImg.jpg"
        cv2.imwrite(videoImage, frame)
        LineFollowerAngleDetection(videoImage)
    if cv2.waitKey(1) == ord("l"):
        LF = True
    if cv2.waitKey(1) == ord("s"):
        LF = False
    if cv2.waitKey(1) == ord('q'):
        videoCaptureObject.release()
        cv2.destroyAllWindows()

#Sannie is a genius
#Find the position of the line
#If the top of the line is not centered, turn based on its distance from the center
#Check depth every few seconds
import cv2
import numpy as np
import argparse

from skimage.transform import (hough_line, hough_line_peaks)
import math

def midpoint(videoImg): #Find the center of the two lines
    image = cv2.imread(videoImg)

    result = image.copy()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    #mask everything but the red

    #Method:
    #increase contrast
    #decrease noise cv.fastNlMeansDenoisingColored()
    #mask
    #draw lines 

    mask1 = cv2.inRange(image, (0, 50, 20), (5, 255, 255))
    mask2 = cv2.inRange(image, (175, 50, 20), (180, 255, 255))
    #cv2.waitKey()
    mask = cv2.bitwise_or(mask1, mask2)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

    edges = cv2.Canny(mask, 50, 150)

    #find and draw lines on images
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength = 30, maxLineGap = 30)

    #draw line on the original image
    i = 0

    for leftx1, lefty1, leftx2, lefty2 in lines[0]:
        cv2.line(result, (leftx1, lefty1), (leftx2, lefty2), (255, 255, 255), 10)
        #cv2.imshow('',result) #bm: threading

        if lefty1 > lefty2:
            leftTopX = leftx2
            print("left circle")
            #cv2.circle(image, center_coordinates, radius, color, thickness)
            cv2.circle(result, (leftx2, lefty2), 3, (5, 255, 255), 3)
        else:
            print("left circle")
            leftTopX = leftx1
            cv2.circle(result, (leftx1, lefty1), 3, (5, 255, 255), 3)

    for rightx1, righty1, rightx2, righty2 in lines[1]:
        #If the lines are too close together (the detected lines are on the same line)
        if abs(rightx1 - leftx1) < 100:
            print("Line is too close")
            i+=2
        else:
            cv2.line(result, (rightx1, righty1), (rightx2, righty2), (255, 255, 255), 10)
            #cv2.imshow('', result) #bm: threading
            if righty1 > righty2:
                print("right circle")
                rightTopX = rightx2
                cv2.circle(result, (rightx2, righty2), 3, (5, 255, 255), 3)
            else:
                print("right circle")
                rightTopX = rightx1
                cv2.circle(result, (rightx1, righty1), 3, (5, 255, 255), 3)

    while i > 1:
        print("Checking next line")
        if len(lines) <i:
            i = 0
        else:
            for rightx1, righty1, rightx2, righty2 in lines[i]:
                if abs(rightx1 - leftx1) < 100:
                    i+=1
                else:
                    cv2.line(result, (rightx1, righty1), (rightx2, righty2), (255, 255, 255), 10)
                    #cv2.imshow('', result) #bm: threading
                    if righty1 > righty2:
                        print("right circle")
                        rightTopX = rightx2
                        cv2.circle(result, (rightx2, righty2), 3, (5, 255, 255), 3)
                    else:
                        print("right circle")
                        rightTopX = rightx1
                        cv2.circle(result, (rightx1, righty1), 3, (5, 255, 255), 3)
                    i = 0


    midpointX = (int)((leftTopX + rightTopX) / 2) #account for the rounding when we're checking it against the center value
    cv2.circle(result, (midpointX, 10), 3, (5, 255, 255), 3)
    cv2.imshow('', result)

    return midpointX

def StraightLFPWMOutput(videoImg):
    midpointX = midpoint(videoImg)
    midpointY = 0

    image = cv2.imread(videoImg)
    centerX = image.shape[1]/2

    angleToAdjust = math.atan(abs(centerX - midpointX)/image.shape[0])
    speed = 1
    if (midpointX < centerX):
        joyX = speed * (math.sin(angleToAdjust)) * -1 #incorrect calculation
    elif midpointX >= centerX:
        joyX = speed * (math.sin(angleToAdjust)) #incorrect calculation
    joyY = speed * (math.cos(angleToAdjust))
    print("Joystick Coords:")
    print("X: " + str(joyX))
    print("Y: " + str(joyY))


videoCaptureObject = cv2.VideoCapture(0)
result = True
LF = False

while result:
    ret, frame = videoCaptureObject.read()
    #find a way to take away all these if statements bc i think its part of whats causing the lag
    #if the line follower program isn't initiated
    if LF == False:
        cv2.imshow("Capturing Video", frame)
    #if the liine follower program is initiated
    if LF == True:
        videoImg = "/Users/valeriefan/Desktop/MATE-ROV-IP/Autonomous/videoImg.jpg"
        cv2.imwrite(videoImg, frame)
        StraightLFPWMOutput(videoImg)
        #JoystickValue(videoImage)
    #initiate the line follower program
    if cv2.waitKey(1) == ord("l"):
        LF = True
    #end the line follower program
    if cv2.waitKey(1) == ord("s"):
        LF = False
    #end the program all together
    if cv2.waitKey(1) == ord('q'):
        videoCaptureObject.release()
        cv2.destroyAllWindows()

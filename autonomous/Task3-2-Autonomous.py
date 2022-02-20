#Calibration
    #Make sure that the bot is parallel to the lines
    #Center the bot
        #Calculate the midpoint of the line, compare the distance of two x coordinates from
        #x=0 and x=500 and check whether the distances are equal
        #if they're not equal,
        #Calculate the average distance from the edges, find the difference between the average
        #and the smaller distance, and then use vectors to determine the speed and angle that
        #the bot needs to go to center itself
    #Adjust the depth of the bot

#During Run time
    #Adjust the angle of the bot, and every 5 seconds check whether or not the depth is in the necessary range
        #Check if the distance from the edge of the blue line is in a certain range

import cv2
import numpy as np
import argparse

from skimage.transform import (hough_line, hough_line_peaks)
import math


#def adjustAngle():
#def adjustDepth():

def center(videoImg):
    line = trackLine(videoImg)
    leftx1 = line[0]
    lefty1 = line[1]
    leftx2 = line[2]
    lefty2 = line[3]

    rightx1 = line[0]
    righty1 = line[1]
    rightx2 = line[2]
    righty2 = line[3]

    #find midpoint of each line
    leftDis = leftx1
    rightDis = 500 - rightx1

    #compare distances
    if (abs(leftDis - rightDis) > 50): #change range
        #takes average distance
        avg = (leftDis + rightDis)/2
        if leftDis <= rightDis:
            changeInX = avg - leftDis
        else:
            changeInX = leftDis - avg
        changeInY = 100
        distanceToAdjust = math.sqrt(changeInX ** 2 + changeInY ** 2)
        if leftx1 != leftx2:
            angleToAdjust = math.atan(abs(leftx1 - leftx2)/abs(lefty1 - lefty2))

    #calculate the pwm to output to the bot by calculating the force necessary to push the bot a certain distance
    #

def trackLine(videoImg):
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

    #draw line on the original image
    i = 0

    for leftx1, lefty1, leftx2, lefty2 in lines[0]:
        cv2.line(result, (leftx1, lefty1), (leftx2, lefty2), (255, 255, 255), 10)
        cv2.imshow('',result) #bm: threading

    for rightx1, righty1, rightx2, righty2 in lines[1]:
        #If the lines are too close together (the detected lines are on the same line)
        if abs(rightx1 - leftx1) < 100:
            print("Line is too close")
            i+=2
        else:
            cv2.line(result, (rightx1, righty1), (rightx2, righty2), (255, 255, 255), 10)
            cv2.imshow('', result) #bm: threading

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
                    cv2.imshow('', result) #bm: threading
                    i = 0
    #if rightx1 - leftx1 > 10, check coordinates of line[2]

    center_width = image.shape[0]/2
    height = image.shape[1]

    if leftx1 > rightx1:
        temp = leftx1
        rightx1 = leftx1
        leftx1 = temp

        temp = leftx2
        rightx2 = leftx2
        leftx2 = temp

    if lefty1 > lefty2:
        temp = lefty1
        lefty1 = lefty2
        lefty1 = temp

        temp = righty1
        righty1 = righty2
        righty1 = temp

    line = [leftx1, lefty1, leftx2, lefty2, rightx1, righty1, rightx2, righty2]

    print(line)
    return line

def angleOfLines(videoImg): #given 3 points, where x1,y1 is the shared point
    #calculate the bottom center point of the image
    image = cv2.imread(videoImg)

    center_width = image.shape[0]/2
    height = image.shape[1]

    line = trackLine(videoImg)
    x1a = line[0]
    y1a = line[1]
    x2a = line[2]
    y2a = line[3]

    if y2a <= y1a:
        filler = y1a
        y1a = y2a
        y2a = filler
        filler = x1a
        x1a = x2a
        x2a = filler

    x1 = int(center_width)
    y1 = int(height)
    x2 = x2a + (int(center_width)) - x1
    y2 = y2a + (int(height))-y1
    x3 = int(center_width)
    y3 = 0

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
        #print("Positive")
        angle = math.pi-angle
        if y2 == y1:
            angle = abs(angle)
        print("angle: " + str(math.pi-angle))
        return angle
    if x2 > x1:
        #print("Negative")
        print("angle: " + str(math.pi-angle))
        return (math.pi - angle) * -1

#def calibrate(): #calls adjustAngle, center, and adjust depth

videoCaptureObject = cv2.VideoCapture(0)
result = True
LF = False
# while result:
#     ret, frame = videoCaptureObject.read()
#     videoImg = "/Users/valeriefan/Desktop/MATE-ROV-IP/Autonomous/videoImg.jpg"
#     cv2.imwrite(videoImg, frame)
#     angleBetweenLines(videoImg)


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
        angleOfLines(videoImg)
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

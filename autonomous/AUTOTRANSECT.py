import cv2
import numpy as np
from time import sleep
import math

horizontal = [-1, -1, -1, -1]
vertical = [ -1, -1, -1, -1]
numH = 0
numV = 0
posH = -1
posV = -1
center_width = 0
center_height = 0
width = 0
height = 0
transectRow = ["right", "left", "right"]
rowCount = 0
mode = "hor"

def angleBetweenLines(x1, y1, x2, y2, x3, y3): #given 3 points, where x1,y1 is the shared point
    v1 = (x2-x1, y2-y1)
    v2 = (x3-x1, y3-y1)
    dot = np.dot(v1, v2)
    magv1 = math.sqrt(v1[0]**2 + v1[1]**2)
    magv2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cosAngle = dot/(magv1*magv2)
    angle = math.acos(cosAngle) #in radians
    # print("x1: " + str(x1))
    # print("x2:" + str(x2))
    # print("x3: " + str(x3))
    # print(angle)
    return(angle)

def horOrVert(x1, x2, y1, y2):
    global horizontal
    global vertical
    global numH
    global numV
    if y2 <= y1:
        filler = y1
        y1 = y2
        y2 = filler
        filler = x1
        x1 = x2
        x2 = filler
    angle_radians = angleBetweenLines((int(center_width)), (int(height)), x2+(int(center_width))-x1, y2+(int(height))-y1, (int(center_width)), 0)
    angle = math.degrees(angle_radians)
    print(angle)
    if (angle >= 90 and angle < 135):
        if abs(x2-x1) > abs(horizontal[0]-horizontal[2]):
            horizontal = [x1, y1, x2, y2] #the last horizontal line is saved
            # print("horizontal")
        numH = numH + 1
    if (angle >= 135 and angle < 181):
        if abs(y2-y1) > abs(vertical[1]-horizontal[3]):
        # print("vertical")
            vertical = [x1, y1, x2, y2] #the last vertical line is saved
        numV = numV + 1

def findPosition():
    global numH
    global numV
    global horizontal
    global vertical
    global posH
    global posV
    global img

    if numH > 0:
        print("Number of Horizontal Lines: " + str(numH))
        print("Horizontal Line: " + str(horizontal))
        print(horizontal)
        cv2.line(img, (horizontal[0], horizontal[1]), (horizontal[2], horizontal[3]), (100, 0, 0), 10) #draws one horizontal line
        posH = (horizontal[0] + horizontal[2])/2
        print("Position: " + str(posH))
    if numV > 0:
        print("Number of Vertical Lines: " + str(numV))
        print("Vertical Line: " + str(vertical))
        cv2.line(img, (vertical[0], vertical[1]), (vertical[2], vertical[3]), (100, 0, 0), 10) #draws one vertical line
        posV = (vertical[0] + vertical[2])/2
        print("Position: " + str(posV))

def sendToThrusters():
    global mode
    global rowCount
    if mode == "hor":
        if transectRow[rowCount] == "right":
            #send thruster values through the queue to move right
            if posV < (center_width + 25) and posV >= (center_width - 25):
                mode = "ver"
        elif transectRow[rowCount] == "left":
            #send thruster values throught the queue to move left
            if posV < (center_width + 25) and posV >= (center_width - 25):
                mode = "ver"
    if mode == "ver":
        #send thruster values to move down
        if posH < (center_height + 25) and posH >= (center_height - 25):
            mode = "hor"
            rowCount = rowCount + 1

def findLines(image):
    global numH
    global numV
    global center_width
    global height
    global center_height
    global width
    global img

    img = image
    width = img.shape[1]
    center_width = width/2
    height = img.shape[0]
    center_height = height/2

    #change to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #mask everything but the red
    lower_red = np.array([0,50,50]) #example value
    upper_red = np.array([10,255,255]) #example value
    mask = cv2.inRange(gray_hsv, lower_red, upper_red)
    # mask = cv2.bitwise_and(img, img, mask=mask)

    #simplifies everything that is not masked to be red (should help lessen the lines in the actual thing?)
    img[mask>0]=(0,0,255)

    mask = cv2.bitwise_and(gray_hsv, gray_hsv, mask=mask)
    # cv2.imshow("asdf", img)
    cv2.imshow("asdf", mask)

    #find lines
    cv2.waitKey(0)

    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)

    if len(lines) > 0:
        numH = 0 #resets the number of horizontal and vertical lines per frame
        numV = 0
        for line in lines:
           x1, y1, x2, y2 = line[0]
           # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)
           horOrVert(x1, x2, y1, y2)
           #detect angle between lines
    else:
        print("no lines")

    findPosition()

    cv2.imshow("linesDetected", img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

def autoTransect(img):
    findLines(img)
    sendToThrusters()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = cap.read()
        cv2.imshow("video", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            img = frame
            cap.release()
            cv2.destroyAllWindows()
            break
    # img = cv2.imread("/Users/valeriefan/Desktop/download.png")
    autoTransect(img)

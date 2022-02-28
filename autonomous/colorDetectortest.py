import cv2
import numpy as np

color_explore = np.zeros((150,150,3), np.uint8)
color_selected = np.zeros((150,150,3), np.uint8)


#save selected color RGB in file
def write_to_file(R,G,B):
    f = open("saved_color.txt", "a")
    RGB_color=str(R) + "," + str(G) + "," + str(B) + str("\n")
    f.write(RGB_color)
    f.close()

red = 0
blue = 0
green = 0

#Mouse Callback function
def show_color(event,x,y,flags,param):
    global red
    global blue
    global green
    global findColor

    B=img[y,x][0]
    G=img[y,x][1]
    R=img[y,x][2]
    color_explore [:] = (B,G,R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected [:] = (B,G,R)
        B=color_selected[10,10][0]
        G=color_selected[10,10][1]
        R=color_selected[10,10][2]
        print(R,G,B)
        write_to_file(R,G,B)
        print(hex(R),hex(G),hex(B))
        red = R
        blue = B
        green = G
        findColor = False


    #if event == cv2.EVENT_RBUTTONDOWN:


#live update color with cursor
cv2.namedWindow('color_explore')
cv2.resizeWindow("color_explore", 50,50);

#Show selected color when left mouse button pressed
cv2.namedWindow('color_selected')
cv2.resizeWindow("color_selected", 50,50);

#image window for sample image
cv2.namedWindow('')

#sample image path
img_path="/Users/valeriefan/Desktop/lines2.jpg"

#read sample image
img=cv2.imread(img_path)

#mouse call back function declaration
#while loop to live update
findColor = True
while (findColor):
    cv2.imshow('image',img)
    cv2.imshow('color_explore',color_explore)
    cv2.imshow('color_selected',color_selected)
    cv2.setMouseCallback('image',show_color)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

colorDetected = [blue, green, red]
print(colorDetected)
# low = [(blue - 50, green - 50, red - 50)]
# high = [(blue + 50, green + 50, red + 50)]
blueLow = blue - 50
greenLow = green - 50
redLow = red - 50
lower = np.array([blueLow, greenLow, redLow])

blueHigh = blue + 50
greenHigh = green + 50
redHigh = red + 50
high = np.array([blueHigh, greenHigh, redHigh])

mask = cv2.inRange(img, lower, high)

# mask = cv2.inRange(img, (blue - 50, green - 50, red - 50), (blue + 50, green + 50, red + 50))
output = cv2.bitwise_and(img, img, mask = mask)

blur = cv2.GaussianBlur(output, (5,5), cv2.BORDER_DEFAULT)
#cv2.imshow("mask", mask)
#cv2.waitKey()

#find edges
edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()

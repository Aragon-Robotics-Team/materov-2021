import cv2

# function to display the coordinates of
# of the points clicked on the image

count = 0
xcoords = []
xcoords = [0 for i in range(2)]
ycoords = []
ycoords = [0 for i in range(2)]


def click_event(event, x, y, flags, params):
    global count
    # checking for left mouse clicks
    if count < len(xcoords):
        if event == cv2.EVENT_LBUTTONDOWN:

            # displaying the coordinates
            # on the Shell
            xcoords[count-1] = x
            ycoords[count-1] = y
            print(x, ' ', y)

            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(x) + ',' +
                        str(y), (x,y), font,
                        1, (255, 0, 0), 2)
            cv2.imshow('image', img)
            count = count + 1

# driver function
# reading the image
img = cv2.imread('/Users/valeriefan/Desktop/thin-red-line-flag-united-states-america-country-police-thin-red-line-flag-137248115.jpg')

# displaying the image
cv2.imshow('image', img)

# setting mouse handler for the image
# and calling the click_event() function
#if count < len(xcoords):
cv2.setMouseCallback('image', click_event)

# wait for a key to be pressed to exit
cv2.waitKey(0)
cv2.destroyAllWindows()

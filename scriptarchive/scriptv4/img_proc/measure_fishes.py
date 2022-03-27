import cv2
import imutils
import glob
import math


fishCoords = [[0,0],[0,0],[0,0],[0,0]]
#[laserX1, laserY1],
#[laserX2, laserY2],
#[fishX1, fishY1],
#[fishX2, fishY2]
measureFishieClick = False
measureFishieCalc = False
countFishCoords = 0
fishImg = ""

fishPictureCount = 0
allFishLengths = [0,0,0]

def click_event(event, x, y, flags, params):
    global image
    global countFishCoords
    global measureFishieClick
    # checking for left mouse clicks for laser points
    if measureFishieClick==True:
        if fishPictureCount < 3:
            #print("click event")
            #print("MeasureFishieClick is true in click event")
            if countFishCoords < 4:
                if event == cv2.EVENT_LBUTTONDOWN:
                    #print("Button is clicked is true in click event")
                    # displaying the coordinates on the Shell
                    fishCoords[countFishCoords][0] = x
                    fishCoords[countFishCoords][1] = y
                    countFishCoords = countFishCoords + 1
                    # xcoords[countFishCoords-1] = x
                    # ycoords[countFishCoords-1] = y
                    print(x, ' ', y)

                    # displaying the coordinates
                    # on the image window
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(fishImg, str(x) + ',' +
                                str(y), (x,y), font,
                                1, (255, 0, 0), 2)
                    #q.put(fishImg)
                    cv2.imshow('Fish', fishImg)
                    #countFishCoords = countFishCoords + 1
            else:
                measureFishieClick = False
                #print("starting fish calculations")
                measureFishieCalculations()

def measureFishieCalculations():
    global fishPictureCount
    global countFishCoords
    global measureFishieClick
    global fishCoords

    #finding distances
    laserPixels = math.sqrt(((fishCoords[0][0]-fishCoords[1][0])**2) + ((fishCoords[0][1]-fishCoords[1][1]) **2))
    print("Laser Pixels per inch: " + str(laserPixels))
    fishPixels = math.sqrt(((fishCoords[2][0]-fishCoords[3][0])**2) + ((fishCoords[2][1]-fishCoords[3][1]) **2))
    print("Total Fish Pixels: " + str(fishPixels))
    fishLength = fishPixels / laserPixels
    print("Fish Length in inches: " + str(fishLength))
    allFishLengths[fishPictureCount] = fishLength
    fishPictureCount = fishPictureCount + 1

def measureFishie():
    #reset variables for new image
    global countFishCoords
    global measureFishieClick
    global fishCoords
    global fishImg
    countFishCoords = 0
    measureFishieClick = True

    #take 3photos and measure
    if fishPictureCount < 3:
        #show image and read coordinates
        print("Fish #: " + str(fishPictureCount + 1))
        #ret, frame = glob.videoCaptureObject.read()
        fishImg = glob.frame
        cv2.imshow("Fish", fishImg)
        cv2.setMouseCallback("Fish", click_event)
    else:
        #print all the measured fish lengths, input N, a, and b, and calculate the biomass of the cohort
        print("Fish Lengths: " + str(allFishLengths))
        averageFishLength = (allFishLengths[0]+allFishLengths[1]+allFishLengths[2])/3
        print("Average Fish Length: " + str(averageFishLength))

        askForValues = True
        while askForValues:
            #ask for the values
            numFish = int(input("Enter the number of fish (N): "))
            print("Number of Fish: " + str(numFish))

            numA = int(input("Enter the value of A: "))
            print("Value of A: " + str(numA))

            numB = int(input("Enter the value of B: "))
            print("Value of B: " + str(numB))

            askForValuesInput = input("Are these values correct? Type Y or N: ")

            if askForValuesInput == "Y":
                #calculate the biomass of the cohort
                askForValues = False
                print("Calculating biomass of the cohort using the equation M = N * a * L^b")
                fishMass = numFish * numA * ((averageFishLength)**numB)
                print("Biomass of the Cohort: " + str(fishMass))
            elif askForValuesInput == "N":
                #if these values are wrong, as for them again
                askForValues = True
            else:
                print("You're kind of stupid for not even typing Y or N, enter all the values in again")
                askForValues = True
        cv2.destroyAllWindows()

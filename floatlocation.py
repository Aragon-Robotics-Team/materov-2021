import math


def floatLocation():
    ask = True
    while ask:
        print("Current Speed in m/s: ")
        speed = float(input())
        print("Current Direction in degrees: ")
        dir = float(input())
        print("Time till next surface event in hours: ")
        time = float(input())

        print("Speed: " + str(speed))
        print("Direction: " + str(dir))
        print("Time: " + str(time))
        print("Are these values correct? Type Y or N")
        askResponse = input()
        if askResponse == "Y":
            ask = False
        if askResponse == "N":
            ask = True

    distance = (time * 3600) * speed / 1000 #multiply time in seconds by the speed to find the distance in meters, divde by 1000 to find distance in km

    print("The float travels " + str(distance) + " km at " + str(dir) + " degrees")
    #calculate the angle within the triangle
    if dir <= 90:
        angle = (90 - dir) * math.pi / 180
        gridX = distance * math.cos(angle) / 2 #each grid is 2km
        gridY = distance * math.sin(angle) / 2
    elif 90 < dir <= 180:
        angle = (180 - dir) * math.pi / 180
        gridX = distance * math.sin(angle) / 2 #each grid is 2km
        gridY = distance * math.cos(angle) / 2
    elif 180 < dir <= 270:
        angle = (dir - 180) * math.pi / 180
        gridX = distance * math.sin(angle) / 2 #each grid is 2km
        gridY = distance * math.cos(angle) / 2
    elif 270 < 180 < 360:
        angle = (dir - 270) * math.pi / 180
        gridX = distance * math.cos(angle) / 2 #each grid is 2km
        gridY = distance * math.sin(angle) / 2


    if dir <= 90:

        print(str(gridX) + " blocks to the east (right) and " + str(gridY) + " north (up)")
    elif 90 < dir <= 180:
        print(str(gridX) + " blocks to the east (right) and " + str(gridY) + " south (down)")
    elif 180 < dir <= 270:
        print(str(gridX) + " blocks to the west (left) and " + str(gridY) + " south (down)")
    elif 270 < 180 < 360:
        print(str(gridX) + " blocks to the west (left) and " + str(gridY) + " north (up)")

    print("Round to the nearest block, the blocks surrounding the correct block also count")
floatLocation()

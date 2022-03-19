from time import sleep, time
import pygame
import serial

serialOn = True
joyTestsOn = True
deadBand = 0.07  # axis value must be greater than this number
LH = 0  # Left horizontal axis
LV = 1  # Left vertical axis
RH = 2  # Right horizontal axis
RV = 3  # Right vertical axis

SpeedSize = 4
MaxSpeed = 1900
MinSpeed = 1100

serialPort = '/dev/cu.usbmodem14401'
minBytes = 1

mapK = 400
tspeedMiddle = 1500
tspeedUp = 1700
tspeedDown = 1300

squareButton = 15  # button open
triangleButton = 12  # button close
circleButton = 13  # up constant speed
xButton = 14  # down constant speed

startButton = 3  # starts loop()
shareButton = 0  # exits loop()

initSleep = 3
loopSleep = 0

arduinoParams = [tspeedMiddle, tspeedMiddle, tspeedMiddle, tspeedMiddle, 0, 0, 0]
# this array keeps updating thruster values

arduino = None
j = None


def main():
    joy_init()


def joy_init():
    ######################## 1. Initializing Serial
    if serialOn:
        global arduino
        arduino = serial.Serial(port=serialPort, baudrate=115200, timeout=1)
    ######################## 2. Initializing PyGame
    pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init()
    global j
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller
    controllerName = j.get_name()
    print('Detected controller : %s' % controllerName)
    print(pygame.joystick.get_count())
    # pygame.event.set_allowed(pygame.JOYBUTTONUP)

    sleep(initSleep)

    joy_tests()


def LinearLoop():
    program_starts = time()
    while True:
        pygame.event.pump()

        """
        get buttons and thrusters
        calculations and edit tspeeds
        check if over or under boundary speeds
        set incoming arduino data array to tspeeds
        repeatedly check if teleop is being ended
        """
        buttonopen = j.get_button(squareButton)
        buttonclose = j.get_button(triangleButton)
        upconst = j.get_button(circleButton)
        downconst = j.get_button(xButton)
        JS_X = j.get_axis(LH)
        JS_Y = j.get_axis(LV)  # y-direction joystick values are flipped
        JS_Y_UD = j.get_axis(RV)

        # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
        turn1, turn2, = JS_X * mapK, JS_X * mapK
        forward1, forward2 = JS_Y * mapK, JS_Y * mapK
        updown = JS_Y_UD * mapK

        # calculating thruster speeds
        tspeeds = [tspeedMiddle, tspeedMiddle, tspeedMiddle, tspeedMiddle, buttonopen,
                   buttonclose]

        if abs(upconst) == 1:
            tspeeds[2] = tspeedUp  # 1700
            tspeeds[3] = tspeedUp
        elif abs(downconst) == 1:
            tspeeds[2] = tspeedDown  # 1300
            tspeeds[3] = tspeedDown
        elif abs(JS_Y_UD) > deadBand:
            tspeeds[2] = int(tspeedMiddle + updown)  # side thrusters
            tspeeds[3] = int(tspeedMiddle + updown)

        if abs(JS_X) > deadBand and abs(JS_Y) > deadBand:
            tspeeds[0] = int(tspeedMiddle + forward1 + turn1)  # left thruster
            tspeeds[1] = int(tspeedMiddle + forward2 - turn2)  # right thruster
        elif abs(JS_X) > deadBand >= abs(JS_Y):  # only turn
            tspeeds[0] = int(tspeedMiddle + turn1)  # cast to integer
            tspeeds[1] = int(tspeedMiddle - turn2)
        elif abs(JS_X) <= deadBand < abs(JS_Y):
            tspeeds[0] = int(tspeedMiddle - forward1)  # cast to integer
            tspeeds[1] = int(tspeedMiddle - forward2)

        # assign statuses
        global arduinoParams
        arduinoParams = tspeeds

        for i in range(SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
            arduinoParams[i] = min(MaxSpeed, arduinoParams[i])
            arduinoParams[i] = max(MinSpeed, arduinoParams[i])

        if j.get_button(shareButton) == 1:
            serial_send_print()
            print("Stopping linear teleop")
            break
        serial_send_print()
        pygame.event.clear()
        sleep(loopSleep)
        now = time()
        print("It has been {0} seconds since the loop started".format(now - program_starts))


def NonLinearLoop():
    while True:
        pygame.event.pump()

        buttonopen = j.get_button(squareButton)
        buttonclose = j.get_button(triangleButton)
        upconst = j.get_button(circleButton)
        downconst = j.get_button(xButton)
        JS_X = j.get_axis(LH)
        JS_Y = j.get_axis(LV)  # y-direction joystick values are flipped
        JS_Y_UD = - j.get_axis(RV)

        updown = JS_Y_UD * mapK

        NL_X = mapK * (JS_X ** 3)
        NL_Y = mapK * (JS_Y ** 3)

        tspeeds = [tspeedMiddle, tspeedMiddle, tspeedMiddle, tspeedMiddle, buttonopen, buttonclose]

        # button z thrusters
        if abs(upconst) == 1:
            tspeeds[2] = tspeedUp
            tspeeds[3] = tspeedUp
        elif abs(downconst) == 1:
            tspeeds[2] = tspeedDown
            tspeeds[3] = tspeedDown
        elif abs(JS_Y_UD) > deadBand:
            tspeeds[2] = int(tspeedMiddle + updown)  # side thrusters
            tspeeds[3] = int(tspeedMiddle + updown)

        if abs(JS_X) > deadBand and abs(JS_Y) > deadBand:  # calculate thruster values
            tspeeds[0] = int(tspeedMiddle + NL_X + NL_Y)
            tspeeds[1] = int(tspeedMiddle + (NL_X - NL_Y))
        elif abs(JS_X) > deadBand >= abs(JS_Y):  # only turn
            tspeeds[0] = int(tspeedMiddle + NL_X)  # cast to integer
            tspeeds[1] = int(tspeedMiddle - NL_X)
        elif abs(JS_X) <= deadBand < abs(JS_Y):  # only forward/back
            tspeeds[0] = int(tspeedMiddle - NL_Y)  # cast to integer
            tspeeds[1] = int(tspeedMiddle - NL_Y)

        # assign statuses
        arduinoParams = tspeeds

        for i in range(SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
            arduinoParams[i] = min(MaxSpeed, arduinoParams[i])
            arduinoParams[i] = max(MinSpeed, arduinoParams[i])

        if j.get_button(shareButton) == 1:
            serial_send_print()
            print("Stopping Non-linear teleop")
            break
        serial_send_print()
        pygame.event.clear()
        sleep(loopSleep)


def serial_send_print():  # print to terminal / send regularly updated array to arduino

    stringToSend = ','.join(str(x) for x in arduinoParams) + '\n'
    print('py: ' + stringToSend)  # print python
    stringFromArd = ''
    if serialOn:
        arduino.write(stringToSend.encode("ascii"))  # send to arduino
        while arduino.in_waiting < minBytes:  # wait for data
            pass
        stringFromArd = arduino.readline().decode("ascii")  # read arduino data

    print('ard: ' + stringFromArd)  # print arduino data


def joy_tests():
    while joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                    print("Select Has Been Pressed")
                if event.button == 1:
                    print("Left Joystick button has been pressed")
                if event.button == 2:
                    print("Right Joystick button has been pressed")
                if event.button == 3:
                    print("Start has been pressed. Will exit joytests.")
                    LinearLoop()
                if event.button == 4:
                    print("Surface top button has been pressed")
                if event.button == 5:
                    print("Surface right button has been pressed")
                if event.button == 6:
                    print("Surface Bottom Has Been Pressed")
                if event.button == 7:
                    print("Surface left button has been pressed")
                if event.button == 8:
                    print("Left 2 has been pressed")
                if event.button == 9:
                    print("Right 2 has been pressed")
                if event.button == 10:
                    print("Left 1 has been pressed")
                if event.button == 11:
                    print("Right 1 has been pressed")
                if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                    print("Triangle Has Been Pressed")
                if event.button == 13:
                    print("Circle has been pressed")
                if event.button == 14:
                    print("X has been pressed")
                if event.button == 15:
                    print("Square has been pressed")
                if event.button == 16:
                    print("Center PS has been pressed")
                    NonLinearLoop()
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(j.get_axis(0)) > deadBand:
                    zero = j.get_axis(0)
                    print('1 has been moved ' + str(zero))
                if event.axis == 1 and abs(j.get_axis(1)) > deadBand:
                    one = j.get_axis(1)
                    print('2 has been moved ' + str(one))
                if event.axis == 2 and abs(j.get_axis(2)) > deadBand:
                    two = j.get_axis(2)
                    print('3 has been moved ' + str(two))
                if event.axis == 3 and abs(j.get_axis(3)) > deadBand:
                    three = j.get_axis(3)
                    print('4 has been moved ' + str(three))
                if event.axis == 4 and abs(j.get_axis(4)) > deadBand:
                    four = j.get_axis(4)
                    print('x has been moved ' + str(four))


if __name__ == '__main__':
    main()

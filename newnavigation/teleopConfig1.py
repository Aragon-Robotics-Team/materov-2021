"""
Configuration for everything
"""
from time import sleep, time
import pygame
from serial import Serial
from tracer import start, end, agg


class Config:
    def __init__(self, computerType, serialOn):
        if computerType == "RPI":
            self.computerType = computerType
            self.serialPort = '/dev/ttyACM0'
            self.LH = 0  # Left horizontal axis
            self.LV = 1  # Left vertical axis
            self.RH = 3  # Right horizontal axis
            self.RV = 4  # Right vertical axis

            self.squareButton = 2  # button open
            self.triangleButton = 3  # button close
            self.circleButton = 1  # up constant speed
            self.xButton = 0  # down constant speed

            self.startButton = 9  # starts linear()
            self.shareButton = 8  # exits
            self.centerButton = 10  # non linear

        elif computerType == "Mac":
            self.computerType = computerType
            self.serialPort = '/dev/cu.usbmodem14401'
            self.LH = 0  # Left horizontal axis
            self.LV = 1  # Left vertical axis
            self.RH = 2  # Right horizontal axis
            self.RV = 3  # Right vertical axis

            self.squareButton = 15  # button open
            self.triangleButton = 12  # button close
            self.circleButton = 13  # up constant speed
            self.xButton = 14  # down constant speed

            self.startButton = 3  # starts linear()
            self.shareButton = 0  # exits
            self.centerButton = 16  # non linear

        self.serialOn = serialOn
        self.serialRecieveOn = False
        self.joyTestsOn = True
        self.deadBand = 0.1  # axis value must be greater than this number

        self.SpeedSize = 4
        self.MaxSpeed = 1900
        self.MinSpeed = 1100

        self.minBytes = 10

        self.mapK = 400
        self.tspeedMiddle = 1500
        self.tspeedUp = 1700
        self.tspeedDown = 1300

        self.initSleep = 5
        self.loopSleep = 0.2

        self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, 0, 0]
        # this array keeps updating thruster values
        self.buttonopen = None
        self.buttonclose = None
        self.upconst = None
        self.downconst = None
        self.JS_X = None
        self.JS_Y = None
        self.JS_Y_UD = None

        self.arduino = None
        self.j = None


    def joy_init(self):
        ######################## 1. Initializing Serial
        if self.serialOn:
            self.arduino = Serial(port=self.serialPort, baudrate=115200, timeout=1)
        ######################## 2. Initializing PyGame
        pygame.init()  # Initiate the pygame functions
        pygame.joystick.init()
        pygame.display.init()
        self.j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
        self.j.init()  # Initiate the joystick or controller
        controllerName = self.j.get_name()
        print('Detected controller : %s' % controllerName)
        print(pygame.joystick.get_count())
        # pygame.event.set_allowed(pygame.JOYBUTTONUP)

        sleep(self.initSleep)

        if self.computerType=="Mac":
            self.joy_tests_mac()
        elif self.computerType=="RPI":
            self.joy_tests_rpi()

    def joy_tests_mac(self):
        while self.joyTestsOn:
            sleep(0.1)
            for event in pygame.event.get():
                # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "Select Has Been Pressed")
                    if event.button == 1:
                        print(event.button, "Left Joystick button has been pressed")
                    if event.button == 2:
                        print(event.button, "Right Joystick button has been pressed")
                    if event.button == 3:
                        print(event.button, "Start has been pressed. Will exit joytests.")
                        self.LinearLoop()
                    if event.button == 4:
                        print(event.button, "Surface top button has been pressed")
                    if event.button == 5:
                        print(event.button, "Surface right button has been pressed")
                    if event.button == 6:
                        print(event.button, "Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print(event.button, "Surface left button has been pressed")
                    if event.button == 8:
                        print(event.button, "Left 2 has been pressed")
                    if event.button == 9:
                        print(event.button, "Right 2 has been pressed")
                    if event.button == 10:
                        print(event.button, "Left 1 has been pressed")
                    if event.button == 11:
                        print(event.button, "Right 1 has been pressed")
                    if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "Triangle Has Been Pressed")
                    if event.button == 13:
                        print(event.button, "Circle has been pressed")
                    if event.button == 14:
                        print(event.button, "X has been pressed")
                    if event.button == 15:
                        print(event.button, "Square has been pressed")
                    if event.button == 16:
                        print(event.button, "Center PS has been pressed")
                        self.NonLinearLoop()
                elif event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0 and abs(self.j.get_axis(0)) > self.deadBand:
                        zero = self.j.get_axis(0)
                        print('0 has been moved ' + str(zero))
                    if event.axis == 1 and abs(self.j.get_axis(1)) > self.deadBand:
                        one = self.j.get_axis(1)
                        print('1 has been moved ' + str(one))
                    if event.axis == 2 and abs(self.j.get_axis(2)) > self.deadBand:
                        two = self.j.get_axis(2)
                        print('2 has been moved ' + str(two))
                    if event.axis == 3 and abs(self.j.get_axis(3)) > self.deadBand:
                        three = self.j.get_axis(3)
                        print('3 has been moved ' + str(three))
                    if event.axis == 4 and abs(self.j.get_axis(4)) > self.deadBand:
                        four = self.j.get_axis(4)
                        print('4 has been moved ' + str(four))

    def joy_tests_rpi(self):
        while self.joyTestsOn:
            sleep(0.1)
            for event in pygame.event.get():
                # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "X Has Been Pressed")
                    if event.button == 1:
                        print(event.button, "Circle has been pressed")
                    if event.button == 2:
                        print(event.button, "Triangle has been pressed")
                    if event.button == 3:
                        print(event.button, "Square has been pressed.")
                    if event.button == 4:
                        print(event.button, "Surface left button has been pressed")
                    if event.button == 5:
                        print(event.button, "Surface right button has been pressed")
                    if event.button == 6:
                        print(event.button, "Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print(event.button, "Surface left button has been pressed")
                    if event.button == 8:
                        print(event.button, "Share has been pressed")
                    if event.button == 9:
                        print(event.button, "Start has been pressed. will start linear teleop")
                        self.LinearLoop()
                    if event.button == 10:
                        print(event.button, "PS Center has been pressed. will start NON linear teleop")
                        self.NonLinearLoop()
                    if event.button == 11:
                        print(event.button, "Left joystick has been pressed")
                    if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "Right joystick Has Been Pressed")
                    if event.button == 13:
                        print(event.button, "cross top")
                    if event.button == 14:
                        print(event.button, "cross bottom")
                    if event.button == 15:
                        print(event.button, "cross left")
                    if event.button == 16:
                        print(event.button, "cross right")
                elif event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0 and abs(self.j.get_axis(0)) > self.deadBand:
                        zero = self.j.get_axis(0)
                        print('0 has been moved ' + str(zero))
                    if event.axis == 1 and abs(self.j.get_axis(1)) > self.deadBand:
                        one = self.j.get_axis(1)
                        print('1 has been moved ' + str(one))
                    if event.axis == 2 and abs(self.j.get_axis(2)) > self.deadBand:
                        two = self.j.get_axis(2)
                        print('Top Left trigger axis has been moved ' + str(two))
                    if event.axis == 3 and abs(self.j.get_axis(3)) > self.deadBand:
                        three = self.j.get_axis(3)
                        print('3 has been moved ' + str(three))
                    if event.axis == 4 and abs(self.j.get_axis(4)) > self.deadBand:
                        four = self.j.get_axis(4)
                        print('4 has been moved ' + str(four))

    def LinearLoop(self):
        program_starts = time()
        while True:
            start("first-half")
            pygame.event.pump()

            """
            get buttons and thrusters
            calculations and edit tspeeds
            check if over or under boundary speeds
            set incoming arduino data array to tspeeds
            repeatedly check if teleop is being ended
            """
            self.get_buttons()

            # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
            turn1, turn2, = self.JS_X * self.mapK, self.JS_X * self.mapK
            forward1, forward2 = self.JS_Y * self.mapK, self.JS_Y * self.mapK
            updown = self.JS_Y_UD * self.mapK

            # calculating thruster speeds
            tspeeds = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.buttonopen,
                       self.buttonclose]
            end("first-half")
            start("second-half")
            start("calcs")
            if abs(self.upconst) == 1:
                tspeeds[2] = self.tspeedUp  # 1700
                tspeeds[3] = self.tspeedUp
            elif abs(self.downconst) == 1:
                tspeeds[2] = self.tspeedDown  # 1300
                tspeeds[3] = self.tspeedDown
            elif abs(self.JS_Y_UD) > self.deadBand:
                tspeeds[2] = int(self.tspeedMiddle - updown)  # side thrusters
                tspeeds[3] = int(self.tspeedMiddle - updown)

            if abs(self.JS_X) > self.deadBand and abs(self.JS_Y) > self.deadBand:
                tspeeds[0] = int(self.tspeedMiddle - forward1 + turn1)  # left thruster
                tspeeds[1] = int(self.tspeedMiddle - forward2 - turn2)  # right thruster
            elif abs(self.JS_X) > self.deadBand >= abs(self.JS_Y):  # only turn
                tspeeds[0] = int(self.tspeedMiddle + turn1)  # cast to integer
                tspeeds[1] = int(self.tspeedMiddle - turn2)
            elif abs(self.JS_X) <= self.deadBand < abs(self.JS_Y):
                tspeeds[0] = int(self.tspeedMiddle - forward1)  # cast to integer
                tspeeds[1] = int(self.tspeedMiddle - forward2)
            end("calcs")

            start("check and limit")
            self.speed_limit(tspeeds)
            if self.check_button():
                break
            end("check and limit")
            start("end behavior")
            self.serial_send_print()

            end("end behavior")

            pygame.event.clear()
            sleep(self.loopSleep)

    def NonLinearLoop(self):
        while True:

            pygame.event.pump()

            self.get_buttons()

            NL_X = self.mapK * (self.JS_X ** 3)
            NL_Y = self.mapK * ((-self.JS_Y) ** 3)
            NL_Y_UD = self.mapK * ((-self.JS_Y_UD) ** 3)

            tspeeds = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.buttonopen,
                       self.buttonclose]

            # button z thrusters
            if abs(self.upconst) == 1:
                tspeeds[2] = self.tspeedUp
                tspeeds[3] = self.tspeedUp
            elif abs(self.downconst) == 1:
                tspeeds[2] = self.tspeedDown
                tspeeds[3] = self.tspeedDown
            elif abs(self.JS_Y_UD) > self.deadBand:
                tspeeds[2] = int(self.tspeedMiddle + NL_Y_UD)  # side thrusters
                tspeeds[3] = int(self.tspeedMiddle + NL_Y_UD)

            if abs(self.JS_X) > self.deadBand and abs(self.JS_Y) > self.deadBand:  # calculate thruster values
                tspeeds[0] = int(self.tspeedMiddle + NL_X + NL_Y)
                tspeeds[1] = int(self.tspeedMiddle + (NL_X - NL_Y))
            elif abs(self.JS_X) > self.deadBand >= abs(self.JS_Y):  # only turn
                tspeeds[0] = int(self.tspeedMiddle + NL_X)  # cast to integer
                tspeeds[1] = int(self.tspeedMiddle - NL_X)
            elif abs(self.JS_X) <= self.deadBand < abs(self.JS_Y):  # only forward/back
                tspeeds[0] = int(self.tspeedMiddle + NL_Y)  # cast to integer
                tspeeds[1] = int(self.tspeedMiddle + NL_Y)

            self.speed_limit(tspeeds)
            if self.check_button():
                break
            self.serial_send_print()

            pygame.event.clear()
            sleep(self.loopSleep)

    def speed_limit(self, tspeeds):
        # assign statuses
        self.arduinoParams = tspeeds

        for i in range(self.SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
            self.arduinoParams[i] = min(self.MaxSpeed, self.arduinoParams[i])
            self.arduinoParams[i] = max(self.MinSpeed, self.arduinoParams[i])

    def get_buttons(self):
        self.buttonopen = self.j.get_button(self.squareButton)
        self.buttonclose = self.j.get_button(self.triangleButton)
        self.upconst = self.j.get_button(self.circleButton)
        self.downconst = self.j.get_button(self.xButton)
        self.JS_X = self.j.get_axis(self.LH)
        self.JS_Y = self.j.get_axis(self.LV)  # y-direction joystick values are flipped
        self.JS_Y_UD = self.j.get_axis(self.RV)

    def check_button(self):
        if self.j.get_button(self.shareButton) == 1:
            self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, 0, 0]
            self.serial_send_print()
            print("Stopping teleop, either linear or nonlinear")
            print(agg)
            return True


    def serial_send_print(self):  # print to terminal / send regularly updated array to arduino

        stringToSend = ','.join(str(x) for x in self.arduinoParams) + '.'
        print('py: ' + stringToSend)  # print python
        stringFromArd = ''
        if self.serialOn:
            self.arduino.write(stringToSend.encode("ascii"))  # send to arduino
            start('arduino-wait')
            while (self.serialRecieveOn and (self.arduino.in_waiting <= self.minBytes)):  # wait for data
                pass
            end('arduino-wait')
            stringFromArd = self.arduino.readline().decode("ascii")  # read arduino data
        print('ard: ' + stringFromArd)  # print arduino data

if __name__ == '__main__':
    pass
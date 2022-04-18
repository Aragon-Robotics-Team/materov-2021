# """
# Configuration for everything
# """
from time import sleep, time
import pygame
import serial
# from serial import Serial
from scriptv10.nav.tracer import start, end, agg # mac imports
# from nav.tracer import start, end, agg  # RPI IMPORTS

# gui, killswitch
# from input_queue


class Config:
    def __init__(self, computerType, serialOn, serialRecieveOn, input_queue, output_queue):
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
            self.serialPort = '/dev/cu.usbmodem142101'
            self.LH = 0  # Left horizontal axis
            self.LV = 1  # Left vertical axis6
            self.RH = 2  # Right horizontal axis
            self.RV = 3  # Right vertical axis

            self.squareButton = 15  # button open
            self.triangleButton = 12  # button close
            self.circleButton = 13  # up constant speed
            self.xButton = 14  # down constant speed

            self.startButton = 3  # starts linear()
            self.shareButton = 0  # exits
            self.centerButton = 16  # non linear

        self.input_queue = input_queue  # THE QUEUES THE AMAZING QUEUES (kyoo-eez)
        self.output_queue = output_queue

        self.serialOn = serialOn
        self.serialRecieveOn = True
        self.joyTestsOn = True
        self.deadBand = 0.1  # axis value must be greater than this number

        self.SpeedSize = 4
        self.MaxSpeed = 1740
        self.MinSpeed = 1260

        self.minBytes = 10

        self.mapK = 240
        self.tspeedMiddle = 1500
        self.tspeedUp = 1700
        self.tspeedDown = 1300

        self.initSleep = 2
        self.loopSleep = 0.2

        self.buttonopen = None
        self.buttonclose = None
        self.upconst = None
        self.downconst = None
        self.JS_X = None
        self.JS_Y = None
        self.JS_Y_UD = None

        self.arduino = None
        self.j = None

        # THIS IS FOR THE QUEUE
        self.statuses = [1500, 1500, 1500, 1500, 0, 0, 0, 0, 0, 0]
        self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, 0, 0]
        # this array keeps updating thruster values

        self.loop = True

    def joy_init(self):
        ######################## 1. Initializing Serial
        self.serialOn = False
        if self.serialOn:
            self.arduino = serial.Serial(port=self.serialPort, baudrate=115200, timeout=1)
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

        if self.computerType == "Mac":
            self.joy_tests_mac()
        elif self.computerType == "RPI":
            self.joy_tests_rpi()

    def joy_tests_mac(self):
        # while self.joyTestsOn:
        while self.joyTestsOn:
            sleep(0.1)
            for event in pygame.event.get():
                # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "Select Has Been Pressed")
                        self.statuses[4] = 1
                    if event.button == 1:
                        print(event.button, "Left Joystick button has been pressed")
                        self.statuses[5] = 1
                    if event.button == 2:
                        print(event.button, "Right Joystick button has been pressed")
                        self.statuses[6] = 1
                    if event.button == 3:
                        print(event.button, "Start has been pressed. Will exit joytests.")
                        self.statuses[7] = 1
                        self.statuses[8] = 1
                        self.output_queue.put(self.statuses)
                        print("statuses sent")
                        self.LinearLoop()
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
                        # self.NonLinearLoop()
                elif event.type == pygame.JOYBUTTONUP:
                    if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "Select Has Been Released")
                        self.statuses[4] = 0
                    if event.button == 1:
                        print(event.button, "Left Joystick button has been released")
                        self.statuses[5] = 0
                    if event.button == 2:
                        print(event.button, "Right Joystick button has been released")
                        self.statuses[6] = 0
                    if event.button == 3:
                        print(event.button, "Start has been released.")
                        self.statuses[7] = 0
                    if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                        print(event.button, "Triangle Has Been released")
                    if event.button == 13:
                        print(event.button, "Circle has been released")
                    if event.button == 14:
                        print(event.button, "X has been released")
                    if event.button == 15:
                        print(event.button, "Square has been released")
                    if event.button == 16:
                        print(event.button, "Center PS has been released")
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

            self.output_queue.put(self.statuses)
            # print("put in queue")

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
            # self.queuereciever()

    def LinearLoop(self):
        program_starts = time()
        self.loop = True
        self.statuses[8] = 1
        self.statuses[8] = 0
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
            self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle,
                                  self.buttonopen,
                                  self.buttonclose]
            end("first-half")
            start("second-half")
            start("calcs")
            if abs(self.upconst) == 1:
                self.arduinoParams[2] = self.tspeedUp  # 1700
                self.arduinoParams[3] = self.tspeedUp
            elif abs(self.downconst) == 1:
                self.arduinoParams[2] = self.tspeedDown  # 1300
                self.arduinoParams[3] = self.tspeedDown
            elif abs(self.JS_Y_UD) > self.deadBand:
                self.arduinoParams[2] = int(self.tspeedMiddle - updown)  # side thrusters
                self.arduinoParams[3] = int(self.tspeedMiddle - updown)

            if abs(self.JS_X) > self.deadBand and abs(self.JS_Y) > self.deadBand:
                self.arduinoParams[0] = int(self.tspeedMiddle - forward1 + turn1)  # left thruster
                self.arduinoParams[1] = int(self.tspeedMiddle - forward2 - turn2)  # right thruster
            elif abs(self.JS_X) > self.deadBand >= abs(self.JS_Y):  # only turn
                self.arduinoParams[0] = int(self.tspeedMiddle + turn1)  # cast to integer
                self.arduinoParams[1] = int(self.tspeedMiddle - turn2)
            elif abs(self.JS_X) <= self.deadBand < abs(self.JS_Y):
                self.arduinoParams[0] = int(self.tspeedMiddle - forward1)  # cast to integer
                self.arduinoParams[1] = int(self.tspeedMiddle - forward2)
            end("calcs")

            print("tspeeds" + str(self.arduinoParams))

            start("check and limit")
            self.speed_limit()

            self.statusesupdate()

            if self.ended():
                break
            end("check and limit")
            start("end behavior")

            self.serial_send_print()

            end("end behavior")

            self.statusesupdate()
            pygame.event.clear()
            sleep(self.loopSleep)
            # self.queuereciever()

    def NonLinearLoop(self):
        self.statuses[8] = 1
        self.statuses[9] = 1
        while True:

            pygame.event.pump()

            self.get_buttons()

            NL_X = self.mapK * (self.JS_X ** 3)
            NL_Y = self.mapK * ((-self.JS_Y) ** 3)
            NL_Y_UD = self.mapK * ((-self.JS_Y_UD) ** 3)

            self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle,
                                  self.buttonopen,
                                  self.buttonclose]

            # button z thrusters
            if abs(self.upconst) == 1:
                self.arduinoParams[2] = self.tspeedUp
                self.arduinoParams[3] = self.tspeedUp
            elif abs(self.downconst) == 1:
                self.arduinoParams[2] = self.tspeedDown
                self.arduinoParams[3] = self.tspeedDown
            elif abs(self.JS_Y_UD) > self.deadBand:
                self.arduinoParams[2] = int(self.tspeedMiddle + NL_Y_UD)  # side thrusters
                self.arduinoParams[3] = int(self.tspeedMiddle + NL_Y_UD)

            if abs(self.JS_X) > self.deadBand and abs(self.JS_Y) > self.deadBand:  # calculate thruster values
                self.arduinoParams[0] = int(self.tspeedMiddle + NL_X + NL_Y)
                self.arduinoParams[1] = int(self.tspeedMiddle + (NL_X - NL_Y))
            elif abs(self.JS_X) > self.deadBand >= abs(self.JS_Y):  # only turn
                self.arduinoParams[0] = int(self.tspeedMiddle + NL_X)  # cast to integer
                self.arduinoParams[1] = int(self.tspeedMiddle - NL_X)
            elif abs(self.JS_X) <= self.deadBand < abs(self.JS_Y):  # only forward/back
                self.arduinoParams[0] = int(self.tspeedMiddle + NL_Y)  # cast to integer
                self.arduinoParams[1] = int(self.tspeedMiddle + NL_Y)

            self.statusesupdate()
            self.speed_limit()
            if self.ended():
                break
            print("tspeeds" + str(self.arduinoParams))
            self.serial_send_print()

            pygame.event.clear()
            sleep(self.loopSleep)

    def speed_limit(self):
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
        # statuses array buttons order: square, triangle, circle, x

    def ended(self):
        self.statuses[8] = 0
        if self.j.get_button(self.shareButton) == 1:  # if end button is pressed
            self.statuses[8] = 1
            self.statusesupdate()  # update gui that it's about to end, before ending
            self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, 0, 0]
            self.serial_send_print()
            print("Stopping teleop, either linear or nonlinear")
            print(agg)
            return True

    def statusesupdate(self):
        self.statuses[0] = self.arduinoParams[0]
        self.statuses[1] = self.arduinoParams[1]
        self.statuses[2] = self.arduinoParams[2]
        self.statuses[3] = self.arduinoParams[3]
        self.statuses[4] = self.buttonopen
        self.statuses[5] = self.buttonclose
        self.statuses[6] = self.upconst
        self.statuses[7] = self.downconst

        self.output_queue.put(self.statuses)
        print("statuses" + str(self.statuses))

    def serial_send_print(self):  # print to terminal / send regularly updated array to arduino

        stringToSend = ','.join(str(x) for x in self.arduinoParams) + '.'
        print('py: ' + stringToSend)  # print python
        stringFromArd = ''
        if self.serialOn:
            self.arduino.write(stringToSend.encode("ascii"))  # send to arduino
            start('arduino-wait')
            while self.serialRecieveOn and (self.arduino.in_waiting <= self.minBytes):  # wait for data
                pass
            stringFromArd = self.arduino.readline().decode("ascii")  # read arduino data

            end('arduino-wait')

            print('ard: ' + stringFromArd)  # print arduino data
    #
    # def queuereciever(self):
    #     if self.input_queue.empty() == False:
    #         self.loop = self.input_queue.get()
    #         print('recieved from queue')


if __name__ == '__main__':
    pass

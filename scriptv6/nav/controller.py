def controllerStart():
    import struct

    import pygame
    import serial
    import time
    from time import sleep

    class Thrust():

        def __init__(self, master = None):
            self.deadband = 0.2  # axis value must be greater than this number
            self.LH = 0 #Left horizontal axis
            self.LV = 1 #Left vertical axis
            self.RH = 2 #Right horizontal axis
            self.RV = 3 #RIght vertical axis

            self.serialPort = '/dev/cu.usbmodem14101'

            self.serialOn = False
            self.joyTestsOn = True

            self.turnconstant = 400
            self.forwardconstant = 400
            self.thrustermiddle = 1500
            self.trianglebutton = 2
            self.startbutton = 9

            self.servocloseindex = 2 #using triangle
            self.servoopenindex = 3 # using square
            self.thrusterleftindex = 0
            self.thrusterrightindex = 1

            self.initsleep = 3
            self.loopsleep = 1/12

        def joy_init(self):
            ######################## 1. Initializing Serial
            if self.serialOn:
                global arduino
                arduino = serial.Serial(port=self.serialPort, baudrate=115200, timeout=1)

            ######################## 2. Initializing PyGame
            pygame.init()  # Initiate the pygame functions
            pygame.joystick.init()
            pygame.display.init()
            global j
            j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
            j.init()  # Initiate the joystick or controller

            print('Detected controller : %s' % j.get_name())  # Print the name of any detected controllers
            # pygame.event.set_allowed(pygame.JOYBUTTONUP) # only allow JOYSTICKAXISMOTION events to appear on queue
            # pygame.event.set_allowed(pygame.JOYBUTTONDOWN)
            # pygame.event.set_allowed(pygame.JOYAXISMOTION)
            sleep(self.initsleep)

            ######################## 2. Initializing  global variables
            global finallist
            finallist = [self.thrustermiddle, self.thrustermiddle, 0, 0]

        def joytests(self):
            sleep(0.1)
            for event in pygame.event.get():
                # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
                if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                            print("X Has Been Pressed")
                        if event.button == 1:
                            print("Circle has been pressed")
                        if event.button == 2:
                            print("Triangle has been pressed") #
                        if event.button == 3:
                            print("Square has been pressed.")
                        if event.button == 4:
                            print("Shoulder L1 has been pressed")
                        if event.button == 5:
                            print("Shoulder R1 has been pressed")
                        if event.button == 6:
                            print("Surface Bottom Has Been Pressed")
                        if event.button == 7:
                            print("Shoulder R2 has been pressed")
                        if event.button == 8:
                            print("Share has been pressed")
                        if event.button == 9:
                            print("Start has been pressed. Will exit joytests")
                            loop()
                        if event.button == 10:
                            print("Center has been pressed")
                        if event.button == 11:
                            print("Left Joystick button has been pressed") #
                        if event.button == 12: # event.type == pygame.JOYBUTTONUP:
                            print("Right Joystick button Has Been Pressed") #
                        if event.button == 13:
                            print("Surface up has been pressed")
                        if event.button == 14:
                            print("Surface bottom has been pressed")
                        if event.button == 15:
                            print("Surface left has been pressed")
                        if event.button == 16:
                            print("Surface Right has been pressed")
                elif event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0 and abs(j.get_axis(0))> self.deadband:
                        zero = j.get_axis(0)
                        print('0 (left horizontal) has been moved ' + str(zero))
                    if event.axis == 1 and abs(j.get_axis(1))> self.deadband:
                        one = j.get_axis(1)
                        print('1 (left vertical) has been moved ' + str(one))
                    if event.axis == 2 and abs(j.get_axis(2))> self.deadband:
                        two = j.get_axis(2)
                        print('Shoulder L2 has been moved ' + str(two))
                    if event.axis == 3 and abs(j.get_axis(3))> self.deadband:
                        three = j.get_axis(3)
                        print('3 (right vertical) has been moved ' + str(three))
                    if event.axis == 4 and abs(j.get_axis(4)) > self.deadband:
                        four = j.get_axis(4)
                        print('4 (right horizontal) has been moved ' + str(four))

        def loop():
            while True:
                pygame.event.pump()
                #get buttons
                #get thrusters
                #write and read

                buttonclose = j.get_button(self.trianglebutton)
                buttonopen = j.get_button(self.startbutton)
                JS_X = j.get_axis(self.LH)
                JS_Y = j.get_axis(self.LV)

                # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
                turn1, turn2, forward1, forward2 = JS_X * self.turnconstant, JS_X * self.turnconstant, JS_Y * self.forwardconstant, JS_Y * self.turnconstant
                # calculating thruster speeds

                if abs(JS_X) > self.deadband and abs(JS_Y) > self.deadband: #calculate thruster values
                    thrustervalue1 = int(self.thrustermiddle - forward1 + turn1)  # y-direction joystick values are flipped
                    thrustervalue2 = int(self.thrustermiddle - forward2 - turn2)
                elif abs(JS_X) > self.deadband and abs(JS_Y) <= self.deadband: #only turn
                    thrustervalue1 = int(self.thrustermiddle + turn1)  # cast to integer
                    thrustervalue2 = int(self.thrustermiddle - turn2)
                elif abs(JS_X) <= self.deadband and abs(JS_Y) > self.deadband:
                    thrustervalue1 = int(self.thrustermiddle - forward1)  # cast to integer
                    thrustervalue2 = int(self.thrustermiddle - forward2)
                else:
                    thrustervalue1 = 1500
                    thrustervalue2 = 1500

                # assign statuses to listf
                finallist[self.servoopenindex] = buttonopen
                finallist[self.servocloseindex] = buttonclose
                finallist[self.thrusterleftindex] = thrustervalue1
                finallist[self.thrusterrightindex] = thrustervalue2

                for i in range(2): # making sure thruster values don't go above 1900 and below 1100
                    if finallist[i] > 1900:
                        finallist[i] = 1900
                    if finallist[i] < 1100:
                        finallist[i] = 1100

                # print('values: ' + str(finallist[0]) + ',' + str(finallist[1]) + ',' + str(finallist[2]) + ',' + str(finallist[3]))
                # print(str(thrustervalue1) + ',' + str(thrustervalue2))
                stringToSend = str(finallist[0]) + ',' + str(finallist[1]) + ',' + str(finallist[2]) + ',' + str(finallist[3]) + '\n'
                print('py: ' + str(stringToSend.encode()))
                if self.serialOn == True:
                    serialSendAndPrint(str(finallist[0]), str(finallist[1]), str(finallist[2]), str(finallist[3]))
                if j.get_button(8) == 1:
                    serialSendAndPrint(1500, 1500, 0, 0)
                    break
                pygame.event.clear()
                sleep(self.loopsleep)

        def serialSendAndPrint(w, x, y, z):
            stringToSend = str(w) + ',' + str(x) + ',' + str(y) + ',' + str(z) + '\n'
            print('py: ' + stringToSend.encode())  # print python
            arduino.write(stringToSend.encode("ascii"))  # send to arduino
            while arduino.in_waiting < 10:  # wait for data
                pass
            data = arduino.readline().decode("ascii")  # read arduino data
            print('ard: ' + data)  # print arduino data

        def write_read(): # not using

            # write = str(finallist[0])
            arduino.write(bytes('ewewe', 'utf-8'))
            #str(finallist[0]) + ' ' + str(finallist[1])+ ' ' + str(finallist[2])+ ' ' + str(finallist[3])
            # arduino.write(struct.pack('iiBB', finallist[0], finallist[1], finallist[2], finallist[3]))
            time.sleep(0.5)
            data = arduino.readline().decode('utf-8') # rstrip
            return data

    thruster = Thrust()
    thruster.joy_init()

    while True:
        thruster.joytests()

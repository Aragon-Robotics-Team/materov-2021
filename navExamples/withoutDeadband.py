"""
This code is intended for learning purposes. It does not contain any elements of tracer, autonomous, queue, or multiprocessing.

This file is the simplified version of OG nav with NO DEADBAND implemented.
It pulls a few methods from originalNav and simplifies them.

Go to originalNav to find code that contains everything
"""


def Loop(self):
    while True:
        pygame.event.pump()

        self.get_buttons()

        # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
        turn = self.JS_X * self.mapK  # mapK = 400
        forward = self.JS_Y * self.mapK
        updown = self.JS_Y_UD * self.mapK

        ##### UP DOWN THRUSTERS (VERTICAL MOVEMENT)
        self.arduinoParams = self.arduinoParamsConst
        ## control method: designated buttons for constant speed
        if abs(self.upconst) == 1:
            self.arduinoParams[2] = self.tspeedUp  # 1700
            self.arduinoParams[3] = self.tspeedUp
        elif abs(self.downconst) == 1:
            self.arduinoParams[2] = self.tspeedDown  # 1300
            self.arduinoParams[3] = self.tspeedDown
        ## control method: y-axis on left joystick
        else:
            self.arduinoParams[2] = int(self.tspeedMiddle - updown)  # side thrusters
            self.arduinoParams[3] = int(self.tspeedMiddle + updown)

        ##### DIRECTIONAL THRUSTERS ("X-Y PLANE" MOVEMENT)
        self.arduinoParams[0] = int(self.tspeedMiddle - forward + turn)  # left thruster
        self.arduinoParams[1] = int(self.tspeedMiddle - forward - turn)  # right thruster

        print("tspeeds" + str(self.arduinoParams))

        self.serial_send_print(self.arduinoParams)

        pygame.event.clear()

        sleep(self.loopSleep)


def serial_send_print(self, arr):  # print to terminal / send regularly updated array to arduino

    stringToSend = ','.join(str(x) for x in arr) + '.'
    print('py: ' + stringToSend)  # print python
    if self.serialOn:
        self.arduino.write(stringToSend.encode("ascii"))  # send to arduino
        while self.serialRecieveOn and (self.arduino.in_waiting <= self.minBytes):  # wait for data
            pass
        bytes = self.arduino.in_waiting
        stringFromArd = self.arduino.readline().decode("ascii")  # read arduino data with timeout = 1

        print('ard: ' + stringFromArd + ', ' + str(bytes))  # print arduino data


def get_buttons(self):

    self.buttonopen = self.j.get_button(self.squareButton)
    self.buttonclose = self.j.get_button(self.triangleButton)
    self.upconst = self.j.get_button(self.circleButton)
    self.downconst = self.j.get_button(self.xButton)
    self.JS_X = self.j.get_axis(self.LH)
    self.JS_Y = self.j.get_axis(self.LV)  # y-direction joystick values are flipped
    self.JS_Y_UD = self.j.get_axis(self.RV)


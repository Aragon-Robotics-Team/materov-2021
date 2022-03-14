
# Importing Libraries

from time import sleep
import pygame
import serial


def joy_init(config):
    ######################## 1. Initializing Serial
    if config.serialOn:
        global arduino
        arduino = serial.Serial(port=config.serialPort, baudrate=115200, timeout=1)
    ######################## 2. Initializing PyGame
    pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init()
    global j
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller
    global controllerName
    controllerName = j.get_name()
    print('Detected controller : %s' % controllerName)
    print(pygame.joystick.get_count())
    # pygame.event.set_allowed(pygame.JOYBUTTONUP)

    sleep(config.initSleep)

    if controllerName == "Sony PLAYSTATION(R)3 Controller":
        joy_tests_ps3()
    else:
        joy_tests()


def joy_tests(config):
    while config.joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    print("X Has Been Pressed")
                if event.button == 1:
                    print("Circle has been pressed")
                if event.button == 2:
                    print("Triangle has been pressed")
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
                    LinearLoop(config)  # starts loop()
                if event.button == 10:
                    print("Center has been pressed")
                    NonLinearLoop(config)
                if event.button == 11:
                    print("Left Joystick button has been pressed")
                if event.button == 12:
                    print("Right Joystick button Has Been Pressed")
                if event.button == 13:
                    print("Surface up has been pressed")
                if event.button == 14:
                    print("Surface bottom has been pressed")
                if event.button == 15:
                    print("Surface left has been pressed")
                if event.button == 16:
                    print("Surface Right has been pressed")
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(j.get_axis(0)) > config.deadBand:
                    zero = j.get_axis(0)
                    print('0 (left horizontal) has been moved ' + str(zero))
                if event.axis == 1 and abs(j.get_axis(1)) > config.deadBand:
                    one = j.get_axis(1)
                    print('1 (left vertical) has been moved ' + str(one))
                if event.axis == 2 and abs(j.get_axis(2)) > config.deadBand:
                    two = j.get_axis(2)
                    print('Shoulder L2 has been moved ' + str(two))
                if event.axis == 3 and abs(j.get_axis(3)) > config.deadBand:
                    three = j.get_axis(3)
                    print('3 (right vertical) has been moved ' + str(three))
                if event.axis == 4 and abs(j.get_axis(4)) > config.deadBand:
                    four = j.get_axis(4)
                    print('4 (right horizontal) has been moved ' + str(four))


def joy_tests_ps3(config):
    while config.joyTestsOn:
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
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(j.get_axis(0)) > config.deadBand:
                    zero = j.get_axis(0)
                    print('1 has been moved ' + str(zero))
                if event.axis == 1 and abs(j.get_axis(1)) > config.deadBand:
                    one = j.get_axis(1)
                    print('2 has been moved ' + str(one))
                if event.axis == 2 and abs(j.get_axis(2)) > config.deadBand:
                    two = j.get_axis(2)
                    print('3 has been moved ' + str(two))
                if event.axis == 3 and abs(j.get_axis(3)) > config.deadBand:
                    three = j.get_axis(3)
                    print('4 has been moved ' + str(three))
                if event.axis == 4 and abs(j.get_axis(4)) > config.deadBand:
                    four = j.get_axis(4)
                    print('4 has been moved ' + str(four))


def LinearLoop(config):
    while True:
        pygame.event.pump()
        # get buttons
        # get thrusters
        # write and read

        buttonopen = j.get_button(config.squareButton)
        buttonclose = j.get_button(config.triangleButton)
        upconst = j.get_button(config.circleButton)
        downconst = j.get_button(config.xButton)
        JS_X = j.get_axis(config.LH)
        JS_Y = j.get_axis(config.LV) # y-direction joystick values are flipped
        JS_Y_UD = j.get_axis(config.RV)

        # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
        turn1, turn2,  = JS_X * config.mapK, JS_X * config.mapK
        forward1, forward2 = JS_Y * config.mapK, JS_Y * config.mapK
        updown = JS_Y_UD * config.mapK

        # calculating thruster speeds
        tspeed_1, tspeed_2, tspeed_3, tspeed_4 = 1500, 1500, 1500, 1500

        if abs(upconst) == 1:
            tspeed_3 = 1700
            tspeed_4 = 1700
        if abs(downconst) == 1:
            tspeed_3 = 1300
            tspeed_4 = 1300

        if abs(JS_Y_UD) > config.deadBand:
            tspeed_3 = int(config.tspeedMiddle + updown)  # side thrusters
            tspeed_4 = int(config.tspeedMiddle + updown)

        if abs(JS_X) > config.deadBand and abs(JS_Y) > config.deadBand:
            tspeed_1 = int(config.tspeedMiddle + forward1 + turn1)  # left thruster
            tspeed_2 = int(config.tspeedMiddle + forward2 - turn2)  # right thruster
        elif abs(JS_X) > config.deadBand >= abs(JS_Y):  # only turn
            tspeed_1 = int(config.tspeedMiddle + turn1)  # cast to integer
            tspeed_2 = int(config.tspeedMiddle - turn2)
        elif abs(JS_X) <= config.deadBand < abs(JS_Y):
            tspeed_1 = int(config.tspeedMiddle - forward1)  # cast to integer
            tspeed_2 = int(config.tspeedMiddle - forward2)

        # assign statuses to toArduino
        config.toArduino[0] = tspeed_1  # left thruster
        config.toArduino[1] = tspeed_2  # right thruster
        config.toArduino[2] = tspeed_3
        config.toArduino[3] = tspeed_4
        config.toArduino[4] = buttonopen
        config.toArduino[5] = buttonclose

        for i in range(2):  # making sure thruster values don't go above 1900 and below 1100
            if config.toArduino[i] > 1900:
                config.toArduino[i] = 1900
            if config.toArduino[i] < 1100:
                config.toArduino[i] = 1100

        if j.get_button(config.shareButton) == 1:
            serial_send_print(1500, 1500, 1500, 1500, 0, 0)
            break
        serial_send_print(str(config.toArduino[0]), str(config.toArduino[1]), str(config.toArduino[2]), str(config.toArduino[3]), str(config.toArduino[4]), str(config.toArduino[5]))
        pygame.event.clear()
        sleep(config.loopSleep)


def NonLinearLoop(config):
    while True:
        pygame.event.pump()
        # get buttons
        # get thrusters
        # write and read

        buttonopen = j.get_button(config.squareButton)
        buttonclose = j.get_button(config.triangleButton)
        upconst = j.get_button(config.circleButton)
        downconst = j.get_button(config.xButton)
        JS_X = j.get_axis(config.LH)
        JS_Y = j.get_axis(config.LV) # y-direction joystick values are flipped
        JS_Y_UD = -j.get_axis(config.RV)

        updown = JS_Y_UD * config.mapK

        NL_X = config.mapK *(JS_X**3)
        NL_Y = config.mapK *(JS_Y**3)

        # calculating thruster speeds
        tspeed_1, tspeed_2, tspeed_3, tspeed_4 = 1500, 1500, 1500, 1500

        # button z thrusters
        if abs(upconst) == 1:
            tspeed_3 = 1700
            tspeed_4 = 1700
        if abs(downconst) == 1:
            tspeed_3 = 1300
            tspeed_4 = 1300

        # joystick z thrusters
        if abs(JS_Y_UD) > config.deadBand:
            tspeed_3 = int(config.tspeedMiddle + updown)  # side thrusters
            tspeed_4 = int(config.tspeedMiddle + updown)

        if abs(JS_X) > config.deadBand and abs(JS_Y) > config.deadBand: #calculate thruster values
            tspeed_1 = int(config.tspeedMiddle + NL_X + NL_Y)
            tspeed_2 = int(config.tspeedMiddle + (NL_X - NL_Y))
        elif abs(JS_X) > config.deadBand and abs(JS_Y) <= config.deadBand: #only turn
            tspeed_1 = int(config.tspeedMiddle + NL_X)  # cast to integer
            tspeed_2 = int(config.tspeedMiddle - NL_X)
        elif abs(JS_X) <= config.deadBand and abs(JS_Y) > config.deadBand: #only forward/back
            tspeed_1 = int(config.tspeedMiddle - NL_Y)  # cast to integer
            tspeed_2 = int(config.tspeedMiddle - NL_Y)
        else:
            tspeed_1 = 1500
            tspeed_2 = 1500

        # assign statuses to toArduino
        config.toArduino[0] = tspeed_1  # left thruster
        config.toArduino[1] = tspeed_2  # right thruster
        config.toArduino[2] = tspeed_3
        config.toArduino[3] = tspeed_4
        config.toArduino[4] = buttonopen
        config.toArduino[5] = buttonclose

        for i in range(2):  # making sure thruster values don't go above 1900 and below 1100
            if config.toArduino[i] > 1900:
                config.toArduino[i] = 1900
            if config.toArduino[i] < 1100:
                config.toArduino[i] = 1100

        if j.get_button(config.shareButton) == 1:
            serial_send_print(1500, 1500, 1500, 1500, 0, 0)
            print('Stopping teleop')
            break
        serial_send_print(str(config.toArduino[0]), str(config.toArduino[1]), str(config.toArduino[2]), str(config.toArduino[3]), str(config.toArduino[4]), str(config.toArduino[5]))
        pygame.event.clear()
        sleep(config.loopSleep)


def serial_send_print(config, a, b, c, d, e, f):  # six rings by ariana grande

    stringToSend = '%s,%s,%s,%s,%s,%s\n' % (a, b, c, d, e, f)
    print('py: ' + stringToSend)  # print python
    stringFromArd = ''
    if config.serialOn:
        arduino.write(stringToSend.encode("ascii"))  # send to arduino
        while arduino.in_waiting < 10:  # wait for data
            pass
        stringFromArd = arduino.readline().decode("ascii")  # read arduino data
    print('ard: ' + stringFromArd)  # print arduino data


if __name__ == "__main__":
    joy_init()
    # serial_send_print(1, 2, 3, 2, 3, 3, 3)

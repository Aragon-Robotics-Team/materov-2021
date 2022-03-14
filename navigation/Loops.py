
# Importing Libraries

from time import sleep
import pygame
import serial


def LinearLoop(config):
    while True:
        pygame.event.pump()
        # get buttons
        # get thrusters
        # write and read

        buttonopen = config.j.get_button(config.squareButton)
        buttonclose = config.j.get_button(config.triangleButton)
        upconst = config.j.get_button(config.circleButton)
        downconst = config.j.get_button(config.xButton)
        JS_X = config.j.get_axis(config.LH)
        JS_Y = config.j.get_axis(config.LV) # y-direction joystick values are flipped
        JS_Y_UD = config.j.get_axis(config.RV)

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

        if config.j.get_button(config.shareButton) == 1:
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

        buttonopen = config.j.get_button(config.squareButton)
        buttonclose = config.j.get_button(config.triangleButton)
        upconst = config.j.get_button(config.circleButton)
        downconst = config.j.get_button(config.xButton)
        JS_X = config.j.get_axis(config.LH)
        JS_Y = config.j.get_axis(config.LV) # y-direction joystick values are flipped
        JS_Y_UD = -config.j.get_axis(config.RV)

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

        if config.j.get_button(config.shareButton) == 1:
            serial_send_print(1500, 1500, 1500, 1500, 0, 0)
            print('Stopping teleop')
            break
        serial_send_print(config, str(config.toArduino[0]), str(config.toArduino[1]), str(config.toArduino[2]), str(config.toArduino[3]), str(config.toArduino[4]), str(config.toArduino[5]))
        pygame.event.clear()
        sleep(config.loopSleep)


def serial_send_print(config, a, b, c, d, e, f):  # six rings by ariana grande

    stringToSend = '%s,%s,%s,%s,%s,%s\n' % (a, b, c, d, e, f)
    print('py: ' + stringToSend)  # print python
    stringFromArd = ''
    if config.serialOn:
        config.arduino.write(stringToSend.encode("ascii"))  # send to arduino
        while config.arduino.in_waiting < 10:  # wait for data
            pass
        stringFromArd = config.arduino.readline().decode("ascii")  # read arduino data
    print('ard: ' + stringFromArd)  # print arduino data


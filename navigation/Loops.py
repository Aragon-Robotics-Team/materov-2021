
# Importing Libraries

import time
import pygame
import serial


def LinearLoop(config):
    program_starts = time.time()
    while True:
        pygame.event.pump()

        """
        get buttons and thrusters
        calculations and edit tspeeds
        check if over or under boundary speeds
        set incoming arduino data array to tspeeds
        repeatedly check if teleop is being ended
        """
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
        tspeeds = [config.tspeedMiddle, config.tspeedMiddle, config.tspeedMiddle, config.tspeedMiddle, buttonopen, buttonclose]

        if abs(upconst) == 1:
            tspeeds[2] = config.tspeedUp  # 1700
            tspeeds[3] = config.tspeedUp
        elif abs(downconst) == 1:
            tspeeds[2] = config.tspeedDown  # 1300
            tspeeds[3] = config.tspeedDown
        elif abs(JS_Y_UD) > config.deadBand:
            tspeeds[2] = int(config.tspeedMiddle + updown)  # side thrusters
            tspeeds[3] = int(config.tspeedMiddle + updown)

        if abs(JS_X) > config.deadBand and abs(JS_Y) > config.deadBand:
            tspeeds[0] = int(config.tspeedMiddle + forward1 + turn1)  # left thruster
            tspeeds[1] = int(config.tspeedMiddle + forward2 - turn2)  # right thruster
        elif abs(JS_X) > config.deadBand >= abs(JS_Y):  # only turn
            tspeeds[0] = int(config.tspeedMiddle + turn1)  # cast to integer
            tspeeds[1] = int(config.tspeedMiddle - turn2)
        elif abs(JS_X) <= config.deadBand < abs(JS_Y):
            tspeeds[0] = int(config.tspeedMiddle - forward1)  # cast to integer
            tspeeds[1] = int(config.tspeedMiddle - forward2)

        # assign statuses
        config.arduinoParams = tspeeds

        for i in range(config.SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
            config.arduinoParams[i] = min(config.MaxSpeed, config.arduinoParams[i])
            config.arduinoParams[i] = max(config.MinSpeed, config.arduinoParams[i])

        if config.j.get_button(config.shareButton) == 1:
            serial_send_print(config)
            print("Stopping linear teleop")
            break
        serial_send_print(config)
        pygame.event.clear()
        time.sleep(config.loopSleep)
        now = time.time()
        print("It has been {0} seconds since the loop started".format(now - program_starts))


def NonLinearLoop(config):
    while True:
        pygame.event.pump()

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

        tspeeds = [config.tspeedMiddle, config.tspeedMiddle, config.tspeedMiddle, config.tspeedMiddle, buttonopen, buttonclose]

        # button z thrusters
        if abs(upconst) == 1:
            tspeeds[2] = config.tspeedUp
            tspeeds[3] = config.tspeedUp
        elif abs(downconst) == 1:
            tspeeds[2] = config.tspeedDown
            tspeeds[3] = config.tspeedDown
        elif abs(JS_Y_UD) > config.deadBand:
            tspeeds[2] = int(config.tspeedMiddle + updown)  # side thrusters
            tspeeds[3] = int(config.tspeedMiddle + updown)

        if abs(JS_X) > config.deadBand and abs(JS_Y) > config.deadBand:  # calculate thruster values
            tspeeds[0] = int(config.tspeedMiddle + NL_X + NL_Y)
            tspeeds[1] = int(config.tspeedMiddle + (NL_X - NL_Y))
        elif abs(JS_X) > config.deadBand >= abs(JS_Y):  # only turn
            tspeeds[0] = int(config.tspeedMiddle + NL_X)  # cast to integer
            tspeeds[1] = int(config.tspeedMiddle - NL_X)
        elif abs(JS_X) <= config.deadBand < abs(JS_Y):  # only forward/back
            tspeeds[0] = int(config.tspeedMiddle - NL_Y)  # cast to integer
            tspeeds[1] = int(config.tspeedMiddle - NL_Y)

        # assign statuses
        config.arduinoParams = tspeeds

        for i in range(config.SpeedSize):  # making sure thruster values don't go above 1900 and below 1100
            config.arduinoParams[i] = min(config.MaxSpeed, config.arduinoParams[i])
            config.arduinoParams[i] = max(config.MinSpeed, config.arduinoParams[i])

        if config.j.get_button(config.shareButton) == 1:
            serial_send_print(config)
            print("Stopping Non-linear teleop")
            break
        serial_send_print(config)
        pygame.event.clear()
        sleep(config.loopSleep)


def serial_send_print(config):  # print to terminal / send regularly updated array to arduino

    stringToSend = ','.join(str(x) for x in config.arduinoParams) + '\n'
    print('py: ' + stringToSend)  # print python
    stringFromArd = ''
    if config.serialOn:
        config.arduino.write(stringToSend.encode("ascii"))  # send to arduino
        while config.arduino.in_waiting < config.minBytes:  # wait for data
            pass
        stringFromArd = config.arduino.readline().decode("ascii")  # read arduino data
    print('ard: ' + stringFromArd)  # print arduino data

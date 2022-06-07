from time import sleep, time
import pygame
from serial import Serial
from serialWorks2.nav.tracer import start, end, agg

"""
This code is intended for learning purposes. It does not contain any elements of tracer, autonomous, queue, or multiprocessing.

This file is the simplified version of OG nav WITH A DEADBAND implemented.
It pulls a few methods from originalNav and simplifies them.

Go to originalNav to find code that contains everything
"""

#### VARIABLES

serialPort = '/dev/cu.usbmodem14401'
LH = 0  # Left horizontal axis
LV = 1  # Left vertical axis
RH = 2  # Right horizontal axis
RV = 3  # Right vertical axis


deadBand = 0.1  # axis value must be greater than this number to have effect

minBytes = 10  # python waits until there are minBytes amount of bytes in serial buffer, then reads. 
# honestly prob kind of useless since there's either like 26 or 0 bytes in the serial buffer at all times

mapK = 400
tspeedMiddle = 1500
tspeedUp = 1700
tspeedDown = 1300

initSleep = 2
loopSleep = 0.2

JS_X = 0
JS_Y = 0
JS_Y_UD = 0

arduino = None
j = None

arduinoParamsConst = [tspeedMiddle, tspeedMiddle, tspeedMiddle, tspeedMiddle, 0, 0, 0]


#### INITIALIZATION
def init():
    ######################## 1. Initializing Serial
    global arduino  # we have to do "global" because we want to alter the value of the outer scope variables
    arduino = Serial(port=serialPort, baudrate=115200, timeout=1)

    ######################## 2. Initializing PyGame
    pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init()
    global j
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller

    sleep(initSleep)


#### CONTINUOUS LOOP
def loop():

    while True:
        pygame.event.pump()

        get_axises()  # gets the current statuses of the axises, see method below

        turn = JS_X * mapK  # mapK = 400
        forward = JS_Y * mapK
        updown = JS_Y_UD * mapK

        arduinoParams = arduinoParamsConst  # resetting arduinoParams, our constantly updating array

        ##### UP DOWN THRUSTERS (VERTICAL MOVEMENT)
        if abs(JS_Y_UD) > deadBand:
            arduinoParams[2] = int(tspeedMiddle - updown)  # side thrusters
            arduinoParams[3] = int(tspeedMiddle + updown)

        ##### DIRECTIONAL THRUSTERS ("X-Y PLANE" MOVEMENT)
        if abs(JS_X) > deadBand and abs(JS_Y) > deadBand:
            arduinoParams[0] = int(tspeedMiddle - forward + turn)  # left thruster
            arduinoParams[1] = int(tspeedMiddle - forward - turn)  # right thruster
        elif abs(JS_X) > deadBand >= abs(JS_Y):  # only turn
            arduinoParams[0] = int(tspeedMiddle + turn)  # cast to integer
            arduinoParams[1] = int(tspeedMiddle - turn)
        elif abs(JS_X) <= deadBand < abs(JS_Y):
            arduinoParams[0] = int(tspeedMiddle - forward)  # cast to integer
            arduinoParams[1] = int(tspeedMiddle - forward)

        print("tspeeds" + str(arduinoParams))

        serial_send_print(arduinoParams)

        pygame.event.clear()

        sleep(loopSleep)


#### COMMUNICATION PIPELINE W/ THE ARDUINO
def serial_send_print(arr):  # print to terminal / send regularly updated array to arduino

    stringToSend = ','.join(str(x) for x in arr) + '.'  # separates the arr elements with a comma and adds a period at the end
    print('py: ' + stringToSend)  # print python
    
    arduino.write(stringToSend.encode("ascii"))  # send to arduino with ascii encoding (just a type of encoding, you can use any type)
    while (arduino.in_waiting <= minBytes):  # this while loop waits for data to appear before moving on to reading it
        pass
    intbytes = arduino.in_waiting  # number of bytes
    stringFromArd = arduino.readline().decode("ascii")  # read arduino data

    print('ard: ' + stringFromArd + ', ' + str(intbytes))  # print arduino data


#### GETS THE CURRENT POSITIONS OF JOYSTICKS FOR CALCULATIONS
def get_axises():
    global JS_X
    global JS_Y
    global JS_Y_UD

    JS_X = j.get_axis(LH)  # x-axis position on the left joystick for left/right
    JS_Y = j.get_axis(LV)  # y-direction joystick values are flipped
    # y-axis position on the left joystick for forward/backward
    
    JS_Y_UD = j.get_axis(RV)  # y-axis position on the right joystick for depth control (vertical movement)


if __name__ == '__main__':
    init()  # initialization, such as making arduino and serial objects
    loop()

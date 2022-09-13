from time import sleep, time
import pygame
from serial import Serial
from serialWorks2.nav.tracer import start, end, agg

"""
This code is intended for learning purposes. It does not contain any elements of tracer, autonomous, queue, or multiprocessing.

This file is the simplified version of OG nav with NO DEADBAND implemented.
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

initSleep = 2
loopSleep = 0.4

# axis values (constantly updating)
JS_X = 0
JS_Y = 0
JS_Y_UD = 0

arduino = None
j = None

# constantly updating array
arduinoParams = [tspeedMiddle, tspeedMiddle, tspeedMiddle, tspeedMiddle, 0, 0, 0]


#### INITIALIZATION - of arduino and joystick
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


def loop():
    while True:
        pygame.event.pump()

        get_axises()

        turn = JS_X * mapK  # mapK = 400
        forward = JS_Y * mapK
        updown = JS_Y_UD * mapK

        global arduinoParams

        ##### UP DOWN THRUSTERS (VERTICAL MOVEMENT)
        arduinoParams[2] = int(tspeedMiddle - updown)  # side thrusters
        arduinoParams[3] = int(tspeedMiddle + updown)

        ##### DIRECTIONAL THRUSTERS ("X-Y PLANE" MOVEMENT)
        arduinoParams[0] = int(tspeedMiddle - forward + turn)  # left thruster
        arduinoParams[1] = int(tspeedMiddle - forward - turn)  # right thruster

        print("tspeeds" + str(arduinoParams))

        serial_send_print(arduinoParams)

        pygame.event.clear()

        sleep(loopSleep)


#### COMMUNICATION PIPELINE W/ THE ARDUINO
def serial_send_print(arr):  # print to terminal / send regularly updated array to arduino

    # separates the arr elements with a comma and adds a period at the end
    stringToSend = ','.join(str(x) for x in arr) + '.'

    # print python
    print('py: ' + stringToSend)

    # send to arduino with ascii encoding (encoding is basically making it complicated for machine to read it)
    arduino.write(stringToSend.encode("ascii"))

    # this while loop waits for data to appear before moving on to reading it
    while (arduino.in_waiting <= minBytes):
        pass

    # number of bytes in buffer
    intbytes = arduino.in_waiting

    # read complicated arduino data and decode it into readable string format
    stringFromArd = arduino.readline().decode("ascii")

    # print decoded arduino data + number of bytes in buffer
    print('ard: ' + stringFromArd + ', ' + str(intbytes))


#### GETS THE CURRENT POSITIONS OF JOYSTICKS FOR CALCULATIONS
def get_axises():
    global JS_X  # again, global bc we have to alter outer-scope variable
    global JS_Y
    global JS_Y_UD

    JS_X = j.get_axis(LH)  # x-axis position on the left joystick for left/right
    JS_Y = j.get_axis(LV)  # y-direction joystick values are flipped
    # y-axis position on the left joystick for forward/backward

    JS_Y_UD = j.get_axis(RV)  # y-axis position on the right joystick for depth control (vertical movement)


if __name__ == '__main__':
    init()  # initialization, such as making arduino and serial objects
    loop()  # main loop

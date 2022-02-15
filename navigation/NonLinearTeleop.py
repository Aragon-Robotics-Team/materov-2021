# Importing Libraries
import struct

import pygame
import serial
import time
from time import sleep
from struct import *


#global in a function will be visible to the whole program
deadband = 0.2  # axis value must be greater than this number
LH = 0 #Left horizontal axis
LV = 1 #Left vertical axis
RH = 2 #Right horizontal axis
RV = 3 #RIght vertical axis

serialOn = False

turnconstant = 400
forwardconstant = 400
thrustermiddle = 1500
trianglebutton = 12
squarebutton = 15

servocloseindex = 2 #using triangle
servoopenindex = 3 # using square
thrusterleftindex = 0
thrusterrightindex = 1

initsleep = 3
loopsleep = 1/12


def init():
    ######################## 1. Initializing Serial
    if serialOn:
        global arduino
        arduino = serial.Serial(port='/dev/cu.usbmodem14301', baudrate=115200, timeout=1)

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
    sleep(initsleep)

    ######################## 2. Initializing  global variables
    global finallist
    finallist = [thrustermiddle, thrustermiddle, 0, 0]

def loop():
    while True:
        pygame.event.pump()
        #get buttons
        #get thrusters
        #write and read

        buttonclose = j.get_button(trianglebutton)
        buttonopen = j.get_button(squarebutton)
        JS_X = j.get_axis(LH)
        JS_Y = j.get_axis(LV)

        # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
        # turn1, turn2, forward1, forward2 = JS_X * turnconstant, JS_X * turnconstant, JS_Y * forwardconstant, JS_Y * turnconstant
        # calculating thruster speeds
        NL_X = turnconstant*(JS_X**3)
        NL_Y = turnconstant*(JS_Y**3)

        if abs(JS_X) > deadband and abs(JS_Y) > deadband: #calculate thruster values
            thrustervalue1 = int(thrustermiddle + NL_X + NL_Y)
            thrustervalue2 = int(thrustermiddle + (NL_X - NL_Y))
        elif abs(JS_X) > deadband and abs(JS_Y) <= deadband: #only turn
            thrustervalue1 = int(thrustermiddle + NL_X)  # cast to integer
            thrustervalue2 = int(thrustermiddle - NL_X)
        elif abs(JS_X) <= deadband and abs(JS_Y) > deadband: #only forward/back
            thrustervalue1 = int(thrustermiddle - NL_Y)  # cast to integer
            thrustervalue2 = int(thrustermiddle - NL_Y)
        else:
            thrustervalue1 = 1500
            thrustervalue2 = 1500

        # assign statuses to listf
        finallist[servoopenindex] = buttonopen
        finallist[servocloseindex] = buttonclose
        finallist[thrusterleftindex] = thrustervalue1
        finallist[thrusterrightindex] = thrustervalue2

        for i in range(2): # making sure thruster values don't go above 1900 and below 1100
            if finallist[i] > 1900:
                finallist[i] = 1900
            if finallist[i] < 1100:
                finallist[i] = 1100

        # print('values: ' + str(finallist[0]) + ',' + str(finallist[1]) + ',' + str(finallist[2]) + ',' + str(finallist[3]))
        # print(str(thrustervalue1) + ',' + str(thrustervalue2))
        stringToSend = str(finallist[0]) + ',' + str(finallist[1]) + ',' + str(finallist[2]) + ',' + str(finallist[3]) + '\n'
        print('py: ' + str(stringToSend.encode()))
        if serialOn == True:
            arduino.write(stringToSend.encode("ascii"))
            while arduino.in_waiting < 10:
                pass
            data = arduino.readline().decode("ascii")
            print('ard: ' + data)
        pygame.event.clear()
        sleep(loopsleep)
def write_read(): # not using

    # write = str(finallist[0])
    arduino.write(bytes('ewewe', 'utf-8'))
    #str(finallist[0]) + ' ' + str(finallist[1])+ ' ' + str(finallist[2])+ ' ' + str(finallist[3])
    # arduino.write(struct.pack('iiBB', finallist[0], finallist[1], finallist[2], finallist[3]))
    time.sleep(0.5)
    data = arduino.readline().decode('utf-8') # rstrip
    return data


if __name__ == "__main__":
    init()
    loop()
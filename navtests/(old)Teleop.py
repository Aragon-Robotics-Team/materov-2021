# Importing Libraries
import struct

import pygame
import serial
import time
from time import sleep
from struct import *
from pySerialTransfer import pySerialTransfer as txfer


#global in a function will be visible to the whole program
deadband = 0.2  # axis value must be greater than this number
LH = 0 #Left horizontal axis
LV = 1 #Left vertical axis

turnconstant = 300
forwardconstant = 300
thrustermiddle = 1500
trianglebutton = 12
squarebutton = 15

servocloseindex = 2 #using triangle
servoopenindex = 3 # using square
thruster1index = 0
thruster2index = 1


def init():
    ######################## 1. Initializing Serial
    global arduino
    arduino = serial.Serial(port='/dev/cu.usbmodem143101', baudrate=115200, timeout=.1) # ? here or above?

    ######################## 2. Initializing PyGame
    # pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init() # for some reason we have to do this or else it will be an error video system not initialized or something
    global j # making this global might not be the best idea, we have to work on object-oriented programming with python
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller

    print('Detected controller : %s' % j.get_name())  # Print the name of any detected controllers
    pygame.event.set_allowed(pygame.JOYBUTTONUP) # only allow JOYSTICKAXISMOTION events to appear on queue
    pygame.event.set_allowed(pygame.JOYBUTTONDOWN)
    pygame.event.set_allowed(pygame.JOYAXISMOTION)

    ######################## 2. Initializing  global variables
    global finallist
    finallist = [thrustermiddle, thrustermiddle, 0, 0]

def loop():
    while True:
                pygame.event.pump()

                buttonclose, buttonopen = j.get_button(trianglebutton), j.get_button(squarebutton)

                #assign button statuses to list
                finallist[servoopenindex] = buttonopen
                finallist[servocloseindex] = buttonclose

                HAxis, VAxis = j.get_axis(LH), j.get_axis(LV) #get joystick values
                if abs(HAxis) > deadband or abs(VAxis) > deadband: #calculate thruster values
                    # print('x-axis: ' + str(HAxis)) print('y-axis: ' + str(VAxis))
                    turn1, turn2, forward1, forward2 = HAxis * turnconstant, HAxis * turnconstant, VAxis * forwardconstant, VAxis * turnconstant

                    #calculating thruster speeds
                    thrustervalue1 = int(thrustermiddle - forward1 + turn1)  # cast to integer
                    thrustervalue2 = int(thrustermiddle - forward2 - turn2)

                    #assign thruster statuses to list
                    finallist[thruster1index] = thrustervalue1
                    finallist[thruster2index] = thrustervalue2

                print('values: ' + str(finallist[0]) + ',' + str(finallist[1]) + ',' + str(finallist[2]) + ',' + str(finallist[3]))
                pygame.event.clear()  # clears the queue so it doesn't get overloaded...?
                returnVal = write_read()
                print(returnVal)
                print(type(returnVal))
                # if len(returnVal) > 1 : print(returnVal)
                # sleep(0.03)

def write_read():
    write = str(finallist[0])
    arduino.write(bytes('ewewe', 'utf-8'))
    #str(finallist[0]) + ' ' + str(finallist[1])+ ' ' + str(finallist[2])+ ' ' + str(finallist[3])
    # arduino.write(struct.pack('iiBB', finallist[0], finallist[1], finallist[2], finallist[3]))
    time.sleep(0.5)
    data = arduino.readline().decode('utf-8') # rstrip
    return data


if __name__ == "__main__":
    init()
    loop()

    # you can write any string as long as you change the respective settings on the arduino side as well. for example, thrustervalue1 + ',' + thrustervalue2 and on the arduino side, read string until ',' or something

    # have arduino read your values and say it back to make sure its getting them
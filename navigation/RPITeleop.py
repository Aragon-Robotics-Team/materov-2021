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

serialPort = '/dev/cu.usbmodem14101'

serialOn = True
joyTestsOn = True

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
        arduino = serial.Serial(port=serialPort, baudrate=115200, timeout=1)

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

def joytests():
    while joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                        print("X Has Been Pressed") #
                    if event.button == 1:
                        print("Circle has been pressed") #
                    if event.button == 2:
                        print("Right Joystick button has been pressed") #
                    if event.button == 3:
                        print("Square has been pressed. Will exit joytests.") #
                        loop()
                    if event.button == 4:
                        print("Shoulder L1 has been pressed")
                    if event.button == 5:
                        print("Shoulder R1 has been pressed")
                    if event.button == 6:
                        print("Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print("Shoulder R2 has been pressed")
                    if event.button == 8:
                        print("Select has been pressed")
                    if event.button == 9:
                        print("Start has been pressed")
                    if event.button == 10:
                        print("Center has been pressed")
                    if event.button == 11:
                        print("Left Joystick button has been pressed")
                    if event.button == 12: # event.type == pygame.JOYBUTTONUP:
                        print("Triangle Has Been Pressed")
                    if event.button == 13:
                        print("Surface up has been pressed")
                    if event.button == 14:
                        print("Surface bottom has been pressed")
                    if event.button == 15:
                        print("Surface left has been pressed")
                    if event.button == 16:
                        print("Surface Right has been pressed")
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(j.get_axis(0))> deadband:
                    zero = j.get_axis(0)
                    print('0 (left horizontal) has been moved ' + str(zero))
                if event.axis == 1 and abs(j.get_axis(1))> deadband:
                    one = j.get_axis(1)
                    print('1 (left vertical) has been moved ' + str(one))
                if event.axis == 2 and abs(j.get_axis(2))> deadband:
                    two = j.get_axis(2)
                    print('Shoulder L2 has been moved ' + str(two))
                if event.axis == 3 and abs(j.get_axis(3))> deadband:
                    three = j.get_axis(3)
                    print('3 (right vertical) has been moved ' + str(three))
                if event.axis == 4 and abs(j.get_axis(4)) > deadband:
                    four = j.get_axis(4)
                    print('4 (right horizontal) has been moved ' + str(four))

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
        turn1, turn2, forward1, forward2 = JS_X * turnconstant, JS_X * turnconstant, JS_Y * forwardconstant, JS_Y * turnconstant
        # calculating thruster speeds

        if abs(JS_X) > deadband and abs(JS_Y) > deadband: #calculate thruster values
            thrustervalue1 = int(thrustermiddle - forward1 + turn1)  # y-direction joystick values are flipped
            thrustervalue2 = int(thrustermiddle - forward2 - turn2)
        elif abs(JS_X) > deadband and abs(JS_Y) <= deadband: #only turn
            thrustervalue1 = int(thrustermiddle + turn1)  # cast to integer
            thrustervalue2 = int(thrustermiddle - turn2)
        elif abs(JS_X) <= deadband and abs(JS_Y) > deadband:
            thrustervalue1 = int(thrustermiddle - forward1)  # cast to integer
            thrustervalue2 = int(thrustermiddle - forward2)
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

        if j.get_button(0) == 1:
            break
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
    joytests()
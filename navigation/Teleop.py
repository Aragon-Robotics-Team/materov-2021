# Importing Libraries
import pygame
import serial
import time
from time import sleep

#global in a function will be visible to the whole program
deadband = 0.2  # axis value must be greater than this number
arduino = serial.Serial(port='/dev/cu.usbmodem142101', baudrate=115200, timeout=.1)
LH = 0 #Left horizontal axis
LV = 1 #Left vertical axis

turnconstant = 300
forwardconstant = 300
thrustermiddle = 1500


def init():
    ######################## 1. Initializing Serial

    ######################## 2. Initializing PyGame
    # pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init() # for some reason we have to do this or else it will be an error video system not initialized or something
    global j # making this global might not be the best idea, we have to work on object-oriented programming with python
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller
    print('Detected controller : %s' % j.get_name())  # Print the name of any detected controllers
    # pygame.event.set_allowed(pygame.JOYAXISMOTION) # only allow JOYSTICKAXISMOTION events to appear on queue


def loop():
    while True:
                pygame.event.pump()
                HAxis = j.get_axis(LH) #get joystick values
                VAxis = j.get_axis(LV)
                if abs(HAxis) > deadband or abs(VAxis) > deadband: #check for deadband fulfillment
                    print('x-axis: ' + str(HAxis))
                    print('y-axis: ' + str(VAxis))
                    turn1 = HAxis * turnconstant
                    forward1 = VAxis * forwardconstant
                    turn2 = HAxis * turnconstant
                    forward2 = VAxis * turnconstant
                    #calculating thruster speeds
                    thrustervalue1 = int(thrustermiddle - forward1 + turn1)  # cast to integer
                    thrustervalue2 = int(thrustermiddle - forward2 - turn2)

                    print('Thruster value: ' + str(thrustervalue1) + ',' + str(thrustervalue2))

                    #have arduino read your values and say it back to make sure its getting them
                    value = write_read(str(thrustervalue1) + ',' + str(thrustervalue2) + ',')

                    # you can write any string as long as you change the respective settings on the arduino side as well
                    # for example, thrustervalue1 + ',' + thrustervalue2
                    # and on the arduino side, read string until ',' or something

                    print('Arduino reads: ' + value)  # printing the value to make sure values match up with previously printed values
                    pygame.event.clear() # clears the queue so it doesn't get overloaded...?

                    sleep(0.1)  # wait 0.3 seconds so the terminal dont go crazy

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').rstrip()   # rstrip removes whitespace decode decodes, surprisingly
    return data


if __name__ == "__main__":
    init()
    loop()
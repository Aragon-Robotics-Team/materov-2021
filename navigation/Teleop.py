# Importing Libraries
import pygame
import serial
import time
from time import sleep

#global in a function will be visible to the whole program
deadband = 0.2  # axis value must be greater than this number
arduino = serial.Serial(port='/dev/cu.usbmodem141101', baudrate=115200, timeout=.1)
LH = 0 #Left horizontal axis
LV = 1 #Left vertical axis

turn = 500
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
        HAxis = j.get_axis(LH)
        if abs(HAxis) > deadband:
            print(HAxis)
            thrustervalue = int(HAxis * turn + thrustermiddle)  # cast to integer
            print('Thruster value: ' + str(thrustervalue))
            value = write_read(str(thrustervalue))
            print('Arduino reads: ' + value)  # printing the value
            pygame.event.clear() # clears the queue so it doesn't get overloaded...?

        sleep(0.3)  # wait 0.3 seconds so the terminal dont go crazy

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').rstrip() # rstrip removes whitespace decode decodes, surprisingly
    return data


if __name__ == "__main__":
    init()
    loop()
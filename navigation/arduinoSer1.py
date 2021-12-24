# Importing Libraries
import pygame
import serial
import time
from time import sleep


def init():
    # Global variables
    global j
    global deadband
    global arduino
    global LH # Left horizontal axis
    LH = 0
    global LV #Left vertical axis
    LV = 1

    ######################## 1. Initializing Serial
    arduino = serial.Serial(port='/dev/cu.usbmodem142101', baudrate=115200, timeout=.1)

    ######################## 2. Initializing PyGame
    pygame.init()  # Initiate the pygame functions
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller
    print('Detected controller : %s' % j.get_name())  # Print the name of any detected controllers
    pygame.event.set_allowed(pygame.JOYAXISMOTION) # only allow JOYSTICKAXISMOTION events to appear on queue
    deadband = 0.2 # axis value must be greater than this number


def loop():
    while True:
        event = pygame.event.poll() # return a single event from the queue - we limited events to purely JOYAXISMOTION so there is no need to check what type of event it is
        if abs(j.get_axis(LH))  > deadband*2:
            print(pygame.event.event_name(event.type))
            HAxis = j.get_axis(LH)
            thrustervalue = int(HAxis * 500 + 1500)  # cast to integer
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
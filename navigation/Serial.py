# imports
import pygame
import serial
from time import sleep

def init():
    global ser
    ser = serial.Serial('/dev/cu.usbmodem14101', 9600)  # change serial port to ard one, this also opens serial port
    print(ser.name)  # print port name

    # global joystick
    # pygame.joystick.init()  # initialize joystick
    #
    # # getting id print('this is the joystick id' + str(joystick.get_instance_id()))
    #
    # joystick = pygame.joystick.Joystick(0)  # get instance ID and replace '0'?
    #
    # print(str(joystick.get_numaxes()) + '\n')  # number of axes
    #
    # print(joystick.get_init())
    # print(joystick.get_id())
    # print(joystick.get_name())
    # print(joystick.get_numaxes())
    # print(joystick.get_numballs())
    # print(joystick.get_numbuttons())
    # print(joystick.get_numhats())
    # print(joystick.get_axis(0))
    # print(joystick.get_axis(1))
    # print(joystick.get_axis(2))
    # print(joystick.get_axis(3))

def rep():

    while True:  # loops repeatedly
        # joystickValue = joystick.get_axis(3)
            # 3 is the supposed axis name of the right stick up/down axis
        # singleThrusterValue = (joystickValue * 400) + 1500
        # print(singleThrusterValue) #print the thruster speed before sending


        ser.write(bytes(str(1), 'utf-8'))
        print(str(1))
        sleep(3)

        ser.write(bytes(str(0), 'utf-8'))
        print(str(0))
        sleep(1)

if __name__ == "__main__": # for testing purposes: if other classes call a method from this class, will run all these methods
    init()
    rep()

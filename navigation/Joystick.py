# imports
import pygame
import serial
from time import sleep

def init():

    global joystick
    pygame.init()
    # joystick = pygame.joystick.Joystick(pygame.joystick.Joystick.get_instance_id) #for x in range(pygame.joystick.get_count())]  #print out settings

    print(joystick)



    print(str(joystick.get_numaxes()) + '\n') #number of axes

    print(joystick.get_init())
    print(joystick.get_id())
    print(joystick.get_name())
    print(joystick.get_numaxes())
    print(joystick.get_numballs())
    print(joystick.get_numbuttons())
    print(joystick.get_numhats())
    print(joystick.get_axis(0))
    print(joystick.get_axis(1))
    print(joystick.get_axis(2))
    print(joystick.get_axis(3))

def rep():
    while True:  # loops repeatedly

        pygame.event.pump()
        joystickValue = joystick.get_axis(3)
            # 3 is the supposed axis name of the right stick up/down axis
        # singleThrusterValue = (joystickValue * 400) + 1500
        # print(singleThrusterValue) #print the thruster speed before sending
        print(str(joystickValue))

        # ser.write(bytes(str(1), 'utf-8'))
        # print(str(1))
        # sleep(3)
        #
        # ser.write(bytes(str(0), 'utf-8'))
        # print(str(0))
        sleep(0.1)

if __name__ == "__main__": # for testing purposes: if other classes call a method from this class, will run all these methods
    init()
    rep()

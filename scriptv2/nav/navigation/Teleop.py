
# Importing Libraries

"""
CALLED BY CONFIG
"""

from time import sleep
import pygame
import serial

import joy_tests_ps3, joy_tests
# DO NOT IMPORT CONFIG

def joy_init(config):
    ######################## 1. Initializing Serial
    if config.serialOn:
        config.arduino = serial.Serial(port=config.serialPort, baudrate=115200, timeout=1)
    ######################## 2. Initializing PyGame
    pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init()
    config.j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    config.j.init()  # Initiate the joystick or controller
    controllerName = config.j.get_name()
    print('Detected controller : %s' % controllerName)
    print(pygame.joystick.get_count())
    # pygame.event.set_allowed(pygame.JOYBUTTONUP)

    sleep(config.initSleep)

    if controllerName == "Sony PLAYSTATION(R)3 Controller":
        joy_tests_ps3(config)
    else:
        joy_tests(config)


if __name__ == "__main__":
    pass
    # config = PS4Config()
    # joy_init(config)
    # serial_send_print(1, 2, 3, 2, 3, 3, 3)

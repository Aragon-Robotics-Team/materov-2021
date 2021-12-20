# imports
import pygame
import serial
from time import sleep

def init():
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()

    joysticks = []

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    #     offset = 0
    #     for i in range(joystick.get_numaxes() / 2):
    #         joysticks.append(JoystickMonitor(offset))
    #         offset += 200

    # clock = pygame.time.Clock()
    status = True
    while status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.JOYAXISMOTION:
                joystick = pygame.joystick.Joystick(event.joy)
                print(joystick.get_axis(0))
                print(joystick.get_axis(1))
                print(joystick.get_axis(2))
                print(joystick.get_axis(3))
                if event.axis == 0 or event.axis == 1:
                    xaxis = 0
                    yaxis = 1
                    stick = 0
                    x, y = (joystick.get_axis(xaxis) * 100, joystick.get_axis(yaxis) * 100)
                    print(str(joystick.get_axis(yaxis)))
                    print(str(joystick.get_axis(xaxis)))
                    # joysticks[stick].relocateJoystick(x, y)

if __name__ == "__main__": # for testing purposes: if other classes call a method from this class, will run all these methods
    init()

import pygame, sys, time  # Imports Modules
from pygame.locals import *

def example4(): # https://stackoverflow.com/questions/46506850/how-can-i-get-input-from-an-xbox-one-controller-in-python
    import pygame
    from time import sleep
    pygame.init()
    deadband = 0.1
    keepPlaying = True
    print("example4")

    myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
    myjoystick.init()

    while keepPlaying:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: # event.type == pygame.JOYBUTTONUP:
                    print("Select Has Been Pressed")
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    print("Select has been Released")

if __name__ == "__main__":
    example4()

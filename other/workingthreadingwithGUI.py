from tkinter import *
from threading import *
from time import sleep
import pygame, sys, time

root = Tk()

root.geometry("400x400")

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

def threading():
    t1 = Thread(target = joystick)
    t1.start()


# def joystick():
#     while True:
#         print("asdf")
#         sleep(0.1)

def joystick():
    pygame.init()
    joysticks = []
    clock = pygame.time.Clock()
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

def button():
    print("hello")

Button(root, text="Start Controller input", command = threading).pack()

Button(root, text="Click Me", command = button).pack()

init()

root.mainloop()

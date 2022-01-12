#python3 /Users/valeriefan/github/test-materov-2021/other/threadingtest.py
import threading
import pygame, sys, time  # Imports Modules
from time import sleep
from pygame.locals import *
from tkinter import *

# def init():
#     ######################## 1. Initializing Serial
#
#     ######################## 2. Initializing PyGame
#     # pygame.init()  # Initiate the pygame functions
#     pygame.joystick.init()
#     pygame.display.init() # for some reason we have to do this or else it will be an error video system not initialized or something
#     global j # making this global might not be the best idea, we have to work on object-oriented programming with python
#     j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
#     j.init()  # Initiate the joystick or controller
#     print('Detected controller : %s' % j.get_name())  # Print the name of any detected controllers
#     # pygame.event.set_allowed(pygame.JOYAXISMOTION) # only allow JOYSTICKAXISMOTION events to appear on queue

def joystick():
    print("asdf")
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
                    if event.button == 1:
                        print("Left Joystick button has been pressed")
                    if event.button == 2:
                        print("Right Joystick button has been pressed")
                    if event.button == 3:
                        print("Start has been pressed")
                    if event.button == 4:
                        print("Surface top button has been pressed")
                    if event.button == 5:
                        print("Surface right button has been pressed")
                    if event.button == 6:
                        print("Surface Bottom Has Been Pressed")
                    if event.button == 7:
                        print("Surface left button has been pressed")
                    if event.button == 8:
                        print("Left 2 has been pressed")
                    if event.button == 9:
                        print("Right 2 has been pressed")
                    if event.button == 10:
                        print("Left 1 has been pressed")
                    if event.button == 11:
                        print("Right 1 has been pressed")
                    if event.button == 12: # event.type == pygame.JOYBUTTONUP:
                        print("Triangle Has Been Pressed")
                    if event.button == 13:
                        print("Circle has been pressed")
                    if event.button == 14:
                        print("X has been pressed")
                    if event.button == 15:
                        print("Square has been pressed")
                    if event.button == 16:
                        print("Center PS has been pressed")
            # elif event.type == pygame.JOYAXISMOTION:
            #     if event.axis == 0 and abs(myjoystick.get_axis(0))> deadband:
            #         one = myjoystick.get_axis(0)
            #         print('1 has been moved ' + str(one))
            #     if event.axis == 1 and abs(myjoystick.get_axis(1))> deadband:
            #         two = myjoystick.get_axis(1)
            #         print('2 has been moved ' + str(two))
            #     if event.axis == 2 and abs(myjoystick.get_axis(2))> deadband:
            #         three = myjoystick.get_axis(2)
            #         print('3 has been moved ' + str(three))
            #     if event.axis == 3 and abs(myjoystick.get_axis(3))> deadband:
            #         four = myjoystick.get_axis(3)
            #         print('4 has been moved ' + str(four))

# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline().decode('utf-8').rstrip() # rstrip removes whitespace decode decodes, surprisingly
#     return data

def asdf():
    print("hello")


cont1 = True
top = Tk()
btn = Button(top, text = "hello", command = asdf)
btn.pack()
top.mainloop()


if __name__ == "__main__":
    t1 = threading.Thread(target = joystick)
    t2 = threading.Thread(target = gui)

    # init()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

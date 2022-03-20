
import sys

import pygame
import keyboard


from pygame.locals import *

from time import sleep
pygame.init()
deadband = 0.1
keepPlaying = True
print("example4")

# pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)
clock = pygame.time.Clock()
#
# pygame.joystick.init()
# joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
# for joystick in joysticks:
#     print(joystick.get_name())

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
motion = [0, 0]

myjoystick = pygame.joystick.Joystick(0) #since we only have one joystick, we know the instance ID is 0
myjoystick.init()

while True:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, colors[my_square_color], my_square)
    if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10

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
        elif event.type == pygame.JOYAXISMOTION:
            #print(event)
            if event.axis < 2:
                motion[event.axis] = event.value
            if event.axis == 0 and abs(myjoystick.get_axis(0))> deadband:
                zero = myjoystick.get_axis(0)
                print('1 has been moved ' + str(zero))
            if event.axis == 1 and abs(myjoystick.get_axis(1))> deadband:
                one = myjoystick.get_axis(1)
                print('2 has been moved ' + str(one))
            if event.axis == 2 and abs(myjoystick.get_axis(2))> deadband:
                two = myjoystick.get_axis(2)
                print('3 has been moved ' + str(two))
            if event.axis == 3 and abs(myjoystick.get_axis(3))> deadband:
                three = myjoystick.get_axis(3)
                print('4 has been moved ' + str(three))
            if event.axis == 4 and abs(myjoystick.get_axis(4)) > deadband:
                four = myjoystick.get_axis(4)
                print('4 has been moved ' + str(four))

#
# while True:
#
#     screen.fill((0, 0, 0))
#
#     pygame.draw.rect(screen, colors[my_square_color], my_square)
#     if abs(motion[0]) < 0.1:
#         motion[0] = 0
#     if abs(motion[1]) < 0.1:
#         motion[1] = 0
#     my_square.x += motion[0] * 10
#     my_square.y += motion[1] * 10
#
#     for event in pygame.event.get():
#         if keyboard.read_key() == "s":
#             print(event)
#             if event.button == 0:
#                 my_square_color = (my_square_color + 1) % len(colors)
#         if keyboard.read_key() == "w":
#             print(event)
#         if event.type == JOYAXISMOTION:
#             print(event)
#             if event.axis < 2:
#                 motion[event.axis] = event.value
#         if event.type == JOYHATMOTION:
#             print(event)
#         if event.type == JOYDEVICEADDED:
#             joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
#             for joystick in joysticks:
#                 print(joystick.get_name())
#         if event.type == JOYDEVICEREMOVED:
#             joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()
#
#     pygame.display.update()
#     clock.tick(60)

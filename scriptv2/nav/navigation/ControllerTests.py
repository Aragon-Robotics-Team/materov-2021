
# Importing Libraries

"""
CALLED BY TELEOP
"""

from time import sleep
import pygame
import LinearLoop, NonLinearLoop


def joy_tests_ps3(config):
    while config.joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    print("X Has Been Pressed")
                if event.button == 1:
                    print("Circle has been pressed")
                if event.button == 2:
                    print("Triangle has been pressed")
                if event.button == 3:
                    print("Square has been pressed.")
                if event.button == 4:
                    print("Shoulder L1 has been pressed")
                if event.button == 5:
                    print("Shoulder R1 has been pressed")
                if event.button == 6:
                    print("Surface Bottom Has Been Pressed")
                if event.button == 7:
                    print("Shoulder R2 has been pressed")
                if event.button == 8:
                    print("Share has been pressed")
                if event.button == 9:
                    print("Start has been pressed. Will exit joytests")
                    LinearLoop(config)  # starts loop()
                if event.button == 10:
                    print("Center has been pressed")
                    NonLinearLoop(config)
                if event.button == 11:
                    print("Left Joystick button has been pressed")
                if event.button == 12:
                    print("Right Joystick button Has Been Pressed")
                if event.button == 13:
                    print("Surface up has been pressed")
                if event.button == 14:
                    print("Surface bottom has been pressed")
                if event.button == 15:
                    print("Surface left has been pressed")
                if event.button == 16:
                    print("Surface Right has been pressed")
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(config.j.get_axis(0)) > config.deadBand:
                    zero = config.j.get_axis(0)
                    print('0 (left horizontal) has been moved ' + str(zero))
                if event.axis == 1 and abs(config.j.get_axis(1)) > config.deadBand:
                    one = config.j.get_axis(1)
                    print('1 (left vertical) has been moved ' + str(one))
                if event.axis == 2 and abs(config.j.get_axis(2)) > config.deadBand:
                    two = config.j.get_axis(2)
                    print('Shoulder L2 has been moved ' + str(two))
                if event.axis == 3 and abs(config.j.get_axis(3)) > config.deadBand:
                    three = config.j.get_axis(3)
                    print('3 (right vertical) has been moved ' + str(three))
                if event.axis == 4 and abs(config.j.get_axis(4)) > config.deadBand:
                    four = config.j.get_axis(4)
                    print('4 (right horizontal) has been moved ' + str(four))


def joy_tests(config):
    while config.joyTestsOn:
        sleep(0.1)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                    print("Select Has Been Pressed")
                if event.button == 1:
                    print("Left Joystick button has been pressed")
                if event.button == 2:
                    print("Right Joystick button has been pressed")
                if event.button == 3:
                    print("Start has been pressed. Will exit joytests.")
                    LinearLoop(config)
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
                if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                    print("Triangle Has Been Pressed")
                if event.button == 13:
                    print("Circle has been pressed")
                if event.button == 14:
                    print("X has been pressed")
                if event.button == 15:
                    print("Square has been pressed")
                if event.button == 16:
                    print("Center PS has been pressed")
                    NonLinearLoop(config)
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and abs(config.j.get_axis(0)) > config.deadBand:
                    zero = config.j.get_axis(0)
                    print('1 has been moved ' + str(zero))
                if event.axis == 1 and abs(config.j.get_axis(1)) > config.deadBand:
                    one = config.j.get_axis(1)
                    print('2 has been moved ' + str(one))
                if event.axis == 2 and abs(config.j.get_axis(2)) > config.deadBand:
                    two = config.j.get_axis(2)
                    print('3 has been moved ' + str(two))
                if event.axis == 3 and abs(config.j.get_axis(3)) > config.deadBand:
                    three = config.j.get_axis(3)
                    print('4 has been moved ' + str(three))
                if event.axis == 4 and abs(config.j.get_axis(4)) > config.deadBand:
                    four = config.j.get_axis(4)
                    print('x has been moved ' + str(four))

# if __name__ == '__main__':
#     config = PS4Config()
#     joy_init(config)

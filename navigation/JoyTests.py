import pygame, sys, time  # Imports Modules
from pygame.locals import *


def example3(): # http://programarcadegames.com/python_examples/show_file.php?file=joystick_calls.py

    """
    Sample Python/Pygame Programs
    Simpson College Computer Science
    http://programarcadegames.com/
    http://simpson.edu/computer-science/

    Show everything we can pull off the joystick
    """
    import pygame

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


    class TextPrint(object):
        """
        This is a simple class that will help us print to the screen
        It has nothing to do with the joysticks, just outputting the
        information.
        """

        def __init__(self):
            """ Constructor """
            self.reset()
            self.x_pos = 10
            self.y_pos = 10
            self.font = pygame.font.Font(None, 20)

        def print(self, my_screen, text_string):
            """ Draw text onto the screen. """
            text_bitmap = self.font.render(text_string, True, BLACK)
            my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
            self.y_pos += self.line_height

        def reset(self):
            """ Reset text to the top of the screen. """
            self.x_pos = 10
            self.y_pos = 10
            self.line_height = 15

        def indent(self):
            """ Indent the next line of text """
            self.x_pos += 10

        def unindent(self):
            """ Unindent the next line of text """
            self.x_pos -= 10


    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [500, 700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Initialize the joysticks
    pygame.joystick.init()

    # Get ready to print
    textPrint = TextPrint()

    # -------- Main Program Loop -----------
    while not done:
        # EVENT PROCESSING STEP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
            # JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

        # DRAWING STEP
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        textPrint.reset()

        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()

        textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
        textPrint.indent()

        # For each joystick:
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()

            textPrint.print(screen, "Joystick {}".format(i))
            textPrint.indent()

            # Get the name from the OS for the controller/joystick
            name = joystick.get_name()
            textPrint.print(screen, "Joystick name: {}".format(name))

            # Usually axis run in pairs, up/down for one, and left/right for
            # the other.
            axes = joystick.get_numaxes()
            textPrint.print(screen, "Number of axes: {}".format(axes))
            textPrint.indent()

            for i in range(axes):
                axis = joystick.get_axis(i)
                textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
            textPrint.unindent()

            buttons = joystick.get_numbuttons()
            textPrint.print(screen, "Number of buttons: {}".format(buttons))
            textPrint.indent()

            for i in range(buttons):
                button = joystick.get_button(i)
                textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
            textPrint.unindent()

            # Hat switch. All or nothing for direction, not like joysticks.
            # Value comes back in an array.
            hats = joystick.get_numhats()
            textPrint.print(screen, "Number of hats: {}".format(hats))
            textPrint.indent()

            for i in range(hats):
                hat = joystick.get_hat(i)
                textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
            textPrint.unindent()

            textPrint.unindent()

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

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
                if event.axis == 0 and abs(myjoystick.get_axis(0))> deadband:
                    one = myjoystick.get_axis(0)
                    print('1 has been moved ' + str(one))
                if event.axis == 1 and abs(myjoystick.get_axis(1))> deadband:
                    two = myjoystick.get_axis(1)
                    print('2 has been moved ' + str(two))
                if event.axis == 2 and abs(myjoystick.get_axis(2))> deadband:
                    three = myjoystick.get_axis(2)
                    print('3 has been moved ' + str(three))
                if event.axis == 3 and abs(myjoystick.get_axis(3))> deadband:
                    four = myjoystick.get_axis(3)
                    print('4 has been moved ' + str(four))

def example10():
    import pygame
    pygame.joystick.init()
    pygame.display.init()
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()

    # Prints the values for axis0
    while True:
        pygame.event.pump()
        print("x axis: ", j.get_axis(0))
        print("y axis: ", j.get_axis(1))
        print("y axis: ", j.get_axis(2))
        print("y axis: ", j.get_axis(3))
        pygame.event.clear()


def example5():
    pygame.display.init()
    pygame.joystick.init()
    pygame.joystick.Joystick(0).init()

    # Prints the joystick's name
    JoyName = pygame.joystick.Joystick(0).get_name()
    print("Name of the joystick:")
    print(JoyName)
    # Gets the number of axes
    JoyAx = pygame.joystick.Joystick(0).get_numaxes()
    print("Number of axis:")
    print(JoyAx)

    # Prints the values for axis0
    while True:
        pygame.event.pump()
        print(pygame.joystick.Joystick(0).get_axis(0))

def example6():
    #http://programarcadegames.com/python_examples/show_file.php?file=joystick_calls.py
    import pygame
    from time import sleep
    pygame.init()
    pygame.joystick.init()
    done = False
    while not done:
        sleep(0.1)
        for event in pygame.event.get():
            joystick_count = pygame.joystick.get_count() # = 1
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)
                print(str(axis))

def example7(): #http://programarcadegames.com/python_examples/show_file.php?file=joystick_calls.py
    import pygame
    from time import sleep
    pygame.init()
    pygame.joystick.init()
    done = False
    while not done:
        sleep(0.1)
        for event in pygame.event.get():
            joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
        LH = joystick.get_axis(0)
        LV = joystick.get_axis(1)
        RH = joystick.get_axis(2)
        RV = joystick.get_axis(3)
        print("LH: " + str(LH) + "; LV: " + str(LV) + "; RH: " + str(RH) + "; RV: " + str(RV))
def customevent():
    # put at the top your code

    import pygame
    pygame.init()

    GUIBUTTON = pygame.USEREVENT + 1
    NEWGUIBUTTON = pygame.event.Event(GUIBUTTON)
    pygame.event.post(NEWGUIBUTTON)

    # put in a new method
    import pygame
    pygame.init()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.GUIBUTTON:
                print('GUI button pressed')




if __name__ == "__main__":
    example4()

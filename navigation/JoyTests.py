import pygame, sys, time  # Imports Modules
from pygame.locals import *

def example1(): # https://www.programcreek.com/python/example/56152/pygame.JOYAXISMOTION (example 8)
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
                elif event.axis == 3 or event.axis == 4:
                    xaxis = 4
                    yaxis = 3
                    stick = 1
                    x, y = (joystick.get_axis(xaxis) * 100, joystick.get_axis(yaxis) * 100)
                    print(str(joystick.get_axis(yaxis)))
                    print(str(joystick.get_axis(xaxis)))
                    # joysticks[stick].relocateJoystick(x, y)

def example2(): # https://stackoverflow.com/questions/62568024/pygame-raspberrypi-3b-with-a-ps3-controller
    pygame.init()  # Initializes Pygame

    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()  # Initializes Joystick

    # get count of joysticks=1, axes=27, buttons=19 for DualShock 3

    joystick_count = pygame.joystick.get_count()
    print("joystick_count")
    print(joystick_count)
    print("--------------")

    numaxes = joystick.get_numaxes()
    print("numaxes")
    print(numaxes)
    print("--------------")

    numbuttons = joystick.get_numbuttons()
    print("numbuttons")
    print(numbuttons)
    print("--------------")

    name = joystick.get_name()
    print('name')
    print(name)
    print('--------------')


    loopQuit = False
    while loopQuit == False:

        # test joystick axes and prints values

        for i in range(0, 4):
            outstr = ""
            axis = joystick.get_axis(i)
            outstr = "axis " + outstr + str(i) + ":" + str(axis) + "|"
            print(outstr)

        # test controller buttons
        outstr = ""
        # for i in range(0, numbuttons):
        #     button = joystick.get_button(i)
        #     outstr = outstr + str(i) + ":" + str(button) + "|"
        # print(outstr)

        for event in pygame.event.get():
            if event.type == QUIT:
                loopQuit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loopQuit = True

            # Returns Joystick Button Motion
            if event.type == pygame.JOYBUTTONDOWN:
                print("joy button down")
            if event.type == pygame.JOYBUTTONUP:
                print("joy button up")
            if event.type == pygame.JOYBALLMOTION:
                print("joy ball motion")
            # axis motion is movement of controller
            # dominates events when used
            if event.type == pygame.JOYAXISMOTION:
                print("joy axis motion")

        time.sleep(0.3)
    pygame.quit()
    sys.exit()

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
    joysticks = []
    clock = pygame.time.Clock()
    keepPlaying = True
    print("example4")


    # for al the connected joysticks
    for i in range(0, pygame.joystick.get_count()):
        # create an Joystick object in our list
        joysticks.append(pygame.joystick.Joystick(i))
        # initialize them all (-1 means loop forever)
        joysticks[-1].init()
        # print a statement telling what the name of the controller is
        print("Detected joystick "), joysticks[-1].get_name(), "'"
    while keepPlaying:
        clock.tick(20)
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONUP:
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
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    one = event.get_axis(0)
                    print('1 has been moved ' + str(one))
                if event.axis == 1:
                    two = event.get_axis(1)
                    print('2 has been moved ' + str(two))
                if event.axis == 2:
                    three = pygame.joystick.get_axis(2)
                    print('3 has been moved ' + str(three))
                if event.axis == 3:
                    four = pygame.joystick.get_axis(3)
                    print('4 has been moved ' + str(four))



if __name__ == "__main__":
    example4()
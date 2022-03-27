
from nav.teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from nav.tracer import agg

def teleopMain():
    robot = Config('Mac', True, False) # comp type, serial on, serial recieve on
    #robot = teleopConfig1.Config('Mac', True, False)
    robot.joy_init()

if __name__ == '__main__':
    teleopMain()

#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

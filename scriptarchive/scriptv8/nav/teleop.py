from teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from tracer import agg
def teleopMain():
    robot = Config('Mac', True, False) # comp type, serial on, serial recieve on
    robot.joy_init()
    
if __name__ == '__main__':
    teleopMain()

#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

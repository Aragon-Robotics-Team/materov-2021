from teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from tracer import agg
def main():
    robot = Config('Mac', True, False) # comp type, serial on, serial recieve on
    robot.joy_init()

if __name__ == '__main__':
    main()

#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

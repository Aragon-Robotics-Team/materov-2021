from newnavigation.teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from tracer import agg
def main():
    robot = Config('Mac', False)
    robot.joy_init()
if __name__ == '__main__':
    main()


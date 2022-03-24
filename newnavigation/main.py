from teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from tracer import agg
def main():
    robot = Config('RPI', True)
    robot.joy_init()
    
if __name__ == '__main__':
    main()

#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

from navigationSingleFile.teleopConfig1 import Config
from tracer import agg
def main():
    robot = Config()
    robot.joy_init()
if __name__ == '__main__':
    main()


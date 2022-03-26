from teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from tracer import agg
def main():
<<<<<<< HEAD
    robot = Config('RPI', True)
=======
    robot = Config('Mac', True, False) # comp type, serial on, serial recieve on
>>>>>>> 324450329a7416b7c8b94eaaccd84516cde55965
    robot.joy_init()
    
if __name__ == '__main__':
    main()

#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

from teleopConfig1 import Config  # rpi imports
# from serialWorks.nav.teleopConfig1 import Config
def teleopMain():
    robot = Config('RPI', True, True) # comp type, serial on, serial recieve on
    robot.joy_init()
    
if __name__ == '__main__':
    teleopMain()

#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

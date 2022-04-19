from scriptarchive.serialWorks.nav.teleopConfig1 import Config  # on rpi, DELETE navNoQueue part
# from tracer import agg
def teleopMain():
    robot = Config('Mac', True, True) # comp type, serial on, serial recieve on
    robot.joy_init()
    
if __name__ == '__main__':
    teleopMain()

#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


"""
Configuration for everything
"""
from navigation.Teleop import joy_init


class Config():
    def __init__(self):
        self.serialOn = False
        self.joyTestsOn = True
        self.deadBand = 0.07  # axis value must be greater than this number
        self.LH = 0  # Left horizontal axis
        self.LV = 1  # Left vertical axis
        self.RH = 3  # Right horizontal axis
        self.RV = 4  # Right vertical axis

        self.SpeedSize = 4
        self.MaxSpeed = 1900
        self.MinSpeed = 1100

        self.serialPort = '/dev/ttyACM0'
        self.minBytes = 10

        self.mapK = 400
        self.tspeedMiddle = 1500
        self.tspeedUp = 1700
        self.tspeedDown = 1300

        self.startButton = 9  # starts loop()
        self.shareButton = 8  # exits loop()

        self.initSleep = 3
        self.loopSleep = 1/25

        self.arduinoParams = [self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, self.tspeedMiddle, 0, 0, 0]  #this array keeps updating thruster values
        self.arduino = None
        self.j = None

class PS4Config(Config):
    def __init__(self):
        Config.__init__(self)
        # this is for the ps4 controller
        self.squareButton = 3  # button open
        self.triangleButton = 2  # button close
        self.circleButton = 1  # up constant speed
        self.xButton = 0  # down constant speed

class PS3Config(Config):
    def __init__(self):
        Config.__init__(self)
        # this is for the ps3 controller
        self.squareButton = 15  # button open
        self.triangleButton = 12  # button close
        self.circleButton = 13  # up constant speed
        self.xButton = 14  # down constant speed

if __name__ == "__main__":
    config = PS4Config()
    joy_init(config)

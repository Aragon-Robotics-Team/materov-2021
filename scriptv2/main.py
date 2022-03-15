#insert import statements
import glob
import gui #use gui.top.update()

from video_input import photomosaic

from scriptv2.nav.teleopConfig import PS3Config
from scriptv2.nav.navigation.Teleop import joy_init

#joy_init() #for controllers


# t1 = threading.Thread(target=joytests) <-- doesn't work because pygame is not threadsafe
# t1.start()
#
# t1 = threading.Thread(target = video)
# t1.start()

if __name__ == "__main__":
    config = PS3Config()
    joy_init(config)
    while True:
        #joytests() #<-- Fatal error sometimes?????
        #imgqueue.queue() #<-- same effect as directly calling the video module; it lags bc the images are being shown and the controller
        #is being checked at the same time
        gui.root.update()
        if glob.photomosaicVideo == True:
            photomosaic()
        # else:
        #     general_video()
        #video.general_video()


#MOVE TELEOP/SERIAL (WITH SLEEP) IN ONE PROCESS, EVEYRTHING ELSE IN ANOTHER PROCESS <-- ISOLATE SLEEP IN ONE PROCESS TO AVOID LAG
#In order to match up the two processes and avoid impedance mismatch. Only add event into the queue
#if the queue is empty, that way, only the events that the teleop/serial process can run at the time is added in, so there is no built up lag
#Use priority queue to make sure the new command in queue has priority

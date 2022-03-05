#insert import statements
import glob
import gui #use gui.top.update()

import cv2
from video_input import general_video
from video_input import photomosaic

from nav.controller import joy_init
from nav.controller import joytests
import threading

from img_proc import imgqueue

#joy_init() #for controllers

# t1 = threading.Thread(target=joytests) <-- doesn't work because pygame is not threadsafe
# t1.start()
#
# t1 = threading.Thread(target = video)
# t1.start()

if __name__ == "__main__":
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


#MOVE TELEOP AND AUTONOMOUS TO ANOTHER PROCESS

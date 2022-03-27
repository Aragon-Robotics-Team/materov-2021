#insert import statements
#import glob
import gui #use gui.root.update()


import cv2
from video_input import general_video
from video_input import photomosaic

from nav.controller import joy_init
from nav.controller import joytests
import threading

from img_proc import imgqueue

import multiprocessing
#joy_init() #for controllers

# t1 = threading.Thread(target=joytests) <-- doesn't work because pygame is not threadsafe
# t1.start()
#
# t1 = threading.Thread(target = video)
# t1.start()
#
# if __name__ == "__main__":
#         #joytests() #<-- Fatal error sometimes?????
#         #imgqueue.queue() #<-- same effect as directly calling the video module; it lags bc the images are being shown and the controller
#         #is being checked at the same time
#         gui.root.update()
#         if glob.photomosaicVideo == True:
#             photomosaic()
#         # else:
#         #     general_video()
#         #video.general_video()

class Thruster(multiprocessing.Process):
    def __init__ (self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        proc_name = self.name
        print("starting joy init")
        joy_init()
        print("starting joy tests")
        i = 0
        while i<6:
            self.joytests()
            i = i + 1
            #status = self.input_

class GUI_proc(multiprocessing.Process):
    def __init__ (self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        proc_name = self.name
        while True:
            # print(gui.hello)
            #gui.root.update()
            gui.root.update()
            #updateGUI()

#multiprocessing.set_start_method('spawn')
if __name__ == "__main__":

    thruster_in_queue = multiprocessing.Queue() #input the autonomous output
    thruster_out_queue = multiprocessing.Queue() #output the controller values

    #multiprocessing.set_start_method('spawn')

    gui_obj = GUI_proc(thruster_out_queue, thruster_in_queue)
    #gui_obj.__init()

    gui_obj.run()

    #gui.updateGUI()
    #thruster = Thruster(thruster_in_queue, thruster_out_queue)
    #thruster.start()

    #multiprocessing.set_start_method('spawn')

#MOVE TELEOP/SERIAL (WITH SLEEP) IN ONE PROCESS, EVEYRTHING ELSE IN ANOTHER PROCESS <-- ISOLATE SLEEP IN ONE PROCESS TO AVOID LAG
#In order to match up the two processes and avoid impedance mismatch. Only add event into the queue
#if the queue is empty, that way, only the events that the teleop/serial process can run at the time is added in, so there is no built up lag
#Use priority queue to make sure the new command in queue has priority

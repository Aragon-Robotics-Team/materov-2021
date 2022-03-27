import multiprocessing
#import gui
import guiv2

from time import sleep

#import cv2
from video_input import general_video
from video_input import photomosaic

from nav.controller import joy_init
from nav.controller import joytests
import threading

#from img_proc import imgqueue


class ThrusterProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        while True:
            msg = self.input_queue.get()
            print(msg)
            #print ("hello")


class GUIProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        p = multiprocessing.Process(target = guiv2.appStart)
        p.start()

            #guiv2.guiStart()
            # gui.updateGUI()
            # #gui.root.mainloop()
            # self.output_queue.put("hello") #queue works :)))


if __name__ == "__main__":
    thruster_in_queue = multiprocessing.Queue() #input the autonomous output
    thruster_out_queue = multiprocessing.Queue() #output the controller values

    gui_proc = GUIProcess(thruster_out_queue, thruster_in_queue)
    gui_proc.start()

    sleep(0.1)

    thruster_proc = ThrusterProcess(thruster_in_queue, thruster_out_queue)
    thruster_proc.start()

import gui #use gui.root.update()

import cv2
from video_input import general_video
from video_input import photomosaic

from nav.controller import joy_init
from nav.controller import joytests
import threading

from img_proc import imgqueue

import multiprocessing

class ThrusterProcess(multiprocessing.Process):
    def __init__ (self, input_queue, output_queue):
        print("Started Thruster Process")
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def start(self):
        process = multiprocessing.Process(target = self.run)
        process.start()
    def run(self):
        print("starting joy init")
        print("starting joy tests")
        proc_name = self.name
        #joy_init()
        i = 0
        while True:
            print("trhuster")
        #     self.joytests()
        #     i = i + 1
        #     #status = self.input_

class GUIProcess(multiprocessing.Process, gui):
    #import gui
    def __init__ (self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        gui.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    #def start(self):
        #multiprocessing.set_start_method('spawn')
        #process = multiprocessing.Process(target = self.run)
        #process.start()
    def run(self):
        print("Starting GUI Process")
        proc_name = self.name
        print("past name")
        gui.root.mainloop()
        # while True:
        #     # print(gui.hello)
        #     #gui.root.update()
        #     gui.root.update()
        #     #updateGUI()
    def stop(self):
        self.run = False

#multiprocessing.set_start_method('spawn')
if __name__ == "__main__":

    thruster_in_queue = multiprocessing.Queue() #input the autonomous output
    thruster_out_queue = multiprocessing.Queue() #output the controller values

    #multiprocessing.set_start_method('spawn')

    gui_proc = GUIProcess(thruster_out_queue, thruster_in_queue)
    #gui_obj.__init()
    #thruster_proc = ThrusterProcess(thruster_in_queue, thruster_in_queue)

    #thruster_proc.start()
    gui_proc.start()
    #gui_proc.stop()
    #thruster_proc.run()
    #gui_proc.run()
    #thruster_proc.run()

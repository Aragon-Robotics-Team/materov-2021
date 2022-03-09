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

import platform

def ThrusterProcess():
    print("Starting joy tests")
    teleop = True
    autonomous = True
    automode = ""
    while True:
        print("thruster")
        #if teleop == True:
            #joytests() #<-- in the future just have this be the code that goes from teleop calcs to serial
        #for autonomous, change it so that the it takes info from the queue (auto = queue.get) and changes to calculations

def GUIProcess():
    #print("gui")
    gui.root.mainloop()

if __name__ == "__main__":
    # if platform.system() == "Darwin":
    #     multiprocessing.set_start_method('spawn')
    thruster_proc = multiprocessing.Process(target = ThrusterProcess)
    gui_proc = multiprocessing.Process(target = GUIProcess)

    #joy_init()
    gui_proc.start()
    #thruster.start()

    gui_proc.stop()

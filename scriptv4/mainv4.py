import gui #use gui.root.update()


import cv2
from video_input import general_video
from video_input import photomosaic

from nav.controller import joy_init
from nav.controller import joytests
import threading

from img_proc import imgqueue

import multiprocessing

def GUIProcess():
    gui.root.mainloop()

gui_proc = multiprocessing.Process(target = GUIProcess)
gui_proc.start()

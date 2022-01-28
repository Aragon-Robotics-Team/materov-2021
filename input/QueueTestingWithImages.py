#general imports
import threading
import queue
#gui imports
import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar

import cv2

#set up GUI
root = tk.Tk()
root.config(bg ='gray')

q = queue.Queue()

def helloWorldThreading():
    threading.Thread(target=helloWorld).start()

def helloWorld():
    item = cv2.imread("/Users/valeriefan/Desktop/lines2.jpg")
    q.put(item)

def queue(): #Needs forever loop, therefore can't use root.mainloop()
    if q.empty() == False:
        item = q.get()
        cv2.imshow("Threading Image", item)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        q.task_done()

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()

Result = True
while Result:
    #sleep(0.1)
    root.update()
    queue()

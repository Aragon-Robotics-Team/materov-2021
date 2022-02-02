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

#set up GUI
root = tk.Tk()
root.config(bg ='gray')

q = queue.Queue()

def helloWorldThreading():
    threading.Thread(target=helloWorld).start()

def helloWorld():
    item = "Hello World"
    q.put(item)

def queue(): #Needs forever loop, therefore can't use root.mainloop()
    if SimpleQueue.empty() == False:
        item = q.get()
        print("From Queue: " + item)
        print("From Queue: " + item)
        q.task_done()

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()

Result = True
while Result:
    #sleep(0.1)
    root.update()
    queue()

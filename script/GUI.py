import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import queue

from imageprocessing import measurefish
from imageprocessing import photomosaic

#GUI SETUP
root = tk.Tk()
root.config(bg ='gray')

#measure fish
Bu = tk.Button(root, text="Measure Fish (Click to 3 times to take photos and calculate)", command = measurefish.measureFishie).pack()
Bu = tk.Button(root, text="Reset Fish Measuring", command = measurefish.resetMeasureFish).pack()

#photomosaic
Bu  = tk.Button(root, text = "Photomosaic", command = photomosaic.photomosaicThreading).pack()

def helloWorld():
    print("helloWorld")

Bu = tk.Button(root, text="Hello World", command = helloWorld).pack()

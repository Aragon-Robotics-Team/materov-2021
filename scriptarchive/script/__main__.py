#GUI Imports
import tkinter as tk
import time
import sys
import os
import tkinter.font as font
from tkinter import messagebox, RIGHT, LEFT, StringVar
import queue

#Pygame imports
import pygame
from time import sleep

#Image Processing imports
import numpy as np
import threading
import cv2
import imutils
import keyboard
import math

#files
from imageprocessing import measurefish
from imageprocessing import photomosaic
import controller
import GUI
import videocapture
import queuemodule

Result = True
while Result:
    #controller()
    videocapture.videoCapture()
    queuemodule.queue()
    GUI.root.update()

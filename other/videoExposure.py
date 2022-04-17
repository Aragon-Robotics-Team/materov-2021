import arducam_mipicamera as arducam
import v4l2 #sudo pip install v4l2
import time
import cv2 #sudo apt-get install python-opencv
# import RPi.GPIO as gp
import sys
import os

def set_controls(camera):
    try:
        print("Reset the focus...")
        camera.reset_control(v4l2.V4L2_CID_FOCUS_ABSOLUTE)
    except Exception as e:
        print(e)
        print("The camera may not support this control.")
    try:
        print("Enable Auto Exposure...")
        camera.software_auto_exposure(enable = True)
        print("Enable Auto White Balance...")
        camera.software_auto_white_balance(enable = True)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Open the first channel of I2c
    # switch_camera('A')
    camera = arducam.mipi_camera()
    print("Open camera...")
    camera.init_camera()
    # print("Setting the resolution...")
    # fmt = init_all_camera(camera, 1920, 1080)
    # switch to A channel
    # index = ord('A')
    # switch_camera(chr(index))
    camera.set_control(v4l2.V4L2_CID_EXPOSURE, 12000)
    # switch to B channel
    # index = ord('B')

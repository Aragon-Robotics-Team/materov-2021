from __future__ import print_function
import cv2
import time
import numpy as np
# import numpy as np
import argparse
# import cv2

result = True

GSTREAMER_PIPELINE = "nvarguscamerasrc sensor-mode=0   exposuretimerange='1000000 1000000' wbmode=0 gainrange='1 1' ispdigitalgainrange='1 1' tnr-mode=2 tnr-strength=1.0 ee-mode=2 ! video/x-raw(memory:NVMM), width=(int)3264, height=(int)2464,format=(string)NV12, framerate=(fraction)21/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !  appsink"
# arducam_set_control(0x02100000, V4L2_CID_EXPOSURE, 500)
#
# def adjust_gamma(image, gamma=1.1):
# 	# build a lookup table mapping the pixel values [0, 255] to
# 	# their adjusted gamma values
# 	invGamma = 1.0 / gamma
# 	table = np.array([((i / 255.0) ** invGamma) * 255
# 		for i in np.arange(0, 256)]).astype("uint8")
# 	# apply gamma correction using the lookup table
# 	return cv2.LUT(image, table)

videoCaptureObject = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)

time.sleep(1)
print("start")
while result:
    ret,frame = videoCaptureObject.read()
    # frame = adjust_gamma(frame)
    # cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Capturing Video",frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()

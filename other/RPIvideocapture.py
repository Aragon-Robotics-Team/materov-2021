from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

result = True

while result:
    camera.capture(rawCapture, format = "bgr")
    image = rawCapture.array
    cv2.imshow("Image", image)
    # if (cv2.waitKey(1) & 0xFF == ord('q')):
    #     videoCaptureObject.release()
    #     cv2.destroyAllWindows()

import cv2
import time

videoCaptureObject = cv2.VideoCapture(0)
result = True

time.sleep(1)
print("start")
while result:
    ret,frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video",frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()

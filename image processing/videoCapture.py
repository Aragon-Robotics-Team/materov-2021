import cv2

videoStreamObject = cv2.VideoCapture(0)
result = True
while(result):
    #when space is pressed
    if (cv2.waitKey(1)):
        #read the image from the camera
        ret, frame = videoCaptureObject.read()
        #show the iamge
        cv2.imshow("NewPicture.jpg", frame)
        #stop loop
        result = False

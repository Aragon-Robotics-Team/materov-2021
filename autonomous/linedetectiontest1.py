import cv2

videoCaptureObject = cv2.VideoCapture(0)
#ret, frame = videoCaptureObject.read()
videoImage = "/Users/valeriefan/Desktop/MATE-ROV-IP/Autonomous/videoImg.jpg"
#image = cv2.imread(videoImage)

result = True
while result:
    ret, frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video", frame)
    if cv2.waitKey(1) == ord('q'):
        cv2.imwrite(videoImage, frame)
        result = False
#image = videoImg
image = cv2.imread(videoImage)
result = image.copy()
#cv2.imshow("Image", image)
#cv2.waitKey()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

#mask everything but the red
#([17, 15, 100], [50, 56, 200])

mask = cv2.inRange(image, (17, 15, 100), (50, 56, 200))
output = cv2.bitwise_and(image, image, mask = mask)
# mask1 = cv2.inRange(image, (0, 50, 20), (5, 255, 255))
# mask2 = cv2.inRange(image, (175, 50, 20), (180, 255, 255))
#cv2.waitKey()
#mask = cv2.bitwise_or(mask1, mask2)
blur = cv2.GaussianBlur(mask, (5,5), cv2.BORDER_DEFAULT)
#cv2.imshow("mask", mask)
#cv2.waitKey()

#find edges
edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Edges", edges)
cv2.waitKey(0)

import cv2
cap = cv2.VideoCapture(0)
cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
cv2.imshow("hello", cv2image)

import multiprocessing
import cv2

def show_image():
    img = cv2.imread("/Users/valeriefan/Desktop/lines2.jpg")
    cv2.imshow("hasdf", img )

p1 = multiprocessing.Process(target = show_image)

p1.start()

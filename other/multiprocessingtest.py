import multiprocessing
import cv2

def hello():
    i = 0
    while i < 6:
        p1_output_queue.put("output " + str(i))
        print(p1_input_queue.get())
        i = i + 1

def goodbye():
    i = 0
    while i < 6:
        p1_input_queue.put("input " + str(i))
        print(p1_output_queue.get())
        i = i + 1

p1_input_queue = multiprocessing.Queue()
p1_output_queue = multiprocessing.Queue()

p1 = multiprocessing.Process(target=hello)
p2 = multiprocessing.Process(target=goodbye)

p1.start()
p2.start()

import queue

q = queue.Queue()

def queue(): #Needs forever loop, therefore can't use root.mainloop()
    if q.empty() == False:
        item = q.get()
        print(type(item))
        if (type(item) == np.ndarray):
            print("Input Type : Image Path")
            cv2.imshow("Threading Image", item)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        q.task_done()

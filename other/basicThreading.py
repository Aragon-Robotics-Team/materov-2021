import threading

def one():
    while True:
        print("1")

def two():
    while True:
        print("2")
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=one)
    t2 = threading.Thread(target=two)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

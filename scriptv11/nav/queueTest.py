from multiprocessing import Process, Queue, set_start_method
import time


def main(input_queue):
    time.sleep(0.5)
    queue_data = 4
    while not input_queue.empty():
        queue_data = input_queue.get()
    print(queue_data)

if __name__ == '__main__':
    set_start_method('spawn')
    input_queue = Queue()
    p = Process(target=main, args=(input_queue,))
    p.start()
    one = 1
    two = 2
    three = 3
    input_queue.put(one)
    input_queue.put(two)
    input_queue.put(three)
    p.join()

# import multiprocessing as mp
#
# def foo(q):
#     q.put('hello')
#
# if __name__ == '__main__':
#     mp.set_start_method('spawn')
#     q = mp.Queue()
#     p = mp.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

# from multiprocessing import Process
#
# def f(name):
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
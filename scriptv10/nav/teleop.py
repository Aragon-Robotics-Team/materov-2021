# from nav.teleopConfig1 import Config  # RPI IMPORTS
import multiprocessing

from scriptv10.nav.teleopConfig1 import Config # mac imports

def teleopMain(input_queue, output_queue):
    # robot = Config('Mac', True, False, input_queue, output_queue) # comp type, serial on, serial recieve on, input, output queue

    # statuses = [0, 0, 0, 0, 1, 1, 1, 1]
    # output_queue.put(statuses)
    # print("put in queue")

    robot = Config('Mac', True, False, input_queue, output_queue)
    robot.joy_init()



if __name__ == '__main__':
    thruster_in_queue = multiprocessing.Queue()
    thruster_out_queue = multiprocessing.Queue()
    teleopMain(thruster_in_queue, thruster_out_queue)

#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

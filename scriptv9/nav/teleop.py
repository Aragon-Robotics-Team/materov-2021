import nav.teleopConfig1
# from nav.teleopConfig1 import Config  # on rpi, DELETE newnavigation part
from nav.tracer import agg

def teleopMain(in_queue, out_queue):
    # robot = Config('Mac', True, False, input_queue, output_queue) # comp type, serial on, serial recieve on
    # #robot = teleopConfig1.Config('Mac', True, False)
    # robot.joy_init()

    input_queue = in_queue
    output_queue = out_queue
    # statuses = [0, 0, 0, 0, 1, 1, 1, 1]
    # output_queue.put(statuses)
    # print("put in queue")

    nav.teleopConfig1.teleop_1(input_queue, output_queue)

if __name__ == '__main__':
    teleopMain()

#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

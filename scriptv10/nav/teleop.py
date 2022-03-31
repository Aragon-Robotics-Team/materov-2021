from nav.teleopConfig1 import Config  # RPI IMPORTS
<<<<<<< HEAD

=======
# from scriptv10.nav.teleopConfig1 import Config # mac imports
>>>>>>> bc1b4d4880271f9f59697434ebceb150c0481f51

def teleopMain(input_queue, output_queue):
    # robot = Config('Mac', True, False, input_queue, output_queue) # comp type, serial on, serial recieve on, input, output queue

    # statuses = [0, 0, 0, 0, 1, 1, 1, 1]
    # output_queue.put(statuses)
    # print("put in queue")

    robot = Config('Mac', True, False, input_queue, output_queue)
    robot.joy_init()



if __name__ == '__main__':
    teleopMain()

#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

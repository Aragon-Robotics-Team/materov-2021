import multiprocessing
import gui

from time import sleep
from img_proc import measure_fishes

class GUIProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue, fish_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.fish_queue = fish_queue
    def run(self):
        p = multiprocessing.Process(target = gui.appStart, args = (self.input_queue, self.output_queue, self.fish_queue))
        p.start()


if __name__ == "__main__":
    thruster_in_queue = multiprocessing.Queue() #input the autonomous output
    thruster_out_queue = multiprocessing.Queue() #output the controller values
    fish_queue = multiprocessing.Queue()

    gui_proc = GUIProcess(thruster_out_queue, thruster_in_queue, fish_queue)
    gui_proc.start()

    while True:
        # print("hello")
        if fish_queue.empty() == False:
            averageLength = fish_queue.get()
            print("averageLength recieved")
            measure_fishes.ValuesAndCalc(averageLength)

import multiprocessing
from nav import controller
import gui


class ThrusterProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        controller.controllerStart()
        # p = multiprocessing.Process(target = controller.controllerStart(), args = (self.input_queue, self.output_queue, self.fish_queue))
        # p.start()

if __name__ == "__main__":
    thruster_in_queue = multiprocessing.Queue()
    thruster_out_queue = multiprocessing.Queue()

    thruster_proc = ThrusterProcess(thruster_in_queue, thruster_out_queue)
    thruster_proc.start()
<<<<<<< HEAD
    #
    # while True:
    #     gui.updateGUI()
=======

    while True:
        gui.updateGUI()
>>>>>>> 7d6a68796e6014e5997257d2daa8a2aca4fc94ed

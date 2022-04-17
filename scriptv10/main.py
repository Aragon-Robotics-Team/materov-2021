import multiprocessing

from nav.teleop import teleopMain  # RPI IMPORTS
import gui

class ThrusterProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        #nav.teleop.teleopMain()
        teleopMain(self.input_queue, self.output_queue)
        # print("h")
        # pygame.init()
        # print("h")
        # pygame.joystick.init()
        # p = multiprocessing.Process(target = controller.controllerStart(), args = (self.input_queue, self.output_queue, self.fish_queue))
        # p.start()

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')

    thruster_in_queue = multiprocessing.Queue()
    thruster_out_queue = multiprocessing.Queue()
    # gui.queue(thruster_in_queue, thruster_out_queue)

    #
    thruster_proc = ThrusterProcess(thruster_in_queue, thruster_out_queue)
    thruster_proc.start()
    # thruster_proc.join()
    while True:
        gui.root.update()
# hehehe

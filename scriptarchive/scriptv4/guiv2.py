from multiprocessing import Process
import glob
from img_proc.measure_fishes import measureFishie


def appStart():
     import tkinter as tk

     class Application(tk.Frame):
         def __init__(self, master = None):
             tk.Frame.__init__(self,master)
             # self.grid()
             self.setup()
        #TEST HELLO------------------------------------------------------------------------------------------------------
         def asdf(self):
             print("hello")
        #PHOTOMOSAIC------------------------------------------------------------------------------------------------------
         def startPhotomosaic(self):
             print("asdf")
             glob.photomosaicCount = 0
             print("Starting photomosaic")
             print("Type s 4 times to take snapshots, and one more time to construct the photomosaic")
             print("Type q to quit the photomosaic")
             glob.photomosaicVideo = True #switches video feed to photomosaic Video
             #IS BROKEN??? FIX
         #MEASURE FISHIES ------------------------------------------------------------------------------------------------------
         def start_measure_fish(self):
             measureFishie()
         def resetMeasureFish(self):
             print("Measuring Fish Task Reset")
             glob.allFishLengths = [0,0,0]
             glob.countfishCoords = 0
             glob.fishPictureCount = 0

         def setup(self):
             root = tk.Tk()
             root.geometry("1300x750")
             #TEST HELLO------------------------------------------------------------------------------------------------------
             btn = tk.Button(root, text = "hello", command = self.asdf)
             btn.grid(row = 0, column = 1, sticky = 'e')
             #PHOTOMOSAIC------------------------------------------------------------------------------------------------------
             btn = tk.Button(root, text = "Start Photomosaic", command = self.startPhotomosaic)
             btn.grid(row = 1,column = 1, sticky = 'e')

             #MEASURE FISHIES ------------------------------------------------------------------------------------------------------
             label = tk.Label(root, text = "(Click to 3 times to take photos and calculate)", font = 10)
             label.grid(row = 3, column = 1, sticky = 'n')

             btn = tk.Button(root, text="Measure Fish", command = self.start_measure_fish)
             btn.grid(row = 2,column = 1, sticky = 'e')

     app = Application()
     # app.master.title("Progress Bar")
     #app.mainloop()
     while True:
         #joytests() #<-- Fatal error sometimes?????
         #imgqueue.queue() #<-- same effect as directly calling the video module; it lags bc the images are being shown and the controller
         #is being checked at the same time
         app.update()
         if glob.photomosaicVideo == True:
             photomosaic()
         # else:
         #     general_video()
         #video.general_video()


if __name__ == '__main__':
    p = Process(target = appStart)
    p.start()

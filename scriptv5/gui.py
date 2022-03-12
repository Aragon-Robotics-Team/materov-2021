def appStart(input_q, output_q, fish_q):
    import tkinter as tk
    import cv2
    from img_proc import measure_fishes
    from img_proc.measure_fishes import averageLength
    from img_proc.measure_fishes import measureFish
    from PIL import Image, ImageTk
    from time import sleep

    input_queue = input_q
    output_queue = output_q
    fish_queue = fish_q

    videoCaptureObject = cv2.VideoCapture(0)
    #fish_queue.put()

    class Application(tk.Frame):
        def __init__(self, master = None):
            tk.Frame.__init__(self,master)
            # self.grid()
            self.setup()
            self.fishCount = 0

        #PHOTOMOSAIC ------------------------------------------------------------------------------------------------------

        #MEASURE FISHIES ------------------------------------------------------------------------------------------------------
        def start_measure_fish(self):
            ret, frame = videoCaptureObject.read()
            if self.fishCount < 3:
                measureFish(frame)
                self.fishCount = self.fishCount + 1
            else:
                print("calculating average length")
                averageFishLength = averageLength()
                fish_q.put(averageFishLength)
                print("put in queue")

        def resetMeasureFish(self):
            measure_fishes.resetFish()

        #VIDEO FEED ------------------------------------------------------------------------------------------------------


        #SET UP ------------------------------------------------------------------------------------------------------
        def setup(self):
            root = tk.Tk()
            root.geometry("1300x750")

            #MEASURE FISHIES ------------------------------------------------------------------------------------------------------
            label = tk.Label(root, text = "(Click to 3 times to take photos and calculate)", font = 10)
            label.grid(row = 3, column = 1, sticky = 'n')

            btn = tk.Button(root, text="Measure Fish", command = self.start_measure_fish)
            btn.grid(row = 2,column = 1, sticky = 'e')

            #VIDEO FEED ------------------------------------------------------------------------------------------------------
            # label = tk.Label(root, height = 700, width = 1000)
            # label.grid(row = 0, column = 0, rowspan = 30)

            # def show_frames():
            #    # Get the latest frame and convert into Image
            #    cv2image= cv2.cvtColor(videoCaptureObject.read()[1],cv2.COLOR_BGR2RGB)
            #    img = Image.fromarray(cv2image)
            #    # Convert image to PhotoImage
            #    imgtk = ImageTk.PhotoImage(image = img)
            #    label.imgtk = imgtk
            #    label.configure(image=imgtk)
            #    # Repeat after an interval to capture continiously
            #    label.after(20, show_frames)
            #
            # show_frames()




    app = Application()
    while True:
        app.update()

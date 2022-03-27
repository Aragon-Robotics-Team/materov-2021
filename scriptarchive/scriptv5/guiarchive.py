def appStart(input_q, output_q, fish_q):
    import tkinter as tk
    import cv2
    from img_proc import measure_fishes
    from img_proc.measure_fishes import averageLength
    from img_proc.measure_fishes import measureFish
    from PIL import Image, ImageTk
    from time import sleep
    import threading

    input_queue = input_q
    output_queue = output_q
    fish_queue = fish_q

    #fish_queue.put()
    videoCaptureObject = cv2.VideoCapture(0)
    class Application(tk.Frame):
        def __init__(self, master = None):
            print("init")
            tk.Frame.__init__(self,master)
            print("fish count")
            # self.grid()
            self.fishCount = 0
            print("setup")

            self.root = tk.Tk()
            self.root.geometry("1300x750")
            #self.setup()

            #MEASURE FISHIES ------------------------------------------------------------------------------------------------------

            self.label = tk.Label(self.root, text = "(Click to 3 times to take photos and calculate)", font = 10)
            self.label.grid(row = 3, column = 1, sticky = 'n')

            self.btn = tk.Button(self.root, text="Measure Fish", command = self.start_measure_fish)
            self.btn.grid(row = 2,column = 1, sticky = 'e')

            self.vid_label = tk.Label(self.root, height = 700, width = 1000)
            self.vid_label.grid(row = 0, column = 0, rowspan = 30)

            # video_thread = threading.Thread(target = self.show_frames)
            # video_thread.start()
            self.show_frames()

        # root = tk.Tk()
        # root.geometry("1300x750")

        #PHOTOMOSAIC ------------------------------------------------------------------------------------------------------

        #MEASURE FISHIES ------------------------------------------------------------------------------------------------------
        fishCount = 0
        def start_measure_fish(self):
            ret, frame = videoCaptureObject.read()
            if Application.fishCount < 3:
                measureFish(frame)
                Application.fishCount = Application.fishCount + 1
            else:
                print("calculating average length")
                averageFishLength = averageLength()
                fish_q.put(averageFishLength)
                print("put in queue")

        def resetMeasureFish(self):
            measure_fishes.resetFish()

        # label = tk.Label(root, text = "(Click to 3 times to take photos and calculate)", font = 10)
        # label.grid(row = 3, column = 1, sticky = 'n')
        #
        # btn = tk.Button(root, text="Measure Fish", command = start_measure_fish)
        # btn.grid(row = 2,column = 1, sticky = 'e')

        #VIDEO FEED ------------------------------------------------------------------------------------------------------
        #cap = cv2.VideoCapture(0)

        # label = tk.Label(root, height = 700, width = 1000)
        # label.grid(row = 0, column = 0, rowspan = 30)
        # Define function to show frame
        def show_frames(self):
           # Get the latest frame and convert into Image
           cv2image= cv2.cvtColor(videoCaptureObject.read()[1],cv2.COLOR_BGR2RGB)
           img = Image.fromarray(cv2image)
           # Convert image to PhotoImage
           imgtk = ImageTk.PhotoImage(master = self.root, image = img)
           self.vid_label.imgtk = imgtk
           self.vid_label.configure(image=imgtk)
           # Repeat after an interval to capture continiously
           self.vid_label.after(10, self.show_frames)


        #SET UP ------------------------------------------------------------------------------------------------------
        # def setup(self):
        #     root = tk.Tk()
        #     root.geometry("1300x750")
        #
        #     #MEASURE FISHIES ------------------------------------------------------------------------------------------------------
        #     label = tk.Label(root, text = "(Click to 3 times to take photos and calculate)", font = 10)
        #     label.grid(row = 3, column = 1, sticky = 'n')
        #
        #     btn = tk.Button(root, text="Measure Fish", command = self.start_measure_fish)
        #     btn.grid(row = 2,column = 1, sticky = 'e')
        #
        #     #VIDEO FEED ------------------------------------------------------------------------------------------------------
        #     label = tk.Label(root, height = 700, width = 1000)
        #     label.grid(row = 0, column = 0, rowspan = 30)

            # def show_frames(label):
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

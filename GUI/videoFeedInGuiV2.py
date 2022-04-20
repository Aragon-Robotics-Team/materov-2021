
# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

if __name__ == "__main__":

   # Import required Libraries
   from tkinter import *
   from PIL import Image, ImageTk
   import cv2

   # Create an instance of TKinter Window or frame
   win = Tk()

   # Set the size of the window
   win.geometry("1400x2000")

   # Create a Label to capture the Video frames
   label = Label(win, height=700, width=700)
   label.place(x=700, y=0)
   cap = cv2.VideoCapture(0)


   show_frames()


   while True:
       win.update()

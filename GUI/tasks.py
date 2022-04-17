
# import tkinter module
from tkinter import *
import tkinter as tk


# Create Object
root = Tk()

# Initialize tkinter window with dimensions 100x100
root.geometry('300x900')

taskcanvas = Canvas(root, height = 600, width = 300, bg="#fff")
taskcanvas.pack()

task1text = "TASK 1 - 100 points \n \nReplace a damaged section of an inter-array cable: \n \nVisual inspection - 5 points \n \nCut cable on both sides of damaged section - 10 points \n \nRemove damaged section by pulling the metal connectors off - 5 points \n \nInstall new cable section - 10 points \n \nSecure the new section with 2 (each) connectors by pushing it sideways - 10 points \n \nReplacing a damaged buoyancy module on an inter-array cable of a floating offshore wind turbine: \n \n Turn the clamp upright and remove from water - 10 points \n \nPut on new clamp facing down - 10 points \n \nMonitor the environment: \n \nDeploy the hydrophone in the box and wait 5 mins till recovery - 10 points \n \nPull pin and remove net from water - 15 points \n \nDrive the bot into the box - 5 or 15 points"

task2text = "apples - 500 points"

task3text = "watermelon - 600 points"

task4text = "snacks - 1000000 points"

task5text = "martin - 10000000000000000000000 points"

text=tk.Text(taskcanvas, width = 35, height = 500, wrap = WORD, padx = 5, pady = 5)
text.place(x= 5, y= 50)

def task1():
    text.delete("1.0","end")
    text.insert(tk.END, task1text)

def task2():
    text.delete("1.0","end")
    text.insert(tk.END, task2text)

def task3():
    text.delete("1.0","end")
    text.insert(tk.END, task3text)

def task4():
    text.delete("1.0","end")
    text.insert(tk.END, task4text)

def task5():
    text.delete("1.0","end")
    text.insert(tk.END, task5text)

######################################################

Bu = Button(taskcanvas, text = "Task 1", command = task1).place(x= 30, y= 10)

Bu = Button(taskcanvas, text = "Task 2", command = task2).place(x= 95,y= 10)

Bu = Button(taskcanvas, text = "Task 3", command = task3).place(x= 165,y= 10)

Bu = Button(taskcanvas, text = "Task 4", command = task4).place(x= 230,y= 10)

# pack the text-Aera in the window
root.mainloop()

import tkinter as tk
from tkinter import ttk
import Week6SecondWindow

class MainWindow: # Main window class
  def __init__(self): # Constructor method for main window
    self.win = tk.Tk()
    self.win.title("SEN4017 - Week 6")
    self.win.iconbitmap("python.ico")
    self.win.geometry("500x500+500+200")
    self.win2 = None
    self.lbl1 = None
    self.btn1 = None
    self.btn2 = None
    self.create_widgets()
    



  def create_widgets(self): # Method to create widgets
    self.lbl1 = ttk.Label(self.win, text="This is the main window", font=("Arial", 20))
    self.btn1 = ttk.Button(self.win, text="Open Second Window", command=self.open_new_window)
    self.btn2 = ttk.Button(self.win, text="Close", command=self.win.destroy)

    self.lbl1.pack(pady=(20, 0))
    self.btn1.pack(pady=(20, 0))
    self.btn2.pack(pady=(20, 0))

  def open_new_window(self):
    self.win2 = Week6SecondWindow.SecondWindow(self) # Create an instance of the second window class
    self.win2.grab_set() # Prevent interaction with the main window 

  


app = MainWindow() # Create an instance of the main window class
app.win.mainloop() # Start the main loop
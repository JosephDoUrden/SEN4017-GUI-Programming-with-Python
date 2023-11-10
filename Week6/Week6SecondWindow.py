import tkinter as tk
from tkinter import ttk

class SecondWindow(tk.Toplevel): # Second window class
  def __init__(self, parent): # Constructor method for second window
    super().__init__()
    self.parent = parent
    self.title("Second Window")
    self.iconbitmap("python.ico")
    self.geometry("300x200+700+400")

    self.lbl1 = None
    self.btn1 = None
    self.entry1 = None

    self.create_widgets()

    self.protocol("WM_DELETE_WINDOW", self.destroy) # Handle window close event



  def create_widgets(self): # Method to create widgets
    self.lbl1 = ttk.Label(self, text="Second window", font=("Arial", 20))
    self.btn1 = ttk.Button(self, text="Close", command=self.close_window)

    self.entry1 = ttk.Entry(self)
    self.entry1.pack(pady=(20, 0))
    self.entry1.bind("<Return>", self.return_key)

    self.lbl1.pack(pady=(20, 0))
    self.btn1.pack(pady=(20, 0))

  def return_key(self, event): # Method to handle return key press
    self.parent.win.title(self.entry1.get())
    self.close_window()

  def close_window(self):
    print("Closing window")
    self.destroy()


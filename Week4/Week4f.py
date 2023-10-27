import tkinter as tk
from tkinter import ttk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
win.iconbitmap('python.ico')

def click_handler():
  ttk.Label(win, text=spin_value.get()).pack() # Display a label when the button is clicked

spin_value = tk.StringVar(value="3") # Create a StringVar to store the value of the Spinbox
spin_values = tuple(range(1, 20, 3)) # Create a range of values for the Spinbox

spinbox1 = ttk.Spinbox(
  win, 
  values=spin_values, 
  wrap=True, 
  state="readonly", 
  textvariable=spin_value,
  command=click_handler
  ) # Create a Spinbox

spinbox1.pack() # Display the Spinbox


win.mainloop()
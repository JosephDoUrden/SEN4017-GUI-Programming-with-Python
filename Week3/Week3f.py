import tkinter as tk
from tkinter import ttk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+500+200")


# Create a label
label1 = tk.Label(win, text="Enter your name:", font=("Arial", 20), bg="red", fg="white")
label2 = tk.Label(win, text="")
entry1 = ttk.Entry(win, width=30)


def click_handler(): # Create a function
  if(len(entry1.get()) > 0): # Check if the entry is not empty
    label2.configure(text="Hello " + entry1.get()) # Set the text of label2
    entry1.delete(0, 'end') # Clear the entry
  else: # If the entry is empty
    label2.configure(text="Please enter your name") # Set the text of label2
    entry1.focus() # Set the focus to the entry widget

button1 = ttk.Button(win, text='Send', command=click_handler) # Create a button

# Place the label in the window
label1.pack()
entry1.pack()
button1.pack()
label2.pack()



win.mainloop()
import tkinter as tk
from tkinter import ttk
from time import sleep

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
win.iconbitmap('python.ico')

def start_progressbar():
  progressbar1.start(interval=100) # Start the progressbar

def stop_progressbar():
  progressbar1.stop() # Stop the progressbar

def run_progressbar():
  progressbar1["value"] = 0
  progressbar1["maximum"] = 100
  for i in range(0, 101, 20):
    print(i)
    progressbar1["value"] = i
    progressbar1.update()
    sleep(1)



progressbar1 = ttk.Progressbar(
  win, 
  orient="horizontal", 
  length=250, 
  mode="determinate"
  ) # Create a horizontal progressbar

progressbar1.pack(pady=50) # Display the progressbar

ttk.Button(win, text="Start", command=start_progressbar).pack(pady=10) # Display a button
ttk.Button(win, text="Stop", command=stop_progressbar).pack(pady=10) # Display a button
ttk.Button(win, text="Run", command=run_progressbar).pack(pady=10) # Display a button


win.mainloop()
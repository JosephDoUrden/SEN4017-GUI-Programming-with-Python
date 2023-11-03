import tkinter as tk
from centerscreen import center_screen_geometry

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")

# Set the window to center of the screen
win.geometry(center_screen_geometry(
  screen_width=win.winfo_screenwidth(), 
  screen_height=win.winfo_screenheight(), 
  win_width=600, 
  win_height=300
  ))


win.mainloop()
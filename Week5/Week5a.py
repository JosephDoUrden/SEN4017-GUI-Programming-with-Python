import tkinter as tk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")

win_width = 600
win_height = 400

# Get the screen dimension
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = int((screen_width / 2) - (win_width / 2))
y = int((screen_height / 2) - (win_height / 2))

# Set the window to center of the screen
win.geometry(f"{win_width}x{win_height}+{x}+{y}")


win.mainloop()
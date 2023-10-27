import tkinter as tk
from tkinter import ttk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
win.iconbitmap('python.ico')

menubar = tk.Menu(win) # Create a menubar
win.configure(menu=menubar) # Display the menubar

file_menu = tk.Menu(menubar) # Create a file menu
file_menu.add_command(label="Exit", command=win.destroy) # Add a command to the file menu

menubar.add_cascade(label="File", menu=file_menu, underline=0) # Add the file menu to the menubar



win.mainloop()
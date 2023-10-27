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
file_menu.add_command(label="New", accelerator="CMD+N", underline=0) # Add a command to the file menu
file_menu.add_command(label="Open...", underline=0) # Add a command to the file menu
file_menu.add_separator() # Add a separator to the file menu
file_menu.add_command(label="Exit", command=win.destroy, underline=1) # Add a command to the file menu

help_menu = tk.Menu(menubar, tearoff=False) # Create a help menu
help_menu.add_command(label="About...", underline=0) # Add a command to the help menu  

menubar.add_cascade(label="File", menu=file_menu, underline=0) # Add the file menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu, underline=0) # Add the file menu to the menubar



win.mainloop()
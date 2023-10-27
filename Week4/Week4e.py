import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog as fd

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 4")
win.geometry("500x500+500+200")
win.iconbitmap('python.ico')

check_state = tk.BooleanVar() # Create a BooleanVar to store the state of the checkbutton

def print_state(): # Create a function to print the state of the checkbutton
  print(check_state.get()) # Print the state of the checkbutton

def exit_app(): # Create a function to exit the application
  if msg.askyesno(title="Exit", message="Are you sure you want to exit?"): # Display a message box to confirm the exit
    win.destroy() # Destroy the window

def file_open(): # Create a function to open a file
  file_filter = (
    ('Text files', '*.txt'),
    ('PDF files', '*.pdf'),
    ('All files', '*.*')
  ) # Create a tuple of file types
  selected_file = fd.askopenfilename(
    title='Open a file', 
    filetypes=file_filter
    ) # Display a file dialog to select a file
  ttk.Label(win, text=selected_file).pack() # Display the selected file in a label

menubar = tk.Menu(win) # Create a menubar
win.configure(menu=menubar) # Display the menubar

file_menu = tk.Menu(menubar) # Create a file menu
file_menu.add_command(
  label="New", 
  accelerator="CMD+N", 
  underline=0,
  command=lambda: msg.showwarning(title="Warning", message="All unsaved changes will be lost!")
  ) # Add a command to the file menu
file_menu.add_command(
  label="Open...", 
  underline=0,
  command=file_open
  ) # Add a command to the file menu

file_menu.add_separator() # Add a separator to the file menu

sub_menu = tk.Menu(file_menu, tearoff=False) # Create a submenu
sub_menu.add_command(label="Zoom In") # Add a command to the submenu
sub_menu.add_command(label="Zoom Out") # Add a command to the submenu

file_menu.add_cascade(label="Editor", menu=sub_menu, underline=0) # Add the submenu to the file menu

file_menu.add_separator() # Add a separator to the file menu

file_menu.add_command(label="Exit", command=exit_app, underline=1) # Add a command to the file menu

help_menu = tk.Menu(menubar, tearoff=False) # Create a help menu
help_menu.add_checkbutton(label="Send anonymous stats", onvalue=True, offvalue=False, variable=check_state, command=print_state) # Add a checkbutton to the help menu
help_menu.add_separator() # Add a separator to the help menu
help_menu.add_command(
  label="About...", 
  command=lambda: msg.showinfo(
    title="About", 
    message="SEN4017 - Introduction to GUI Programming with Python"
    )) # Add a command to the help menu

menubar.add_cascade(label="File", menu=file_menu, underline=0) # Add the file menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu, underline=0) # Add the file menu to the menubar



win.mainloop()
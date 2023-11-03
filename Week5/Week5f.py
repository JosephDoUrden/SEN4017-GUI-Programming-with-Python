import tkinter as tk
from tkinter import ttk
from datetime import datetime

def show_context_menu(event):
  context_menu.tk_popup(x=event.x_root, y=event.y_root) # event.x_root and event.y_root are the coordinates of the mouse

def show_date_time():
  labels.append(ttk.Label(win, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), font=("Arial", 26))) # strftime() formats the date and time
  labels[-1].pack(pady=(10, 0)) # -1 is the last item in the list

def clear():
  for label in labels:
    label.destroy()
  labels.clear()

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")
labels = []

context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date_time)
context_menu.add_command(label="Clear")
context_menu.add_separator() # Adds a separator
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-3>", show_context_menu) # <Button-3> is the right mouse button



win.mainloop()
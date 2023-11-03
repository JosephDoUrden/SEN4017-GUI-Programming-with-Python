import tkinter as tk
from tkinter import ttk
from datetime import datetime

def show_context_menu(event):
  context_menu.tk_popup(x=event.x_root, y=event.y_root) # event.x_root and event.y_root are the coordinates of the mouse

def show_date_time():
  labels.append(ttk.Label(content, text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), font=("Arial", 26))) # strftime() formats the date and time
  labels[-1].pack(pady=(10, 0)) # -1 is the last item in the list
  canvas.update() # Update the canvas
  configure_canvas() # Configure the canvas to scroll


def clear():
  for label in labels:
    label.destroy()
  labels.clear()

def configure_canvas(event):
  canvas.configure(scrollregion=canvas.bbox("all")) # Configure the canvas to scroll  # bbox("all") returns the bounding box of all items in the canvas
  canvas.itemconfig("content_window", width=canvas.winfo_width()) # Configure the canvas to scroll  # winfo_width() returns the width of the canvas



def configure_canvas_event(event):
  configure_canvas()

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")
labels = []

# Main container frame (canvas + scrollbar)
container = ttk.Frame(win) # Create a container
container.pack(fill=tk.BOTH, expand=True) # Pack the container

# Container with scrollbar support
canvas = tk.Canvas(container) # Create a canvas
canvas.pack(fill=tk.BOTH, expand=True) # Pack the canvas

# Scrollbar component
scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview) # Create a scrollbar
scrollbar.place(relx=1, rely=0, relheight=1, anchor=tk.NE) # Place the scrollbar

# Link canvas to scrollbar
canvas.configure(yscrollcommand=scrollbar.set) # Configure the canvas

# Actual container frame that keeps the widgets
content = tk.Frame(canvas) # Create a frame inside the canvas
content.pack(fill=tk.BOTH, expand=True) # Pack the frame

# Place the content frame inside the canvas
canvas.create_window(0, 0, window=content, anchor=tk.NW, tags="content_window") # Create a window inside the canvas
canvas.bind("<Configure>", configure_canvas_event) # Configure the canvas to scroll

context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Show date and time", command=show_date_time)
context_menu.add_command(label="Clear")
context_menu.add_separator() # Adds a separator
context_menu.add_command(label="Exit", command=win.destroy)

win.bind("<Button-3>", show_context_menu) # <Button-3> is the right mouse button



win.mainloop()
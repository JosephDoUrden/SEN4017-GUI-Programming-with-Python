import tkinter as tk
from tkinter import ttk

def click_event(event): # event is an object
  if event.num == 1:
    button = "Left mouse button"
  elif event.num == 2:
    button = "Middle mouse button"
  elif event.num == 3:
    button = "Right mouse button"

  message = button + " clicked at " + event.widget["text"]
  ttk.Label(win, text=message).pack()

def mouse_enter(event):
  event.widget.configure(text="Mouse entered") # event.widget is the widget that triggered the event

def mouse_leave(event):
  event.widget.configure(text="Mouse left")

def mouse_move(event):
  win.title(f"{event.x}, {event.y}")


# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")

btn1 = ttk.Button(win, text="Button 1")
btn2 = ttk.Button(win, text="Button 2")

btn1.pack(pady=(20, 0))
btn2.pack(pady=20)

btn1.bind("<Button-1>", click_event) # <Button-1> is the left mouse button
btn2.bind("<Button-3>", click_event) # <Button-3> is the right mouse button
btn1.bind("<Enter>", mouse_enter) # <Enter> is when the mouse enters the widget
btn1.bind("<Leave>", mouse_leave) # <Leave> is when the mouse leaves the widget
win.bind("<Motion>", mouse_move) # <Motion> is when the mouse moves


win.mainloop()
import tkinter as tk
from tkinter import ttk

def key_press(event):
  label1["text"] = event.keysym

def focus_gained(event):
  label1["text"] = "Entry box focused"

def focus_lost(event):
  label1["text"] = "Entry box lost focus"

def return_key(event):
  label1["text"] = entry1.get().upper()


# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 5")
win.iconbitmap("python.ico")
win.geometry("300x300+200+200")

entry1 = ttk.Entry(win)
button1 = ttk.Button(win, text="Button 1")
label1 = ttk.Label(win, text="", font=("Arial", 26))

entry1.pack(pady=20)
button1.pack(pady=(0, 20))
label1.pack()

entry1.bind("<Key>", key_press) # <Key> is when a key is pressed
entry1.bind("<FocusIn>", focus_gained) # <FocusIn> is when the widget gains focus
entry1.bind("<FocusOut>", focus_lost) # <FocusOut> is when the widget loses focus
entry1.bind("<Return>", return_key) # <Return> is when the return key is pressed



win.mainloop()
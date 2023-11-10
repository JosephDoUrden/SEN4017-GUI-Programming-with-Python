import tkinter as tk
from tkinter import ttk

def open_second_window():
    # Create the second window
    win2 = tk.Toplevel() # This is the only difference
    win2.title("Second Window")
    win2.iconbitmap("python.ico")
    win2.geometry("500x500+500+200")

    ttk.Label(win2, text="This is the second window").pack(pady=(20, 0))
    btn3 = ttk.Button(win2, text="Close", command=win2.destroy)
    btn3.pack(pady=(20, 0))

# Create the main window
win = tk.Tk()
win.title("SEN4017 - Week 6")
win.iconbitmap("python.ico")
win.geometry("500x500+500+200")

btn1 = ttk.Button(win, text="Button", command=open_second_window)
btn2 = ttk.Button(win, text="Close", command=win.destroy)

btn1.pack(pady=(20, 0))
btn2.pack(pady=(20, 0))

win.mainloop()

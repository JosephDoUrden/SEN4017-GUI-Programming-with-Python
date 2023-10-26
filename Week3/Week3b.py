import tkinter as tk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+500+200")

# Create a label
label1 = tk.Label(win, text="Label 1", font=("Arial", 20), bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", font=("Arial", 20), bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", font=("Arial", 20), bg="blue", fg="white")

# Place the label in the window
label1.pack(padx=10, pady=10, fill=tk.X, side=tk.TOP)
label2.pack(side=tk.RIGHT, ipadx=10, ipady=10)
label3.pack(side=tk.LEFT, ipadx=10, ipady=10)



win.mainloop()
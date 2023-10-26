import tkinter as tk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+500+200")


# Create a label
label1 = tk.Label(win, text="Enter your name:", font=("Arial", 20), bg="red", fg="white")
label2 = tk.Label(win, text="")
entry1 = tk.Entry(win, width=30)

# Create a button
def click_handler():
  label2.configure(text="Hello " + entry1.get())

button1 = tk.Button(win, text='Send', command=click_handler)

# Place the label in the window
label1.pack()
entry1.pack()
button1.pack()
label2.pack()



win.mainloop()
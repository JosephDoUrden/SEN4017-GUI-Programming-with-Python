import tkinter as tk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("300x300+500+200")

#Column configure
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=2)
win.columnconfigure(2, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(1, weight=2)
win.rowconfigure(2, weight=1)

# Create a label
label1 = tk.Label(win, text="Label 1", font=("Arial", 20), bg="red", fg="white")
label2 = tk.Label(win, text="Label 2", font=("Arial", 20), bg="green", fg="white")
label3 = tk.Label(win, text="Label 3", font=("Arial", 20), bg="blue", fg="white")

# Place the label in the window
label1.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
label2.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')
label3.grid(row=2, column=1, padx=10, pady=10, sticky='nswe')



win.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("500x300+500+200")


notebook1 = ttk.Notebook(win)  # Create a notebook
notebook1.pack(pady=30)  # Pack the notebook

tab1 = ttk.Frame(notebook1, width=200, height=200)  # Create a tab
tab2 = ttk.Frame(notebook1, width=200, height=200)  # Create a tab

tab1.pack()  # Pack the tab
tab2.pack()  # Pack the tab

notebook1.add(tab1, text='Tab 1')  # Add the tab to the notebook
notebook1.add(tab2, text='Tab 2')  # Add the tab to the notebook

scrolledtext1 = scrolledtext.ScrolledText(tab1, width=40, wrap='word')  # Create a scrolledtext
scrolledtext1.pack(fill='both')  # Pack the scrolledtext

label_frame1 = ttk.LabelFrame(tab2, text='Checkbox')  # Create a label frame
label_frame1.pack(padx=10, pady=10, fill='both')  # Pack the label frame

def click_handler():
  print(selected_value.get())
selected_value = tk.StringVar()  # Create a variable to store the selected value
checkbox1 = ttk.Checkbutton(label_frame1, text='I agree to the terms and conditions', onvalue='Agree', offvalue='Disagree', command=click_handler)  # Create a checkbox





win.mainloop()

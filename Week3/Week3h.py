import tkinter as tk
from tkinter import ttk

# Create a window
win = tk.Tk()
win.title("SEN4017 - Week 3")
win.geometry("500x300+500+200")


# Create a label
label1 = ttk.Label(win, text="First Number: ", font=("Arial", 20))
label2 = ttk.Label(win, text="Second Number: ", font=("Arial", 20))
label3 = ttk.Label(win, text="Operator: ", font=("Arial", 20))
entry1 = ttk.Entry(win, width=30)  # Create an entry widget
entry2 = ttk.Entry(win, width=30)  # Create an entry widget
frame1 = ttk.Frame(win) # Create a frame
operator = tk.StringVar()  # Create a variable to store the operator
radio1 = ttk.Radiobutton(frame1, text='+', variable=operator, value='+')  # Create a radiobutton
radio2 = ttk.Radiobutton(frame1, text='-', variable=operator, value='-')  # Create a radiobutton
radio3 = ttk.Radiobutton(frame1, text='*', variable=operator, value='*')  # Create a radiobutton
radio4 = ttk.Radiobutton(frame1, text='/', variable=operator, value='/')  # Create a radiobutton



def click_handler():
    selected_operator = operator.get()  # Get the selected operator
    if selected_operator == '+':
        result = int(entry1.get()) + int(entry2.get())
    elif selected_operator == '-':
        result = int(entry1.get()) - int(entry2.get())
    elif selected_operator == '*':
        result = int(entry1.get()) * int(entry2.get())
    elif selected_operator == '/':
        result = int(entry1.get()) / int(entry2.get())
    else:
        result = 'Invalid operator'
    # Set the text of the button to the result
    button1.configure(text='The result is ' + str(result))
    entry1.focus_set()  # Set the focus to the first entry widget


button1 = ttk.Button(win, text='Calculate', command=click_handler)  # Create a button

# Place the label in the window
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)

# Set the padx property to add padding to the left and right of the widget
entry1.grid(row=0, column=1, padx=(0, 10))
entry2.grid(row=1, column=1, padx=(0, 10))
frame1.grid(row=2, column=1, padx=(0, 10), sticky='w')
radio1.pack(anchor='w')
radio2.pack(anchor='w')
radio3.pack(anchor='w')
radio4.pack(anchor='w')



# Set the sticky property to align the button to the left and right
button1.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)


win.mainloop()

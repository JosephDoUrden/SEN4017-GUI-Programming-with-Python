import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SEN4017")

# win.state(newstate="zoomed")
win.resizable(False, False) #window resize

win.geometry("300x200+600+300") # pencere boyutundan sonra gelen kısım uygulama koştuğunda pencerenin ekranda açılacağı kordinatlar
# tk.Label(win, text="A label").grid(column=0, row=0)

def click_handler():
  button1.configure(text="Clicked!")
  label1.configure(text="Button Clicked!", foreground="red")

label1 = ttk.Label(win, text="A Label")
label1.grid(column=0, row=0)

button1 = ttk.Button(win, text="A Button", command=click_handler)
button1.grid(column=1, row=1)




win.mainloop()
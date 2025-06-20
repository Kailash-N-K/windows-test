from tkinter import *

def key_pressed(value):
    if textBox.get() == "":
        print(value)
        return False

root=Tk()
root.title("Serial Monitor")
root.iconbitmap("serial_monitor.ico")
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 0)

key_press_register = (root.register(key_pressed), '%P')

textBox = Entry(root, relief="sunken", width = 50, validate="key", validatecommand=key_press_register)
textBox.pack(fill="x", padx=5, pady=5, ipady=5)

root.mainloop()
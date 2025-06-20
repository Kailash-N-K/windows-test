import serial
from tkinter import *
from tkinter.ttk import Combobox

import serial.tools.list_ports

selectedPort = serial.Serial(write_timeout=1)


def key_pressed(event):
    textBox.delete(0, "end")
    if selectedPort.is_open and [i.name for i in serial.tools.list_ports.comports() if
                                 i.name == selectedPort.port and "BTHENUM" in i.hwid and int(
                                     i.hwid[i.hwid.rfind("&") + 1:i.hwid.rfind("_")], 16) == 0] != [
        selectedPort.port]:
        try:
            selectedPort.write(event.keycode.to_bytes(1))
        except serial.serialutil.SerialTimeoutException:
            print("ERROR")
    else:
        print("Incoming Port Detected")


def key_released(event):
    textBox.delete(0, "end")
    if selectedPort.is_open and [i.name for i in serial.tools.list_ports.comports() if
                                 i.name == selectedPort.port and "BTHENUM" in i.hwid and int(
                                     i.hwid[i.hwid.rfind("&") + 1:i.hwid.rfind("_")], 16) == 0] != [
        selectedPort.port]:
        try:
            print("Connection Successful...")
        except serial.serialutil.SerialTimeoutException:
            print("ERROR")
    else:
        print("Incoming Port Detected")


def refresh_list():
    portList.config(values=["N/A"] + [i[0] for i in serial.tools.list_ports.comports()])

    if portList.get() not in [i[0] for i in serial.tools.list_ports.comports()]:
        portList.current(0)


def set_serial_port(event):
    global selectedPort
    if selectedPort.port != portList.get():
        selectedPort.close()
        selectedPort.port = portList.get()
        waitLabel.grid()
        root.update()
        if not selectedPort.is_open:
            try:
                selectedPort.open()
                if selectedPort.is_open and [i.name for i in serial.tools.list_ports.comports() if
                                             i.name == selectedPort.port and "BTHENUM" in i.hwid and int(
                                                 i.hwid[i.hwid.rfind("&") + 1:i.hwid.rfind("_")], 16) == 0] != [
                    selectedPort.port]:
                    try:
                        print("Connection Successful...")
                    except:
                        print("ERROR")
                else:
                    print("Incoming Port Detected")
            except serial.SerialException:
                print("ERROR")
        waitLabel.grid_remove()


# def entry_validation(value):
#     if textBox.get() == "":
#         print(value)
#         return False


root = Tk()
root.title("Serial Monitor")
root.iconbitmap("serial_monitor.ico")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# key_press_register = (root.register(entry_validation), "%P")

entryFrame = Frame(root)
entryFrame.grid(row=0, column=0, sticky=NSEW)

textBox = Entry(entryFrame, relief="sunken", width=50)
textBox.pack(fill="x", padx=5, pady=5, ipady=5)
textBox.bind("<KeyPress>", key_pressed)
textBox.bind("<KeyRelease>", key_released)

# textBox = Entry(entryFrame, relief="sunken", width = 50, validate="key", validatecommand=key_press_register)
# textBox.pack(fill="x", padx=5, pady=5, ipady=5)
# textBox.bind("<KeyPress>", key_pressed)
# textBox.bind("<KeyRelease>", key_released)
#
# sendButton = Button(root, text="Send", width=10)
# sendButton.grid(row=0, column=1, padx=(0, 5), pady=5, sticky=NSEW)

portList = Combobox(root, values=["N/A"] + [i[0] for i in serial.tools.list_ports.comports()], state="readonly",
                    postcommand=refresh_list)
portList.grid(row=1, column=0, pady=5)
portList.current(0)
portList.bind("<<ComboboxSelected>>", set_serial_port)

waitLabel = Label(root, text="Please wait...")
waitLabel.grid(row=2, column=0)
waitLabel.grid_remove()

root.mainloop()

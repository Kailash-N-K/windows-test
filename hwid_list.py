import serial.tools.list_ports

a = [i.hwid for i in serial.tools.list_ports.comports() if "BTHENUM" in i.hwid and int(i.hwid[i.hwid.rfind("&") + 1:i.hwid.rfind("_")], 16) == 0]

print(a)


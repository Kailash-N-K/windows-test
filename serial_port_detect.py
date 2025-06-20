import serial
print("One")
ser = serial.Serial('COM4')
print("Two")
print(ser.name)
ser.write(b'hello')
ser.close()

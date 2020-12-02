
#!/usr/bin/env python
import time
import serial

while 1:
    ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
while 1:
    x=ser.readline()
    if len(x)>0:
        print(x.decode('utf-8'))
        break
    else:
        a=input("enter your text:")
        if len(a)>0:
            ser.write(a.encode('utf-8'))
        else:
            continue

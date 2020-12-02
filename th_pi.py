import threading
import serial
import time
import colorama
from colorama import Fore,Back,Style

def serwrite():
    while 1:
        a=input()
        ser.write(a.encode('utf-8'))
def serread():
    while 1:
        x=ser.readline()
        if len(x)>0:
                print(Fore.GREEN +"Received data from windows: "+ x.decode('utf-8') + Style.RESET_ALL)

if __name__=="__main__":
    ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
    colorama.init()
    t1=threading.Thread(target=serwrite)
    t2=threading.Thread(target=serread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
 

from numpy.core.defchararray import encode
from numpy.core.fromnumeric import shape
import serial
import time
import numpy as np
import RPi.GPIO as GPIO

class uart:
    def __init__(self, baud):
        self.ser = serial.Serial(
            port = '/dev/serial0',
            baudrate = baud,
            timeout = 1
        )
        self.buff = np.empty(shape=0, dtype=int)
        self.msg_len = 0
    
    def received(self):
        if self.ser.in_waiting>0:
            self.buff = np.append(self.buff, int(ord(self.ser.read())))
            if self.buff.size < 4:
                return
            
            self.msg_len = self.buff[3]

            if len(self.buff) < self.msg_len:
                return

            print(self.buff[:self.msg_len])
            self.buff[0] = 0xDF
            self.ser.write(list(self.buff[:self.msg_len]))
            self.buff = self.buff[self.msg_len:]
    
def getCurrentTimeInMs():
    return time.time()*1000

if __name__ == "__main__":
    pi_com = uart(9600)
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(16, 0)
    
    last_tick = getCurrentTimeInMs()
    delay_time = 50 #unit:ms
    while(GPIO.input(18)):
        new_tick = getCurrentTimeInMs()
        pi_com.received()
        #print(new_tick)
        if (new_tick - last_tick) >= delay_time:
            last_tick = new_tick
            
    GPIO.cleanup()
    
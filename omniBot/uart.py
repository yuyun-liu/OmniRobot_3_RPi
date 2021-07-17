import serial
import RPi.GPIO

class uart:
    def __init__(self, baudrate):
        self.Baudrate = baudrate
        self.ser = serial.Serial("/dev/ttyACM1", baudrate, timeout = 0.2)
    
    def receive(self):
        command = ser.read()
        print(command)
    
if __name__ == "__main__":
    pi_com = uart(9600)
    #pi_com
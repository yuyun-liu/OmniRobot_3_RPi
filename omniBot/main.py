import time
import RPi.GPIO as GPIO
import threading
from uart import uart

com1 = uart(9600)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)

while(GPIO.input(18)):
    com1.received()

GPIO.cleanup()
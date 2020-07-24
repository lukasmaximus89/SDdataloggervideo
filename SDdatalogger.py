import imu
import uos
import time
from m5stack import *
from machine import SDCard, Pin

sd = SDCard(slot = 2, sck = Pin(23), miso = Pin(33), mosi = Pin(19), freq = 10000000)
uos.mount(sd, "/sd")

imu0 = imu.IMU()
data = imu0.acceleration[1]

f = open("/sd/new.txt", "w")
flag = True

def buttonA_wasPressed():
    global flag
    flag = False
    pass
btnA.wasPressed(buttonA_wasPressed)

while flag == True:
    data = imu0.acceleration[1]
    f.write('{},'.format(data))
    time.sleep_ms(500)
f.close()



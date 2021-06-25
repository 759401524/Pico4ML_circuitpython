import time
import busio
from board import *
from adafruit_icm20x import ICM20948

i2c = busio.I2C(scl=GP5,sda=GP4)  # uses board.SCL and board.SDA
icm = ICM20948(i2c,0x68)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    print("Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (icm.magnetic))
    print("")
    time.sleep(1)
# This example moves a servo its full range (180 degrees by default) and then back.
#Adapted from adafruit example code by A. Roques, Oct 2018

from board import SCL, SDA
import busio, time

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# This example also relies on the Adafruit motor library available here:
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
from adafruit_motor import servo

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50



# The pulse range is 1000 - 2000 by default.
servo7 = servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2400)

#for the pins
while True:
    servo7.angle = 80
    time.sleep(5)
    servo7.angle = 120
    time.sleep(5)
'''
#for the gate - uncomment this and comment out the above to test
while True:
    servo7.angle = 45
    time.sleep(5)
    #servo7.angle = 135
    time.sleep(5)'''

pca.deinit()

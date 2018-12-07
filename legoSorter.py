#import all necessary libraries
from board import SCL, SDA
import busio, time
from bh1745 import BH1745
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

#set up the RGB sensor
bh1745 = BH1745()
bh1745.setup()

#set the LEDs on the sensor and wait a minute to ignore the initial reading
bh1745.set_leds(0.5)
time.sleep(1)

#set up the servo sensor
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

#set up a global variable for the time between bricks
global waitTime
waitTime = 5

#define our 4 servo motors - you may need to change these parameters as you see fit
pins = servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2400)
gate_RGBY = servo.Servo(pca.channels[2], min_pulse=600, max_pulse=2400)
gate_RG = servo.Servo(pca.channels[4], min_pulse=600, max_pulse=2400)
gate_BY = servo.Servo(pca.channels[3], min_pulse=600, max_pulse=2400)

#this function sets the gate as required for a red brick, then waits
def red():
    pins.angle = 82
    print("red!")
    gate_RGBY.angle = 50
    gate_RG.angle = 50
    time.sleep(waitTime)
#this function sets the gate as required for a green brick, then waits
def green():
    pins.angle = 82
    print("green!")
    gate_RGBY.angle = 50
    gate_RG.angle = 130
    time.sleep(waitTime)
#this function sets the gate as required for a blue brick, then waits
def blue():
    pins.angle = 82
    print("blue!")
    gate_RGBY.angle = 130
    gate_BY.angle = 50
    time.sleep(waitTime)
#this function sets the gate as required for a yellow brick, then waits
def yellow():
    pins.angle = 82
    print("yellow!")
    gate_RGBY.angle = 130
    gate_BY.angle = 130
    time.sleep(waitTime)


while True:
    #loads the next brick into the sensor
    pins.angle = 125
    #get sensor values
    r, g, b, c = bh1745.get_rgbc_raw()
    #reduce blue because the LEDs make everything appear slightly bluer than real life
    b = b * 0.925
    #publish readings for manual checks
    print(r, g, b, c)
    time.sleep(1)
    #logic to decide colours - this was decided via trial and error! 
    if r - g < 100 and r - g > -100:
        yellow()
    elif r > g and r > b:
        red()
    elif g > b and g > r:
        green()
    elif b > g and b > r:
        blue()
        
#stop the servo driver.
pca.deinit()


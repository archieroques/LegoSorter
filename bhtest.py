#adapted from pimoroni example code by A. Roques, Oct 2018
#imports libraries
import time
from bh1745 import BH1745

#initialise sensor
bh1745 = BH1745()

#set up sensor and sensor LEDs
bh1745.setup()
bh1745.set_leds(1)

time.sleep(1.0)  # Skip the reading that happened before the LEDs were enabled

try:
    while True:
        #get the readings and print them
        r, g, b, c = bh1745.get_rgbc_raw()
        print(r, g, b, c)
        time.sleep(0.5)

except KeyboardInterrupt:
    #turn off the LEDs if code stops running
    bh1745.set_leds(0)

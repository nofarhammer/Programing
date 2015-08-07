import mraa
import math
import time

from random import randrange
c=0
r=0
g=0
b=0

# Set up the LCD
x=mraa.I2c(0)
x.address(0x62)

# Set up the ADC
adc = mraa.Aio(0)

# initialise device
x.writeReg(0, 0)
x.writeReg(1, 0)

# sent RGB color data
while 1:
        degree = adc.read()             # Read the ADC value
        r=(math.floor(degree)*10+400)%256
        g=(math.floor(degree)*15+150)%256
        b=(math.floor(degree)*20+1)%256
        x.writeReg(0x08, r)
        x.writeReg(0x04, g)
        x.writeReg(0x02, b)
        time.sleep(0.5)

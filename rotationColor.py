import mraa
import math
import time

from random import randrange
c=0
r=0
g=0
b=0

rot=mraa.Aio(0)
x=mraa.I2c(0)
x.address(0x62)

# Set up the PWM
pwm = mraa.Pwm(5)
pwm.enable(True)
pwm.period_us(5000)

# Set up the ADC
adc = mraa.Aio(0)

# initialise device
x.writeReg(0, 0)
x.writeReg(1, 0)

# sent RGB color data
while c<10:
        degree = adc.read()             # Read the ADC value
        r=(math.floor(degree)*10+400)%100
        g=(math.floor(degree)*15+150)%100
        b=(math.floor(degree)*20+1)%100
        x.writeReg(0x08, r)
        x.writeReg(0x04, g)
      #  x.writeReg(0x02, b)
        c=c+1
        time.sleep(0.5)

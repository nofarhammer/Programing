import mraa
import math

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
       # print (rot.read())
        r=randrange(0,256)
        g-randrange(0,256)
        b=randrange(0,256)
        x.writeReg(0x08, r)
        x.writeReg(0x04, g)
        c=c+1
        value = adc.read()             # Read the ADC value
        print (adc)
        led_intensity = value/1024  # Determine the duty cycle based on ADC value
        pwm.write(led_intensity)   
        time.sleep(0.5)

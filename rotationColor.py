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

# initialise device
x.writeReg(0, 0)
x.writeReg(1, 0)

# sent RGB color data
while c<10:
        print (x.read())
        r=randrange(0,256)
        g-randrange(0,256)
        b=randrange(0,256)
        x.writeReg(0x08, r)
        x.writeReg(0x04, g)
        c=c+1

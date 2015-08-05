import mraa
import pyupm_i2clcd as lcd
import math

myLCD = mraa.I2C(0)
#rotate = mraa.A0(0)
myLCD.dir(mraa.DIR_OUT)


 
# display - lcd
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
 
while 1:
		r=math.floor(random()*10)
		g=math.floor(random()*10)
		b=math.floor(random()*10)
       # lcdDisplay.setCursor(0, 0)
        lcdDisplay.set_color(r,g,b)


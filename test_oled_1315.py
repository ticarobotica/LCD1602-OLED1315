from machine import Pin, SoftI2C
from time import sleep_ms
from ssd1306 import SSD1306_I2C

i2c_oled=SoftI2C(sda=Pin(8), scl=Pin(9), freq=100000)
oled=SSD1306_I2C(128,64,i2c_oled)

oled.fill(0)
oled.show()

while 1:
    oled.text("Linia 1",0,0)
    oled.text("Linia 2",0,10)
    oled.text("Linia 3",0,20)
    oled.text("Linia 4",0,30)
    oled.text("Linia 5",0,40)
    oled.text("Linia 6",0,50)  
    oled.show()
    
    sleep_ms(1000)
    oled.fill(0)
    
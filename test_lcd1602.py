from machine import Pin, SoftI2C
from time import sleep_ms
from lcd1602 import LCD1602

i2c_lcd=SoftI2C(sda=Pin(6), scl=Pin(7), freq=100000)
lcd=LCD1602(i2c_lcd, 2, 16)


while 1:
    lcd.setCursor(0,0)
    lcd.print("Linia 1")
    
    lcd.setCursor(0,1)
    lcd.print("Linia 2")
    
    lcd.setCursor(8,0)
    lcd.print("Linia 3")
    
    lcd.setCursor(8,1)
    lcd.print("Linia 4")
    
    sleep_ms(1000)
    
    lcd.clear()
    
    
    
    
    
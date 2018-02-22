#!/usr/bin/python

import time
import Adafruit_CharLCD as LCD

# GPIO.BCM
rs = 14 
e = 15
d4 = 18
d5 = 17
d6 = 27
d7 = 22

cols = 16
rows = 2

lcd = LCD.Adafruit_CharLCD(rs, e, d4,d5,d6,d7, cols, rows)

lcd.message('Hello\nWorld')
time.sleep(2)
lcd.clear()
lcd.show_cursor(True)
lcd.message('Cursor time!')
time.sleep(2)
lcd.clear()

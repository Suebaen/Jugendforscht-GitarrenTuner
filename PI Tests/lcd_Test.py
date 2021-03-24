from rpi_lcd import LCD
from time import sleep
lcd = LCD()
a = 1
print("schau auf dein Display")
lcd.text("Hello",1)
lcd.text("1  2  3  4  5  6" ,2)
a = input()
if (a == 'A'):
    lcd.clear()
    lcd.text("A", 1)
    lcd.text("1  2  3  4  5  6", 2)
elif (a == 'B'):
    lcd.clear()
    lcd.text("B", 1)
    lcd.text("1  2  3  4  5  6", 2)

import time

import Adafruit_MCP3008
from Adafruit_LED_Backpack import SevenSegment
import RPi.GPIO as GPIO

CLK  = 16
MISO = 23
MOSI = 24
CS   = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)

mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
display = SevenSegment.SevenSegment()
display.begin()
colon = False

while True:
 value = mcp.read_adc(0)
 value = round((value/(1024/15.0)+10)*2)/2

 display.clear()
 display.print_float(value, decimal_digits=1)
 display.set_colon(colon)
 display.write_display()
 time.sleep(0.1)

 display.clear()
 display.print_float((10*value), decimal_digits=0)
 display.set_colon(colon)
 display.write_display()
 time.sleep(0.1)

 if GPIO.input(18):
  GPIO.output(5, False)
 else:
  GPIO.output(5, True)






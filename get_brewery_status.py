#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)

while True:
	if GPIO.input(18):
		GPIO.output(5, False)
	else:
		GPIO.output(5, True)

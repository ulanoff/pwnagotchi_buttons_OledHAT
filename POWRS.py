#!/bin/python
import RPi.GPIO as GPIO
import os
import time

gpio_pin_number=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    time.sleep(1.5)
    if (GPIO.input(gpio_pin_number) == 0):
        os.system("sudo shutdown -h now")
    else:
        os.system("sudo reboot -h now")
except:
    pass

GPIO.cleanup()

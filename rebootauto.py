#!/bin/python

import RPi.GPIO as GPIO
import os

gpio_pin_number=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    os.system("sudo touch /root/.pwnagotchi-auto && systemctl restart pwnagotchi")
except:
    pass
GPIO.cleanup()

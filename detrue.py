#!/bin/python

import RPi.GPIO as GPIO
import os

gpio_pin_number=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    os.system("sudo sed -i 's/personality.deauth = false/personality.deauth = true/g' /etc/pwnagotchi/config.toml && systemctl restart pwnagotchi")
except:
    pass

GPIO.cleanup()

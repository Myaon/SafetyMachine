#!/usr/bin/python 
# coding:utf-8 
import time
import RPi.GPIO as GPIO
import os
 
GPIO.setmode(GPIO.BCM)
 
#GPIO18pinを入力モードとし、pull up設定とします 
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
GPIO.wait_for_edge(12, GPIO.FALLING)
 
print("割り込みOK!")
 
GPIO.cleanup()

os.system("sudo reboot")

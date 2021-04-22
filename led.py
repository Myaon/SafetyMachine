import RPi.GPIO as GPIO

Red = 21
Blue = 16
Green =20

GPIO.setmode(GPIO.BCM)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)

def setRGB(R,G,B):
	GPIO.output(Red,R)
	GPIO.output(Green,G)
	GPIO.output(Blue,B)

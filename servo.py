import pigpio
import time
pi=pigpio.pi()

def switchServo():
	pi.set_servo_pulsewidth(18,1500)
	time.sleep(3)
	pi.set_servo_pulsewidth(18,2000)

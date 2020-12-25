import webiopi
import subprocess

# Debug
webiopi.setDebug()
GPIO = webiopi.GPIO
Blue = 21
Green =20

# WebIOPi起動時CALL
def setup(): 
	webiopi.debug("Script with macros - Setup") 
#	GPIO.setFunction(Blue, GPIO.OUT)
#	GPIO.setFunction(Green, GPIO.OUT)
#	GPIO.digitalWrite(Blue, GPIO.HIGH)
#	GPIO.digitalWrite(Green, GPIO.LOW)

# WebIOPi終了時に呼ばれる関数
def destroy(): 
	webiopi.debug("Script with macros - Destroy") 
#	GPIO.digitalWrite(Blue, GPIO.LOW)
	
#defult function
@webiopi.macro
def forward(): 
	webiopi.debug("circle")
#	GPIO.digitalWrite(Green, GPIO.HIGH)
	subprocess.call(["python", "/home/pi/Desktop/safety/Tanaka/special/circle.py"])
	webiopi.debug("circle_stop")
#	GPIO.digitalWrite(Green, GPIO.LOW)
	
@webiopi.macro
def stop(): 
	webiopi.debug("checkCode")
#	GPIO.digitalWrite(Green, GPIO.HIGH)
	subprocess.call(["python", "/home/pi/Desktop/safety/Tanaka/special/checkCode.py"])
	webiopi.debug("checkCode_stop")
#	GPIO.digitalWrite(Green, GPIO.LOW)

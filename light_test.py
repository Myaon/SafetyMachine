# -*- coding: utf-8 -*-
import subprocess
import cv2

time_count = 0

while True:
	time_count=time_count+1
            
	if(time_count>=100):
		subprocess.call(['python', '/home/pi/Desktop/SafetyMachine/save_data.py'])
		time_count=0
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

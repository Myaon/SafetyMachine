# -*- coding: utf-8 -*-
from pyzbar.pyzbar import decode
import cv2

import requests
ifttt_url = 'https://maker.ifttt.com/trigger/raspberry/with/key/gHPH_xDKR664IVIr2YtRRj6BbQoQi-K0mCowIJCGPF3'

# Googleスプレッドシート関連
# url1 = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1=1'
# url0 = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1=0'

import csv
from datetime import datetime

def send_csv(state):
	with open('barcode.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([datetime.now(),state])

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

cap = cv2.VideoCapture(0)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
font = cv2.FONT_HERSHEY_SIMPLEX
oldData = ""

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        d = decode(frame)
        if d:
            for barcode in d:
                x,y,w,h = barcode.rect
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                barcodeData = barcode.data.decode('utf-8')
                #frame = cv2.putText(frame,barcodeData,(x,y-10),font,.5,(0,0,255),2,cv2.CV_AA)
                #print(x+(w/2) )
                if x+(w/2) > 320:
                   send_csv(1)
                   requests.get(ifttt_url)
                else:
                    send_csv(0)
                if oldData != barcodeData:
                   print(barcodeData)
                   oldData = barcodeData
                   send_csv(barcodeData)
                time.sleep(0.5)
        cv2.imshow('frame',frame)
        
    # 物理スイッチを押して停止
    if GPIO.input(22) == GPIO.HIGH:
        break

    # キーボード入力で"q"を押して停止
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
GPIO.cleanup()

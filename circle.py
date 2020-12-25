# -*- coding: utf-8 -*-
import picamera
import picamera.array
import cv2
import numpy as np
minLineLength = 100
maxLineGap = 10

import urllib2

def internet_on():
	try:
		urllib2.urlopen('http://216.58.192.142', timeout=1)
		return True
	except urllib2.URLError as err:
		return False

import requests
ifttt_url = 'https://maker.ifttt.com/trigger/raspberry/with/key/gHPH_xDKR664IVIr2YtRRj6BbQoQi-K0mCowIJCGPF3'

# Googleスプレッドシート関連
# url1 = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1=1'
# url0 = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1=0'

import csv
from datetime import datetime
#import main

def send_csv(state):
	with open('state.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([datetime.now(),state])

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (640, 480)

        while True:
            #main.NoIntervalTime()
            # stream.arrayにBGRの順で映像データを格納
            camera.capture(stream, 'bgr', use_video_port=True)
            # 映像データをグレースケール画像grayに変換
            gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
            # ガウシアンぼかしを適用して、認識精度を上げる
            blur = cv2.GaussianBlur(gray, (9,9), 0)
            # blur = cv2.Canny(gray,50,150,apertureSize = 3)
            # ハフ変換を適用し、映像内の円を探す
            circles = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT,
                      dp=1, minDist=50, param1=120, param2=40, 
                      minRadius=5, maxRadius=100)

            if circles is not None:
                for c in circles[0]:
                    # 見つかった円の上に赤い円を元の映像(system.array)上に描画
                    if c[0] > 320.0:
                        # c[0]:x座標, c[1]:y座標, c[2]:半径
                        cv2.circle(stream.array, (c[0],c[1]), c[2], (0,0,255), 2)
                        print(c[2])
                        send_csv(1)
                        # requests.get(url1)
                        if internet_on():
                            requests.get(ifttt_url)
                    else :
                        cv2.circle(stream.array, (c[0],c[1]), c[2], (0,255,0), 2)
                        send_csv(0)
                        # requests.get(url0)
                        
            # system.arrayをウインドウに表示
            cv2.imshow('frame', stream.array)
            
            # 物理スイッチを押して停止
            if GPIO.input(22) == GPIO.HIGH:
                break
                
            # キーボード入力で"q"を押して停止
            if cv2.waitKey(1) & 0xFF == ord('q'):
                GPIO.cleanup()
                break

            # streamをリセット
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()

# -*- coding: utf-8 -*-
import picamera
import picamera.array
import cv2
import numpy as np

import csv
def toCSV(state):
	with open('fusen.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(state)

import urllib2

def internet_on():
	try:
		urllib2.urlopen('http://216.58.192.142', timeout=1)
		return True
	except urllib2.URLError as err:
		return False

import requests
ifttt_url = 'https://maker.ifttt.com/trigger/raspberry/with/key/gHPH_xDKR664IVIr2YtRRj6BbQoQi-K0mCowIJCGPF3'

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (640, 480)
        # カメラのフレームレートを15fpsにセット
        camera.framerate = 15
        # ホワイトバランスをfluorescent(蛍光灯)モードにセット
        camera.awb_mode = 'fluorescent'

        while True:
            # stream.arrayにBGRの順で映像データを格納
            camera.capture(stream, 'bgr', use_video_port=True)
            print(stream.array[240,320])
            
            # 映像データをHSV形式に変換
            hsv = cv2.cvtColor(stream.array, cv2.COLOR_BGR2HSV)
            print(hsv[240,320])
            print("\n")
            
            # 物理スイッチを押して停止
            if GPIO.input(22) == GPIO.HIGH:
                break
                
            # キーボード入力で"q"を押して停止
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #print(stream.array[265,270])
                #print(stream.array[265,370])
                #toCSV(stream.array[240,320])
                #cv2.imwrite("resc.png", stream.array)
                GPIO.cleanup()
                break
                
            cv2.circle(stream.array,(320,240),3,(0,0,0),thickness=-1)
            #cv2.circle(stream.array,(270,265),3,(0,0,0),thickness=-1)
            #cv2.circle(stream.array,(370,265),3,(0,0,0),thickness=-1)
            
            # system.arrayをウインドウに表示
            cv2.imshow('frame', stream.array)

            # streamをリセット
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()

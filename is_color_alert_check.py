# -*- coding: utf-8 -*-
import cv2
import numpy as np
import led
import RPi.GPIO as GPIO
import urllib2
import requests
import pygame.mixer
import time
import subprocess

# 物理スイッチ設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
  cap = cv2.VideoCapture(0)
  led.setRGB(0,0,1)
  
  # mixer moduleの初期化
  pygame.mixer.init()
  # 再生音源の設定
  pygame.mixer.music.load("/home/pi/SafetyMachine/alert.mp3")
  #play_sound = pygame.mixer.Sound("open_jtalk.wav")
  
  while True:
    # スイッチ状態デバッグ
    #print(GPIO.input(25),GPIO.input(18))
    
    # カメラ未接続で終了
    if (cap.isOpened() == False):
      led.setRGB(0,1,0)
      break
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    #フレームが取得できなかった場合は、画面を閉じる
    if not ret:
      break

    # 映像データをHSV形式に変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 取り出す色を指定
    lower_green = np.array([170,150,50])
    upper_green = np.array([180,255,255])

    # 取り出す色を指定
    lower_red = np.array([0,150,150])
    upper_red = np.array([20,255,255])

    #マスク処理
    #mask1 = cv2.inRange(hsv, lower_green, upper_green)
    #mask2 = cv2.inRange(hsv, lower_red, upper_red)

    #mask = mask1 + mask2
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 輪郭抽出する。
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if(contours):
      # 面積が最大の輪郭を取得する
      contour = max(contours, key=lambda x: cv2.contourArea(x))
      
      # サイズが一定以上であれば
      if(cv2.contourArea(contour) >= 1000):
        print(cv2.contourArea(contour))
        led.setRGB(1,0,0)
        
        
        
    # ウィンドウに出力
    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    # キー入力割り込み処理
    key = cv2.waitKey(1)
    # Escキーを入力されたら画面を閉じる
    if key == 1048603:
      led.setRGB(0,0,0)
      GPIO.cleanup()
      break
      
  cap.release()
  cv2.destroyAllWindows()
  
except KeyboardInterrupt:
  led.setRGB(0,0,0)
  # ひとつ上の階層に画像を保存
  cv2.imwrite("../frame3.png", frame)
  cv2.imwrite("../mask3.png", mask)
  cv2.imwrite("../res3.png", res)
  GPIO.cleanup()

except Exception as e:
  import logging
  logging.basicConfig(filename="test.log",level=logging.DEBUG)
  logging.error(e)
  led.setRGB(0,1,0)
  
else:
  led.setRGB(1,0,0)

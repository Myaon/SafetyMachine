# -*- coding: utf-8 -*-
import picamera
import picamera.array
import cv2
import numpy as np
import subprocess

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        # カメラの解像度を320x240にセット
        camera.resolution = (320, 240)
        # カメラのフレームレートを15fpsにセット
        camera.framerate = 15
        # ホワイトバランスをfluorescent(蛍光灯)モードにセット
        camera.awb_mode = 'fluorescent'
        
        while True:
            # stream.arrayにBGRの順で映像データを格納
            camera.capture(stream, 'bgr', use_video_port=True)
            
            # 物理スイッチを押して停止
            if GPIO.input(22) == GPIO.HIGH:
                break
                
            # キーボード入力で"q"を押して停止
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite("mask_sample.png", stream.array)
                GPIO.cleanup()
                subprocess.call(['python', '/home/pi/Desktop/SafetyMachine/python3/max_window.py'])
                break
            
            # system.arrayをウインドウに表示
            cv2.imshow('frame', stream.array)

            # streamをリセット
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()

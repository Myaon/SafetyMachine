# -*- coding: utf-8 -*-
import picamera
import picamera.array
import cv2
import numpy as np

import led

x1=0
x2=0

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

            # 映像データをHSV形式に変換
            hsv = cv2.cvtColor(stream.array, cv2.COLOR_BGR2HSV)
            
            # 取り出す色を指定
            lower1 = np.array([20,0,30])
            upper1 = np.array([30,140,200])
            lower2 = np.array([60,0,30])
            upper2 = np.array([70,150,200])
            
            #マスク処理
            mask1 = cv2.inRange(hsv, lower1, upper1)
            res1 = cv2.bitwise_and(stream.array, stream.array, mask=mask1)
            mask2 = cv2.inRange(hsv, lower2, upper2)
            res2 = cv2.bitwise_and(stream.array, stream.array, mask=mask2)
            
            #cv2.imshow("frame",stream.array)
            #cv2.imshow("mask",mask)
            
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #cv2.imwrite("stream.png", stream.array)
                #cv2.imwrite("mask.png", mask)
                #cv2.imwrite("res1.png", res1)
                #cv2.imwrite("res2.png", res2)
                GPIO.cleanup()
                break
                
            # １色目の処理
            ret1,thresh1=cv2.threshold(mask1,127,255,0)
            contours1,hierarchy1=cv2.findContours(thresh1,1,2)
            
            if(contours1):
                list1=[]
                for i in range(0,len(contours1)):
                    # 面積リスト化
                    list1.append(cv2.contourArea(contours1[i]))
                    
                    # 一定面積以下の輪郭を除去
                    if cv2.contourArea(contours1[i])<20:
                        cv2.polylines(mask1,contours1[i],True,0,5)
                        
                max_cnt1=max(contours1,key=lambda x:cv2.contourArea(x))
                x1,y1,w1,h1=cv2.boundingRect(max_cnt1)
                print(list1)
                
            # ２色目の処理
            ret2,thresh2=cv2.threshold(mask2,127,255,0)
            contours2,hierarchy2=cv2.findContours(thresh2,1,2)
            
            if(contours2):
                for i in range(0,len(contours2)):
                    # 一定面積以下の輪郭を除去
                    if cv2.contourArea(contours2[i])<20:
                        cv2.polylines(mask2,contours2[i],True,0,5)
                        
                max_cnt2=max(contours2,key=lambda x:cv2.contourArea(x))
                x2,y2,w2,h2=cv2.boundingRect(max_cnt2)
                
            cv2.imshow("res1",mask1)
            cv2.imshow("res2",mask2)
                
            # 表裏判定：裏のとき
            if(x1 > x2):
                led.setRGB(1,0,0)
                
            if(x1 <= x2):
                led.setRGB(0,1,0)
            
            stream.seek(0)
            stream.truncate()
            
        cv2.destroyAllWindows()

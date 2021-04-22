# -*- coding: utf-8 -*-
import cv2
import numpy as np
try:
  cap = cv2.VideoCapture(0)
  while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    #フレームが取得できなかった場合は、画面を閉じる
    if not ret:
      break

    # 映像データをHSV形式に変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 取り出す色を指定
    lower_green = np.array([0,210,50])
    upper_green = np.array([10,255,255])

    #マスク処理
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # ウィンドウに出力
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    #cv2.imshow("res",res)
    
    key = cv2.waitKey(1)
    # Escキーを入力されたら画面を閉じる
    if key == 27:
      break

    elif key == ord("q"):
      break
    
    elif key == ord("s"):
      cv2.imwrite("frame.png", frame)
      cv2.imwrite("mask.png", mask)
      cv2.imwrite("res.png", res)
      break
    
  cap.release()
  cv2.destroyAllWindows()
except KeyboardInterrupt:
  led.setRGB(0,0,0)
  GPIO.cleanup()

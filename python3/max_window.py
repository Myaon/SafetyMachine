# -*- coding: utf-8 -*-
import cv2
import Tkinter as tk

import pyautogui as pgui
from ConfigParser import ConfigParser

TkRoot = tk.Tk()
WindowName = "show"

config = ConfigParser()
config.read('config.ini')

frame = cv2.imread("mask_sample.png")

# ウィンドウをフルスクリーンに設定
cv2.namedWindow(WindowName,cv2.WINDOW_NORMAL)
cv2.setWindowProperty(WindowName, cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

# ディスプレイサイズ取得
desplay_width = TkRoot.winfo_screenwidth()
desplay_height = TkRoot.winfo_screenheight()

# フレームをリサイズ
resize_frame = cv2.resize(frame, (desplay_width , desplay_height))

# 描画
cv2.imshow(WindowName, resize_frame)
key = cv2.waitKey(0)&0xff

hsv = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2HSV)

# マウス位置取得
x, y = pgui.position()
# マウス位置の色取得
mask = hsv[y, x]
print(mask)

# 終了キーに合わせて保存先変更
if key == ord('a'):
	config.set('masking','color1',mask)
if key == ord('b'):
	config.set('masking','color2',mask)
	
# 設定ファイルに書き込み
with open('config.ini','wb') as f:
	config.write(f)
	
cv2.destroyAllWindows()

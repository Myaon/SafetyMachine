# -*- coding: utf-8 -*-
import cv2
import Tkinter as tk

TkRoot = tk.Tk()
WindowName = "show"

frame = cv2.imread("back.png")

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
cv2.waitKey(0)
cv2.destroyAllWindows()

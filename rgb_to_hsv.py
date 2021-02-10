# -*- coding: utf-8 -*-
import cv2
import numpy as np
blank=np.zeros((100,100,3))
#blank+=[180,54,24][::-1] #赤
blank+=[4,72,111][::-1] #青
cv2.imwrite('blank.png',blank)

rgb=cv2.imread('blank.png')
hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
print(hsv[1,1])

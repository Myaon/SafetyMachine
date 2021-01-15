# -*- coding: utf-8 -*-
import cv2

import csv

def toCSV(state):
	with open('hsv.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(state)

im = cv2.imread("resp.png")
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

for x in range(hsv.shape[0]):
	for y in range(hsv.shape[1]):
		#print(im[x,y]) 
		toCSV(hsv[x,y])




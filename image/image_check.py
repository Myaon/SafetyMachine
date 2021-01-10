# -*- coding: utf-8 -*-
import cv2

import csv

def toCSV(state):
	with open('color.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(state)

im = cv2.imread("resp.png")

for x in range(im.shape[0]):
	for y in range(im.shape[1]):
		#print(im[x,y]) 
		toCSV(im[x,y])




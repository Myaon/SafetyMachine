# -*- coding: utf-8 -*-
import csv
import requests
from datetime import datetime

import GY_30_sample
import bme280_sample
import jtalk

url = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1='

def toCSV(state):
	with open('light.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(state)
		
def toSpreadSheet(state):
	requests.get(url+state)
	
#[日時, 温度, 湿度, 気圧, 照度]
bme = bme280_sample.readData()
data=[str(datetime.now()), bme[0], bme[1], bme[2], str(GY_30_sample.getLux())]    
data_str = ",".join(data)
toCSV(data)
toSpreadSheet(data_str)

#jtalk.toText("作業環境に注意して下さい")

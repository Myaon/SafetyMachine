# -*- coding: utf-8 -*-
import csv
import requests
from datetime import datetime

url1 = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1=1'
url0 = 'https://script.google.com/macros/s/AKfycbyPfN0raWgCIkL6zd6aJtsoe31rJ2gX-Yq2X3NqrNa7m5HY4kLt/exec?data1=0'

def toCSV(state):
	with open('state.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(state)
		#writer.writerow([datetime.now(),state])
		
def toSpreadSheet(state):
	requests.get(url1)


from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.ini')

section = 'masking'

print(config.get(section,'color1'))

config.set(section,'color1',"12,23,34")

with open('config.ini','wb') as f:
	config.write(f)

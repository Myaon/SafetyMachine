# -*- coding: utf-8 -*-

import smbus

bus = smbus.SMBus(1);
address = 0x23;
LxRead1=bus.read_i2c_block_data(address,0x20)
#LxRead2=bus.read_i2c_block_data(address,0x10)
print(str(LxRead1[1]*10))
#print(str(LxRead2[1]*10))

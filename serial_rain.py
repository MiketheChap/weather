#!/usr/bin/env python
import sys
import time

import serial
ser = serial.Serial('/dev/ttyACM1', 9600)

while ser.isOpen():
    datastring = ser.readline()
    print datastring
    #print 'The time is:', time.ctime()
time.sleep(2000)
ser.close()

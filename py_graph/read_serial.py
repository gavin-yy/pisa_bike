#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial
import time
# import thread


def print_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp, end=',')
    print(":   ", end=',')

# def serial_rx_thread(no, ser):
#     while (1):
#         str = ser.read(256)

#         if len(str) >= 1:
#             print_time_stamp()

#         for i in range(0, len(str)-1):
#             #print("%.2x " % struct.unpack('B',str[i] ), end='')
#             # not add "\n" at the end
#             print("%.2x " % struct.unpack('B',str[i] ),

# 	if len(str) >= 1:
# 		print ""

#         if len(str) >= 1:
# 	    print " (len=%d) \r\n" % len(str)


def test():
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.001)

    if ser.isOpen():
        print("open success")
    else:
        print("open failed")

    while (1):
        str = ser.read(256)

        if len(str) >= 1:
            print_time_stamp()
            print(str)
    
    # time.sleep(1000*1000)

if __name__== '__main__':  
    test() 



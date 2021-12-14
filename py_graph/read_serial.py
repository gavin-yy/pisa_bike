##serial_read
#!/usr/bin/env python
# -*- coding: utf-8 -*

import serial
import time
import re
# import thread
import draw


def print_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp, end=',')
    print(": ", end=',')

# def serial_rx_thread(no, ser):
# while (1):
# str = ser.read(256)

# if len(str) >= 1:
# print_time_stamp()

# for i in range(0, len(str)-1):
# #print("%.2x " % struct.unpack('B',str[i] ), end='')
# # not add "\n" at the end
# print("%.2x " % struct.unpack('B',str[i] ),

# if len(str) >= 1:
# print ""

# if len(str) >= 1:
# print " (len=%d) \r\n" % len(str)

def extrace_data(str):
    # YAW: 80.4, PITCH: 3.4, ROLL: 7.5
    #['YAW:', '48.1', 'PITCH:', '-3.1', 'ROLL:', '1.8', '', '', '']
    items = re.split(r'\s', str)
    print(items)
    if( len(items) < 6) :
        return
    return [ float(items[1]), float(items[3]), float(items[5]) ]


def main():
    iamge = draw.draw_img()

    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=5)

    if ser.isOpen():
        print("open serial port success")
    else:
        print("open serial port  failed")
        return

    while (1):
        str = ser.readline()

        if len(str) >= 1 and str.decode().find('YAW') != -1:
            ditems = extrace_data(str.decode())
            if (ditems is None) or (len(ditems) < 3):
                continue

            iamge.append_data_array(ditems)
    # time.sleep(1000*1000)

if __name__== '__main__':
    main()
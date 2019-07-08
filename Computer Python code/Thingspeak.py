#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:00:54 2017

@author: ahmed fawzy
"""

import serial   #used to read data from serial port.
import urllib   #used to send https request.
import time     #used to get time.

ApiWriteKey = "IN2WPXEHMEGLFQ6I" #repalce this with your write api key here.

#port name:"COM3", baud rate:9600, timeout:1 
uart=serial.Serial("COM3", 9600, timeout = 1)   #And don't forget to change port name :D

currentTime=time.time() #get time from the begining of uni xsystem.
prevTime = 0
waitTime = 16

while 1 :
    
        msg = uart.readline().decode('ascii') #read data coming from RX arduino.
        print("current Temperature : " + msg) 
        
        currentTime = time.time() 
        
        if (prevTime + waitTime) <= currentTime : #check if 16 seconds has passed cause thingspeak.com accepts data with a time gap of 15 seconds. 
            prevTime = currentTime
            print("sennding to Thingspeak.com : " + msg)
            urllib.urlopen("https://api.thingspeak.com/update?api_key=" + ApiWriteKey + "&field1=" + msg)    #send data to thingspeak.com
        

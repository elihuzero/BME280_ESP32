
# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket
  

from time import sleep

from machine import Pin, I2C
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import BME280

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
#help ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

ssid = 'eLiHuZeRo_4'
password = 'bb52cade4e2f09c2eee00cd75c'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


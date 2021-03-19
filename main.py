# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
from time import sleep
import BME280

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

while True:
  bme = BME280.BME280(i2c=i2c)
  #temp = (bme.read_temperature()/100)
  #temp = str(round(temp))
  #temp1 = bme.temperature
  hum = (bme.read_humidity()/1000)
  hum = str(round(hum))
  #hum1 = bme.humidity
  #pres = (bme.read_pressure())
  #pres = str(round(pres))
  pres1 = bme.pressure
  #pres = (bme.pressure)/100)
  # uncomment for temperature in Fahrenheit
  temp = (bme.read_temperature()/100) * (9/5) + 32
  temp = str(round(temp)) 
  #print('Temperatura: ', temp1)
  #print('Humedad: ', hum1)
  #print('Presion: ', pres)
  
  #Este es el bueno
  #print('Temperatura: ', temp)
  #print('Humedad: ', hum)
  #print('Presion: ', pres1)
  #print('Presion: ', pres)
  
  # APRS-IS login info
  serverHost = 'rotate.aprs2.net'
  serverPort = 14580
  aprsUser = 'XE1REB-10'
  aprsPass = '24503'
  formato = 'utf-8'

  # APRS packet
  callsign = 'FW9275'
  btext1=("!2108.15N/10139.42W_000/000g000t0")
  btext2=("r000p000P000h")
  btext3=("b0")
  btext4=("ESP32BME280")
  btext = btext1+temp+btext2+hum+btext3+pres1+btext4
  #print (btext)

  # create socket & connect to server
  sSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sSock.connect((serverHost, serverPort))
  # logon
  sSock.send(('user %s pass %s vers ESP32BME280\n' % (aprsUser, aprsPass)).encode(formato))
  # send packet
  sSock.send(('%s>APRS:%s\n' % (callsign, btext)).encode(formato))
  # close socket
  #sSock.shutdown(0)
  sSock.close()
  sleep(120)
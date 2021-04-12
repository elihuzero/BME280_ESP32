
from machine import Pin, I2C, reset
from time import sleep
import BME280
import urequests 


# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)  
a = 0
while a <= 9:
  #while True:
  a += 1
  bme = BME280.BME280(i2c=i2c)
  #Humedad
  hum = (bme.read_humidity()/1000)
  hum = str(round(hum))
  #Presion
  pres1 = bme.pressure
  #Temperatura
  temp = (bme.read_temperature()/100 * (9/5) + 32)
  temp = str(round(temp)) 
  #Codigo para el Beeper
  temp1 = (bme.read_temperature()/100)
  temp1 = str(round(temp1))
  press = bme.pressure1
  headers = {
  'Content-Type': 'application/json',
  }  
  auth = ('XE1REB','sXaQCahNgBXDhbGI4oPm')
  var1 = "{ "
  var2 = '"text"'
  var3 = ": "
  var3a = '"XE1REB13: ENES_UNAM Temp='
  var3b = temp1
  var3c = "C" 
  var3d = " Press="
  var3e = press
  var3f = "hPa"
  var3g = " Hum="
  var3h = hum
  var3i = "%"
  var3j = '"'
  var4 = var3a + var3b + var3c + var3d + var3e + var3f + var3g + var3h + var3i + var3j
  var5 = ", "
  var6 = '"callSignNames"'
  var7 = ": "
  var8 = "["
  var9 = '"XE1REB"'
  var10 = "]"
  var11 = ", "
  var12 = '"transmitterGroupNames"'
  var13 = ": "
  var14 = "["
  var15 = '"xa-all"'
  var16 = "]"
  var17 = ", "
  var18 = '"emergency"'
  var19 = ": "
  var20 = "false "
  var21 = "}"
  data1 = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 
  response = urequests.post('http://www.hampager.de:8080/calls', headers=headers, data=data1, auth=auth)
  #Fin Codigo Beeper
  
  #Codigo APRS WX
  # APRS-IS login info
  serverHost = 'rotate.aprs2.net'
  serverPort = 14580
  aprsUser = 'XE1REB-13'
  aprsPass = '24503'
  formato = 'utf-8'

  # APRS packet
  #Pagina para Coordenadas https://www.sunearthtools.com/dp/tools/conversion.php?lang=es
  #GPS: ddmm.mmmm[N,S]ddmm.mmmm[E,W] (Dec Min)
  callsign = 'XE1REB-13'
  btext1=("!2102.67N/10140.35W_000/000g000t0")
  btext2=("r000p000P000h")
  btext3=("b0")
  btext4=("ESP32BME280")
  btext = btext1+temp+btext2+hum+btext3+pres1+btext4
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
  sleep(300)
  #Fin Codigo APRS
else:
  reset()

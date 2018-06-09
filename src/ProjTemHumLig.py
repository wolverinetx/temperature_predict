#!/usr/bin/python
#Import Library
import sys
import time
import Adafruit_DHT #Libreria sensor DHT22
import smbus
import mysql.connector as mariadb
import BH1750

#Define data sensor DHT22
sensor = Adafruit_DHT.AM2302 #DHT22 #'AM2302'
pin = 4

def db_storage():
  mariadb_connection = mariadb.connect(host='localhost', user='user_apl', password='user_apl2018', database='bd_light_temp_hum')
  cursor = mariadb_connection.cursor()
  
  try:
        # Obtain time
        dateTime = time.strftime("%Y-%m-%d %X")
        datee = time.strftime("%Y-%m-%d")
        timee = time.strftime("%X")
        # Obtain the humidity and the temperature from the sensor 
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) #(Adafruit_DHT.AM2302, 4)
        # Obtain the variable light from the sensor
        light = float(BH1750.readLight())
                    
        # Imprime en la consola las variables temperatura y humedad con un decimal
        # print(time.strftime("%Y-%m-%d %X")+'  '+time.strftime("%Y-%m-%d")+'  '+time.strftime("%X")+'  '+'{0:0.2f}  {1:0.2f}'.format(temperature, humidity)+ '  '+ '{0:0.6f}'.format(light) + " lx")
        print(dateTime+'  '+datee+'  '+timee+'  '+'{0:0.2f}  {1:0.2f}'.format(temperature, humidity)+ '  '+ '{0:0.6f}'.format(light) + " lx")
        #print(dateTime+'  ')
        
        # Storage in database Mariadb
        cursor.execute("INSERT INTO light_temperature_humidity (lth_datetime,lth_date,lth_time,lth_value_light,lth_value_temperature,lth_value_humidity) VALUES (%s,%s,%s,%s,%s,%s)", (dateTime,datee,timee,'{:.6f}'.format(light),'{:.2f}'.format(temperature),'{:.2f}'.format(humidity)))
        #cursor.execute("INSERT INTO light_temperature_humidity (lth_datetime,lth_date,lth_time,lth_value_light,lth_value_temperature,lth_value_humidity) VALUES (%s,%s,%s,%s,%s,%s)", (time.strftime("%Y-%m-%d %X"),time.strftime("%Y-%m-%d"),time.strftime("%X"),'{0:0.6f}'.format(light),'{0:0.2f}'.format(temperature),'{0:0.2f}'.format(humidity)))    

  # Se ejecuta en caso de que falle alguna instruccion dentro del try   
  except mariadb.Error as error:
      print("Error: {}".format(error))
  mariadb_connection.commit()
  mariadb_connection.close()

def main():
        # Ciclo principal infinito
        while True:
                    db_storage()
                    
                    # Duerme 1.5 segundo
                    time.sleep(1.5) #1.4)

if __name__=="__main__":
   main()


# Se ejecuta en caso de que falle alguna instruccion dentro del try
# except Exception,e:
	# Imprime en pantalla el error e
  #      print str(e)

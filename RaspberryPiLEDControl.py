from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
import urllib.request
import requests
import threading
import json
import time
import random

## hardware def
led1 = LED(14)
led2 = LED(15)
led3 = LED(18)


##To read the data from thingspeak
def read_data_thingspeak():
	URL='https://api.thingspeak.com/channels/1728230/fields/1.json?api_key='
	KEY='E8AKHE9RFZ3NPKP8'
	HEADER='&results=1'
	NEW_URL=URL+KEY+HEADER
	print(NEW_URL)
	
	get_data = requests.get(NEW_URL).json()
	print(get_data)
	channel_id=get_data['channel']['id']
	print(channel_id)
	
	field_1=get_data['feeds']
	print(field_1)
	moisture=[]
	for x in field_1:
		moisture.append(x['field1'])
		print(x['field1'])
	#moisture = field_1['field1']
	return moisture

##Event Functions
def ledLow():
		led1.on()
		
		led2.off()
		
		led3.off()
		
		
def ledMed():
		led2.on()
		
		led3.off()
		
		led1.off()
		
		
def ledHigh():	
		led3.on()
		
		led2.off()
		
		led1.off()
		
if __name__ == '__main__':
	while True: #infinite loop
		moistureList = read_data_thingspeak()
		moistureStr = (moistureList[0])
		moisture = int(moistureStr)
		
		if moisture < 200:
			ledLow()
		elif moisture < 600:
			ledMed()
		else:
			ledHigh()
		time.sleep(10)

	

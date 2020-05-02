import sys
import urllib2
from time import sleep
import Adafruit_DHT as dht

myAPI = 'My id to be taken ' 
baseURL = 'later' % myAPI 
def DHT22_data():
	
	humi, temp = dht.read_retry(dht.DHT22, 23) 
	return humi, temp
while True:
	try:
		humi, temp = DHT22_data()
		
		if isinstance(humi, float) and isinstance(temp, float):
			
			humi = '%.2f' % humi 					   
			temp = '%.2f' % temp
			
			
			conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s' % (temp, humi))
			print conn.read()
			# Closing the connection
			conn.close()
		else:
			print 'Error'
		
		sleep(20)
	except:
		break

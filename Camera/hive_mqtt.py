import paho.mqtt.client as paho
import time
from datetime import datetime
import json
import ssl

def pub(counter):

	def on_publish(client, userdata, mid):
		print("mid: "+str(mid))
	
	client = paho.Client()
	client.on_publish = on_publish
	#client.connect("broker.mqttdashboard.com", 1883)
	awshost = "a2194p2itxgbgc-ats.iot.us-west-2.amazonaws.com"      # Endpoint
	awsport = 8883                                              # Port no.   
	clientId = "fahmanpi"                                     # Thing_Name
	thingName = "fahmanpi"                                    # Thing_Name
	caPath = "/home/pi/certs/AmazonRootCA1.pem"                                      # Root_CA_Certificate_Name
	certPath = "/home/pi/certs/certificate.pem.crt"                            # <Thing_Name>.cert.pem
	keyPath = "/home/pi/certs/private.pem.key"                          # <Thing_Name>.private.key
	
	client.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
	
	client.connect(awshost, awsport, keepalive=60)    
	client.loop_start()
	
	
	
	device_name = "fahmanpi"
	time_stamp = datetime.now()
	paylodmsg0="{"
	paylodmsg1="\"device_name\" : \""
	paylodmsg2 = "\",\"time_stamp\": \""
	paylodmsg3 = "\", \"number_of_People\":"
	paylodmsg4="}"
	paylodmsg = "{} {} {} {} {} {} {} {}".format(paylodmsg0, paylodmsg1,device_name, paylodmsg2,time_stamp, paylodmsg3,counter,paylodmsg4)	
	paylodmsg = json.dumps(paylodmsg) 
	paylodmsg_json = json.loads(paylodmsg)
	client.publish("school/area1", paylodmsg_json, qos=1)
	time.sleep(5)

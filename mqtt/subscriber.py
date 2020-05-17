"""This script is an example of subscriber to CloudMQTT Broker"""
import paho.mqtt.client as mqttClient
import time


# Define event callbacks
def on_connect(mosq, obj, rc):
    print('Reconnect: {}'.format(str(rc)))

def on_subscribe(mosq, obj, mid, granted_qos):
    print('Subscribed: {}, QoS: {}'.format(str(mid), str(granted_qos)))
 


# After you successfully the publisher and subscribe code, 
# try to create your own MQTT broker by create an account at cloudmqtt.com
broker_address= 'mqtt.eclipse.org'
port = 1883 

 
client = mqttClient.Client()               #create new instance
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
    time.sleep(0.1)
 
try:
    while True: 
        #value = input('Enter the message:')
        client.subscribe('python/')
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
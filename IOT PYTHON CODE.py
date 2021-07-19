import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json

#Provide your IBM Watson Device Credentials
organization = "gy3kt7"
deviceType = "iotdevice"
deviceId = "1001"
authMethod = "token"
authToken = "qwertyuiop"


# Initialize the device client.
L=0
F=0

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data['command'])


        if cmd.data['command']=='switchon':
                print("SWITCH ON IS RECEIVED")
                
                
        elif cmd.data['command']=='seitchoff':
                print("SWITCH OFF IS RECEIVED")
        
        
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        L=23
        F=45
        #Send Temperature & Humidity to IBM Watson
        data = {"d":{ 'lubricantlevel' : L, 'flowrate': F }}
        print (data)
        def myOnPublishCallback():
            print ("Published Lubricant level = %s C" % L, "Flow rate = %s %%" % F, "to IBM Watson")

        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()

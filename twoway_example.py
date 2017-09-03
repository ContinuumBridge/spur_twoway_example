#!/usr/bin/env python
# twoway_example.py
# Copyright (C) ContinuumBridge Limited, 2017
# Written by Peter Claydon
#

import json
import os.path
import signal
import ibmiotf.application
 
HOME                    = os.getcwd()
 
#api watson={"org": "adqdih", "auth-key": "a-adqdih-ledf1cloph", "auth-token": ")FvwxZWtT(@GpLE5&t"}
config = {
"org": "adqdih",
"auth-key": "a-adqdih-3igw2njxct",
"auth-token": "vnd2lLIqFXPFBYbgAF",
"screensetName": "Watson_Clean",
"listName": "Test",
"buttonName": "Test_Button_703"
}

deviceTypeId            = config["screensetName"]
deviceId                = config["listName"] + "-" + config["buttonName"]

print("deviceTypeId: {}, deviceId: {}".format(deviceTypeId, deviceId))

def watsonCallback(event):
    data = json.dumps(event.data)
    print("{} event received from button {}, data: {}".format(event.event, event.device, data))
    commandData={"test_response" : "test"}
    watsonClient.publishCommand(deviceTypeId, deviceId, "test", "json", commandData)
    print("Successfully publishted update")

try:
    options = {
        "org": config["org"],
        "id": "spur",
        "auth-method": "apikey",
        "auth-key": config["auth-key"],
        "auth-token": config["auth-token"]
    }
    watsonClient = ibmiotf.application.Client(options)
    print("Created Watson client")
except ibmiotf.ConnectionException as e:
    print("Watson Client creation exception: {}, organsiation: {}".format(e, watsonParams))
    exit()

deviceTypeInfo = watsonClient.api.getDeviceType(deviceTypeId)
print("Got deviceTypeInfo")
print("devieTupeInfo: {}".format(deviceTypeInfo))

try:
    watsonClient.connect()
    print("Watson client connected")
except ibmiotf.ConnectionException as e:
    print("Unable to connect to Watson, exception: {}".format(e))
    exit()

watsonClient.deviceEventCallback = watsonCallback
print("Watson client callback registered")
watsonClient.subscribeToDeviceEvents(deviceType=deviceTypeId)
print("Watson client subscribed to events")

signal.pause()

#!/usr/bin/env python
# twoway_example.py
# Copyright (C) ContinuumBridge Limited, 2017
# Written by Peter Claydon
#

import json
import time
import sys
import os.path
import logging
import logging.handlers
import ibmiotf.application
 
config                  = {}
HOME                    = os.getcwd()
CB_LOGFILE              = HOME + "/client.log"
CB_LOGGING_LEVEL        = "DEBUG"
 
config = {
"org": "adqdih",
"auth-key": "a-adqdih-ledf1cloph",
"auth-token": ")FvwxZWtT(@GpLE5&t",
"screensetName": "Watson_Clean",
"listName": "Test",
"buttonName": "Button_703"
}

deviceTypeId            = config["screensetName"]
deviceId                = config["listName"] + "-" + config["buttonName"]

def watsonCallback(event):
    print("{} event received from button {}, data: {}".format(event.event, event.device, json.dumps(event.data)))

try:
    #options = ibmiotf.application.ParseConfigFile(configFilePath)
    options = {
        "org": config["org"],
        "id": "spur",
        "auth-method": "apikey",
        "auth-key": config["auth-key"],
        "auth-token": config["auth-token"]
    }
    watsonClient = ibmiotf.application.Client(options)
except ibmiotf.ConnectionException as e:
    print("Watson Client creation exception: {}, organsiation: {}".format(e, watsonParams))
    exit()

try:
    watsonClient.connect()
except ibmiotf.ConnectionException as e:
    print("Watson client connection or subscription exception: {}, organsiation: {}".format(e, watsonParams))

watsonClient.deviceEventCallback = watsonCallback
print("Watson client callback registered")
watsonClient.subscribeToDeviceEvents(deviceType=deviceTypeId)
print("Watson client subscribed to events")
time.sleep(30)

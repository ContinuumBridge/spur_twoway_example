#!/usr/bin/env python
# twoway_example.py
# Copyright (C) ContinuumBridge Limited, 2017
# Written by Peter Claydon
#

import json
import time
import sys
import signal
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
"auth-key": "a-adqdih-3igw2njxct",
"auth-token": "vnd2lLIqFXPFBYbgAF",
"screensetName": "Watson_Clean",
"listName": "Test",
"buttonName": "Button_703"
}

deviceTypeId            = config["screensetName"]
deviceId                = config["listName"] + "-" + config["buttonName"]

def watsonCallback(event):
    data = json.dumps(event.data)
    print("{} event received from button {}, data: {}".format(event.event, event.device, data))
    commandData={"test_response" : "test"}
    watsonClient.publishCommand(deviceTypeId, deviceId, "test", "json", commandData)
    print("Successfully publishted update")

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
    print("Unable to connect to Watson, exception: {}".format(e))
    exit()

watsonClient.deviceEventCallback = watsonCallback
print("Watson client callback registered")
watsonClient.subscribeToDeviceEvents(deviceType=deviceTypeId)
print("Watson client subscribed to events")
signal.pause()

#!/usr/bin/env python
# twoway_example.py
# Copyright (C) ContinuumBridge Limited, 2017
# Written by Peter Claydon
#

import json
import ibmiotf.application
 
#api watson={"org": "adqdih", "auth-key": "a-adqdih-ledf1cloph", "auth-token": ")FvwxZWtT(@GpLE5&t"}
#api: watson={"org":"adqdih", "auth-key": "a-adqdih-ledf1cloph", "auth-token": ")FvwxZWtT(@GpLE5&t"}
config = {
"org": "adqdih",
"auth-key": "a-adqdih-3igw2njxct",
"auth-token": "vnd2lLIqFXPFBYbgAF",
"screensetName": "Watson_Clean",
"listName": "Test",
"buttonName": "Test_Button_703"
}

options = {
    "org": "adqdih",
    "id": "spur",
    "auth-method": "apikey",
    "auth-key": "a-adqdih-ledf1cloph",
    "auth-token": ")FvwxZWtT(@GpLE5&t"
}
watsonClient = ibmiotf.application.Client(options)
print("Created Watson client")

#watsonClient.connect()
print("Watson client connected")

watsonClient.deviceEventCallback = watsonCallback
print("Watson client callback registered")
watsonClient.subscribeToDeviceEvents(deviceType=deviceTypeId)
print("Watson client subscribed to events")


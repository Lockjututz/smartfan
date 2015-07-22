#!/usr/bin/python

import requests, json

def sendLogsToServer(logsList):
    payload = [{'fromDate':'2015-07-22 22:17:00', 'temp':'23', 'humid':'34'}]
    r = requests.post("http://192.168.0.200:8071/smartfan-server/storelogs",data=json.dumps(payload))
    if r.status != 200:
        print "Non-OK response"

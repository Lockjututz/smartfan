#!/usr/bin/python

import requests, json
import sensor_repository as repo

remote_url = "http://192.168.0.200:8071"

def sendLogsToServer():
    req1 = requests.get(remote_url + "/latestlog/")
    if req1.status_code == 200:
        timestamp = json.loads(req1.content)['timestamp']
        payload = repo.getLogsAfterTimestamp(timestamp)
        postReqHeaders = {"Content-Type":"application/json"}
        req2 = requests.post(remote_url + "/storelogs/", data=json.dumps(payload), headers=postReqHeaders)
        if req2.status_code != 200:
            print "Non-OK response"
            #TODO add proper logging

#! /bin/python
import dht11_sensor
import sensor_repository as repo
import backend_service as backend
import tellstick_client
from multiprocessing import Pool
import time
import logging
from sys import exc_info

def setupLogging():
    logging.basicConfig(filename='status.log',level=logging.WARNING)
    logging.warning('Logging (re)started at %s', time.strftime("%d-%m-%Y %H:%M:%S"))

def sensorReadFailure(logs):
    return logs == -1 or logs == -2 or logs == -3

def last3LogsAreOverTempLimit(last3Logs):
    return len(filter(lambda x: x["temperature"] >= 24, last3Logs)) == 3

def isDaytime(hour):
    return hour > 9 and hour < 22
    
def sendLogsToServer():
    logging.info("Sending logs to server")
    backend.sendLogsToServer()

def main():
    setupLogging()

    pool = Pool(processes=1)
    while (True):
        try:
            for i in range(10):
                logs = dht11_sensor.readSensor()
                if sensorReadFailure(logs):
                    time.sleep(2)
                    continue
        
            if not sensorReadFailure(logs):
                # store sensor logs locally
                repo.storeData(logs['temp'], logs['humid'])
            
                # send logs to backend server
                pool.apply_async(sendLogsToServer, [])
                
                # make fan activation decision
                if isDaytime(int(time.strftime('%H'))) and last3LogsAreOverTempLimit(repo.getLastTrio()):
                    tellstick_client.activateFan()
                else:
                    tellstick_client.deactivateFan()
            
            time.sleep(60)
        except:
            logging.error("%s %s",time.strftime("%d-%m-%Y %H:%M:%S"),exc_info())

if __name__ == "__main__":
    main()

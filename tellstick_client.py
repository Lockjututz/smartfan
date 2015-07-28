from tellcore.telldus import TelldusCore
from time import time

def activateFan():
    core = TelldusCore()
    #lamp = core.add_device("lamp", "arctech", "selflearning-switch", house=12345, unit=1)
    #lamp.turn_on()
    
    for device in core.devices():
        #print device.name
        if "Fan control device" == device.name:
            device.turn_on()
            time.sleep(3)
            device.turn_off()

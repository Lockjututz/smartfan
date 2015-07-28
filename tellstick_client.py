from tellcore.telldus import TelldusCore
import time

def activateFan():
    core = TelldusCore()
    for device in core.devices():
        if "Fan control device" == device.name:
            device.turn_on()

def deactivateFan():
    core = TelldusCore()
    for device in core.devices():
        if "Fan control device" == device.name:
            device.turn_off()

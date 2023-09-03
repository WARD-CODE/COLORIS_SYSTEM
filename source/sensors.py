

import os
import time

class PositionSensor:

    def __init__(self, PIN):
        self.pin = PIN
        self.sensor_position = 0
        os.system("gpio mode {} in".format(self.pin))

    def read(self):
        os.system("gpio read {}".format(self.pin))

class InSensor(PositionSensor):
    def __init__(self,PIN):
        super.__init__(PIN)


class OutSensor(PositionSensor):
    def __init__(self,PIN):
        super.__init__(PIN)

class UpSensor:
    pass

class DownSensor:
    pass

class TemperatureSensor:
    def __init__(self, PIN):
        self.PIN = PIN
        self.sensor_value = 0.0
    
    def read(self):
        os.system("gpio mode {} in".format(self.PIN))

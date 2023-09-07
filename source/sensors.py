

import os
import subprocess

class PositionSensor:

    def __init__(self, PIN):
        self.pin = PIN
        self.sensor_position = 0
        os.system("gpio mode {} in".format(self.pin))

    def read(self):
        return int(subprocess.check_output("gpio read {}".format(self.pin), shell = True).decode("utf-8").strip())

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

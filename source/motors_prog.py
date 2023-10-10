
import os
import time

"""
pinout:
    STEP: 2 (physical pinout 7)
    DIR: 1 (physical pinout 5)

parPerRev: the minimum part of rotation (full rotation , half, quarter ...)

"""

class Motor:
    DISTANCE = 0
    LARGEUR = 0
    UNITE = 0
    VIBRATION = 0

    def __init__(self, stepPin,dirPin, partPerRev=25):

        self.stepPin = stepPin
        self.dirPin = dirPin
        self.partPerRev = partPerRev
        os.system("gpio mode {} out".format(self.stepPin))
        os.system("gpio mode {} out".format(self.dirPin))

    def forward(self,distance):    
        os.system("gpio write {} 0".format(self.dirPin))
        for rev in range((distance)*self.partPerRev):    
            os.system("gpio write {} 0".format(self.stepPin))
            time.sleep(0.0005)
            os.system("gpio write {} 1".format(self.stepPin))
            time.sleep(0.0005)


    def backward(self,distance):
        os.system("gpio write {} 1".format(self.dirPin))
        for rev in range((distance)*self.partPerRev):    
            os.system("gpio write {} 0".format(self.stepPin))
            time.sleep(0.0005)
            os.system("gpio write {} 1".format(self.stepPin))
            time.sleep(0.0005)
    
    def config(self,unite,distance,largeur,vibration):
        self.DISTANCE = distance
        self.LARGEUR = largeur
        self.UNITE = unite
        self.VIBRATION = vibration



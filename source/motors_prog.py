
import os
import time

"""
pinout:
    STEP: 2 (physical pinout 7)
    DIR: 1 (physical pinout 5)

parPerRev: the minimum part of rotation (full rotation , half, quarter ...)

"""

class Motor:

    FORWARD_VERTICAL_REV = 8
    BACKWARD_VERTICAL_REV = 8

    PICK_REV = 3 

    FORWARD_HORIZONTAL_REV = 15
    BACKWARD_HORIZONTAL_REV = 15
    HOME_HORIZONTAL_REV = 150

    



    def __init__(self, stepPin,dirPin, partPerRev=200):

        self.stepPin = stepPin
        self.dirPin = dirPin
        self.partPerRev = partPerRev
        self.forward_allow = True
        self.pickup_allow = True
        os.system("gpio mode {} out".format(self.stepPin))
        os.system("gpio mode {} out".format(self.dirPin))

    def forward(self,revolution):    
        os.system("gpio write {} 1".format(self.dirPin))

        for rev in range(revolution*self.partPerRev):    
            os.system("gpio write {} 0".format(self.stepPin))
            time.sleep(0.0005)
            os.system("gpio write {} 1".format(self.stepPin))
            time.sleep(0.0005)


    def backward(self,revolution):
        os.system("gpio write {} 0".format(self.dirPin))
        
        for rev in range(revolution*self.partPerRev):    
            os.system("gpio write {} 0".format(self.stepPin))
            time.sleep(0.0005)
            os.system("gpio write {} 1".format(self.stepPin))
            time.sleep(0.0005)

    def stop(self):
        os.system("gpio write {} 0".format(self.stepPin))



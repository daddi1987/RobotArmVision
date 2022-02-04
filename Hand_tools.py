__author__      = "Davide Zuanon"
__copyright__   = "Copyright 2009, Planet Earth"
__maintainer__ = "Davide Zuanon"
__email__ = "davide.zuanon@outlook.it"
__status__ = "Development"

import time

from pyfirmata import ArduinoNano, SERVO
import serial

class HeadAndTools():

    def __init__(self,port):
        self.HendRobot = ArduinoNano(port)
        #self.HendRobot.readline()

    def setHead(self,PinHead,Value_Open,Value_Close):
        self.PinHead = PinHead
        self.HendRobot.digital[PinHead].mode = SERVO
        self.OpenGripperValue = Value_Open
        self.CloseGripperValue = Value_Close

    def OpenGripper(self):
       self.HendRobot.digital[self.PinHead].write(self.OpenGripperValue)
       print("OpenGripper")
       time.sleep(1)

    def CloseGripper(self):
       self.HendRobot.digital[self.PinHead].write(self.CloseGripperValue)
       print("CloseGripper")
       time.sleep(1)
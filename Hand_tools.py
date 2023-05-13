__author__      = "Davide Zuanon"
__copyright__   = "Copyright 2009, Planet Earth"
__maintainer__ = "Davide Zuanon"
__email__ = "davide.zuanon@outlook.it"
__status__ = "Development"

import time

import pyfirmata
from pyfirmata import ArduinoNano, SERVO, PWM

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

    def LaserPointer(self,PinLaser,state):
       self.HendRobot.digital[PinLaser].write(state)

    def HendLight(self,PinHLight,state):
       self.HendRobot.digital[PinHLight].write(state)

    def HendLightPWM(self, PinHLight, PwmLight):
        self.HendRobot.digital[PinHLight].mode = PWM

        if int(PwmLight) > 100 or int(PwmLight) < 0:
            raise "VALORI DI PWM FUORI SOGLIA MIN-MAX"
        else:
            new_valueLight = PwmLight / 100.0
            self.HendRobot.digital[PinHLight].write(new_valueLight)

__author__      = "Davide Zuanon"
__copyright__   = "Copyright 2009, Planet Earth"
__maintainer__ = "Davide Zuanon"
__email__ = "davide.zuanon@outlook.it"
__status__ = "Development"

# http://archive.fabacademy.org/archives/2016/fablabtoscana2016/projects/laser_pointer2.html
# http://domoticx.com/mechanica-firmware-grbl-info-commandos/
# https://github.com/gnea/grbl/wiki/Grbl-v1.1-Interface
# https://zeevy.github.io/grblcontroller/machine-status-panel.html


# Questo codice serve ad impartire cordinate al braccio robotico, utilizzando la porta seirale collegata
# tramite USB tra From PC to Arduino FW (Grbl Mod. Gripper)
# Lo scopo di questo documento e riuscire a creare una libreria che invii cordinate assolute al Robot e gestisca
# le funzionalità del FW grbl.

import sys
import serial
import time

ReleaseFw = "Grbl 0.9i ['$' for help]"
StringEndMessage = b'\nok\r'


#Class For Read and Feadback value String
class RobotArm():

    StatusRobot = b'<Idle,MPos:0.000,0.000,0.000,WPos:0.000,0.000,0.000>\r'
    # Mapping State Robot
    RobotStop = "Idle"
    RobotRun = "Run"

    def __init__(self,port,baudrate):
        self.RobotArmSerial = serial.Serial(port=port, baudrate=baudrate, bytesize=8, parity='N', stopbits=1, timeout=None)
        self.RobotArmSerial.readline()

    def CheckConnectionRobot(self): # Check Connection
        StringRead = str(self.RobotArmSerial.readline())
        StringRead = StringRead[2:-5]  # Delete last 6 \\r\\n
        LenString = len(StringRead)

        if (StringRead == ReleaseFw):
            #print("Robot Arm Ready")
            RobotReady = "Robot Arm Ready"
            time.sleep(2)
            self.RobotArmSerial.flushInput()

        else:
            #print("Robot Arm Not Ready")
            RobotReady = "Robot Arm Not Ready"
            self.RobotArmSerial.close()
        return(RobotReady)

    def  _Carriage_Return(self):
        self.RobotArmSerial.write(b"\r\n")

    def _writevalue(self,string):
        valueToSend = bytearray(string, 'utf-8')
        self.RobotArmSerial.write(valueToSend)
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.150)
        print(RobotArm._readline(self))
        self.RobotArmSerial.flushInput()

    def _softReset(self):
        self.RobotArmSerial.write(b'\030')
        print(self.RobotArmSerial.readline())
        time.sleep(2)
        self.RobotArmSerial.flushInput()

    def _readline(self):
        eol = b'\r'
        leneol = len(eol)
        line = bytearray()
        while True:
            c = self.RobotArmSerial.read(1)
            if c:
                line += c
                if line[-leneol:] == eol:
                    break
            else:
                break
        return bytes(line)

    def _readFeadback(self):
        eol = b'\r'
        leneol = len(eol)
        Feadback = bytearray()
        while True:
            c = self.RobotArmSerial.read(1)
            if c:
                Feadback += c
                if Feadback[-leneol:] == eol:
                    if Feadback == b'ok\r':
                        Feadback = True
                    else:
                        Feadback = False
                    break
            else:
                break
        return Feadback

    def CheckParameters(self):
        # Check Parameter
        print("\n--------Check Parameter:--------")
        self.RobotArmSerial.write(b"$#\n")
        while True:
            StringRead = RobotArm._readline(self)
            PrintParamiters = str(StringRead)
            PrintParamiters = PrintParamiters.replace("b'","")
            PrintParamiters = PrintParamiters.replace("\\n","")
            PrintParamiters = PrintParamiters.replace("\\r'","")
            print(PrintParamiters)
            if (StringRead == StringEndMessage):
                break

    def ShowHelpMenu(self):
        # Check Help Menu
        print("\n--------Check Help Menu:--------")
        self.RobotArmSerial.write(b"$\n")
        while True:
            StringRead = RobotArm._readline(self)
            PrintHelp = str(StringRead)
            PrintHelp = PrintHelp.replace("b'", "")
            PrintHelp = PrintHelp.replace("\\n", "")
            PrintHelp = PrintHelp.replace("\\r'", "")
            print(PrintHelp)
            if (StringRead == StringEndMessage):
                break

    def CheckParametersSetup(self):
        # Check Setup
        print("\n--------Check Setup:--------")
        self.RobotArmSerial.write(b"$$\n")
        while True:
            StringRead = RobotArm._readline(self)
            PrintSetup = str(StringRead)
            PrintSetup = PrintSetup.replace("b'", "")
            PrintSetup = PrintSetup.replace("\\n", "")
            PrintSetup = PrintSetup.replace("\\r'", "")
            print(PrintSetup)
            if (StringRead == StringEndMessage):
                break

    def StatusRobot(self):  # Check State example ('Idle', 'MPos:0.000', '0.000', '0.000', 'WPos:0.000', '0.000', '0.000')
        self.RobotArmSerial.write(b"?")
        StringRead = RobotArm._readline(self)
        StringRead = str(StringRead)[3:-4]
        StringRead = StringRead.replace("MPos:", "", 1)
        StringRead = StringRead.replace("WPos:", "", 1)
        StringRead = StringRead.replace("n<", "", 1)
        StatusRobot = StringRead.split(',')
        for i in range(6):
            try:
                StatusRobot[1+i] = float(StatusRobot[1+i])
            except:
                #Condiction Error Try Read Serial
                self.RobotArmSerial.write(b"\r\n")
                self.RobotArmSerial.flushInput()
                self.RobotArmSerial.flushOutput()
                time.sleep(5)
                print("Error Tentative")
                break
            RobotArm.StateRobot = tuple(StatusRobot)
        #print(StatusRobot)
        self.RobotArmSerial.write(b"\r\n\r\n")  # End Check state find Termination ok
        FeadBackRobot = RobotArm._readFeadback(self)
        print(FeadBackRobot)
        time.sleep(0.150)  #Insert Sleep Time Frequency 6.5Hz, Fix Control position during move, the document Grbl preveded no more 10Hz call to status position robot. For librery set to 6.5Hz
        self.RobotArmSerial.flushInput()
        self.RobotArmSerial.flushOutput()
        #print("End Read Message: ", FeadBackRobot)
        return(StatusRobot,FeadBackRobot)

    def GoToPosition(self, X_Target, Y_Target, Z_Target, Speed):
        print("------GoToPosition-------")
        X_Target = str(X_Target)
        Y_Target = str(Y_Target)
        Z_Target = str(Z_Target)
        Speed = str(Speed)
        StringMove = "G90X{X_Target}Y{Y_Target}Z{Z_Target}F{Speed}\n".format(X_Target=X_Target, Y_Target=Y_Target, Z_Target=Z_Target, Speed=Speed)
        self.RobotArmSerial.write(StringMove.encode())
        RobotArm._readFeadback(self)

        RobotArm.StatusRobot(self)
        if (RobotArm.StateRobot[0] == "Run"):
            print("First Tentative")
            while RobotArm.StateRobot[0] == "Run": #Wait InPosition Robot State
                self.RobotArmSerial.flushInput()
                print(RobotArm.StatusRobot(self))
                print("Robot Move")
                time.sleep(0.025)
            if (RobotArm.StateRobot[0] == "Idle"):
                X_Target = float(X_Target)
                X_Target = round(X_Target,1)
                ValueXAproximated = RobotArm.StateRobot[1]
                ValueXAproximated = round(ValueXAproximated,1)
                if ValueXAproximated == X_Target:
                    #print("X in Position")
                    Y_Target = float(Y_Target)
                    Y_Target = round(Y_Target, 1)
                    ValueYAproximated = RobotArm.StateRobot[2]
                    ValueYAproximated = round(ValueYAproximated, 1)
                    if ValueYAproximated == Y_Target:
                        #print("Y in Position")
                        Z_Target = float(Z_Target)
                        Z_Target = round(Z_Target, 1)
                        ValueZAproximated = RobotArm.StateRobot[3]
                        ValueZAproximated = round(ValueZAproximated, 1)
                        if ValueZAproximated == Z_Target:
                            #print("Z in Position")
                            print("In Target -- X Axis= " ,X_Target,"mm" ," Y Axis" ,Y_Target,"mm" ," Z Axis" ,Z_Target,"mm")
                            RobotState = "In_Position"
                        else:
                            print("Error: Z not in position")
                    else:
                        print("Error: Y not in position")
                else:
                    print("Error: X not in position")
            else:
                print(RobotArm.StateRobot[0])
        else:
            time.sleep(0.1)
            print("Second Tentative")
            while RobotArm.StateRobot[0] == "Run":  # Wait InPosition Robot State
                self.RobotArmSerial.flushInput()
                print(RobotArm.StatusRobot(self))
                print("Robot Move")
                time.sleep(0.025)
            if (RobotArm.StateRobot[0] == "Idle"):
                X_Target = float(X_Target)
                X_Target = round(X_Target, 1)
                ValueXAproximated = RobotArm.StateRobot[1]
                ValueXAproximated = round(ValueXAproximated, 1)
                if ValueXAproximated == X_Target:
                    # print("X in Position")
                    Y_Target = float(Y_Target)
                    Y_Target = round(Y_Target, 1)
                    ValueYAproximated = RobotArm.StateRobot[2]
                    ValueYAproximated = round(ValueYAproximated, 1)
                    if ValueYAproximated == Y_Target:
                        # print("Y in Position")
                        Z_Target = float(Z_Target)
                        Z_Target = round(Z_Target, 1)
                        ValueZAproximated = RobotArm.StateRobot[3]
                        ValueZAproximated = round(ValueZAproximated, 1)
                        if ValueZAproximated == Z_Target:
                            # print("Z in Position")
                            print("In Target -- X Axis= ", X_Target, "mm", " Y Axis", Y_Target, "mm", " Z Axis",Z_Target, "mm")
                            RobotState = "In_Position"
                        else:
                            print("Error: Z not in position")
                    else:
                        print("Error: Y not in position")
                else:
                    print("Error: X not in position")


# Open GRBL serial port
# Example for Raspberry serial.Serial('/dev/tty.usbmodem1811',115200)
Robot = RobotArm("COM4",115200)
#RobotArmSerial = serial.Serial(port="COM4", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None)

print("Initializing RobotArm")
# Wait for grbl to initialize and flush startup text in serial input
# Wake up grbl

#RobotArmSerial.write(b"\r\n")
Robot._Carriage_Return()

print(Robot.CheckConnectionRobot()) #Check Connection Function launch

Robot._writevalue("$I")

Robot._softReset()
time.sleep(5)

print(Robot.StatusRobot())#StatusRobot
print(Robot.StateRobot[0])#Robot Status
print(Robot.StateRobot[1])# XPosition
print(Robot.StateRobot[2])# YPosition
print(Robot.StateRobot[3])# ZPosition


Robot.CheckParameters() #Go Print Check Parameters

Robot.ShowHelpMenu() #Go Print Help Menu

Robot.CheckParametersSetup() # Print Parameters Setup
i=0
while i < 5:
    #RobotArm().GoToPosition(-80,100.1,40.123,1000) #Function GoToPosition
    Robot.GoToPosition(-80, 100.1, 40.123, 1000)
    print("Command GoTOPos End")

    #RobotArm().GoToPosition(0,0,0,10) #Function GoToPosition second move
    Robot.GoToPosition(0,0,0,1000)
    print("Command GoTOPos End")

    #RobotArm().GoToPosition(80,100.1,40.123,1000) #Function GoToPosition
    Robot.GoToPosition(80,100.1,40.123,1000)
    print("Command GoTOPos End")

    #RobotArm().GoToPosition(0,0,0,10) #Function GoToPosition second move
    Robot.GoToPosition(0,0,0,10)
    print("Command GoTOPos End")

    i= i+1
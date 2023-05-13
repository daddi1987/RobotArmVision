__author__      = "Davide Zuanon"
__copyright__   = "Copyright 2022, Planet Earth"
__maintainer__ = "Davide Zuanon"
__email__ = "davide.zuanon@outlook.it"
__status__ = "Development"

# http://archive.fabacademy.org/archives/2016/fablabtoscana2016/projects/laser_pointer2.html
# http://domoticx.com/mechanica-firmware-grbl-info-commandos/
# https://github.com/gnea/grbl/wiki/Grbl-v1.1-Interface
# https://zeevy.github.io/grblcontroller/machine-status-panel.html


# This code is used to give coordinates to the robotic arm, using the connected seiral door
# via USB between From PC to Arduino FW (Grbl Mod. Gripper)
# The purpose of this document is to be able to create a library that sends absolute coordinates to the Robot and manages
# the functions of the FW grbl.

import serial
import time

import Linearization
from Linearization import LinearAxisRobot

ReleaseFw = "Grbl 1.1h ['$' for help]"
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

    def Write_Value_Setup(self):
        self.RobotArmSerial.write(b"$0=10")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$1=255")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$2=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$3=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$4=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$5=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$6=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$10=1")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$11=0.010")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$12=0.002")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$13=0.010")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$20=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$21=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$22=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$23=0")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$24=25.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$25=500.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$26=250")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$27=1.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$100=36.790")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$101=36.790")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$102=36.790")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$110=50000.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$111=100000.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$112=100000.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$120=100.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$121=250.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$122=250.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$130=200.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$131=172.000")
        self.RobotArmSerial.write(b'\r\n')
        time.sleep(0.500)
        self.RobotArmSerial.write(b"$132=52.000")
        self.RobotArmSerial.write(b'\r\n')
        self.RobotArmSerial.flushInput()
        RobotArm._softReset()

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
            #PrintHelp = PrintHelp.replace("b'", "")
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
        StringRead = StringRead.replace("|",",", 3)
        StringRead = StringRead.replace("MPos:", "", 1)
        StringRead = StringRead.replace("WCO:", "", 1)
        StringRead = StringRead.replace("Ov:", "", 1)
        StringRead = StringRead.replace("FS:", "", 1)
        StringRead = StringRead.replace("n<", "", 1)
        StatusRobot = StringRead.split(',')
        for i in range(5): #Delete 8 for 5 without tentative
            try:
                StatusRobot[1+i] = float(StatusRobot[1+i])
            except:
                #Condiction Error Try Read Serial
                self.RobotArmSerial.write(b"\r\n")
                self.RobotArmSerial.flushInput()
                self.RobotArmSerial.flushOutput()
                time.sleep(0.150)
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
        StringMove = "G90G01X{X_Target}Y{Y_Target}Z{Z_Target}F{Speed}\n".format(X_Target=X_Target, Y_Target=Y_Target, Z_Target=Z_Target, Speed=Speed)
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
                            print("In Target -- X Axis= " ,RobotArm.StateRobot[1],"mm" ," Y Axis" ,RobotArm.StateRobot[2],"mm" ," Z Axis" ,RobotArm.StateRobot[3],"mm")
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

    def IncrementalPosition(self, X_Target, Y_Target, Z_Target, Speed):
        print("------GoToPosition (Incremental)-------")

        if ((RobotArm.StateRobot[1] == 0) and (RobotArm.StateRobot[2] == 0) and (RobotArm.StateRobot[3] == 0)):
            RobotArm.StatusRobot(self)
            ActualPositionX = RobotArm.StateRobot[1] # XActualPosition
            ActualPositionY = RobotArm.StateRobot[2] # YActualPosition
            ActualPositionZ = RobotArm.StateRobot[3] # ZActualPosition
        else:
            ActualPositionX = RobotArm.StateRobot[1] # XActualPosition
            ActualPositionY = RobotArm.StateRobot[2] # YActualPosition
            ActualPositionZ = RobotArm.StateRobot[3] # ZActualPosition

        print(ActualPositionX,ActualPositionY,ActualPositionZ)
        print(X_Target,Y_Target,Z_Target)

        X_Target = str(X_Target)
        Y_Target = str(Y_Target)
        Z_Target = str(Z_Target)
        print(X_Target, Y_Target, Z_Target)
        Speed = str(Speed)
        StringMove = "G91G01X{X_Target}Y{Y_Target}Z{Z_Target}F{Speed}\n".format(X_Target=X_Target, Y_Target=Y_Target, Z_Target=Z_Target, Speed=Speed)
        print(StringMove)
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
                if ValueXAproximated == round((ActualPositionX+X_Target),1):
                    #print("X in Position")
                    Y_Target = float(Y_Target)
                    Y_Target = round(Y_Target, 1)
                    ValueYAproximated = RobotArm.StateRobot[2]
                    ValueYAproximated = round(ValueYAproximated, 1)
                    if ValueYAproximated == round((ActualPositionY+Y_Target),1):
                        #print("Y in Position")
                        Z_Target = float(Z_Target)
                        Z_Target = round(Z_Target, 1)
                        ValueZAproximated = RobotArm.StateRobot[3]
                        ValueZAproximated = round(ValueZAproximated, 1)
                        if ValueZAproximated == round((ActualPositionZ+Z_Target),1):
                            #print("Z in Position")
                            print("In Target -- X Axis= " ,RobotArm.StateRobot[1],"mm" ," Y Axis" ,RobotArm.StateRobot[2],"mm" ," Z Axis" ,RobotArm.StateRobot[3],"mm")
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

    def LinearGoToPosition(self, X_Target_Linear, Y_TargetLinear, Z_TargetLinear, Speed):
        LinearizedRobot = LinearAxisRobot()
        LinearizedRobot.CalculateGrade(X_Target_Linear,Y_TargetLinear,Z_TargetLinear)
        print("------GoToPosition-------")
        X_Target = str(X_Target_Linear)
        Y_Target = str(Linearization.LinearAxisRobot._lowJoint)
        Z_Target = str(Linearization.LinearAxisRobot._highJoint)
        Speed = str(Speed)
        StringMove = "G90G01X{X_Target}Y{Y_Target}Z{Z_Target}F{Speed}\n".format(X_Target=X_Target, Y_Target=Y_Target, Z_Target=Z_Target, Speed=Speed)
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
                            print("In Target -- X Axis= " ,RobotArm.StateRobot[1],"mm" ," Y Axis" ,RobotArm.StateRobot[2],"mm" ," Z Axis" ,RobotArm.StateRobot[3],"mm")
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
  #  def GoToCArtesianPosition(self, X_Target, Y_Target, Z_Target, Speed):

from RobotArmMove import RobotArm
import time
from Hand_tools import HeadAndTools


# Open GRBL serial port
# Example for Raspberry serial.Serial('/dev/tty.usbmodem1811',115200)
Robot = RobotArm("COM4",115200)
#RobotArmSerial = serial.Serial(port="COM4", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None)

print("Initializing RobotArm")
# Wait for grbl to initialize and flush startup text in serial input
# Wake up grbl

Hand = HeadAndTools("COM5")

Hand.setHead(8,90,160)

Hand.OpenGripper()
Hand.CloseGripper()
Hand.OpenGripper()
Hand.CloseGripper()


#Define Firmata Software
#HendRobot = ArduinoNano('COM5')
print("Communication Hend Robot successfully")


#RobotArmSerial.write(b"\r\n")
Robot._Carriage_Return()
#Robot.Write_Value_Setup()


print(Robot.CheckConnectionRobot()) #Check Connection Function launch

Robot._writevalue("$I")

Robot._softReset()
time.sleep(1)

print(Robot.StatusRobot())#StatusRobot
print(Robot.StateRobot[0])#Robot Status
print(Robot.StateRobot[1])# XPosition
print(Robot.StateRobot[2])# YPosition
print(Robot.StateRobot[3])# ZPosition
print(Robot.StateRobot[4])# Speed Travel


Robot.CheckParameters() #Go Print Check Parameters

Robot.ShowHelpMenu() #Go Print Help Menu

Robot.CheckParametersSetup() # Print Parameters Setup
'''
i=0
while i < 5:
    #RobotArm().GoToPosition(-80,100.1,40.123,1000) #Function GoToPosition
    Robot.GoToPosition(-80, 100.1, 40.123, 50000)
    print("Command GoTOPos End")

    #RobotArm().GoToPosition(0,0,0,10) #Function GoToPosition second move
    Robot.GoToPosition(0,0,0,2000)
    print("Command GoTOPos End")

    #RobotArm().GoToPosition(80,100.1,40.123,1000) #Function GoToPosition
    Robot.GoToPosition(80,100.1,40.123,1500)
    print("Command GoTOPos End")

    Robot.GoToPosition(0,0,0,50000)
    print("Command GoTOPos End")

    Robot.GoToPosition(0, 100.1, 0, 5000)
    print("Command GoTOPos End")

    #RobotArm().GoToPosition(0,0,0,10) #Function GoToPosition second move
    Robot.IncrementalPosition(0,10,10,50000)
    print("Command GoTOPos End")

    Robot.IncrementalPosition(0,-10,-10,1500)
    print("Command GoTOPos End")

    Robot.GoToPosition(0, 0, 0, 5000)
    print("Command GoTOPos End")

    i= i+1

'''
Robot.GoToPosition(0, 60, 0, 50000)
print("Command GoTOPos End")

Robot.GoToPosition(0, 60, -50, 50000)

Robot.GoToPosition(-130, 60, -50, 50000)

Robot.GoToPosition(-130, 150, -50, 50000)

Robot.GoToPosition(-130, 150, -110, 50000)

Robot.GoToPosition(-130, 250, -110, 50000)

time.sleep(3)

Robot.GoToPosition(-130, 100, -110, 50000)

Robot.GoToPosition(-130, 100, -50, 50000)

Robot.GoToPosition(0, 100, -50, 50000)

Robot.GoToPosition(0, 0, 0, 50000)


'''
 Example for blink led 13 Arduino Nano
 while True:
        HendRobot.digital[13].write(1)
        time.sleep(1)
        HendRobot.digital[13].write(0)
        time.sleep(1)
'''
#https://www.youtube.com/watch?v=8j3Fo-16Rr8
'''
HendRobot.digital[8].mode = SERVO
HendRobot.digital[8].write(90)
time.sleep(2)
HendRobot.digital[8].write(10)
'''
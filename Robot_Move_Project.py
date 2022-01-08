from RobotArmMove import RobotArm
import time

# Open GRBL serial port
# Example for Raspberry serial.Serial('/dev/tty.usbmodem1811',115200)
Robot = RobotArm("COM4",115200)
#RobotArmSerial = serial.Serial(port="COM4", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None)

print("Initializing RobotArm")
# Wait for grbl to initialize and flush startup text in serial input
# Wake up grbl

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
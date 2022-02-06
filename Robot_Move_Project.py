from RobotArmMove import RobotArm
import time
from Hand_tools import HeadAndTools

# Open GRBL serial port
Robot = RobotArm("COM4",115200)
print("Initializing RobotArm")

# Wait for grbl to initialize and flush startup text in serial input
# Wake up grbl

# module control Hand
Hand = HeadAndTools("COM5")

Hand.setHead(8,0,90)

Hand.OpenGripper()
#Hand.CloseGripper()
print("Communication Hend Robot successfully")

Robot._Carriage_Return()

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

OffsetYBlock = 30
OfsetZBlock = -10
PositionYForBlockDown = 245
PositionZForBlockDown = -110
NumberBlock = 2-1 # Tolto 1 per posizione bassa
i = 0
while i<2:

    NumberBlock = NumberBlock - i;
    PositionYRobotPick = OffsetYBlock * NumberBlock
    PositionYRobotPick = PositionYForBlockDown - PositionYRobotPick


    # Position Ready
    Robot.GoToPosition(0, 70, 0, 10000)
    Robot.GoToPosition(0, 70, -50, 10000)

    #Move W Axis to Target
    Robot.GoToPosition(-120, 70, -50, 2000)

    Robot.GoToPosition(-120, 150, -50, 50000)

    Robot.GoToPosition(-120, 150, -110, 50000)

    Robot.GoToPosition(-120, PositionYRobotPick, -110, 50000) #Y240 previus Z-110

    time.sleep(2)
    Hand.CloseGripper()

    Robot.GoToPosition(-120, 100, -110, 50000)

    Robot.GoToPosition(-120, 100, -50, 50000)

    Robot.GoToPosition(0, 100, -50, 50000)

    Robot.GoToPosition(0, 0, 0, 50000)

    Hand.OpenGripper()

    i = i+1 #Increment Cycle
from RobotArmMove import RobotArm
import time
from Hand_tools import HeadAndTools
from Camera_Arm import RobotCamera
import threading
import concurrent.futures

# define a coroutine for a task
def task_OpenCamera():
    # Open Camera
    Camera = RobotCamera(0)
    # block for a moment


#Open Camera
#Camera = RobotCamera(0)
def task_RobotMove():
    # Open GRBL serial port
    Robot = RobotArm("COM12",115200)
    print("Initializing RobotArm")

    # Wait for grbl to initialize and flush startup text in serial input
    # Wake up grbl

    # module control Hand
    Hand = HeadAndTools("COM14")

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
    '''
    i=0
    while i < 10:
        Robot.LinearGoToPosition(45,0.01,0.01,10000)
        Robot.LinearGoToPosition(0,0.01,0.01, 10000)
        i = i+1
    
    '''

    i = 0
    while i<5:

        NumberBlock = NumberBlock - i;
        PositionYRobotPick = OffsetYBlock * NumberBlock
        PositionYRobotPick = PositionYForBlockDown - PositionYRobotPick

        Hand.HendLightPWM(3,10)
        # Position Ready
        Robot.GoToPosition(0, 55, 0, 10000)
        Robot.GoToPosition(0, 55, -30, 10000)  #Home Position for cartesian move

        #Move W Axis to Target
        Robot.GoToPosition(60, 55, -30, 50000)  #Rotate to 60°
        Hand.HendLightPWM(3, 50)
        Robot.GoToPosition(60, 134, -94, 50000) # GO to Load Position

        Robot.GoToPosition(60, 134, -85, 50000) #Pick position

        Hand.HendLightPWM(3,100)
        time.sleep(1)
        Hand.CloseGripper()
        Hand.LaserPointer(4,1)

        Robot.GoToPosition(0, 55, -30, 50000) #Up position Ready

        Robot.GoToPosition(0, 134, -85, 50000) # Place position intermedial

        Hand.HendLightPWM(3, 50)
        Hand.OpenGripper()
        time.sleep(2)
        Hand.CloseGripper()   #Pick

        #Robot.GoToPosition(0, 55, -30, 50000) #Up position Ready

        Robot.GoToPosition(-60, 55, -30, 50000)  #Rotate to -60°

        Robot.GoToPosition(-60, 134, -85, 50000)  # Place position

        Hand.OpenGripper()
        time.sleep(2)
        Hand.CloseGripper()   #Pick

        Robot.GoToPosition(60, 55, -30, 50000)  # Up position Ready to place stonage

        Robot.GoToPosition(60, 134, -85, 50000)  # Place position

        Hand.OpenGripper()

        Robot.GoToPosition(60, 134, -94, 50000)  # GO to Load Position

        Robot.GoToPosition(60, 55, -30, 50000)  # Up position Ready

        Robot.GoToPosition(60, 55, -30, 50000)  # Up position Ready to Intermedial

        Robot.GoToPosition(0, 0, 0, 50000)  # Up position Ready to place stonage

        Hand.HendLightPWM(3, 0)
        Hand.OpenGripper()
        Hand.LaserPointer(4,0)

        time.sleep(1)

        i = i+1 #Increment Cycle


if __name__ == "__main__":
    # creating thread
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    # submit tasks to the pool
    pool.submit(task_OpenCamera())
    pool.submit(task_RobotMove())

    pool.shutdown(wait=True)
    print("Done!")
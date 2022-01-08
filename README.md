# RobotArmVision

The Robot Arm Vision library is used to drive a robot composed of a maximum of three axes, which has mounted a camera for image acquisition on its hand.
The images provided in real time will be able to modify the trajectory of the object and identify its entity.

## Structure
The Project will consist of a RobotArmMove.py module which consists in giving commands to the Arduino module with the Grbl 1.1 FW installed.
The coordinates will be sent to the robot that will execute them.

##Command
The Principal Command Move Robot are GoToPosition e IncrementalPosition.
##GoToPosition
The accepted Parameters are absolute Target coordinates on three X Y Z axes and movement speed

##IncrementalPosition
Accepted parameters are coordinates of incremental movements on three axes X Y Z and movement speed


##Setup Command

##CheckConnectionRobot 
Control of connection of the Arduino CNC board

##CheckParameters
Parameter control

##CheckParametersSetup
Check the Setup parameters

##ShowHelpMenu
Help command control

##Write_Value_Setup
Write a value of the set-up commands

##StatusRobot
Know the real-time position of the Robot.

##SoftReset
Soft Reset Fw Grbl


The module has been successfully tested using Python 3.10 e Fw Grbl 1.1



# RobotVisionArm
The Robot Arm Vision library is used to drive a robot composed of a maximum of three axes, which has mounted a camera for image acquisition on its hand.
The images provided in real time will be able to modify the trajectory of the object and identify its entity.

![Alt text](https://github.com/daddi1987/RobotArmVision/blob/8afa9801c1566354e4d44adbaa3822d63b4585e5/Photo/Robot.png?raw=true "**RobotArm With Gripper**")

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/da)
![GitHub all releases](https://img.shields.io/github/downloads/daddi1987/RobotArmVision/total)
![GitHub issues](https://img.shields.io/github/issues/daddi1987/RobotArmVision)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/daddi1987/RobotArmVision?style=plastic)

**Editor.md** : The open source embeddable online markdown editor (component), based on CodeMirror & jQuery & Marked.

## Structure
The Project will consist of a RobotArmMove.py module which consists in giving commands to the Arduino module with the Grbl 1.1 FW installed.
The coordinates will be sent to the robot that will execute them.

### Requirments
The module has been successfully tested using Python 3.10 e Fw Grbl 1.1

### Command:
The Principal Command Move Robot are GoToPosition e IncrementalPosition.

|  COMMAND |  DESCRIPTION |
| ------------ | ------------ |
| **GoToPosition:**  |  The accepted Parameters are absolute Target coordinates on three X Y Z axes and movement speed |
| **IncrementalPosition:**  |  Accepted parameters are coordinates of incremental movements on three axes X Y Z and movement speed |


### **Setup Command:**

|  COMMAND |  DESCRIPTION |
| ------------ | ------------ |
| **CheckConnectionRobot:**  | Control of connection of the Arduino CNC board  |
| **CheckParameters:**  | Parameter control  |
| **CheckParametersSetup:**  |Check the Setup parameters   |
|**ShowHelpMenu:**   |Help command control   |
|  **Write_Value_Setup:** |Write a value of the set-up commands   |
| **StatusRobot:**  |  Know the real-time position of the Robot.|
| **SoftReset:** | Soft Reset Fw Grbl |

### **Vision Camera:**
First tests of turning on the camera and setting the basic settings such as geometries and calculation of instantaneous and average frames.

#### GUI:

![Alt text](https://github.com/daddi1987/RobotArmVision/blob/51de02973a85ea8d1802595c33841541bf9dff50/Photo/Camera%20Tracking.bmp?raw=true "**RobotArmTracking**")

#### Robot Gripper with camera, light and laser

![Alt text](https://github.com/daddi1987/RobotArmVision/blob/51de02973a85ea8d1802595c33841541bf9dff50/Photo/IMG_20230513_194156.jpg?raw=true "**RobotArm With Gripper And Light**")

###### Light and Camera

![Alt text](https://github.com/daddi1987/RobotArmVision/blob/51de02973a85ea8d1802595c33841541bf9dff50/Photo/IMG_20230513_194203.jpg?raw=true "**RobotArm With Gripper And Light**")

######  Laser pointer

![Alt text](https://github.com/daddi1987/RobotArmVision/blob/51de02973a85ea8d1802595c33841541bf9dff50/Photo/IMG_20230513_194222.jpg?raw=true "**RobotArm With Gripper And Light**")
	
	

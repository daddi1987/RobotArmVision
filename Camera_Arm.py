__author__      = "Davide Zuanon"
__copyright__   = "Copyright 2022, Planet Earth"
__maintainer__ = "Davide Zuanon"
__email__ = "davide.zuanon@outlook.it"
__status__ = "Development"

import numpy as np
import cv2 as cv
import time
from DrawingTarget import Drawing_Template


class RobotCamera():

    TimeStartCapture = 0
    TimeEndCapturure = 0
    FrameCamera = 30
    StatusRobot = "READY"



    def __init__(self, IdCamera):         #OpenCamera
        self.CameraRobot = cv.VideoCapture(IdCamera)

        #Frame ForSencond Properties Camera
        fps = self.CameraRobot.get(cv.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

        if not self.CameraRobot.isOpened():
            print("Cannot open camera")
            exit()

    def ShowCamera(self):

        FrameForSecond = 0
        FrameForSecondString = ""
        FpsAvg = []
        ValueFrameAvg = 40
        FtpAvgCalculate = "Undefined"

        while True:
            TimeStartCapture = time.time()
            time.sleep(0.01)  # CLOCK
            # Capture frame-by-frame
            ret, frame = self.CameraRobot.read()

            # Getting the width and height of the feed
            height = int(self.CameraRobot.get(4))
            width = int(self.CameraRobot.get(3))


            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            FrameForSecondString = str(FrameForSecond)

            Drawing_Template.DrawingTarget(self,frame,FrameForSecond,FtpAvgCalculate,width,height,self.StatusRobot)


            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break

            TimeEndCapturure = time.time()
            FrameForSecond = round(1/(TimeEndCapturure - TimeStartCapture),2)
            if len(FpsAvg) < ValueFrameAvg :
                FpsAvg.append(FrameForSecond)
            else:
                FtpAvgCalculate = str(round(sum(FpsAvg) / len(FpsAvg),0))
                FpsAvg.clear()
                FpsAvg.append(FrameForSecond)
            print("Estimated frames per second : {0}".format(FrameForSecond))
            print("Average frames per second : {0}".format(FtpAvgCalculate))

        # When everything done, release the capture
        self.CameraRobot.release()
        cv.destroyAllWindows()

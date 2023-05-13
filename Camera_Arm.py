__author__      = "Davide Zuanon"
__copyright__   = "Copyright 2022, Planet Earth"
__maintainer__ = "Davide Zuanon"
__email__ = "davide.zuanon@outlook.it"
__status__ = "Development"

import numpy as np
import cv2 as cv
import time

class RobotCamera():

    TimeStartCapture = 0
    TimeEndCapturure = 0
    FrameCamera = 30


    def __init__(self, IdCamera):         #OpenCamera
        self.CameraRobot = cv.VideoCapture(IdCamera)

        #Frame ForSencond Properties Camera
        fps = self.CameraRobot.get(cv.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

        if not self.CameraRobot.isOpened():
            print("Cannot open camera")
            exit()
        FrameForSecond = 0
        FrameForSecondString = ""

        while True:
            TimeStartCapture = time.time()
            time.sleep(0.025)
            # Capture frame-by-frame
            ret, frame = self.CameraRobot.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            FrameForSecondString = str(FrameForSecond)
            cv.putText(frame,"fps: : {0}".format(FrameForSecondString),(25, 25),cv.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 255),1,cv.LINE_4)
            # Display the resulting frame

            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                break

            TimeEndCapturure = time.time()
            FrameForSecond = 1/(TimeEndCapturure - TimeStartCapture)
            print("Estimated frames per second : {0}".format(FrameForSecond))


        # When everything done, release the capture
        self.CameraRobot.release()
        cv.destroyAllWindows()
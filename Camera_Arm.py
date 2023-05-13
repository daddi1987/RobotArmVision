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

            # Define ROI Box Dimensions big
            top_left_x = int(width / 3)
            top_left_y = int((height / 2) + (height / 4))
            bottom_right_x = int((width / 3) * 2)
            bottom_right_y = int((height / 2) - (height / 4))

            # Define ROI Box Dimensions small
            stop_left_x = int((width / 2) - 50)
            stop_left_y = int((height / 2) + 50)
            sbottom_right_x = int((width / 2) + 50)
            sbottom_right_y = int((height / 2) - 50)
            #widht 640 height 480
            # if frame is read correctly ret is True

            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            FrameForSecondString = str(FrameForSecond)
            cv.putText(frame,"fps: : {0}".format(FrameForSecondString),(25, 25),cv.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 255),1,cv.LINE_4)
            cv.putText(frame, "fpsAVG: : {0}".format(FtpAvgCalculate), (25, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 255), 1, cv.LINE_4)
            # Display the resulting frame and insert overlayer

            # Drawing cross on the webcam feed
            cv.circle(frame, (int(width/2), int(height/2)), 5, (0, 0, 255), -1) # Point
            cv.rectangle(frame, (stop_left_x, stop_left_y), (sbottom_right_x, sbottom_right_y), (0, 255, 0),1)  # small Rectangle
            cv.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2) # Big Rectangle
            cv.line(frame, (0, int(height/2)), (width, int(height/2)), (0, 0, 255), 1) #Vertical
            cv.line(frame, (int(width/2), 0), (int(width/2), height), (0, 0, 255), 1) #Horizzontal

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

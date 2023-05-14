import cv2 as cv



class Drawing_Template():

    def DrawingTarget(self, frame, FrameForSecondString, FtpAvgCalculate, width, height, StatusRobot):

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
        # widht 640 height 480
        # if frame is read correctly ret is True

        cv.putText(frame, "fps: : {0}".format(FrameForSecondString), (25, 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1,cv.LINE_4)
        cv.putText(frame, "fpsAVG: : {0}".format(FtpAvgCalculate), (25, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1,cv.LINE_4)
        cv.putText(frame, "Status: : {0}".format(StatusRobot),(150, 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 264), 1,cv.LINE_4)
        # Display the resulting frame and insert overlayer

        # Drawing cross on the webcam feed
        cv.circle(frame, (int(width / 2), int(height / 2)), 5, (0, 0, 255), -1)  # Point
        cv.rectangle(frame, (stop_left_x, stop_left_y), (sbottom_right_x, sbottom_right_y), (0, 255, 0), 1)  # small Rectangle
        cv.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)  # Big Rectangle
        cv.line(frame, (0, int(height / 2)), (width, int(height / 2)), (0, 0, 255), 1)  # Vertical
        cv.line(frame, (int(width / 2), 0), (int(width / 2), height), (0, 0, 255), 1)  # Horizzontal
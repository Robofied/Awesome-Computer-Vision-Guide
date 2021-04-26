'''
Output : Capturing a video from a webcam
'''

import cv2
import numpy as np


def main():

    # 0 :- To use internel webcam
    # 1 :- External webcam
    # source file path :- mp4, avi etc
    cap = cv2.VideoCapture('../Images and Videos/nature.mp4')

    # While 1 or While True
    while 1:

        # Take each frame
        ret, frame = cap.read()

        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV (Reference : https://colorpicker.me/)
        lower_blue = np.array([50, 150, 50])
        upper_blue = np.array([180, 255, 255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('hsv', hsv)
        cv2.imshow('res', res)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


main()

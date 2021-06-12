'''
Output : Capturing a video from a webcam, Convert RGB Video frame into HSV, Detect Blue Color from the HSV

OpenCV is a vast library that helps in providing various functions for image and video operations. 
With OpenCV, we can capture a video from the camera. 
It lets you create a video capture object which is helpful to capture videos through webcam and 
then you may perform desired operations on that video.
'''

import cv2
import numpy as np

# Define the codec and create VideoWriter object. The output is stored in 'outpy.avi' file.
# fourcc is a 4-byte code used to specify the video codec.
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 1.video_name 2.FourCC code 3.frame per sec 4.frame size
'''
video_name: Input video file
FourCC code: 4-character code of codec used to compress the frames
fps: framerate of videostream
frame size: Height and width of frame
'''
out1 = cv2.VideoWriter('Original_frame.avi', fourcc, 20.0, (1280, 720))

out2 = cv2.VideoWriter('hsv.avi', fourcc, 20.0, (1280, 720))

out3 = cv2.VideoWriter('res.avi', fourcc, 20.0, (1280, 720))

def main():

    # Use cv2.VideoCapture() to get a video capture object for the camera.
    '''
    If the input is the camera, pass 0 instead of the video file name    
    0 :- To use internel webcam
    1 :- External webcam
    video source file with the extension like :- mp4, avi etc
    '''
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

        out1.write(frame)
        out2.write(hsv)
        out3.write(res)
        cv2.imshow('frame', frame)
        cv2.imshow('hsv', hsv)
        cv2.imshow('res', res)

        # Press 'ESC' on keyboard to exit
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    # When everything done, release the video write objects and video capture object
    out1.release()  # video capture stop
    out2.release()  # video capture stop
    out3.release()  # video capture stop

    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

main()

# Difference between between cv2.waitKey(0) and cv2.waitKey(1)

'''
1.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).

2.waitKey(1) will display a frame for 1 ms, after which display will be automatically closed. Since the OS has a minimum time between switching threads, the function will not wait exactly 1 ms, 
it will wait at least 1 ms, depending on what else is running on your computer at that time.

So, if you use waitKey(0) you see a still image until you actually press something while for waitKey(1) the function will show a frame for at least 1 ms only.
'''

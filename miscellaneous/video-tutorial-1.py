## How to capture video and show it.

## Importing libraries
import cv2
import numpy as np
from platform import python_version

## Checking the version of python
print("Running successfully on python version {0}".format(python_version()))

## Creating a variable cap for videoCapture
cap = cv2.VideoCapture(0)

## This loop just to the frames.
while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    
    ## It will run for and if you will press q then it will stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

print("Its done!")
cap.release()
cv2.destroyAllWindows()



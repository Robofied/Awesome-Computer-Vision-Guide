import cv2
import numpy as np

# Read the frame
frame = cv2.imread('../Images and Videos/opencv-logo.png')
frame_copy = frame.copy()

HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Grayscale
grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Bilateral blur
blur = cv2.bilateralFilter(grayscale, d = 9,sigmaColor=75, sigmaSpace= 75, borderType=cv2.BORDER_CONSTANT)

# Houghcircle 
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

# cv2.imshow('Edges', edged)
cv2.imshow('Original_image',frame_copy )
cv2.imshow('detected circles',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


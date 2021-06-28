import cv2
import numpy as np

# Read the frame
frame = cv2.imread('../Images and Videos/opencv-logo.png')

HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

H,S,V = cv2.split(HSV)
Hue = HSV[:, :, 0]
print(H, S, V)
cv2.imshow('HSV', HSV)
cv2.imshow('Hueea', Hue)
cv2.imshow('Hue', H)
cv2.imshow('Saturation', S)
cv2.imshow('Value', V)

# Grayscale
grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Bilateral blur
blur = cv2.bilateralFilter(grayscale, d = 9,sigmaColor=75, sigmaSpace= 75, borderType=cv2.BORDER_CONSTANT)

# # Canny edge 
# median = np.median(blur)

# ## Based on some statistics
# sigma = 0.33
# lower = int(max(0, (1-sigma)*median))
# upper = int(min(255, (1+sigma)*median))
# edged = cv2.Canny(blur, lower, upper)


circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

# cv2.imshow('Edges', edged)
cv2.imshow('detected circles',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
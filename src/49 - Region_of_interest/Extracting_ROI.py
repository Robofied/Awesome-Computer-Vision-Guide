# Task : Extract Region of interest (ROI), Add ROI to destination image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Images and Videos/messi.jpg')

# For finding the co-ordinates of ball use matplotlib
# Convert BGR To RGB (As OpenCV reads in the form BGR image, so image displayed by matplotlib will
# also in the format of BGR image. To convert BGR to RGB, you need a special method in OpenCV i.e. cvtColor

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.show()


# After we get the region of interest (ROI) of the ball, we merge that into copy of the original image,
# so that are original image wouldn't get modified. 

# Height : 145 to 175
# Width : 170 to 200

img_copy = img.copy()
ball = img[145:175, 170:200]
img[145:175, 40:70] = ball
cv2.imshow('ROI',img)
cv2.waitKey(0)


img1 = cv2.imread('../Images and Videos/car2.jpg')
img2 = cv2.imread('../Images and Videos/logo.png')

print(img1.shape)
print(img2.shape)

# Grayscale
grayscale = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# Thresolding (Binary image)
ret, mask = cv2.threshold(grayscale, 10, 255, cv2.THRESH_BINARY)

# I want to put logo on top-left corner, So I create a ROI
height, width, channel = img2.shape
ROI = img1[0:height, 0:width]

# Inverse Binary
binary_inverse = cv2.bitwise_not(mask)

# Bitwise_and operation
res1 = cv2.bitwise_and(ROI, ROI, mask=binary_inverse)

# Image addition operation
final = cv2.add(img2,res1)

# Put logo in ROI and modify the first image
img1_copy = img1.copy()
img1_copy[0:height,0:width] = final

cv2.imshow('thresh',mask)
cv2.imshow('ROI',ROI)
cv2.imshow('Binary_inverse',binary_inverse)
cv2.imshow('RES1',res1)
cv2.imshow('Final',final)
cv2.imshow('Result',img1_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()

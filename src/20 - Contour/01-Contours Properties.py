'''

Contours are a curve joining all the continous points having same intensity(color).

Performing the find contour, try to convert image into binary.


'''

import cv2
import matplotlib.pyplot as pyplot
import numpy as np

img = cv2.imread('../Images and Videos/gradients3.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Applying gaussian smoothing
blur = cv2.GaussianBlur(imgray, ksize = (5, 5), sigmaX = 0)

## Applying thresholding of binary type.
(t, binary) = cv2.threshold(blur, thresh = 200, maxval = 255, type = cv2.THRESH_BINARY)

## Finding the contours
contours, hierarchy =  cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

## Drawing these contours
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(np.array(contours).shape)

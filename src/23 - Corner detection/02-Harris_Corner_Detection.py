# import package
import cv2
import numpy as np

# Read RGB image
img = cv2.imread('../Images and Videos/Building.jpg')
cv2.imshow('original image',img)

# Grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# As Harris takes input as float32 of grayscale
gray = np.float32(gray)
'''
Its arguments are :

img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
'''
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
harris = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[harris>0.1*harris.max()]=[0,255,0]

cv2.imshow('Harris corner',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
 

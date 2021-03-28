'''
output :

without 0 : The RGB image will get displayed ,
with 0 : The GrayScale image will get displayed
'''

import cv2
import numpy as np

# Read an image
img = cv2.imread('../images and videos/dog.png')

# Convert RGB to Grayscale
gray = cv2.imread('../images and videos/dog.png', 0)

# parameters
#   1. Shape - Height, Width, Color
#   2. dtype - type
print('shape:', img.shape)
print('dtype:', img.dtype)

# Display image
cv2.imshow('BGR_Image', img)
cv2.imshow('Grayscale', gray)

# waitkey for 1 sec
k = cv2.waitKey(0)
# Distroy windows that we have created
cv2.destroyAllWindows()

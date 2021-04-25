'''
Output 
----------------------------------------------
without 0 : The RGB image will get displayed ,
with 0 : The GrayScale image will get displayed
'''

import cv2
import numpy as np
from PIL import Image

# When the image file is read with the OpenCV function imread(),
# the order of colors is BGR (blue, green, red).
# On the other hand, in Pillow, the order of colors is assumed to be RGB (red, green, blue).

# When reading a color image file, OpenCV imread() reads as a NumPy array ndarray of row (height) x column (width) x color (3).
# The order of color is BGR (blue, green, red).
img = cv2.imread('../Images and Videos/dog.png')

'''
parameters
  1. Shape - Height, Width, Color
  2. dtype - type
  3. type  - Numpy ndarray
'''
print('Original Image shape:', img.shape)  # 3 Channel
print('Original Image dtype:', img.dtype)
print('Original Image type:', type(img))

# Display image

# But when displaying the image, it show the image as RGB image instead BGR
cv2.imshow('BGR_Image', img)

# The OpenCV function imwrite() that saves an image assumes that the order of colors is BGR,
# so it is saved as a correct image i.e. RGB image.
cv2.imwrite('Save_Dog.png', img)

# Convert RGB to Grayscale (1 Channel)
gray = cv2.imread('../Images and Videos/dog.png', 0)
print('Grayscale shape:', gray.shape)

# Display image - Grayscale
cv2.imshow('Grayscale', gray)

# Pillow read the image as RGB image
Pillow_Image = Image.open('../Images and Videos/dog.png')
Pillow_Image.show()

# We can not display pillow image using cv.imshow

# To verify, whether the cv2.imread reads the image as BGR, we can use Image.fromarray(img)
# The B,G,R ndarray value get's converted into Image
BGR_Img = Image.fromarray(img)
BGR_Img.show()

# Save image using Pillow
BGR_Img.save('Pillow_BGR.jpg')

# Wait until ESC key is pressed
cv2.waitKey(0)

# Distroy windows that we have created
cv2.destroyAllWindows()

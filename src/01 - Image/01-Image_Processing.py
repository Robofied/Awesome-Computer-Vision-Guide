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
# The function imread loads an image from the specified file and returns it. If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format), the function returns an empty matrix
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

'''
Grayscale images do not include any color. They are given in the range of shades that lie between black and white.
For example, white is represented by 255, 255, 255, black is represented by 0, 0, 0, and medium gray is 127, 127, 127. The higher the number is, the lighter the gray becomes.
"Any shades of black and white" is represented by X, X, X. which means that all channel will have equal itensity. But this will not always be the case.
There is different ways to convert RGB to grayscale, where green channel will have more weight then red and green (something like : Y = 0.2989*Red + 0.5870*Green + 0.1140*Blue )
'''

# Convert RGB to Grayscale (1 Channel) : The 0 flag is cv2.CV_LOAD_IMAGE_GRAYSCALE.
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

# Wait until ESC key is pressed - if you remove the below statement then image will be display and then it will be closed down automatically
# waitKey(0) = tells to wait for infinite time until user presses ESC key
cv2.waitKey(0)

# Distroy windows that we have created
cv2.destroyAllWindows()

# Bitwise operations are used in image manipulation and used for extracting essential parts in the image.

# Reference article : https://www.geeksforgeeks.org/arithmetic-operations-on-images-using-opencv-set-2-bitwise-operations-on-binary-images/
# Bitwise operations used are :
'''
AND: A bitwise AND is true if and only if both pixels are greater than zero.
OR: A bitwise OR is true if either of the two pixels is greater than zero.
XOR: A bitwise XOR is true if and only if one of the two pixels is greater than zero, but not both.
NOT: A bitwise NOT inverts the “on” and “off” pixels in an image.
'''
# Also, Bitwise operations helps in image masking.
# Image creation can be enabled with the help of these operations.
# These operations can be helpful in enhancing the properties of the input images.

# NOTE: The Bitwise operations should be applied on input images of same dimensions

'''
Bitwise AND Operation : cv2.bitwise_and(source1, source2, destination, mask)

First frame is the input1,
second frame is the input2 and
destination : output array that has the same size and type as the input arrays.
the mask is used for applying the function (that does an and operation) only on the marked area.
You can see more in the docs : https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#bitwise-and
'''

import cv2 
import numpy as np 
     
img1 = cv2.imread('../Images and Videos/01_Binary.png') 
img2 = cv2.imread('../Images and Videos/02_Binary.png')
  
Bitwise_AND_Operation = cv2.bitwise_and(img2, img1, mask = None)
  
cv2.imshow('Bitwise And', Bitwise_AND_Operation)

cv2.waitKey(0)

'''
Bitwise OR Operation: cv2.bitwise_or(source1, source2, destination, mask)
'''
Bitwise_OR_Operation = cv2.bitwise_or(img2, img1, mask = None)
  
cv2.imshow('Bitwise OR', Bitwise_OR_Operation)

cv2.waitKey(0)

'''
Bitwise XOR operation : cv2.bitwise_xor(source1, source2, destination, mask)
'''

Bitwise_XOR_Operation = cv2.bitwise_xor(img2, img1, mask = None)
  
cv2.imshow('Bitwise XOR', Bitwise_XOR_Operation)

cv2.waitKey(0)


'''
Bitwise NOT Operation : cv2.bitwise_not(source, destination, mask)
Inversion of input array elements.
'''

Bitwise_NOT_Operation1 = cv2.bitwise_not(img1, mask = None)
  
cv2.imshow('Bitwise NOT on Img1', Bitwise_NOT_Operation1)

Bitwise_NOT_Operation2 = cv2.bitwise_not(img2, mask = None)
  
cv2.imshow('Bitwise NOT on Img2', Bitwise_NOT_Operation2)

cv2.waitKey(0)
cv2.destroyAllWindows()

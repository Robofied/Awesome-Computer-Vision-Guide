import cv2
import numpy as np
import matplotlib.pyplot as plt


# Image Addition

'''
You can add two images with the OpenCV function, cv.add(), or simply by the numpy operation res = img1 + img2.
Both images should be of same depth and type, or the second image can just be a scalar value.

Note: 
        There is a difference between OpenCV addition and Numpy addition.
        OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

Example:

We are using uint8 because we are using image which is of 8 bit ( 0 to 255 ) format.
>>> x = np.uint8([250])
>>> y = np.uint8([10])

>>> print( cv.add(x,y) )  # 250+10 = 260 => 255
    [[255]]

>>> print( x+y )          # 250+10 = 260 % 256 = 4
    [4]
'''

img1 = cv2.imread('../Images and Videos/flower_images/F5.jpg')
img2 = cv2.imread('../Images and Videos/flower_images/F6.jpg')

# Image addition using : Add Method 
'''
Syntex : cv.add(src1, src2[, dst[, mask[, dtype]]]) -> dst

Read more about add method from here : https://docs.opencv.org/master/d2/de8/group__core__array.html#ga10ac1bfb180e2cfda1701d06c24fdbd6
'''
print(img1.shape)
print(img2.shape)

# Size of both image should be similar, so resize the img2 to make it size similar to img1

image_addition = cv2.add(img1, img2)
cv2.imshow('Image_addition',image_addition)
cv2.waitKey(0)

# Image Blending : Using add weighted method

'''
Calculates the weighted sum of two arrays.

This is also image addition, but different weights are given to images in order to give a feeling of blending or transparency.

Images are added as per the equation below:

            g(x) = (1−α)*f0(x) + α*f1(x)

By varying α from 0→1, you can perform a cool transition between one image to another.

Here I took two images to blend together. The first image is given a weight of 0.7 and the second image is given 0.3. cv.addWeighted() applies the following equation to the image:

            dst = α*img1 + β*img2 + γ

dst = src1*alpha + src2*beta + gamma;
Here γ is taken as zero.
'''

blending = cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('Image_Blending',blending)
cv2.waitKey(0)
cv2.destroyAllWindows()

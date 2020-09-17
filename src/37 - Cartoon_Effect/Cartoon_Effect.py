#import package

import cv2
import numpy as np

# read image
img = cv2.imread('../Images and Videos/img.jpeg')

# image shape
h,w,c = img.shape
print(f'Image shape : ({h},{w})')

# resize the image
img_resize = cv2.resize(img, (600,600))

# Dataloader
num_bilateral = 7          # number of bilateral filtering steps 

cv2.imshow('original',img)
cv2.imshow('resized_img',img_resize)
# apply small bilateral filter instead of applying one large filter
'''
Arguments of bilateral filter
1. d: Diameter of each pixel neighborhood
2. sigmaColor :  filter sigma in the color space
3. sigmaSpace :  filter sigma in the coordinate space.
'''

for i in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_resize,d=9,
                                        sigmaColor=9,
                                        sigmaSpace=7)

cv2.imshow('Bilateral_Image',img_color)

img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY,
                                   blockSize=9,
                                   C=2)

# single channel (Grayscale)
cv2.imshow('img_edge_before_rgb',img_edge)
print(img_edge.shape)

# 3 channel (RGB)
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
print(img_edge.shape)

cv2.imshow('img_edge_after_rgb',img_edge)
img_cartoon = cv2.bitwise_and(img_color, img_edge)
output = np.hstack([img_resize,img_cartoon])

cv2.imshow('output',output)

# save the image
cv2.imwrite('output.jpg',output)

cv2.waitKey(0)
cv2.destroyAllWindows()








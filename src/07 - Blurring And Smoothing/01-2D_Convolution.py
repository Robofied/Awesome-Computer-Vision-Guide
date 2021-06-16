'''
output : 2D Convolution ( Image Filtering )

Syntax : cv2.filter2D(	src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]]	) ->	dst

Parameters
src	    input image.
dst	    output image of the same size and the same number of channels as src.
ddepth	desired depth of the destination image, see combinations
kernel	convolution kernel (or rather a correlation kernel), a single-channel floating point matrix; if you want to apply different kernels to different channels, split the image into separate color planes using split and process them individually.
anchor	anchor of the kernel that indicates the relative position of a filtered point within the kernel; the anchor should lie within the kernel; default value (-1,-1) means that the anchor is at the kernel center.
delta	optional value added to the filtered pixels before storing them in dst. 
        Note : when ddepth=-1, the output image will have the same depth as the source.

borderType	pixel extrapolation method, see BorderTypes. BORDER_WRAP is not supported.

Reference : https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04

'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('../Images and videos/flower_2.jpg')

'''
2D Convolution ( Image Filtering )
'''

## Creating the kernel for smoothening
kernel = np.ones((5,5), np.float32)/25

## Applying 2D convolution 

# borderType=cv2.BORDER_CONSTANT ( with constant value '0') as a padding 
smooth = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_CONSTANT)

## Plotting the images
images = [img,smooth]
titles = ['Original', '2D Convolution Filter']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],)
    plt.title(titles[i]) 
    plt.axis('off')
plt.show()

'''
Custom kernel operation 
'''

image = cv2.imread('../Images and Videos/logo.png')

kernel = np.ones((3,3),np.float32) * (-1)
kernel[1,1] = 8
print(kernel)
dst = cv2.filter2D(image,-1,kernel)

plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Custom kernel Operation')
plt.xticks([]), plt.yticks([])
plt.show()

'''
We can even apply gaussian filter using 2D Convolution.
just we need to change the kernel. 
'''

image = cv2.imread('../Images and Videos/logo.png')

kernel = np.array([
                    [1/16, 1/8, 1/16],
                    [1/8, 1/4, 1/8],
                    [1/16, 1/8, 1/16]
                  ])

dst = cv2.filter2D(image,-1,kernel)

plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Gaussian filter using 2D Convolution')
plt.xticks([]), plt.yticks([])
plt.show()

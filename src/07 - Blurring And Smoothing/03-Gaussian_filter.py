'''
output : Gaussian Blurring (Image Smoothing)

Syntax :  cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) ->dst

Parameters : 
src	    input image; the image can have any number of channels, which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst	    output image of the same size and type as src.
ksize	Gaussian kernel size. ksize.width and ksize.height can differ but they both must be positive and odd. Or, they can be zero's and then they are computed from sigma.
sigmaX	Gaussian kernel standard deviation in X direction.
sigmaY	Gaussian kernel standard deviation in Y direction; if sigmaY is zero, it is set to be equal to sigmaX, if both sigmas are zeros, they are computed from ksize.width and ksize.height, respectively (see getGaussianKernel for details); to fully control the result regardless of possible future modifications of all this semantics, it is recommended to specify all of ksize, sigmaX, and sigmaY.
borderType	pixel extrapolation method, see BorderTypes. BORDER_WRAP is not supported.

Reference : https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

"""
We’ll see in the code below, when the size of our kernel increases so will the amount of blurring that is applied to our output image. 
However, the blurring will appear to be more “natural” and will preserve edges in our image better than simple average smoothing:
"""

img = cv2.imread('../Images and videos/Gaussian-noise.jpg')

gaussian_3x3 = cv2.GaussianBlur(img, (3,3), sigmaX=0, sigmaY=0)
gaussian_5x5 = cv2.GaussianBlur(img, (5,5), sigmaX=0, sigmaY=0)
gaussian_7x7 = cv2.GaussianBlur(img, (7,7), sigmaX=0, sigmaY=0)
gaussian_9x9 = cv2.GaussianBlur(img, (9,9), sigmaX=0, sigmaY=0)
gaussian_11x11 = cv2.GaussianBlur(img, (11,11), sigmaX=0, sigmaY=0)
images = [img, gaussian_3x3, gaussian_5x5, gaussian_7x7, gaussian_9x9, gaussian_11x11]
titles = ['Original', 'Gaussian Smoothening - 3x3','Gaussian Smoothening - 5x5','Gaussian Smoothening - 7x7','Gaussian Smoothening - 9x9','Gaussian Smoothening - 11x11']

for i in range(0,6):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()


# Callback Function which helps to get the position of trackbar 
def nothing(x):
    pass

# 1.trackbar name  2.window name 3.minimum value 4.maximum value 5.callback function
cv2.namedWindow('trackbars')
cv2.createTrackbar('sigmaX','trackbars',0,50,nothing)  
cv2.createTrackbar('sigmaY','trackbars',0,50,nothing) 
cv2.createTrackbar('ksize','trackbars',0,30,nothing) 


while True: 
    
    # Read the image
    image = cv2.imread('../Images and videos/flower_images/F10.jpg')

    # Get the trackbar position
    sigmaX = cv2.getTrackbarPos('sigmaX','trackbars')
    sigmaY = cv2.getTrackbarPos('sigmaY','trackbars')
    ksize = cv2.getTrackbarPos('ksize','trackbars')

    odd_ksize = [i for i in range(60) if i%2!=0]
    filtered = cv2.GaussianBlur(image,ksize = (odd_ksize[ksize],odd_ksize[ksize]), sigmaX=sigmaX,sigmaY=sigmaY,borderType=cv2.BORDER_CONSTANT)

    cv2.imshow('frame',image)
    cv2.imshow('Gaussian',filtered)

    # Press the 'ESC' to exit
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

cv2.destroyAllWindows()
            


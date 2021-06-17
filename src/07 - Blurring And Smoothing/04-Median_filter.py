'''
output : Median Blurring (Image Smoothing)

Syntax : cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) ->dst

Blurs an image using the median filter.
The function smoothes an image using the median filter with the ksize×ksize aperture. Each channel of a multi-channel image is processed independently. In-place operation is supported.

Parameters : 

src	input 1-, 3-, or 4-channel image; when ksize is 3 or 5, the image depth should be CV_8U, CV_16U, or CV_32F, for larger aperture sizes, it can only be CV_8U.
dst	destination array of the same size and type as src.
ksize	aperture linear size; it must be odd and greater than 1, for example: 3, 5, 7 ...

Reference : https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

# Read image in the form of BGR
image = cv2.imread('../Images and videos/balloons_noisy.png')

# To display image in the form of RGB in plt.show, we have to convert that into RGB format using cv2.cvtColor function
RGB_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# The median filter uses BORDER_REPLICATE internally to cope with border pixels, see BorderTypes : https://docs.opencv.org/master/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5
median = cv2.medianBlur(RGB_image, ksize = 5)

images = [RGB_image,median]
titles = ['Original', 'Median Smoothening']


for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
    
plt.show()


# Callback Function which helps to get the position of trackbar 
def nothing(x):
    pass

# 1.trackbar name  2.window name 3.minimum value 4.maximum value 5.callback function
cv2.namedWindow('trackbars')
cv2.createTrackbar('ksize','trackbars',0,30,nothing) 
cv2.resizeWindow('trackbars',700,50)

while True: 

    # Read image
    image = cv2.imread('../Images and videos/noisy_image.png')

    # Get trackbar position
    ksize = cv2.getTrackbarPos('ksize','trackbars')

    # Odd number list
    odd_ksize = [i for i in range(60) if i%2!=0]

    filtered = cv2.medianBlur(image, ksize=odd_ksize[ksize])

    cv2.imshow('Frame',image)
    cv2.imshow('Median_filter',filtered)

    # Press the 'ESC' to exit
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

cv2.destroyAllWindows()
            
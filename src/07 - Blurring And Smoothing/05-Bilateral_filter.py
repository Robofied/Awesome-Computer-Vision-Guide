'''
output : Median Blurring (Image Smoothing)

Syntax : cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) ->dst

Applies the bilateral filter to an image.

The function applies bilateral filtering to the input image, as described in http://www.dai.ed.ac.uk/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html 
bilateralFilter can reduce unwanted noise very well while keeping edges fairly sharp. However, it is very slow compared to most filters.

Parameters : 

src	Source 8-bit or floating-point, 1-channel or 3-channel image.
dst	Destination image of the same size and type as src .
d	Diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace.
sigmaColor	Filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting in larger areas of semi-equal color.
sigmaSpace	Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is proportional to sigmaSpace.
borderType	border mode used to extrapolate pixels outside of the image, see BorderTypes

Reference : https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread('../Images and videos/carpet.jpg')

bilateral_filter = cv2.bilateralFilter(image, d = 9,sigmaColor=75, sigmaSpace= 75, borderType=cv2.BORDER_CONSTANT)

images = [image,bilateral_filter]
titles = ['Original', 'Bilateral Filtering']

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
cv2.createTrackbar('Diameter','trackbars',0,50,nothing)  
cv2.createTrackbar('sigmaColor','trackbars',0,200,nothing) 
cv2.createTrackbar('sigmaSpace','trackbars',1,200,nothing) 


while True: 
    
    # Read the image
    image = cv2.imread('../Images and Videos/baby.jpg')
    cv2.imshow('image',image)

    # Get the trackbar position
    Diameter = cv2.getTrackbarPos('Diameter','trackbars')
    sigmaColor = cv2.getTrackbarPos('sigmaColor','trackbars')
    sigmaSpace = cv2.getTrackbarPos('sigmaSpace','trackbars')

    odd_ksize = [i for i in range(60) if i%2!=0]
    filtered = cv2.bilateralFilter(image, d = Diameter, sigmaColor = sigmaColor, sigmaSpace = sigmaSpace, borderType=cv2.BORDER_CONSTANT)

    cv2.imshow('frame',image)
    cv2.imshow('Bilateral',filtered)

    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

cv2.destroyAllWindows()
            

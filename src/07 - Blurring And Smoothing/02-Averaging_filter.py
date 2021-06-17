'''
output : Averaging (Image Smoothing)
         1. Blur
         2. Boxfilter

Syntax :  1. Blur 
            cv2.blur(src, ksize[, dst[, anchor[, borderType]]]) -> dst
          2. BoxFilter
            cv2.boxFilter(src, ddepth, ksize[, dst[, anchor[, normalize[, borderType]]]]) ->dst

Parameters : 

src	    input image; it can have any number of channels, which are processed independently, but the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
dst	    output image of the same size and type as src.
ksize	blurring kernel size.
anchor	anchor point; default value Point(-1,-1) means that the anchor is at the kernel center.
ddepth	the output image depth (-1 to use src.depth()).
        Note : when ddepth=-1, the output image will have the same depth as the source.

borderType	border mode used to extrapolate pixels outside of the image, see BorderTypes. BORDER_WRAP is not supported.

Reference : https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37

'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt


'''
Performing average smoothening, Same as 
'''
img = cv2.imread('../Images and videos/flower_2.jpg')

avg_smooth_3x3 = cv2.blur(img, (3,3))   
avg_smooth_5x5 = cv2.blur(img, (5,5))   
avg_smooth_7x7 = cv2.blur(img, (7,7))   
avg_smooth_9x9 = cv2.blur(img, (9,9))   
avg_smooth_11x11 = cv2.blur(img, (11,11))   

images = [img,avg_smooth_3x3,avg_smooth_5x5,avg_smooth_7x7,avg_smooth_9x9,avg_smooth_11x11]
titles = ['Original image', 'Average Smoothening - 3x3','Average Smoothening - 5x5','Average Smoothening - 7x7','Average Smoothening - 9x9','Average Smoothening - 11x11']

for i in range(0,6):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()

'''
Performing average smoothening, Same as 
'''
avg_smooth_3x3 =  cv2.boxFilter(img, ddepth=-1, ksize=(3,3), normalize=True)   
avg_smooth_5x5 =  cv2.boxFilter(img, ddepth=-1, ksize=(5,5), normalize=True)   
avg_smooth_7x7 =  cv2.boxFilter(img, ddepth=-1, ksize=(7,7), normalize=True)   
avg_smooth_9x9 =  cv2.boxFilter(img, ddepth=-1, ksize=(9,9), normalize=True)   
avg_smooth_11x11 =  cv2.boxFilter(img, ddepth=-1, ksize=(11,11), normalize=True)   

images = [img,avg_smooth_3x3,avg_smooth_5x5,avg_smooth_7x7,avg_smooth_9x9,avg_smooth_11x11]
titles = ['Original image', 'Box filtering - 3x3','Box filtering - 5x5','Box filtering - 7x7','Box filtering - 9x9','Box filtering - 11x11']

for i in range(0,6):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()


# Callback Function which helps to get the position of trackbar 
def nothing(x):
    pass

# 1.trackbar name  2.window name 3.minimum value 4.maximum value 5.callback function
cv2.namedWindow('trackbars',cv2.WINDOW_NORMAL)
cv2.resizeWindow('trackbars',700,100)
cv2.createTrackbar('ksize','trackbars',1,30,nothing) 


while True: 

    # Read image
    image = cv2.imread('../Images and videos/flower_images/F9.jpg')

    # Get trackbar position
    ksize = cv2.getTrackbarPos('ksize','trackbars')

    # Odd number list
    odd_ksize = [i for i in range(60) if i%2!=0]

    filtered = cv2.blur(image, (odd_ksize[ksize],odd_ksize[ksize]), borderType=cv2.BORDER_CONSTANT) 

    cv2.imshow('Frame',image)
    cv2.imshow('Gaussian',filtered)

    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break 

cv2.destroyAllWindows()
            
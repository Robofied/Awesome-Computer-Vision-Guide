'''
output : Press the 'q' to see the effect of different type of smoothing operation 
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('../Images and videos/opencv-logo.png')

## Creating the kernel for smoothening
kernel = np.ones((5,5), np.float32)/25

## Applying 2D convolution
smooth = cv2.filter2D(img, -1, kernel)

## Plotting the images
images = [img,smooth]
titles = ['Original', 'Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i]) 

plt.show()

'''
Performing average smoothening, Same as 
'''
avg_smooth = cv2.blur(img, (5,5))

images = [img,avg_smooth]
titles = ['Original', ' Average Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

gaussian = cv2.GaussianBlur(img, (5,5), 0)

images = [img,gaussian]
titles = ['Original', 'Gaussian Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

img2 = cv2.imread('../Images and videos/noisy4.jfif')

median = cv2.medianBlur(img2, 5)

images = [img2,median]
titles = ['Original', 'Median Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])
    
plt.show()

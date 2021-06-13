'''
output : Press the 'q' to see the effect of different type of smoothing operation 
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
smooth = cv2.filter2D(img, -1, kernel)

## Plotting the images
images = [img,smooth]
titles = ['Original', 'Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],)
    plt.xlabel(titles[i]) 

plt.show()

'''
Custom kernel operation 
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

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
Performing average smoothening, Same as 
'''
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
    plt.xlabel(titles[i])

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
    plt.xlabel(titles[i])

plt.show()

img2 = cv2.imread('../Images and videos/Gaussian-noise.jpg')

gaussian_3x3 = cv2.GaussianBlur(img2, (3,3), sigmaX=0, sigmaY=0)
gaussian_5x5 = cv2.GaussianBlur(img2, (5,5), sigmaX=0, sigmaY=0)
gaussian_7x7 = cv2.GaussianBlur(img2, (7,7), sigmaX=0, sigmaY=0)
gaussian_9x9 = cv2.GaussianBlur(img2, (9,9), sigmaX=0, sigmaY=0)
gaussian_11x11 = cv2.GaussianBlur(img2, (11,11), sigmaX=0, sigmaY=0)
images = [img2, gaussian_3x3, gaussian_5x5, gaussian_7x7, gaussian_9x9, gaussian_11x11]
titles = ['Original', 'Gaussian Smoothening - 3x3','Gaussian Smoothening - 5x5','Gaussian Smoothening - 7x7','Gaussian Smoothening - 9x9','Gaussian Smoothening - 11x11']

for i in range(0,6):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

img3 = cv2.imread('../Images and videos/balloons_noisy.png')

median = cv2.medianBlur(img3, 5)

images = [img3,median]
titles = ['Original', 'Median Smoothening']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i])
    plt.xlabel(titles[i])
    
plt.show()


img4 = cv2.imread('../Images and videos/carpet.jpg')

bilateral_filter = cv2.bilateralFilter(img4,9,75,75)


images = [img4,bilateral_filter]
titles = ['Original', 'Bilateral Filtering']

for i in range(0,2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i])
    plt.xlabel(titles[i])
    
plt.show()

'''
Morphological operations are broad set of operations in image processing

Erosion - erodes boundaries of foreground object. Decrease the white region and increasing black region, enlarge the whole. 
Application - removing white noises and detach joint objects 

Dilation - opposite of erosion, increasing while region and decresing black region , fill the whole
Application- joining breaking parts

Opening - errosion followed by dilation

Closing - dilation followed by erosion

There are some operations available in C++ for image processing. 
You can refer at - https://in.mathworks.com/help/images/morphological-dilation-and-erosion.html
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('../Images and videos/morph1.png')

kernel = np.ones((5,5), np.uint8)

# Erosion
erosion = cv2.erode(img,kernel,iterations = 1)

images = [img, erosion]
titles = ['Original', 'Erosion']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

# Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)

images = [img, dilation]
titles = ['Original', 'dilation']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

# Opening (Erosion followed by dilation) : Performing opening operation to remove small objects from image
remove_small_objects = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

images = [img, remove_small_objects]
titles = ['Original', 'Small objects removal (Opening)']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

# Closing (Dilation followed by erosion) : Small hole removal using closing operation
modify_objects = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

images = [img, modify_objects]
titles = ['Original', 'Filling small holes (Closing)']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

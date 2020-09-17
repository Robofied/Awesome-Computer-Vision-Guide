'''
Morphological operations are broad set of operations in 
image processing

Erosion - erodes boundaries of foreground object.
Application - removing white noises and detach joint objects 

Dilation - opposite of erosion, generally erosion followed by dilation
Application- joining breaking parts

Opening - errosion followed by dilation

Closing - dilation followed by erosion

There are some operations available in C++ for image processing. 
You can refer at - https://in.mathworks.com/help/images/morphological-dilation-and-erosion.html
'''

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('./images/morph1.png')

kernel = np.ones((5,5), np.uint8)
## Performing opening operation to remove small objects from image
remove_small_objects = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

images = [img, remove_small_objects]
titles = ['Original', 'Small objects removal']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

## Small hole removal using closing operation

img = cv2.imread('./images/morph2.png')
modify_objects = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

images = [img, modify_objects]
titles = ['Original', 'Filling small holes']

for i in range(2):
    plt.subplot(2,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

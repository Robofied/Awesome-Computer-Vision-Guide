'''
output : Press the escape button to see the effect of adaptive thresolding
'''

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../Images and Videos/image8.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(img,5)

cv2.imshow('blurred',img)
cv2.waitKey(0)

## Performing simple thresholding
## Performing adaptive mean and gaussian thresholding
ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(img, 255,\
     cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)
thresh3 = cv2.adaptiveThreshold(img, 255,\
     cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2) 

images = [thresh1, thresh2, thresh3]
titles = ['Binary', 'Adaptive mean', 'Adaptive Gaussian']

for i in range(3):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


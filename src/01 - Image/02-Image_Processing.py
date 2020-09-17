'''
output : Output image can be resize
         named window can be use to resize the window
         imwrite to save the image
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils


img = cv2.imread('dog.png',cv2.IMREAD_UNCHANGED)

'''
Change the resolution of image

width = int(img.shape[1] * 50/ 100)
height = int(img.shape[0] * 50/ 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation =cv2.INTER_AREA) 
'''

cv2.namedWindow('image' , cv2.WINDOW_NORMAL)  #use to resize the window
cv2.imshow('image',img)

k = cv2.waitKey(0) & 0xFF

if k == 27:                         # wait for ESC key to exit
    cv2.destroyAllWindows() 
elif k == ord('a'):
    cv2.imwrite('img_copy.jpg', img)     # wait for 'a' key to save and exit 
    cv2.destroyAllWindows()

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

print(flags)

##plt.imshow(img, cmap = 'gray', interpolation = ' bicubic')
##plt.xticks([]), plt.yticks([])
##plt.show()

  

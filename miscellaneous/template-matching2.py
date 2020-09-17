'''
Template matching for multiple objects, will not occur using minMaxLoc()

In this will use concept of thresholding on the resultant array from template_match function.

'''

import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/mario.jpg',0 )
template = cv2.imread('images/mario_coin1.png', 0)

w, h = template.shape[::-1]

print(img.shape)
print(template.shape)

res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
thresh =0.1

print(res)

loc = np.where( res >= thresh)

print(loc)
print(loc[::-1])
#print(zip(*loc))

for pt in zip(*loc[::-1]):
    #print(pt)
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('res', img)
cv2.waitKey(0)
#cv2.imwrite('res.png',img_rgb)
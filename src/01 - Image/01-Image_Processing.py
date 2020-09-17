'''
output :

without 0 : The RGB image will get displayed ,
with 0 : The GrayScale image will get displayed
'''

import cv2
import numpy as np
img = cv2.imread('../images and videos/dog.png',0)
while True:
    cv2.imshow('hritik',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
   

'''
output : Resize on interative set of images and also affine transformation  
'''
import cv2
import numpy as np

images = ['DL-1.png','DL-2.jpg', 'DL-3.jpg']

for im in images:

    img = cv2.imread('../Images and Videos/'+str(im))

    height, width = img.shape[:2]

    print(height, width)

    res = cv2.resize(img, (300,300), interpolation= cv2.INTER_CUBIC)

    cv2.imshow('original', img)
    cv2.waitKey(0)

    cv2.imshow('resized',res)
    cv2.waitKey(0)

img = cv2.imread('../Images and Videos/image8.jpg')

height, width = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])

trs = cv2.warpAffine(img, M, (width+100,height+50) )

M = np.float32([[1,0,-50],[0,1,-25]])

trs1 = cv2.warpAffine(trs, M, (width+100+50,height+50+25) )

cv2.imshow('translated',trs1)
cv2.waitKey(0)

img = cv2.imread('../Images and Videos/image8.jpg')

height, width, ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1, pts2)

trs = cv2.warpAffine(img, M, (width, height))

cv2.imshow('Original',img)

cv2.imshow('Affine Transform',trs)
cv2.waitKey(0)
cv2.destroyAllWindows()

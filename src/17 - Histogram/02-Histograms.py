import cv2
import numpy as np 
import matplotlib.pyplot as plt 

np.seterr(divide='ignore', invalid='ignore')

img = cv2.imread('../Images and Videos/messi.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0 , 256])


print(hist)
print(hist.shape)

plt.imshow(hist, interpolation='nearest')
plt.show()

## histogram backprojection

roi = cv2.imread('../Images and Videos/roi.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


target = cv2.imread('../Images and Videos/target.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

M = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256] )
I = cv2.calcHist([hsvt], [0,1], None, [180, 256], [0, 180, 0, 256])

plt.imshow(M, interpolation='nearest')
plt.show()
plt.imshow(I, interpolation='nearest')
plt.show()

R = M/I

h,s,v = cv2.split(hsvt)

B = R[h.ravel(), s.ravel()]

B = np.minimum(B,1)
B = B.reshape(hsvt.shape[:2])

cv2.imshow('trial', B)
cv2.waitKey(0)

## Applying convolution to get output in a desired format
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(B,-1,disc,B)
B = np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

## thresholding to find part of our interest
ret,thresh = cv2.threshold(B,50,255,0)

## merge for converting threshold image into colored channel image(3 channels)
thresh = cv2.merge((thresh,thresh,thresh))

## Bitwise and for finding the intersecting part between target and threshold image, as threshol will be white where we want object and black where we doesn't
res = cv2.bitwise_and(target, thresh)

print(thresh.shape)
print(target.shape)

cv2.imshow('final',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../Images and Videos/gradients3.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)

## Finding the contours
contours, hierarchy =  cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

## Finding centroid of first contour only
cnt = contours[0]

## moment of that contour
M = cv2.moments(cnt)
print(M)

## Calculating centroids coordinates
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(cx, cy)

## Let's use these calculated centroid values to get some new image out of original

cv2.imshow('Original', img)

## Calculating new coordinates for new image 
## Trying to extract the middle portion of it.
x_axis = cx/2
y_axis = cy/2

start_x = int(cx/2)
end_x = int(start_x + cx)

start_y = int(cy/2)
end_y = int(start_y + cy)

## Coordinates for new image
print("Starting coordinates and ending coordinates are ",start_x, start_y, end_x, end_y)

## Cropping new image from original image
new_img = img[start_y:end_y, start_x:end_x]


cv2.imshow('new',new_img)
cv2.waitKey(0)

## Here we are trying to extract the middle sudoko box but due to uneveness of full image, we are not able to detect the correct box, let's see how to change orientation in order to ger better results.

img = cv2.imread('../Images and Videos/gradients3.png')
rows,cols,ch = img.shape

## Performing warp perspective transformation.
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[210,0],[0,210],[210,210]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

imgray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(imgray,127,255,0)

## Finding the contours
contours, hierarchy =  cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(dst, contours, -1, (0,255,0), 3)

## Finding centroid of first contour only
cnt = contours[0]

## moment of that contour
M = cv2.moments(cnt)
print(M)

## Calculating centroids coordinates
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print(cx, cy)

## Let's use these calculated centroid values to get some new image out of original

cv2.imshow('Original', dst)

## Calculating new coordinates for new image 
## Trying to extract the middle portion of it.
x_axis = cx/2
y_axis = cy/2

start_x = int(cx/2)
end_x = int(start_x + cx)

start_y = int(cy/2)
end_y = int(start_y + cy)

## Coordinates for new image
print("Starting coordinates and ending coordinates are ",start_x, start_y, end_x, end_y)

## Cropping new image from original image
new_img = dst[start_y:end_y, start_x:end_x]


cv2.imshow('new',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

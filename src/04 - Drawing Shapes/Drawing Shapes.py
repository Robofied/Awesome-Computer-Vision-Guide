'''
Here will see how to use shapes features of opencv to be use
in different application.
'''

import cv2


img = cv2.imread('images/image8.jpg')
cv2.imshow('hello', img)
cv2.waitKey(0)

## Using lines drawing a simple 3-sided boundary
cv2.line(img, (0,0), (265,0),(255,0,0), 5 )
cv2.line(img, (265,0), (265, 265), (255,0,0), 5)
cv2.line(img, (0,185), (265,185), (255,0,0), 5)

## Displaying the modified image
cv2.imshow('line',img)
cv2.waitKey(0)

##How to draw rectangle around an image
cv2.rectangle(img, (0,0), (265,185), (0,255,0), 3)
cv2.imshow('rectangle', img)
cv2.waitKey(0)

## Putting some text in image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'House', (130,160) ,font, 1, (255,0,0), 2, cv2.LINE_AA )
cv2.imshow('text', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

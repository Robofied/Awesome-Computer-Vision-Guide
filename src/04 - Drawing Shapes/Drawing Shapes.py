'''
Here will see how to use shapes features of opencv to be use
in different application.
'''

import cv2
import numpy as np

# First we try one sample image -

# The grey level or grey value indicates the brightness of a pixel. The minimum grey level is 0.
# The maximum grey level depends on the digitisation depth of the image. For an 8-bit-deep image it is 255.
# '0' gray value indicates - black image 
black_img = np.zeros((512,512,3), np.uint8)

'''
Drawing a line : cv2.line(src, line_point1, line_point2, color, thickness)  
src : It is the image on which line is to be drawn.
rect_point1 :- Start coordinate, here (0, 0) represents the top left corner of line
rect_point2 :- Ending coordinate, here (512, 512)  represents the bottom right corner of line
color: It is the color of line to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
thickness: It is the thickness of the line in px. 
Return Value: It returns an image.
'''
cv2.line(black_img, (0,0),(black_img.shape[0],black_img.shape[1]),(0,255,0),2)
cv2.imshow('Drawing_line', black_img)
cv2.waitKey(0)


'''
Drawing a rectangle : cv2.rectangle(src, rect_point1, rect_point2, color, thickness)  
src : It is the image on which rectangle is to be drawn.
rect_point1 :- Start coordinate, here (350, 100) represents the top left corner of rectangle
rect_point2 :- Ending coordinate, here (450, 200)  represents the bottom right corner of rectangle
color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.
Return Value: It returns an image.
'''
cv2.rectangle(black_img, (350,100),(450,200),(0,255,0),2)
cv2.imshow('Drawing_rect', black_img)
cv2.waitKey(0)

cv2.rectangle(black_img, (350,100),(450,200),(255,0,0),cv2.FILLED)
cv2.imshow('Drawing_rect_filled', black_img)
cv2.waitKey(0)

'''
Drawing a circle : cv2.circle(src, center_point, radius, color, thickness)  
'''
cv2.circle(black_img, (300,400),50,(0,255,255),2, cv2.FILLED)
cv2.imshow('Drawing_circle', black_img)
cv2.waitKey(0)


'''
Drawing a ellipse : cv2.circle(src, center_coordinates, axesLength, startAngle, endAngle, color, thickness)  
'''

# (X coordinate value, Y coordinate value).
center_coordinates = (120, 400)

# (major axis length, minor axis length) = (a,b)
axesLength = (100, 50)

# Ellipse rotation angle in degrees.
angle = 0

# Starting angle of the elliptic arc in degrees. 
startAngle = 0

# Ending angle of the elliptic arc in degrees.  
endAngle = 360
   
# Red color in BGR
color = (0, 0, 255)
   
# Line thickness of 5 px - thickness of the shape border line in px.
thickness = 5
   
# Using cv2.ellipse() method
# Draw a ellipse with red line borders of thickness of 5 px
cv2.ellipse(black_img, center_coordinates, axesLength,
           angle, startAngle, endAngle, color, thickness)
cv2.imshow('Drawing_ellipse', black_img)
cv2.waitKey(0)

'''
Drawing a polygon : cv2.polylines(src,  array of coordinates, True (if it is a closed line), Stroke color, Stroke thickness)  
'''
pts = np.array([[60,15],[80,60],[120,60],[100,15]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(black_img,[pts],True,(255,255,255), 2)
cv2.imshow('Drawing_window', black_img)
cv2.waitKey(0)


## Now we will look for actually images
img = cv2.imread('../Images and videos/image8.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)

## Using lines drawing a simple 3-sided boundary
## cv2.line(src, line_point1, line_point1, color, thickness)  
cv2.line(img, (0,0), (265,0),(255,0,0), 5 )
cv2.line(img, (265,0), (265, 265), (255,0,0), 5)
cv2.line(img, (0,185), (265,185), (255,0,0), 5)

## Displaying the modified image
cv2.imshow('line',img)
cv2.waitKey(0)

## How to draw rectangle around an image
cv2.rectangle(img, (0,0), (265,185), (0,255,0), 3)
cv2.imshow('rectangle', img)
cv2.waitKey(0)

## Putting some text in image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'House', (130,160) ,font, 1, (255,0,0), 2, cv2.LINE_AA )
cv2.imshow('text', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

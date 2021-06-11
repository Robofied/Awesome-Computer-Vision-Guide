'''
Task : Extraction of features from skin lesion in dermoscopic images (Geometric
& colour)
Here we apply masking on skin lesion image using two ways i.e
1. using thresolding
2. using inbuilt masking operation i.e inRange function
we can use either of this to get the desired output
'''
# import package
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):   # callback function which is executed everytime trackbar value changes.
    
    pass

# trackbars
cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2.window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3.default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4.maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5.callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)

# Adjust the trackbar to get the desired output
# lowh = 0, highh = 180
# lows = 77, highs = 232
# lowv = 0 , highv = 168

# set trackbar
cv2.setTrackbarPos('lowh','trackbars',0)
cv2.setTrackbarPos('highh','trackbars',180)
cv2.setTrackbarPos('lows','trackbars',77)
cv2.setTrackbarPos('highs','trackbars',232)
cv2.setTrackbarPos('lowv','trackbars',0)
cv2.setTrackbarPos('highv','trackbars',168)

# Read image
image = cv2.imread('../Images and videos/skin_lesions.jpg')

# Grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Smoothing (blurring)
median_blur = cv2.medianBlur(gray,5)

# Otsu thresolding
ret3, thresh = cv2.threshold(median_blur, 127,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# inverse
thresh2 = cv2.bitwise_not(thresh)

# Bitwise-AND mask and original image
res1 = cv2.bitwise_and(image , image, mask = thresh2)

# find contour
contours,hierarchy = cv2.findContours(thresh2, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)

#PERIMETER
perimeter = cv2.arcLength(cnt,True)

#CENTROID
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#CONTOUR APPROXIMATION
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
approx=np.array(approx)

#CONVEX HULL
hull = cv2.convexHull(cnt)
hull=np.array(hull)

#CONVEXITY CHECK
k = cv2.isContourConvex(cnt)

#STRAIGHT BOUNDING RECTANGLE
x,y,w,h = cv2.boundingRect(cnt)
#img_rect = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
contour,hierarchy =cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in contour:
    area= cv2.contourArea(i)
    if area>500:
        x,y,w,h = cv2.boundingRect(i)
        img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(image,"Skin lesion detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

#PRINTING EVERYTHING
print("Centroid of lesion is: x = ",cx," ;y = ",cy)
print("Area of lesion is ",M['m00'])
print("Perimeter of lesion is ",perimeter)
print("Contour Approximation: ",approx)
print("Convex Hull: ",hull)
print("Is Lesion convex? ",k)
print(M)

# Display image
cv2.imshow('image',image)
cv2.imshow('grayscale',gray)
cv2.imshow('median',median_blur)
cv2.imshow('thresh',thresh)
cv2.imshow('inverse_thresh',thresh2)
cv2.imshow('Output using thresolding method',res1)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Smoothing (blurring)
median_blur_hsv = cv2.medianBlur(hsv,5)

while True:
    # Masking
    lowh = cv2.getTrackbarPos('lowh','trackbars')
    lows = cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')

    # define range of orange skin lesion color in HSV (Change the value for another color using trackbar)
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(median_blur_hsv, lower_red, upper_red)
        
    # Bitwise-AND mask and original image 
    res = cv2.bitwise_and(image , image, mask = mask)

    # Display image
    cv2.imshow('mask',mask)
    cv2.imshow('output using inbuilt masking method',res)

    k = cv2.waitKey(4) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
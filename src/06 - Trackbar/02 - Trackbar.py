'''
Output: Change the value in track bar to see the effect in the input image
Try range : [lowh,lows,lowv] = [0, 0, 0]
            [highh,highs,highv] = [180,255,53]
'''

import cv2
import numpy as np

# Callback Function which helps to get the position of trackbar 
def nothing(x):
    pass

cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1. trackbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2. window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. minimum value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4. maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)


while True :

    # Read frame    
    image = cv2.imread('pexel.jpeg')

    # Change resolution
    image = cv2.resize(image, (400,400))

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    # Get trackbar position    
    lowh = cv2.getTrackbarPos('lowh','trackbars')
    lows = cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')


    # Try range : 
    '''
    [lowh,lows,lowv] = [0, 0, 0]
    [highh,highs,highv] = [180,255,53]
    '''

    # Get Range of HSV Color
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])
    
    # Perform maksing
    mask = cv2.inRange(hsv, lower_red , upper_red)

    cv2.imshow('frame',image)
    cv2.imshow('mask',mask)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break 

# cap.release()
cv2.destroyAllWindows()
            

            

            
            
        

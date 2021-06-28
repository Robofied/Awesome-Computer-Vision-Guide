import cv2
import numpy as np


# Callback Function which helps to get the position of trackbar 
def nothing(x):
    pass

cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars', 1000, 600)
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1. trackbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2. window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. minimum value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4. maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)
cv2.createTrackbar('highv','trackbars',0,255,nothing)
cv2.createTrackbar('blocksize','trackbars',0,30,nothing)
cv2.createTrackbar('constant','trackbars',0,50,nothing)
cv2.createTrackbar('area_size','trackbars',0,1000,nothing)
cv2.createTrackbar('radius','trackbars',0,1000,nothing)
cv2.createTrackbar('m','trackbars',0,100,nothing)

cv2.setTrackbarPos('lowh','trackbars',0)
cv2.setTrackbarPos('highh','trackbars',180)
cv2.setTrackbarPos('lows','trackbars',0)
cv2.setTrackbarPos('highs','trackbars',255)
cv2.setTrackbarPos('lowv','trackbars',55)
cv2.setTrackbarPos('highv','trackbars',94)
cv2.setTrackbarPos('blocksize','trackbars',5)
cv2.setTrackbarPos('constant','trackbars',4)
cv2.setTrackbarPos('area_size','trackbars',500)
cv2.setTrackbarPos('radius','trackbars',50)
cv2.setTrackbarPos('m','trackbars',10)

while True:
    # Read image
    frame = cv2.imread('../Images and Videos/pipe.jpg')

    # BGR to Grayscale 
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # BGR to HSV
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar position    
    lowh = cv2.getTrackbarPos('lowh','trackbars')
    lows = cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')
    k = cv2.getTrackbarPos('blocksize','trackbars')
    c = cv2.getTrackbarPos('constant','trackbars')
    area_size = cv2.getTrackbarPos('area_size','trackbars')
    radius = cv2.getTrackbarPos('radius','trackbars')
    m = cv2.getTrackbarPos('m','trackbars')
    # Try range : 
    '''
    [lowh,lows,lowv] = [0, 0, 55]
    [highh,highs,highv] = [180,255,94]
    '''

    # Get Range of HSV Color
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])
    
    # Perform maksing
    mask = cv2.inRange(HSV, lower_red , upper_red)

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(grayscale,(5,5),0)

    # Adaptive thresolding - Binary 
    odd_ksize = [i for i in range(60) if i%2!=0]
    adative_thresold = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,odd_ksize[k],c)    
    adaptive_inverse = cv2.bitwise_not(adative_thresold)

    # #img_rect = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    contour,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    count = 1
    for i in contour:
        area = cv2.contourArea(i)
        if area>area_size:
            x,y,w,h = cv2.boundingRect(i)
            img = cv2.circle(frame, (x-m,y-m),radius,(0,255,0),3)
            # img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(frame,f"{count}",(x-m,y-m),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
            count+=1

    # circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,20,
    #                         param1=50,param2=30,minRadius=0,maxRadius=0)
    # circles = np.uint16(np.around(circles))
    # for i in circles[0,:]:
    #     # draw the outer circle
    #     cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    #     # draw the center of the circle
    #     cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('adaptive',adative_thresold)
    cv2.imshow('adaptive_inverse',adaptive_inverse)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break 

# cap.release()
cv2.destroyAllWindows()



import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('trackbars')
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2 .window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4 .maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)

cv2.namedWindow('cor')
cv2.createTrackbar('alpha', 'cor', 0,100, nothing)
cv2.createTrackbar('beta', 'cor', 0, 100, nothing)
cv2.setTrackbarPos('alpha', 'cor', 80)
cv2.setTrackbarPos('beta', 'cor', 100)

def mouse_event(event,x, y, flags, para):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        pixel = hsv[y,x]
        cv2.setTrackbarPos('lowh','trackbars',pixel[0] - 10)
        cv2.setTrackbarPos('highh','trackbars',pixel[0] + 10)
        cv2.setTrackbarPos('lows','trackbars',pixel[1] - 10)
        cv2.setTrackbarPos('highs','trackbars',pixel[1] + 20)
        cv2.setTrackbarPos('lowv','trackbars',pixel[2] - 20)
        cv2.setTrackbarPos('highv','trackbars',pixel[2] + 20)

for i in range(10):
    ret,back = cap.read()

while True:

    # Read frame
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # AddWeighted parameters
    alpha = cv2.getTrackbarPos('alpha','cor')
    beta = cv2.getTrackbarPos('beta','cor')

    # Define range of red color in HSV (Change the value for another color)
    lowh = cv2.getTrackbarPos('lowh','trackbars')
    lows = cv2.getTrackbarPos('lows','trackbars') 
    lowv = cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')

    cv2.setMouseCallback('frame',mouse_event)

    # 160,141,0
    # 180,255,255
    # Lower part of hue contain red color from range 0 to 10
    lower_red = np.array([0,100,100])
    upper_red = np.array([15,255,255])

    # Threshold the HSV image to get only red colors 
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Upper part of Hue also contain red color from range 160 to 180
    lower_red = np.array([160,100,100])
    upper_red = np.array([180,255,255])

    # Threshold the HSV image to get only red colors
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Mask 
    mask = mask1 + mask2

    # kernel 
    kernel = np.ones((5,5),np.uint8)

    # Opening
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Dilute
    dilute = cv2.dilate(opening, kernel, iterations = 2)

    # Mask inverse to get the background ( Blackout the cloak part, white the background )
    mask_inverse = cv2.bitwise_not(mask)
    
    # Bitwise-AND mask and original image
    res1 = cv2.bitwise_and(back,back,mask=dilute)
    res2 = cv2.bitwise_and(frame, frame, mask = mask_inverse)

    # Alpha 
    alpha = alpha / 100 if alpha > 0 else 0.01
    beta = beta / 100 if beta > 0 else 0.01
    img = cv2.addWeighted(res1, alpha, res2, beta, 0)
    
    cv2.imshow('frame',frame)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('opening',opening)
    cv2.imshow('dilation',dilute)
    cv2.imshow('mask_inverse',mask_inverse)

    cv2.imshow('res1',res1)
    cv2.imshow('res2',res2)
    cv2.imshow('final',img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

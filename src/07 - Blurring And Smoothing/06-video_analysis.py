import cv2
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):   # callback function which is executed everytime trackbar value changes.
    
    pass

# Add cv2.CAP_DSHOW := when you are getting following warning 
# CV2: “[ WARN:0] terminating async callback” when attempting to take a picture
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# trackbars
cv2.namedWindow('trackbars',cv2.WINDOW_NORMAL)
cv2.createTrackbar('lowh','trackbars',0,180,nothing)  # 1.tracbar name
cv2.createTrackbar('highh','trackbars',0,180,nothing) # 2 .window name
cv2.createTrackbar('lows','trackbars',0,255,nothing)  # 3. default value
cv2.createTrackbar('highs','trackbars',0,255,nothing) # 4 .maximum value
cv2.createTrackbar('lowv','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('highv','trackbars',0,255,nothing)


while True :

    # take each frame
    _, image = cap.read()

    # Get trackabr position 
    lowh  =  cv2.getTrackbarPos('lowh','trackbars')
    lows  =  cv2.getTrackbarPos('lows','trackbars') 
    lowv  =  cv2.getTrackbarPos('lowv','trackbars')
    highh = cv2.getTrackbarPos('highh','trackbars')
    highs = cv2.getTrackbarPos('highs','trackbars')
    highv = cv2.getTrackbarPos('highv','trackbars')

    # Smoothed image using bilateral filter
    smoothed_image = cv2.bilateralFilter(image, d = 9,sigmaColor=75, sigmaSpace= 75, borderType=cv2.BORDER_CONSTANT)

    # Convert Smoothed_image to HSV
    hsv = cv2.cvtColor(smoothed_image,cv2.COLOR_BGR2HSV)

    '''    
    lowh,lows,lowv=48,0,0
    highh,highs,highv=125,255,255

    0, 30, 0, 255, 49, 255
    '''

    # define range of red color in HSV
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])

    # Threshold the HSV image to any color as per your choice
    mask = cv2.inRange(hsv, lower_red , upper_red)

    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(image ,image , mask = mask)

    cv2.imshow('frame',image)
    cv2.imshow('smoothed_image',smoothed_image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(1) & 0xFF    # basically just pressing ESC button then cond will true then it will be break 
    if k == 27:                  # cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds.here it will wait for any key to be pressed then 100ms it will destroy 
        break

cap.release()             # When everything done, release the capture          
cv2.destroyAllWindows()   # use to destroy all windows which you were created
                          # cv2.destroyWindow() where you pass the exact window name as the argument.

    
 #  cv2.namedWindow('Window_name', cv2.WINDOW_NORMAL) : use to resize the window which u are created
 #  cv2.imwrite()   : to save an image.

# Import package
import cv2
import math
import numpy as np
import matplotlib as plt

FilePath = '../Images and Videos/theroad.mp4'
cap = cv2.VideoCapture(FilePath)
w = cap.get(3)
h = cap.get(4)

def callback(x):
    pass


cv2.namedWindow('cor')
cv2.resizeWindow('cor', 700, 1000)

cv2.createTrackbar('lowh', 'cor', 0, 180, callback)
cv2.createTrackbar('highh', 'cor', 0, 180, callback)
cv2.createTrackbar('lows', 'cor', 0, 255, callback)
cv2.createTrackbar('highs', 'cor', 0, 255, callback)
cv2.createTrackbar('lowv', 'cor', 0, 255, callback)
cv2.createTrackbar('highv', 'cor', 0, 255, callback)

cv2.setTrackbarPos('lowh', 'cor',0)
cv2.setTrackbarPos('lows', 'cor', 0)
cv2.setTrackbarPos('lowv', 'cor', 130)
cv2.setTrackbarPos('highh', 'cor', 255)
cv2.setTrackbarPos('highs', 'cor', 255)
cv2.setTrackbarPos('highv', 'cor', 255)


cv2.createTrackbar('minline', 'cor', 0, 500, callback)
cv2.createTrackbar('maxgap', 'cor', 0, 500, callback)

cv2.setTrackbarPos('minline', 'cor', 10)
cv2.setTrackbarPos('maxgap', 'cor', 20)

cv2.createTrackbar('rad', 'cor', 0, 1800, callback)
cv2.createTrackbar('rad2', 'cor', 0, 1800, callback)
cv2.createTrackbar('width', 'cor', 0, 1800, callback)

cv2.setTrackbarPos('rad', 'cor',958)
cv2.setTrackbarPos('rad2', 'cor', 477)
cv2.setTrackbarPos('width', 'cor', 520)

cv2.createTrackbar('centerX', 'cor', 0, 1500, callback)
cv2.createTrackbar('centerY', 'cor', 0, 1500, callback)
cv2.setTrackbarPos('centerX', 'cor', 640)
cv2.setTrackbarPos('centerY', 'cor', 640)

cv2.createTrackbar('alpha', 'cor', 0,100, callback)
cv2.createTrackbar('beta', 'cor', 0, 100, callback)
cv2.setTrackbarPos('alpha', 'cor', 80)
cv2.setTrackbarPos('beta', 'cor', 100)

cv2.namedWindow('Perspective_transform')
cv2.resizeWindow('Perspective_transform', 700, 1000)

# 1280 -> width and 720 -> Height
cv2.createTrackbar('src_x1', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('src_y1', 'Perspective_transform', 0, 720, callback)
cv2.createTrackbar('src_x2', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('src_y2', 'Perspective_transform', 0, 720, callback)
cv2.createTrackbar('src_x3', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('src_y3', 'Perspective_transform', 0, 720, callback)
cv2.createTrackbar('src_x4', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('src_y4', 'Perspective_transform', 0, 720, callback)

cv2.createTrackbar('dist_x1', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('dist_y1', 'Perspective_transform', 0, 720, callback)
cv2.createTrackbar('dist_x2', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('dist_y2', 'Perspective_transform', 0, 720, callback)
cv2.createTrackbar('dist_x3', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('dist_y3', 'Perspective_transform', 0, 720, callback)
cv2.createTrackbar('dist_x4', 'Perspective_transform', 0, 1280, callback)
cv2.createTrackbar('dist_y4', 'Perspective_transform', 0, 720, callback)

cv2.setTrackbarPos('src_x1', 'Perspective_transform', 523)
cv2.setTrackbarPos('src_y1', 'Perspective_transform', 453)
cv2.setTrackbarPos('src_x2', 'Perspective_transform', 811)
cv2.setTrackbarPos('src_y2', 'Perspective_transform', 440)
cv2.setTrackbarPos('src_x3', 'Perspective_transform', 405)
cv2.setTrackbarPos('src_y3', 'Perspective_transform', 639)
cv2.setTrackbarPos('src_x4', 'Perspective_transform', 1261)
cv2.setTrackbarPos('src_y4', 'Perspective_transform', 671)

cv2.setTrackbarPos('dist_x1', 'Perspective_transform', 160)
cv2.setTrackbarPos('dist_y1', 'Perspective_transform', 93)
cv2.setTrackbarPos('dist_x2', 'Perspective_transform', 1200)
cv2.setTrackbarPos('dist_y2', 'Perspective_transform', 0)
cv2.setTrackbarPos('dist_x3', 'Perspective_transform', 200)
cv2.setTrackbarPos('dist_y3', 'Perspective_transform', 710)
cv2.setTrackbarPos('dist_x4', 'Perspective_transform', 1200)
cv2.setTrackbarPos('dist_y4', 'Perspective_transform', 710)


def automatic_canny(images, sigma=0.33):
    median = np.median(images)

    ## Based on some statistics
    lower = int(max(0, (1-sigma)*median))
    upper = int(min(255, (1+sigma)*median))
    edge = cv2.Canny(images, lower, upper,3)
    return edge

def perspectiveWarp(inpImage):

    # Get image size
    img_size = (inpImage.shape[1], inpImage.shape[0])
    src_x1 = cv2.getTrackbarPos('src_x1','Perspective_transform')
    src_y1 = cv2.getTrackbarPos('src_y1','Perspective_transform') 
    src_x2 = cv2.getTrackbarPos('src_x2','Perspective_transform')
    src_y2 = cv2.getTrackbarPos('src_y2','Perspective_transform')
    src_x3 = cv2.getTrackbarPos('src_x3','Perspective_transform')
    src_y3 = cv2.getTrackbarPos('src_y3','Perspective_transform')
    src_x4 = cv2.getTrackbarPos('src_x4','Perspective_transform')
    src_y4 = cv2.getTrackbarPos('src_y4','Perspective_transform')

    dist_x1 = cv2.getTrackbarPos('dist_x1','Perspective_transform')
    dist_y1 = cv2.getTrackbarPos('dist_y1','Perspective_transform') 
    dist_x2 = cv2.getTrackbarPos('dist_x2','Perspective_transform')
    dist_y2 = cv2.getTrackbarPos('dist_y2','Perspective_transform')
    dist_x3 = cv2.getTrackbarPos('dist_x3','Perspective_transform')
    dist_y3 = cv2.getTrackbarPos('dist_y3','Perspective_transform')
    dist_x4 = cv2.getTrackbarPos('dist_x4','Perspective_transform')
    dist_y4 = cv2.getTrackbarPos('dist_y4','Perspective_transform')
    
    # Perspective points to be warped
    src = np.float32([[src_x1,src_y1],
                      [src_x2, src_y2],
                      [src_x3, src_y3],
                      [src_x4, src_y4]])

    # Window to be shown
    dst = np.float32([[dist_x1,dist_y1],
                      [dist_x2,dist_y2],
                      [dist_x3,dist_y3],
                      [dist_x4,dist_y4]])

    # Matrix to warp the image for birdseye window
    matrix = cv2.getPerspectiveTransform(src, dst)
    # Inverse matrix to unwarp the image for final window
    minv = cv2.getPerspectiveTransform(dst, src)
    birdseye = cv2.warpPerspective(inpImage, matrix, img_size)

    # Get the birdseye window dimensions
    height, width = birdseye.shape[:2]

    # Divide the birdseye view into 2 halves to separate left & right lanes
    birdseyeLeft  = birdseye[0:height, 0:width // 2]
    birdseyeRight = birdseye[0:height, width // 2:width]

    return birdseye, birdseyeLeft, birdseyeRight, minv

while True:
    _, img = cap.read()
    
    # Masking
    lowh = cv2.getTrackbarPos('lowh','cor')
    lows = cv2.getTrackbarPos('lows','cor') 
    lowv = cv2.getTrackbarPos('lowv','cor')
    highh = cv2.getTrackbarPos('highh','cor')
    highs = cv2.getTrackbarPos('highs','cor')
    highv = cv2.getTrackbarPos('highv','cor')

    # For ellipse (center cordinates)
    centerX = cv2.getTrackbarPos('centerX','cor')
    centerY = cv2.getTrackbarPos('centerY','cor')

    # addWeighted parameters
    alpha = cv2.getTrackbarPos('alpha','cor')
    beta = cv2.getTrackbarPos('beta','cor')

    # Hide corner using ellipse
    rad = cv2.getTrackbarPos('rad', 'cor')
    rad2 = cv2.getTrackbarPos('rad2', 'cor')
    width = cv2.getTrackbarPos('width', 'cor')
    
    # define range of white color in HSV (Change the value for another color using trackbar)
    lower_red = np.array([lowh,lows,lowv])
    upper_red = np.array([highh,highs,highv])

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',hsv)
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow('mask',mask)

    # Make ellipse to hide (black out) upper region and only focus on the road part
    cv2.ellipse(mask, (640,640), (rad, rad2), 0, 0, 360, (0, 0, 0), width)   


    # Bitwise-AND mask and original image 
    res = cv2.bitwise_and(img , img, mask = mask)    
    cv2.imshow('res',res)

    # Grayscale
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)

    # Gaussian Blur (Remove noise)
    gray_blur = cv2.GaussianBlur(gray,(3, 3), 0)
    
    # Canny edge
    edges = automatic_canny(gray_blur)
    cv2.imshow('Canny edge', edges)
    
    # Thresolding (Binary image)
    ret, thresh = cv2.threshold(edges,125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('thresold',thresh)

    # Define kernel size
    kernel = np.ones((10,10), np.uint8)

    # Apply closing
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)    
    cv2.imshow('closing', closing)

    # Data loader for hough transform
    rho = 1
    theta = np.pi/180
    threshold = 50
    
    min_line_len = cv2.getTrackbarPos('minline', 'cor')
    max_line_gap = cv2.getTrackbarPos('maxgap', 'cor')

    lines = cv2.HoughLinesP(closing, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((closing.shape[0], closing.shape[1], 3), dtype=np.uint8)
    if lines is not None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(line_img, (x1, y1), (x2, y2), [0,0,255],3)
                
        # Merge the image with the lines onto the original.
        # img = img * α + line_img * β + γ
        # NOTE: img and line_img must be the same shape!
        alpha = alpha / 100 if alpha > 0 else 0.01
        beta = beta / 100 if beta > 0 else 0.01
        img = cv2.addWeighted(img, alpha, line_img, beta, 0.0)

    birdView, birdViewL, birdViewR, minverse = perspectiveWarp(img)
    cv2.imshow('birdView',birdView)
    cv2.imshow('birdViewL',birdViewL)
    cv2.imshow('birdViewR',birdViewR)

    cv2.imshow('line_img',line_img)
    '''
    # Apply contour to get the bounding box on the lane        
    contours, hierarchy=cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        area = cv2.contourArea(i)
        if(area>10000):
            x,y,w,h = cv2.boundingRect(i)
            
            rect = cv2.minAreaRect(i)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            
            #cv2.drawContours(img,[box],0,(255,0,0),4)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)
            cv2.putText(img,"Lane detected",(x,y),cv2.FONT_HERSHEY_SIMPLEX,4, (0,255,0),cv2.LINE_AA)
    '''
    cv2.imshow('Output', img)        
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

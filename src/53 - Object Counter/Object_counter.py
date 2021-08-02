import cv2
import numpy as np


# Callback Function which helps to get the position of trackbar
def nothing(x):
    pass


cv2.namedWindow('trackbars')
cv2.resizeWindow('trackbars', 1100, 800)
cv2.createTrackbar('lowh', 'trackbars', 0, 180, nothing)  # 1. trackbar name
cv2.createTrackbar('highh', 'trackbars', 0, 180, nothing)  # 2. window name
cv2.createTrackbar('lows', 'trackbars', 0, 255, nothing)  # 3. minimum value
cv2.createTrackbar('highs', 'trackbars', 0, 255, nothing)  # 4. maximum value
cv2.createTrackbar('lowv', 'trackbars', 0, 255,
                   nothing)  # 5. callback function
cv2.createTrackbar('highv', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('highv', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('blocksize', 'trackbars', 0, 30, nothing)
cv2.createTrackbar('constant', 'trackbars', 0, 50, nothing)
cv2.createTrackbar('area_size', 'trackbars', 0, 1000, nothing)
cv2.createTrackbar('radius', 'trackbars', 0, 1000, nothing)
cv2.createTrackbar('m', 'trackbars', 0, 100, nothing)
cv2.createTrackbar('dp', 'trackbars', 0, 100, nothing)
cv2.createTrackbar('minDist', 'trackbars', 0, 100, nothing)
cv2.createTrackbar('param1', 'trackbars', 0, 100, nothing)
cv2.createTrackbar('param2', 'trackbars', 0, 100, nothing)
cv2.createTrackbar('minRadius', 'trackbars', 0, 100, nothing)
cv2.createTrackbar('maxRadius', 'trackbars', 0, 100, nothing)


cv2.setTrackbarPos('lowh', 'trackbars', 0)
cv2.setTrackbarPos('highh', 'trackbars', 180)
cv2.setTrackbarPos('lows', 'trackbars', 0)
cv2.setTrackbarPos('highs', 'trackbars', 255)
cv2.setTrackbarPos('lowv', 'trackbars', 55)
cv2.setTrackbarPos('highv', 'trackbars', 94)
cv2.setTrackbarPos('blocksize', 'trackbars', 5)
cv2.setTrackbarPos('constant', 'trackbars', 4)
cv2.setTrackbarPos('area_size', 'trackbars', 500)
cv2.setTrackbarPos('radius', 'trackbars', 50)
cv2.setTrackbarPos('m', 'trackbars', 10)
cv2.setTrackbarPos('dp', 'trackbars', 12)
cv2.setTrackbarPos('minDist', 'trackbars', 40)
cv2.setTrackbarPos('param1', 'trackbars', 75)
cv2.setTrackbarPos('param2', 'trackbars', 30)
cv2.setTrackbarPos('minRadius', 'trackbars', 0)
cv2.setTrackbarPos('maxRadius', 'trackbars', 20)

while True:

    # Read image
    frame = cv2.imread('../Images and Videos/pipe_2.jpg')
    w, h, c = frame.shape

    # Copy of image
    frame_copy = frame.copy()

    # BGR to Grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # BGR to HSV
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar position
    lowh = cv2.getTrackbarPos('lowh', 'trackbars')
    lows = cv2.getTrackbarPos('lows', 'trackbars')
    lowv = cv2.getTrackbarPos('lowv', 'trackbars')
    highh = cv2.getTrackbarPos('highh', 'trackbars')
    highs = cv2.getTrackbarPos('highs', 'trackbars')
    highv = cv2.getTrackbarPos('highv', 'trackbars')
    k = cv2.getTrackbarPos('blocksize', 'trackbars')
    c = cv2.getTrackbarPos('constant', 'trackbars')
    area_size = cv2.getTrackbarPos('area_size', 'trackbars')
    radius = cv2.getTrackbarPos('radius', 'trackbars')
    m = cv2.getTrackbarPos('m', 'trackbars')
    dp = cv2.getTrackbarPos('dp', 'trackbars')
    minDist = cv2.getTrackbarPos('minDist', 'trackbars')
    param1 = cv2.getTrackbarPos('param1', 'trackbars')
    param2 = cv2.getTrackbarPos('param2', 'trackbars')
    minRadius = cv2.getTrackbarPos('minRadius', 'trackbars')
    maxRadius = cv2.getTrackbarPos('maxRadius', 'trackbars')

    # Try range :
    '''
    [lowh,lows,lowv] = [0, 0, 55]
    [highh,highs,highv] = [180,255,94]
    '''

    # Get Range of HSV Color
    lower_red = np.array([lowh, lows, lowv])
    upper_red = np.array([highh, highs, highv])

    # Perform maksing
    mask = cv2.inRange(HSV, lower_red, upper_red)

    # Otsu's thresholding after Gaussian filtering
    blur = cv2.bilateralFilter(
        grayscale, d=9, sigmaColor=75, sigmaSpace=75, borderType=cv2.BORDER_CONSTANT)

    # Adaptive thresolding - Binary
    odd_ksize = [i for i in range(60) if i % 2 != 0]
    adative_thresold = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, odd_ksize[k], c)
    adaptive_inverse = cv2.bitwise_not(adative_thresold)

    dp_array = np.arange(0, 100, 0.1)
    dp_array = np.around(dp_array, 1)

    # Houghcircle method
    circles = cv2.HoughCircles(blur, method=cv2.HOUGH_GRADIENT, dp=dp_array[dp], minDist=minDist, param1=param1,
                               param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    circles = np.uint16(np.around(circles))[0, :]

    # Sort the circle with y axis
    circles = sorted(circles, key=lambda x: x[1])

    circles.append([0, h, 0])

    # Dataloader
    # thresold parameter may depend on the input image
    thr = 10
    index = 0
    aux = circles[0][1]

    sorted_circle = []
    count = 0

    if circles is not None:

        for i in range(len(circles)):
            if circles[i][1] - aux > thr:
                sorted_circle.extend(
                    sorted(circles[index:i], key=lambda c: c[0]))
                aux = circles[i][1]
                index = i

        for i in sorted_circle:

            # draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)

            # draw the center of the circle
            count += 1
            cv2.putText(
                frame, f"{count}", (i[0]-m, i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('frame', frame_copy)
    cv2.imshow('frame', frame)

    # Press the ESC to exit
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

# Import package
import cv2
import numpy as np


# callback function which is executed everytime trackbar value changes.
def nothing(x):
    pass


# trackbars
cv2.namedWindow('trackbars')
cv2.createTrackbar('minVal', 'trackbars', 0, 500, nothing)  # 1.tracbar name
cv2.createTrackbar('maxVal', 'trackbars', 0, 1000, nothing)  # 2.window name

# Set trackbar
cv2.setTrackbarPos('minVal', 'trackbars', 0)
cv2.setTrackbarPos('maxVal', 'trackbars', 300)

# Read image
image = cv2.imread('../Images and Videos/Document_01.jpg')
print("Width : {} and height : {}".format(image.shape[1], image.shape[0]))
cv2.imshow('original image', image)

# Resize the image
resized_image = cv2.resize(image, (900, 700))
heightImg, widthImg, channel = resized_image.shape


def automatic_canny(images, sigma=0.33):
    median = np.median(images)

    # Based on some statistics
    lower = int(max(0, (1-sigma)*median))
    upper = int(min(255, (1+sigma)*median))
    edge = cv2.Canny(images, lower, upper)
    return edge


def getBiggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 5000:
            perimeter = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02*perimeter, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area


def getOrderOfLabel(points):

    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), dtype=np.int32)
    add = points.sum(1)

    new_points[0] = points[np.argmin(add)]
    new_points[3] = points[np.argmax(add)]

    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]

    return new_points


def drawRectangle(img, biggest, thickness):
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]),
             (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]),
             (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]),
             (biggest[2][0][0], biggest[2][0][1]), (0, 255, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]),
             (biggest[1][0][0], biggest[1][0][1]), (0, 255, 0), thickness)

    return img


while True:

    # Grayscale
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    # Kernel size
    kernel_size = (5, 5)

    # Gaussian blur
    gaussian_blur = cv2.GaussianBlur(gray, kernel_size, 1)
    cv2.imshow('Gaussian blur', gaussian_blur)

    # Canny edge detection
    '''
    canny_edge = automatic_canny(gaussian_blur)
    cv2.imshow('Canny edge',canny_edge)
    '''

    # Canny edge detection using trackbar
    min_val = cv2.getTrackbarPos('minVal', 'trackbars')
    max_val = cv2.getTrackbarPos('maxVal', 'trackbars')
    canny_edge_trackbar = cv2.Canny(gaussian_blur, min_val, max_val)
    cv2.imshow('Canny edge trackbar', canny_edge_trackbar)

    # kernel for dilation and erosion
    kernel = np.ones((5, 5))

    # Apply dilation
    image_dilation = cv2.dilate(canny_edge_trackbar, kernel, iterations=2)
    cv2.imshow('Image Dilation', image_dilation)
    '''
    # Apply erosion
    image_erosion = cv2.dilate(image_dilation,kernel, iterations=1)        
    cv2.imshow('Image erosion',image_erosion)

    # Apply closing
    closing = cv2.morphologyEx(canny_edge_trackbar, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Image closing',closing)
    '''

    # Find contours

    # Copy image for display purpose
    image_copy = resized_image.copy()

    # Find all contours
    # cv2.RETR_EXTERNAL helps to find the outer edges
    contours, hierarchy = cv2.findContours(
        image_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw all detected contours
    cv2.drawContours(image_copy, contours, -1, (0, 255, 0),
                     10)  # DRAW ALL DETECTED CONTOURS

    # Result of contour
    cv2.imshow('Contours', image_copy)

    # Get only the biggest contour cordinates and area
    biggest, maxArea = getBiggestContour(contours)

    # Another sample image for display
    image_copy_2 = resized_image.copy()
    image_copy_3 = resized_image.copy()

    if biggest.size != 0:

        # Get the order in which we are detecting points of documents(page)
        biggest_in_order = getOrderOfLabel(biggest)
        cv2.circle(
            image_copy_2, (biggest_in_order[0][0][0], biggest_in_order[0][0][1]), 5, (0, 0, 255), cv2.FILLED)
        cv2.circle(
            image_copy_2, (biggest_in_order[1][0][0], biggest_in_order[1][0][1]), 5, (0, 0, 255), cv2.FILLED)
        cv2.circle(
            image_copy_2, (biggest_in_order[2][0][0], biggest_in_order[2][0][1]), 5, (0, 0, 255), cv2.FILLED)
        cv2.circle(
            image_copy_2, (biggest_in_order[3][0][0], biggest_in_order[3][0][1]), 5, (0, 0, 255), cv2.FILLED)

        # Filled circle at 4 corners points
        cv2.drawContours(image_copy_3, biggest_in_order, -1, (0, 255, 0), 20)

        # Make the lines from each point and draw it
        image_copy_3 = drawRectangle(image_copy_3, biggest_in_order, 2)

        # Prepare point for wrap
        pts1 = np.float32(biggest_in_order)
        pts2 = np.float32(
            [[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])

        # Map the points based on the position of points (i.e first corner = [0,0], second corner = [width,0]
        # third corner = [0,height], forth corner = [width,height])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imageWrapColored = cv2.warpPerspective(
            resized_image, matrix, (widthImg, heightImg))

        # Remove false positive ( 20 pixel from each side )
        imageWrapColored = imageWrapColored[20:imageWrapColored.shape[0] -
                                            20, 20:imageWrapColored.shape[1]-20]

        # Convert BGR to Grayscale
        ImageWrapGray = cv2.cvtColor(imageWrapColored, cv2.COLOR_BGR2GRAY)

        # Apply Smoothing (Remove some noise in image)
        ImageWrapGauss = cv2.GaussianBlur(ImageWrapGray, kernel_size, 1)

        # Adaptive thresolding
        ImageWrapThresold = cv2.adaptiveThreshold(
            ImageWrapGauss, 255, 1, 1, 7, 2)

        '''        
        # Otsu thresolding
        ret, ImageWrapThresold = cv2.threshold(ImageWrapGauss,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)        
        '''
        ImageWrapBitwise = cv2.bitwise_not(ImageWrapThresold)
        '''
        # Remove salt and pepper noise
        ImageWrap = cv2.medianBlur(ImageWrapBitwise,5)
        '''

    cv2.imshow('Keypoints detected', image_copy_2)
    cv2.imshow('Contour Drawn', image_copy_3)
    cv2.imshow('Get Perspective image', imageWrapColored)
    cv2.imshow("Otsu thresolded image", ImageWrapBitwise)

    if cv2.waitKey(0) & 0xFF == 27:
        break

# Close all window
cv2.destroyAllWindows()

print(biggest, maxArea, biggest.size)
print(biggest_in_order)
print(biggest_in_order.shape)
print(biggest_in_order[0][0][0], biggest_in_order[0][0][1])
print(biggest_in_order[1][0][0], biggest_in_order[1][0][1])
print(biggest_in_order[2][0][0], biggest_in_order[2][0][1])
print(biggest_in_order[3][0][0], biggest_in_order[3][0][1])
print(imageWrapColored.shape)

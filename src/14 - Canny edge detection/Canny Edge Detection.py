'''
In previous code snippet discussed abot image gradient
method for edge detection. In this snippet will look for more
advanced canny edge detector algo.

This is into 4 phases 

Noise Reduction -> Finding gradient direction and magnitude -> Non-max supression -> Hystresis Thresholding.

In Noise reduction, remove noise using smoothing filters like gaussian.

Finding gradient magnitude -> Using first derivative i.e, Sobel filters will find the direction (angle between horizontal and vertical derivative)
And magnitude using both horiz and vetical  = np.sqrt(Sx**2 + Sy**2)

Non-max supression -> Basically a first stage filtering for non-edges.

Hystersis thresholding -> Using range for maxval and minval, filter edges and non-edges

Question is how to choose min value and max value.

I will show you automatic canny edge detector.
'''

import cv2
import numpy as np 
import matplotlib.pyplot as pyplot

img = cv2.imread('../Images and Videos/messi.jpg',0)

def automatic_canny(images, sigma=0.33):
    median = np.median(images)

    ## Based on some statistics
    lower = int(max(0, (1-sigma)*median))
    upper = int(min(255, (1+sigma)*median))
    edged = cv2.Canny(images, lower, upper)

    cv2.imshow('Edges detected', edged)
    cv2.waitKey(0)


    ## Manually selected values
    edged = cv2.Canny(images, 100, 200)

    cv2.imshow('Edges detected', edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

automatic_canny(img)

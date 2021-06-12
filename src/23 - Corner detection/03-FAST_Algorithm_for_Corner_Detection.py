import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
Implementation of FAST (Features from Accelerated Segment Test) Algorithm for Corner Detection
'''
# Read RGB image
img = cv2.imread('../Images and Videos/Building.jpg')
cv2.imshow('original image',img)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create(50) # 50: Number of keypoint

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None,flags=0)

# NMS -> Non max suppression
cv2.imshow('FAST With NMS',img2)

#Print all default params
print("Threshold: ", fast.getThreshold());
print("nonmaxSuppression: ", fast.getNonmaxSuppression());
print("neighborhood: ", fast.getType());
print("Total Keypoints with nonmaxSuppression: ", len(kp));

cv2.waitKey(0)
cv2.destroyAllWindows()


import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
Implementation of ORB (Oriented FAST and Rotated BRIEF).
ORB: An efficient alternative to SIFT or SURF

ORB is basically a fusion of FAST keypoint detector and BRIEF descriptor
with many modifications to enhance the performance. First it use FAST to find keypoints,
then apply Harris corner measure to find top N points among them. It also use pyramid to produce multiscale-features.

Read more about : https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html
'''

# Read RGB image
img = cv2.imread('../Images and Videos/Building.jpg')
cv2.imshow('original image',img)

orb = cv2.ORB_create(200)  # 200 : No of keypoints

keypoint, descriptor = orb.detectAndCompute(img, None)

# Use two flags
'''
flag = 0
    or
flag = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
'''

img2 = cv2.drawKeypoints(img,keypoint,None,flags=0)
cv2.imshow("ORB_Image2",img2)


img3 = cv2.drawKeypoints(img,keypoint,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("ORB_Image3",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()


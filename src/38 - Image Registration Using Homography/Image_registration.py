# We have two images 1. Reference image and 2. Deformed images , We will transformed the deformed image to look like an reference image

'''
The two main technique associated with image registration is that
1. First we have detect important features or keypoints using "Feature detection" algorithm like ORB (Oriented FAST and Rotated BRIEF)
2. Then we have to match this features using "Feature matching" technique like Brute force matcher
Workflow : 
1. Import 2 images
2. Convert them to gray scale
3. Initiate ORB Detector
4. Find the key points and description
5. Match keypoints - Brute force matcher
6. Seperate a good keypoints from bad keypoints using RANSAC (reject bad keypoints)
7. Register two images (using homology)
'''

import cv2
import urllib.request
import numpy as np

# Read RGB image (Distorted image)
img1 = cv2.imread('../Images and Videos/monkey_distorted.jpg')
cv2.imshow('original image', img1)

# Read RGB image (Reference image)


def url_to_image(url):

    # 1st step
    url_open = urllib.request.urlopen(url)

    # 2nd step
    byte_arr = bytearray(url_open.read())

    # 3rd step (1D array)
    image = np.array(byte_arr, np.int8)

    # 4th step
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image


img2 = url_to_image(
    "https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/monkey.jpg")
cv2.imshow('image', img2)

# Grayscale images
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(200)  # 200 : No of keypoints
keypoint1, descriptor1 = orb.detectAndCompute(gray1, None)
keypoint2, descriptor2 = orb.detectAndCompute(gray2, None)
print(keypoint1, descriptor1)
# Use two flags
'''
flag = 0
    or
flag = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
'''

img3 = cv2.drawKeypoints(gray1, keypoint1, None, flags=0)
img4 = cv2.drawKeypoints(gray2, keypoint2, None, flags=0)

cv2.imshow("ORB_Image3", img3)
cv2.imshow("ORB_Image4", img4)

# Brute-Force matcher is simple. It takes the descriptor of one feature (Distorted image) in first set and is matched with all other features in second set (reference image)
# using some distance calculation. And the closest one is returned.
# cv2.DescriptorMatcher_create(
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
output : Perform masking operation part 2
Reference : https://www.pyimagesearch.com/2021/01/19/image-masking-with-opencv/
'''

# Import package
import cv2
import numpy as np
import matplotlib.pyplot as plt 

"""
Example 01 : Rectangular masking
"""

# load the original input image and display it to our screen
image = cv2.imread('../Images and Videos/target.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)

# Use matplotlib to get the co-ordinates of ROI
img1 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.show()

# A mask is the same size as our image, but has only two pixel
# values, 0 and 255 -- pixels with a value of 0 (background) are
# ignored in the original image while mask pixels with a value of
# 255 (foreground) are allowed to be kept

# We then construct a NumPy array, filled with zeros, with the same width and height as our original image
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (130, 23), (240, 250), 255, -1)
cv2.imwrite('Figure_5.png',mask)
cv2.imshow("Rectangular Mask", mask)

# apply our mask -- notice how only the person in the image is
# cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imwrite('Figure_6.png',masked)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)

"""
Example 02 : Circular masking
"""

# Read 2nd image
image2 = cv2.imread('../Images and Videos/earth.jpg')

img1 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
plt.imshow(img1)
plt.show()

# now, let's make a circular mask with a radius of 100 pixels and
# apply the mask again
mask = np.zeros(image2.shape[:2], dtype="uint8")
cv2.circle(mask, (479, 270), 160, 255, -1)

masked = cv2.bitwise_and(image2, image2, mask=mask)

# show the output images
cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
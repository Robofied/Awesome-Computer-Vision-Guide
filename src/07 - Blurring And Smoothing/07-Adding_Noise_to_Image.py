'''
Output : Add different noise to an image

Reference : https://theailearner.com/2019/05/07/add-different-noise-to-an-image/
'''

# We can add different types of noise in an image like Gaussian, salt-and-pepper, speckle, etc. 
# By knowing this, you will be able to evaluate various image filtering, restoration, and many other techniques. 

# Image noise is a random variation in the intensity values. Thus, by randomly inserting some values in an image, we can reproduce any noise pattern. For randomly inserting values, Numpy random module comes handy. Let’s see how

# import package

import cv2
import numpy as np
 
img = cv2.imread('../Images and Videos/logo.png')

# Draw random samples from a normal (Gaussian) distribution.
# Generate Gaussian noise
mu, sigma = 0,1 
gauss = np.random.normal(mu,sigma,img.size)

gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

# Add the Gaussian noise to the image
img_gauss = cv2.add(img,gauss)

cv2.imshow('gaussian_noise', gauss)

# Display the image
cv2.imshow('Noisy_image',img_gauss)
cv2.waitKey(0)
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
import matplotlib.pyplot as plt
import random

from numpy.core.fromnumeric import size

def gaussian_noise():

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
    res = np.hstack([gauss,img,img_gauss])
    plt.imshow(res, cmap='gray')
    plt.title('Adding Gaussian Noise')
    plt.axis('off')
    plt.show()
    cv2.waitKey(0)

def salt_and_pepper_noise():

    img = cv2.imread('../Images and Videos/logo.png', 0)
    img = img.astype(np.float)
    img = img/255.0
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            img[i,j] = np.random.randint(0, 1, size=(img.shape[1], img.shape[0]))

    cv2.imshow(img)
    cv2.waitKey(0)

salt_and_pepper_noise()
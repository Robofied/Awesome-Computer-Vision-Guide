'''
Output : Add different noise to an image
    'gauss'     Gaussian-distributed additive noise.
    'poisson'   Poisson-distributed noise generated from the data.
    's&p'       Replaces random pixels with 0 or 1.
    'speckle'   Multiplicative noise using out = image + n*image,where
                n is uniform noise with specified mean & variance.

Reference : https://theailearner.com/2019/05/07/add-different-noise-to-an-image/
'''

# We can add different types of noise in an image like Gaussian, salt-and-pepper, speckle, etc. 
# By knowing this, you will be able to evaluate various image filtering, restoration, and many other techniques. 

# Image noise is a random variation in the intensity values. Thus, by randomly inserting some values in an image, we can reproduce any noise pattern. For randomly inserting values, Numpy random module comes handy. Let’s see how

# import package

from operator import pos
import posixpath
import cv2
import random
from numpy.lib.type_check import imag
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


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


def salt_and_pepper_noise(prob):

    # Read image
    img = cv2.imread('../Images and Videos/logo.png')

    # Copy of original image 
    img_copy = img.copy()

    thresh = 1 - prob
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            random_no = random.random()
            if random_no < prob:
                img_copy[i][j] = 0
            elif random_no > thresh:
                img_copy[i][j] = 255
            else: 
                img_copy[i][j] = img[i,j]

    res = np.hstack([img,img_copy])
    plt.imshow(res)
    plt.title('Adding Salt & Papper Noise')
    plt.axis('off')
    plt.show()


def poission_noise():

    # Read image
    img = cv2.imread('../Images and Videos/logo.png')

    # Copy of the image
    image = img.copy()

    info = np.iinfo(image.dtype)
    print(image.dtype, info)

    image = image.astype(np.float64) / info.max

    # Poission noise using skimage library
    poisson_noisy_image = skimage.util.random_noise(image, mode="poisson")

    poisson_noisy_image = 255 * poisson_noisy_image 
    poisson_noisy_image = poisson_noisy_image.astype(np.uint8)

    res = np.hstack([img,poisson_noisy_image])

    df = [img.ravel(), poisson_noisy_image.ravel()]    
    for i in range(2):
        plt.subplot(1,2,(i+1))
        plt.hist(df[i])
    plt.show()

    plt.imshow(res)
    plt.title('Adding Poisson Noise')
    plt.axis('off')
    plt.show()

def speckle():
    # Read image
    image = cv2.imread('../Images and Videos/logo.png')
    row,col,ch = image.shape
    gauss = np.random.randn(row,col,ch)
    gauss = gauss.reshape(row,col,ch)        
    noisy = image + image * gauss
    res = np.hstack([image,noisy])
    plt.imshow(res)
    plt.title('Adding Speckle Noise')
    plt.axis('off')
    plt.show()
    
if __name__=='__main__':
    gaussian_noise()
    salt_and_pepper_noise(prob = 0.05)
    poission_noise()
    speckle()


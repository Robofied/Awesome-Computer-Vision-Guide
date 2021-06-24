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

import cv2
import random
from numpy.lib.type_check import imag
import skimage
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


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
    image = img.copy()
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    poisson_noisy_image = np.random.poisson(image * vals) / float(vals)

    res = np.hstack([img,poisson_noisy_image])
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
# def plotnoise(img, mode, r, c, i):
#     plt.subplot(r,c,i)
#     if mode is not None:
#         gimg = skimage.util.random_noise(img, mode=mode)
#         plt.imshow(gimg)
#     else:
#         plt.imshow(img)
#     plt.title(mode)
#     plt.axis("off")

# def adding_noise_using_skimage_library():

#     img_path="https://i.guim.co.uk/img/media/4ddba561156645952502f7241bd1a64abd0e48a3/0_1251_3712_2225/master/3712.jpg?width=1920&quality=85&auto=format&fit=max&s=1280341b186f8352416517fc997cd7da"
#     img = io.imread(img_path)/255.0

#     row, col = 4,2
#     noise_type = ["gaussian","localvar", "poisson", "salt", "pepper", "s&p", "speckle"]
#     for i in range(1, len(noise_type)+1):    
#         plotnoise(img, noise_type[i-1], row,col, i)
#     plt.show()

# adding_noise_using_skimage_library()

# img_path="https://i.guim.co.uk/img/media/4ddba561156645952502f7241bd1a64abd0e48a3/0_1251_3712_2225/master/3712.jpg?width=1920&quality=85&auto=format&fit=max&s=1280341b186f8352416517fc997cd7da"
# img = skimage.io.imread(img_path)/255.0
# gimg = skimage.util.random_noise(img, mode="s&p")
# plt.imshow(gimg)
# plt.show()
# def plotnoise(img, mode, r, c, i):
#     plt.subplot(r,c,i)
#     if mode is not None:
#         gimg = skimage.util.random_noise(img, mode=mode)
#         plt.imshow(gimg)
#     else:
#         plt.imshow(img)
#     plt.title(mode)
#     plt.axis("off")

# plt.figure(figsize=(18,24))
# r=4
# c=2
# plotnoise(img, "gaussian", r,c,1)
# plotnoise(img, "localvar", r,c,2)
# plotnoise(img, "poisson", r,c,3)
# plotnoise(img, "salt", r,c,4)
# plotnoise(img, "pepper", r,c,5)
# plotnoise(img, "s&p", r,c,6)
# plotnoise(img, "speckle", r,c,7)
# plotnoise(img, None, r,c,8)
# plt.show()
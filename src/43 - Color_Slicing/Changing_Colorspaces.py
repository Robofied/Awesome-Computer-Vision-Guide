import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Then we will read the original colored image from the file system with a call to the imread function.
This function receives as input the path to the file and returns the image as a ndarray.
he image is read in the BGR format.
'''

# BGR Image
image = cv2.imread('../Images and Videos/mandrill_monkey.jpg')

image_copy = image.copy()
# Type and shape ( image.shape[0] => Height and image.shape[1] => Width)
print("[INFO] Type of image : ", type(image)) 
print("[INFO] Original image => width : {} Height : {} channel : {}".format(image.shape[1],image.shape[0],image.shape[2]))
cv2.imshow('Original image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grayscale without using inbuilt function (Reference : https://docs.opencv.org/master/de/d25/imgproc_color_conversions.html)
'''
    Method 01 - Averaging - R,G,B values
                Y = (R+G+B)/3


    Method 2: LUMA-REC-601(non-linear)
    
    The human eye always interprets different colors in a different way. The weights ranging in the order of Green, Red and Blue.

    If three sources appear red, green and blue, and have the same radiance in the visible spectrum,
    then the green will appear the brightest of the three because the luminous efficiency function peaks in the green region of the spectrum.

    The red will appear less bright, and the blue will be the darkest of the three. As a consequence of the luminous efficiency function,
    all saturated blue colors are quite dark and all saturated yellows are quite light.

    If luminance is computed from red, green and blue, the coefficients will be a function of the particular red, green and blue
    spectral weighting functions employed, but the green coefficient will be quite large, the red will have an intermediate value,
    and the blue coefficient will be the smallest of the three.

'''

# Intialize a new array of zeroes with the same shape
gray = np.zeros((image.shape[0],image.shape[1]));
gray2 = np.zeros((image.shape[0],image.shape[1]));

# Map averages of pixels to the grey image : Raw average
for r in range(len(image)): 
    for c in range(len(image[0])): 
        # Use human average
        gray[r][c] = np.average(image_copy[r][c]);

# Method 02 : 'Human' Average - adapted for human eyes
for r in range(len(image)): 
    for c in range(len(image[0])): 
        # Use human average
        gray2[r][c] = 0.299*image_copy[r][c][0] + 0.587*image_copy[r][c][1] + 0.114*image_copy[r][c][2]


'''
Each channel is represented as a ndarray with two dimensions,
which means this can represented by grayscale images.
'''

print("[INFO] 1 Channel => Grayscale ",gray2.shape)

images = [gray, gray2]
title  = ["Average - Method 1","LUMA-REC-601(non-linear) - Method 2"]
for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(title[i])
plt.show()
    

# implementation of rgb2gray scale but instead of 1 channel it's 3 channel
def rgb2gray_3Channel(image):

    b,g,r = image_copy[:,:,0], image_copy[:,:,1], image_copy[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    for i in range(3):
        image_copy[:,:,i] = gray
    return image_copy

grayscale = rgb2gray_3Channel(image)
print("[INFO] 3 Channel => Grayscale width : {} Height : {} channel : {}".format(grayscale.shape[1],grayscale.shape[0],grayscale.shape[2]))
cv2.imshow('grayscale',grayscale)

'''
Now our objective is to see different channels of input image i.e Red,Green and Blue 
'''

# Split the image into B,G,R 
B,G,R = image[:,:,0],image[:,:,1],image[:,:,2]

'''
Another way to split the image is using the function cv2.split
blue, green, red = cv2.split(image)
'''

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# We can only stack image which have same size (width and height) and channel (here all image have channel - 1)
BGR_stacking = np.hstack([gray,B,G,R])
cv2.imshow('BGR_stacking',BGR_stacking)

# Now, this is not the desire output, we want to see only one color in an image
# this possible when we black out other two channel i.e for blue color channel (in case BGR)
# the answer should be [100,0,0] as we know black have intensity value i.e pixel '0'

k = np.zeros_like(B)
blue = cv2.merge([B,k,k])
green = cv2.merge([k,G,k])
red = cv2.merge([k,k,R])

BGR_Color_Scheme = np.hstack([image,blue,green,red])
cv2.imshow('BGR_Color_Scheme',BGR_Color_Scheme)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
You can see variety of inbuilt color spaces
>>> import cv2
>>> flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
>>> print flags

'''

# BGR to RGB
RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# BGR to HSL
HLS = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

# BGR to HSV
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# BGR to LUV
LUV = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)

# BGR to HSV
YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# BGR to YUV
YUV = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

images = [RGB, HLS,HSV, LUV, YCrCb, YUV]
title  = ["RGB", "HLS","HSV", "LUV", "YCrCb", "YUV"]
for i in range(6):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i])
    plt.xlabel(title[i])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

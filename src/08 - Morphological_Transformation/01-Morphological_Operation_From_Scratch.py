# import package
import cv2
import numpy as np
import matplotlib.pyplot as plt
 

# Erosion operation
'''
Condition
1. If complete match then output = 1
2. if partial match then output = 0
3. if complete unmatch then output = 0
'''

def erosion(image,kernel):
    row = image.shape[0] + kernel.shape[0] - 1
    column = image.shape[1] + kernel.shape[0] - 1

    erosion_image = np.zeros((row,column),dtype=np.uint8)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            erosion_image[i + np.int((kernel.shape[0]-1)/2),j + np.int(( kernel.shape[1]-1) / 2)] = image[i,j]

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            # Extract each patch from image     
            patch = erosion_image[i : i + kernel.shape[0],j : j + kernel.shape[1]]

            # element wise comparision
            result = np.equal(patch,kernel)

            # if all true then pixel value becomes 1 else it will 0
            final = np.all(result==True)

            if final:
                image[i,j]=1
            else:
                image[i,j]=0

    return image
            
# Dilation
'''
Condition
1. If complete match then output = 1
2. if partial match then output = 1
3. if complete unmatch then output = 0
'''

def dilation(image,kernel):
    row = image.shape[0] + kernel.shape[0] - 1
    column = image.shape[1] + kernel.shape[0] - 1

    dilation_image = np.zeros((row,column),dtype=np.uint8)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            dilation_image[i + np.int((kernel.shape[0]-1)/2),j + np.int(( kernel.shape[1]-1) / 2)] = image[i,j]

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):

            # Extract each patch from image     
            patch = dilation_image[i : i + kernel.shape[0],j : j + kernel.shape[1]]

            # element wise comparision
            result = np.equal(patch,kernel)

            # if all true then pixel value becomes 1 else it will 0
            final = np.any(result==True)

            if final:
                image[i,j]=1
            else:
                image[i,j]=0

    return image

# Opening ( Erosion followed by dilation)
def opening(image,kernel):
    # first erosion
    erode = erosion(image,kernel)

    # second dilation
    dilate = dilation(erode,kernel)

    return dilate

# Closing ( Dilation followed by erosion)
def closing(image,kernel):
    # first dilation
    dilate = dilation(image,kernel)

    # second dilation
    erode = erosion(dilate,kernel)

    return erode



# Read Image (RGB Image - 3 channel)
image = cv2.imread('../Images and videos/morph1.png')

# Grayscale - 1 channel 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
# Binary - either 0 pixel or 255 pixel (black or white)
(thresh,binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Convert '0' => 0 and '255' => 1
binary = binary/255.0

binary_copy0 = binary.copy()
binary_copy1 = binary.copy()
binary_copy2 = binary.copy()
binary_copy3 = binary.copy()

# 5x5 - Kernel (filled with 1)
kernel = np.ones((5,5),dtype=np.uint8)

# Padding (Because after performing convolution output size of image gets reduced
# so padding will insure that output size is equals to input size)

erosion_image = erosion(binary_copy0,kernel)
dilation_image = dilation(binary_copy1,kernel)


# Opening ( Erosion followed by dilation )
opening_image = opening(binary_copy2,kernel)

# Closing ( Dilation followed by erosion)
closing_image = closing(binary_copy3,kernel)

print(gray.shape)
print(gray.reshape(-1))
print(np.max(thresh))
print(np.min(binary))


images = [image, erosion_image]
titles = ['Original image', 'Erosion']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

images = [image, dilation_image]
titles = ['Original image', 'Dilation']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

images = [image, opening_image]
titles = ['Original image', 'Opening']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

images = [image, closing_image]
titles = ['Original image', 'Closing']

for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()


# Display image
'''
cv2.imshow('Original image',image)
cv2.imshow('Gray',gray)
cv2.imshow('binary',binary)

cv2.imshow('erosion_image',erosion_image)
cv2.imshow('dilation_image',dilation_image)
cv2.imshow('Opening',opening_image)
cv2.imshow('Closing',closing_image)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('../Images and Videos/otsu.jpg')

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret1, thresh1 = cv2.threshold(grayscale,127,255, cv2.THRESH_BINARY)

ret2, thresh2 = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

gauss_img = cv2.GaussianBlur(grayscale, (5,5), 0)
ret3, thresh3 = cv2.threshold(gauss_img, 127,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img,thresh1, thresh2, thresh3]

titles = ['Original image','Global Thresholding (v=127)', "Otsu's Thresholding", "Otsu's Thresholding with Gaussian Blur"]

plt.figure(figsize=(10,5))
for i in range(4):
    plt.subplot(2,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

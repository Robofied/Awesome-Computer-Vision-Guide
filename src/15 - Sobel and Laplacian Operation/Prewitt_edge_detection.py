import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

'''
Same as Sobel except the kernel is different i.e Gx and Gy 
'''

def mult(x,y):
	c = 0
	for i in range(len(x)):
		for j in range(len(y[0])):
			c += x[i][j]*y[i][j]
	if c<0:
		return 0
	elif c>255:
		return 255
	else:
		return c 

Gx = np.array([[-1,-1,-1],[-2,0,2],[1,1,1]])
Gy = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

print(len(Gx))

# Read image as grayscale

img_path = "../Images and Videos/flower.jpg"
image = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)

# remove noise
image = cv2.GaussianBlur(image,(3,3),0)

plt.subplot(1,5,1)
plt.title("Original Image (I)")
plt.imshow(image,cmap = "gray")

(h,w) = image.shape
imgx = np.array([[0]*(w-2)]*(h-2))
imgy = np.array([[0]*(w-2)]*(h-2))
img = np.array([[0]*(w-2)]*(h-2))
print(imgx.shape)
print(image.shape)
for i in range(0,h-2):
	for j in range(0,w-2):
		x = np.array(image[i:i+3,j:j+3])
		imgx[i][j] = mult(x,Gx)

plt.subplot(1,5,2)
plt.title("I*Gx")
plt.imshow(imgx,cmap = "gray")

for i in range(0,h-2):
	for j in range(0,w-2):
		y = np.array(image[i:i+3,j:j+3])
		imgy[i][j] = mult(y,Gy)
plt.subplot(1,5,3)
plt.title("I*Gy")
plt.imshow(imgy,cmap = "gray")


for i in range(imgx.shape[0]):
	for j in range(imgx.shape[1]):
		img[i][j] = math.sqrt((imgx[i][j]*2)+(imgy[i][j]*2))

plt.subplot(1,5,4)
plt.title("Edge Detection using Prewitt")
plt.imshow(img,cmap = "gray")

th = int(input("Enter Threshold Value: ")) # th = 10
(h,w) = img.shape
print(h,w)

for i in range(h):
	for j in range(w):
		if img[i][j] > th:
			img[i][j] = 255
		else:
			img[i][j] = 0
plt.subplot(1,5,5)
plt.title("Threshold Image")
plt.imshow(img,cmap = "gray")
plt.show()

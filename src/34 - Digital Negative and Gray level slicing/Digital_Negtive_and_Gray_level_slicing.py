import cv2
import os

'''
Part 1 :- Perfrom Digital Negative
'''

image= cv2.imread('../Images and Videos/dog.png')

print(image.shape)

Digital_negative = 255 - image 
cv2.imshow('Digital_negative',Digital_negative)

os.makedirs('./Result', exist_ok=True)
cv2.imwrite('./Result/Digital_Negtive.png',Digital_negative)

'''
Part 2: Gray Level Slicing with and without background
'''


r1 = int(input("Enter r1 : "))
r2 = int(input("Enter r2 : "))
print(type(r1),type(r2))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_level_slicing_without_background = gray.copy()
gray_level_slicing_with_background = gray.copy()

print(gray.shape)
h,w= gray.shape

print(image[0][0])
print(gray[0][0])

# Gray level slicing without background

for i in range(h):
    for j in range(w):
        if gray_level_slicing_without_background[i][j] > r1 and gray_level_slicing_without_background[i][j] <r2:
            gray_level_slicing_without_background[i][j] = 255
        else:
            gray_level_slicing_without_background[i][j] = 0

# Gray level slicing without background

for i in range(h):
    for j in range(w):
        if gray_level_slicing_with_background[i][j] > r1 and gray_level_slicing_with_background[i][j] <r2:
            gray_level_slicing_with_background[i][j] = 255
            
cv2.imshow('image',image)
cv2.imshow('gray',gray)
cv2.imshow('Gray level slicing without background',gray_level_slicing_without_background)
cv2.imshow('Gray level slicing with background',gray_level_slicing_with_background)

cv2.imwrite('./Result/gray_level_slicing_without_background.png',gray_level_slicing_without_background)
cv2.imwrite('./Result/gray_level_slicing_with_background.png',gray_level_slicing_with_background)

cv2.waitKey(0)
cv2.destroyAllWindows()






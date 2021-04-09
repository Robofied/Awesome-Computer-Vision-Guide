import streamlit as st
import cv2
import numpy as np

# Original image
img = cv2.imread('../Images and Videos/dog.png')
cv2.imshow('Original_image',img)
def sketch(img):

    # Grayscale 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Gaussian Blur
    img_smoothing = cv2.GaussianBlur(img_gray, (21, 21), sigmaX=0, sigmaY=0)    

    # Matrix division
    final_img = cv2.divide(img_gray,  img_smoothing, scale=256)
    return img_gray, final_img

grayscale, final_img = sketch(img)

# We cannot concatenate 3 Dimensional (Original image) with 1D (grayscale img)
# while using hstack, both matrix should have similar dimension 
result = np.hstack((grayscale,final_img))
cv2.imshow('Sketch',result)

cv2.waitKey(0)
cv2.destroyAllWindows()

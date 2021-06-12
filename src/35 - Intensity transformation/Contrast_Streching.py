import cv2
import numpy as np

'''
most commonly used piecewise-linear transformation functions is contrast stretching.

Contrast can be defined as:

Contrast =  (I_max - I_min)/(I_max + I_min)
'''

# Function to map each intensity level to output intensity level. 
def pixelVal(pix, r1, s1, r2, s2):

    # In between 0 to r1
    if ( pix>=0 and pix <= r1): 
        return (s1 / r1)*pix

    # In between r1 to r2
    elif (pix > r1 and pix <= r2):
        slope = (s2 - s1)/(r2 - r1)
        return (slope) * (pix - r1) + s1

    # Greater then r2
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 
  
# Open the image. 
img = cv2.imread('../Images and Videos/road.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
# Define parameters. 
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
# Vectorize the function to apply it to each value in the Numpy array. 
pixelVal_vec = np.vectorize(pixelVal) 
  
# Apply contrast stretching. 
contrast_stretched = pixelVal_vec(gray, r1, s1, r2, s2) 

print(np.min(contrast_stretched),np.max(contrast_stretched))
# Save edited image. 
cv2.imshow('contrast_stretch.jpg',contrast_stretched)
cv2.imwrite('contrast_stretch.jpg',contrast_stretched)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''

With (r1, s1), (r2, s2) as parameters, the function stretches the intensity levels by essentially decreasing
the intensity of the dark pixels and increasing the intensity of the light pixels. If r1 = s1 = 0 and r2 = s2 = L-1,
the function becomes a straight dotted line in the graph (which gives no effect).
The function is monotonically increasing so that the order of intensity levels between pixels is preserved.

Referece :https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/

'''
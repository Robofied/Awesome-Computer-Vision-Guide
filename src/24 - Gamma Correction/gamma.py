import cv2
import numpy as np

'''
Intensity transformation
Power-law (gamma) transformations can be mathematically expressed as s = cr^{Y}

Y: gamma correction
r: pixel value of the image
s: output pixel value

'''

def gamma_filter(image , gamma = 1.0):
    #invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** gamma) * 255
	    for i in np.arange(0, 256)]).astype("uint8")
 
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

def inv_gamma_filter(image , gamma = 1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
	    for i in np.arange(0, 256)]).astype("uint8")
 
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

# read image
frame = cv2.imread('../Images and Videos/car1.jpg')
print(frame.shape)
frame = cv2.resize(frame, (300,400))
methods = input("1. Gamma(g)\n2. Inverse gamma (ig)\nEnter Method : ")

for gamma in np.arange(0.0,3.5,0.5):
    # if gamma = 1 then output will be original image
    if gamma ==1:
        continue

    gamma = gamma if gamma>0 else 0.1
    output = gamma_filter(frame ,gamma)
    output2 = inv_gamma_filter(frame ,gamma)
    
    if methods=='g':
        cv2.putText(output ,"gamma={}".format(gamma) , (10,30) , cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,120, 255), 2)
        cv2.imshow("images" , np.hstack([frame,output]))
    else:
        cv2.putText(output2 ,"gamma={}".format(gamma) , (10,30) , cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,120, 255), 2)
        cv2.imshow("images" , np.hstack([frame,output2]))
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
For gamma correction:
As can be observed from the outputs ,
gamma>1 (indicated by the curve corresponding to ‘nth power’ label on the graph),
the intensity of pixels decreases i.e. the image becomes darker.
On the other hand, gamma<1 (indicated by the curve corresponding to 'nth root'
label on the graph), the intensity increases i.e. the image becomes lighter.

and vice versa for inverse gamma correction
'''




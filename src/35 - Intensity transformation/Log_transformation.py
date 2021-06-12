import cv2 
import numpy as np 
import warnings
warnings.filterwarnings("ignore")

# Open the image. 
img = cv2.imread('../Images and Videos/flower.jpg') 

cv2.imshow('image',img)

'''
log transformation : S = c*log(1+r)
where s : output intensity value
      r : pixel value of the image

constant c : 255/log(1+m)
where m : maximum pixel value in the image
'''  

def log_transformation(img):
    m = np.max(img)
    try:
        c = int(255/np.log(1+m))
        s = c*np.log(1+img)
    except ZeroDivisionError:
        print("Encounter zero division error")
    
    lf = np.array(s,dtype=np.uint8)
    return lf


print(img.shape)
log_transformed_image = log_transformation(img)

cv2.imshow('log transformed',log_transformed_image)              
# Save the output. 
cv2.imwrite('log_transformed.jpg', log_transformed_image) 

cv2.waitKey(0)
cv2.destroyAllWindows()


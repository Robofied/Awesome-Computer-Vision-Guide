'''
Output: Set width and height of the Change the value in track bar to see the effect in the input image

'''

import cv2
import numpy as np

# Callback Function which helps to get the position of trackbar 
def nothing(x):
    pass

# Use to resize the window which u are created : cv2.namedWindow('Window_name', cv2.WINDOW_NORMAL) 

cv2.namedWindow('trackbars', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('x','trackbars',0,600,nothing)   # 1. trackbar name
cv2.createTrackbar('y','trackbars',0,600,nothing)   # 2. window name
cv2.createTrackbar('width','trackbars',0,400,nothing)  # 3. minimum value
cv2.createTrackbar('height','trackbars',0,400,nothing)  # 4. maximum value
cv2.createTrackbar('red','trackbars',0,255,nothing)  # 5. callback function
cv2.createTrackbar('green','trackbars',0,255,nothing)
cv2.createTrackbar('blue','trackbars',0,255,nothing)

cv2.setTrackbarPos('width','trackbars', 300)
cv2.setTrackbarPos('height','trackbars', 300)
cv2.setTrackbarPos('red','trackbars', 255)

# Define the codec and create VideoWriter object. The output is stored in 'outpy.avi' file.
# fourcc is a 4-byte code used to specify the video codec.
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 1.video_name 2.FourCC code 3.frame per sec 4.window size
out1 = cv2.VideoWriter('Original_frame.avi', fourcc, 10, (600, 600))

while True :

    # Create a black image of size 600 x 600   
    image = np.zeros((600,600,3),np.uint8)

    # Get trackbar position    
    x = cv2.getTrackbarPos('x','trackbars')
    y = cv2.getTrackbarPos('y','trackbars') 
    width = cv2.getTrackbarPos('width','trackbars')
    height = cv2.getTrackbarPos('height','trackbars')
    red = cv2.getTrackbarPos('red','trackbars')
    green = cv2.getTrackbarPos('green','trackbars')
    blue = cv2.getTrackbarPos('blue','trackbars')
    
    # Create a rectangle
    cv2.rectangle(image, (x,y),(x+width, y+height),(blue,green,red),-1)

    # Save video 
    # out1.write(image)

    # Display a video 
    cv2.imshow('frame',image)

    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break 

# cap.release()
cv2.destroyAllWindows()
            

            

            
            
        

import cv2
import numpy as np
import matplotlib.pyplot as plt

def linear_filter_operation(frame, K, L):
    img = frame.astype(np.float)
    img = img * K + L
    img[img > 255] = 255
    img[img < 0] = 0
    img = img.astype(np.uint8)
    return img

def image_operation():

    img = cv2.imread('../Images and Videos/flower_3.jpg')

    # k = 0.5, l = 0
    out1 = linear_filter_operation(img, 0.5, 0)

    # k = 1., l = 10
    out2 = linear_filter_operation(img, 1., 10)

    # k = 0.8, l = 15
    out3 = linear_filter_operation(img, 0.7, 25)

    images = [img, out1, out2, out3]
    titles = ['Input image', 'K=0.5 & L=0', 'K=1 & L=10', 'K=0.8 & L=15']
    
    for i in range(0,4):
        plt.subplot(1,4,(i+1))
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')    

    plt.show()

# Callback Function which helps to get the position of trackbar 
def callback(x):
    pass

# 1.trackbar name  2.window name 3.minimum value 4.maximum value 5.callback function
cv2.namedWindow('trackbars', cv2.WINDOW_NORMAL)
cv2.resizeWindow('trackbars',700, 200)
cv2.createTrackbar('K', 'trackbars', 0, 100, callback)
cv2.createTrackbar('L', 'trackbars', 0, 100, callback)

 
def main():

    while True:

        # Read frame 
        frame = cv2.imread('../Images and Videos/flower_3.jpg')

        # Get the trackbar position
        K = cv2.getTrackbarPos('K', 'trackbars')
        L = cv2.getTrackbarPos('L', 'trackbars')
        K = K/100.0

        # Linear filtering 
        linear_filter = linear_filter_operation(frame, K , L)    
        
        cv2.imshow('frame', frame)
        cv2.imshow('linear_filter',linear_filter)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__=='__main__':
    image_operation()
    main()
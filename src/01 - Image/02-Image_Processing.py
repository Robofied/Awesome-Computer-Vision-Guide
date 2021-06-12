'''
output : Output image can be resize
         named window can be use to resize the window
         imwrite to save the image
'''

# Import package
import cv2
import numpy as np


def main():
    # Display the set of flags which start with COLOR_
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print(flags)

    # Read image
    img = cv2.imread('../Images and Videos/dog.png', cv2.IMREAD_UNCHANGED)

    # Use to resize the window - basically you can strech the window
    cv2.namedWindow('Original_Image', cv2.WINDOW_NORMAL)

    # Display original image
    cv2.imshow('Original_Image', img)

    # Convert into grayscale image
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display grayscale image
    cv2.imshow('grayscale', grayscale)

    # Change the resolution of image
    width = int(img.shape[1] * 50 / 100)
    height = int(img.shape[0] * 50 / 100)
    dim = (width, height)

    resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # Display resized image
    cv2.imshow('resized_img', resized_img)

    k = cv2.waitKey(0) & 0xFF

    if k == 27:                         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('a'):
        # wait for 'a' key to save and exit
        cv2.imwrite('img_copy.jpg', img)
        cv2.destroyAllWindows()


main()

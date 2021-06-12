'''
Method #1: OpenCV, NumPy, and urllib

Reference : https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/

1. First we will use "urllib" library to open connection to supplied url, we get the HTTPS response object in return
2. The raw byte sequence get converted into Numpy array
3. As we get 1D array , which contain a bunch of pixel
4. As we know, our image as 2D image, hence we have to reshape it
5. So for that we will use "imdecode" method , which will return the decoded image 
'''

# Import package

import cv2
import urllib.request
import numpy as np

def url_to_image(url):

    # 1st step
    url_open = urllib.request.urlopen(url)
    print("URL Open", url_open)

    # 2nd step
    byte_arr = bytearray(url_open.read())
    print(byte_arr)

    # 3rd step (1D array)
    image = np.array(byte_arr, np.int8)
    print(image)

    # 4th step
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image

img = url_to_image("https://raw.githubusercontent.com/bnsreenu/python_for_microscopists/master/images/monkey.jpg")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

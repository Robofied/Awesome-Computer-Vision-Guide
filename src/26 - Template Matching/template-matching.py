import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../Images and Videos/messi.jpg', 0)
img2 = img.copy()

template = cv2.imread('../Images and Videos/messi_face.jpg',0)

## [::-1] just to make width and height value interchange
w, h = template.shape[::-1]

print(w,h)

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    res = cv2.matchTemplate(img, template, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc 
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img2, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching result')
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('Detected object')

    plt.suptitle(meth)

    plt.show()


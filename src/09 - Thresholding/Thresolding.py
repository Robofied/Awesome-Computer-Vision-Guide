import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../Images and videos/image8.jpg')

## Let's try converting it to grayscale
## If you want you can try without converting to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret1, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

images = [thresh1, thresh2, thresh3, thresh4, thresh5]
titles = ['Binary', 'Binary inverse', 'Truncate', 'Tozero', 'Tozero inverse']

## Showing up using opencv
for i in range(5):
    cv2.imshow(titles[i], images[i])
    cv2.waitKey(0)


## Showing up using matplotlib
for i in range(5):
    plt.subplot(2,3,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

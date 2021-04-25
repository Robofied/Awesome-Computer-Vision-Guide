import cv2

# img1 = cv2.imread('images/messi.jpg')
# img2 = cv2.imread('images/opencv-logo.png')

# rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols]

# # cv2.imshow("ful",img1)
# # cv2.waitKey(0)

# # cv2.imshow("roi",roi)
# # cv2.waitKey(0)

# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

# cv2.imshow("masked", mask)
# cv2.waitKey(0)

# mask_inv = cv2.bitwise_not(mask)

# cv2.imshow("masked inverse", mask_inv)
# cv2.waitKey(0)

# imb1 = cv2.bitwise_and(roi, roi, mask=mask_inv)

# cv2.imshow("bitwised", imb1)
# cv2.waitKey(0)  


img1 = cv2.imread('images/messi.jpg')
img2 = cv2.imread('images/opencv-logo.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
#img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
#dst = cv2.add(img1_bg,img2_fg)
#img1[0:rows, 0:cols ] = dst
cv2.imshow('image fore',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()





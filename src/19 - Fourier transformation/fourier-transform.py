import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Images and Videos/messi.jpg', 0)

# print(img.shape)

# cv2.imshow('image',img)

##---------------------------------Fourier Transform in numpy ---------------------------------##
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')

plt.show()



##----------------------------------- Fourier Transform in Opencv ------------------------------##

dft = cv2.dft(np.float32(img), flags= cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')

plt.show()

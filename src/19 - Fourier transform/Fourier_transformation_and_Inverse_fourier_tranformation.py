import cv2
import numpy as np
import matplotlib.pyplot as plt
import cmath

# Define pi
pi = cmath.pi

# Read image
img = cv2.imread('../Images and videos/target.jpg', 0)
cv2.imshow('image',img)

height,width = img.shape
print(height,width)

##---------------------------------Fourier Transform using formula ---------------------------------##

# (177 x 177)
templateM = np.zeros((height,height),dtype=complex)

# (284 x 284)
templateN = np.zeros((width,width),dtype=complex)

# intermediate
intermediate = np.zeros((height,width),dtype=float)

# Applying separability property 
# Row transformation
'''
TemplateN shape = (284 x 284)
'''
for x in range(width):
    for y in range(width):
        templateN[x][y] = cmath.exp(-1j*2*pi*x*y/width)

print(templateN.shape)

# Column transformation
'''
TemplateM shape = (177 x 177)
'''
for x in range(height):
    for y in range(height):
        templateM[x][y] = cmath.exp(-1j*2*pi*x*y/height) 

print(templateM.shape)

# Multiply row tranformation x original img x column transformation
'''
Intermediate shape = (284 x 284) * (284*177) * (177,177) = resultant shape (284,177)
'''
# Intermediate state (apply tranformation on original image)
intermediate = templateM.dot(img).dot(templateN)

#intermediate = np.array(intermediate,dtype=np.float32)
print(intermediate.shape)

# FFT Shift to make it into the center
ffts = np.fft.fftshift(intermediate);
#ffts = np.array(ffts,dtype=np.float32)

# Log transformation on ffts
def log_transformation(img):
    m = np.max(img)
    try:
        c = int(255/np.log(1+m))
        s = c*np.log(np.abs(1+img))
    except ZeroDivisionError:
        print("Encounter zero division error")
    
    lf = np.array(s,dtype=np.uint8)
    return lf

magnitude_spectrum = log_transformation(ffts)

# Display plots
'''
images = [img,intermediate,ffts,magnitude_spectrum]
titles = ['original image','Fourier transformed (intermediate)','shifted fourier (ffts)','Fourier transform using formula']
'''
images = [img,magnitude_spectrum]
titles = ['Original images','FT using Formula']
for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

# Inverse fourier transform

templateM = np.zeros((height,height),dtype=complex)
templateN = np.zeros((width,width),dtype=complex)

# Modification in formula 
for x in range(width):
    for y in range(width):
        templateN[x][y] = cmath.exp(1j*2*pi*x*y/width)

for x in range(height):
    for y in range(height):
        templateM[x][y] = cmath.exp(1j*2*pi*x*y/height) 

# Intermediate state (apply tranformation on Fourier transformed image)
IFT = templateM.dot(intermediate).dot(templateN) / width*height
#IFT = np.array(IFT,dtype=np.float32)
Original_img = np.abs(IFT)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(Original_img, cmap = 'gray')
plt.title('Image after IFT using formula'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(Original_img)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()

##---------------------------------Fourier Transform in numpy ---------------------------------##

f = np.fft.fft2(img)
#f = np.array(f,dtype=np.float32)

fshift = np.fft.fftshift(f)
# fshift = np.array(fshift,dtype=np.float32)

magnitude_spectrum_2 = 20*np.log(np.abs(fshift))
'''
images = [img,f,fshift,magnitude_spectrum_2]
titles = ['original image','Fourier transformed','shifted fourier','Fourier transform using inbuilt function']
'''
images = [img,magnitude_spectrum_2]
titles = ['Original images','FT using inbuilt function']
for i in range(2):
    plt.subplot(1,2,(i+1))
    plt.imshow(images[i],'gray')
    plt.xlabel(titles[i])

plt.show()

# Inverse fourier tranformation using inbuilt method 
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after IFT using inbuilt method'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

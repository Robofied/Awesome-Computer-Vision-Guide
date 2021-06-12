import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
1. original images
2. histogram of image
3. equalized histogram
4. histogram of equalized image
'''

image = cv2.imread('../Images and Videos/messi.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

h,w = gray.shape

def calc_frequency(img):
    img = list(img.reshape(-1))
    frequency = []

    for i in range(0,256,1):
        val = img.count(i)
        frequency.append(val)
    return frequency

pixel_frequency = calc_frequency(gray) 

#------------------- PDF ------------------- #
n = sum(pixel_frequency)

print(n)
pdf_dist = []

for i in pixel_frequency:
    pdf_dist.append( i / n)

print(pdf_dist[:10])
# ------------------ CDF --------------------- #

cdf_dist = []

temp=0
for i in pdf_dist:
    cdf_dist.append(i+temp)
    temp = i + temp

print(cdf_dist[:10])
      

# ------------------ Sk ---------------------- #

r = [round(255*i) for i in cdf_dist]
print(r[:10])

equalization = np.zeros_like(gray)


for i in range(h):
    for j in range(w):
        equalization[i][j] = r[gray[i][j]]
    

       
equalization_pixel_frequency = calc_frequency(equalization)       

# ---------------------- Equalization using inbuilt function ------------ #

equ = cv2.equalizeHist(gray)


# ---------------------- Display Histogram plots ------------ #

plt.figure(figsize=(7,5))

n = list(range(0,256,1))
plt.bar(n,pixel_frequency,color='blue')
plt.xlabel('pixel')
plt.ylabel('counts')
plt.title('Histogram of image')
plt.show()

plt.bar(n,equalization_pixel_frequency,color='blue')
plt.xlabel('pixel')
plt.ylabel('counts')
plt.title('Equalize Histogram')
plt.show()

# --------------------------- Display --------------------- #

cv2.imshow('gray',gray)
cv2.imshow('equalization',equalization)
cv2.imshow('Histogram_Equalization',equ)

res = np.hstack((gray,equalization ,equ))   

cv2.imshow('Overall',res)

images = [gray,equalization,equ]
titles = ['Gray','equalization (without inbuilt)','equalization (with inbuilt)']

plt.figure(figsize=(7,5))
for i in range(3):
    plt.subplot(1,3,(i+1))
    plt.imshow(images[i],cmap='gray', vmin=0, vmax=255)
    plt.xlabel(titles[i])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

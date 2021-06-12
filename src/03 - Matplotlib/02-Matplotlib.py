'''
Output : Image processing operation using matplotlib
Reference : https://matplotlib.org/stable/tutorials/introductory/images.html
'''
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import image

# Read an image : It's a 24-bit RGB PNG image (8 bits for each of R, G, B) => (R)8 + (G)8 + (B)8 = 24 bit
# Each channel having an a equal intensity hence it's rendering as a grayscale image
img = image.imread('../Images and Videos/stinkbug.png')
plt.imshow(img)
plt.title("RGB Image")
plt.show()


# Note the dtype there - float32. Matplotlib has rescaled the 8 bit data from each channel to floating point data between 0.0 and 1.0. 
# So now instead of min value to be 0 and max value to be 255, it's min value = 0.0 and max values = 1.0
# As a side note, the only datatype that Pillow can work with is uint8. Matplotlib plotting can handle float32 and uint8, 
# but image reading/writing for any format other than PNG is limited to uint8 data. 

# For RGB and RGBA images, Matplotlib supports float32 and uint8 data types. For grayscale, Matplotlib supports only float32.
print(img)
print('Original Image shape:', img.shape)  # 3 Channel
print('Original Image dtype:', img.dtype)  # Float type
print('Original Image type:', type(img))   # Numpy ndarray

# Applying pseudocolor schemes to image plots
# Each channel will have equal intensity value, let's verify

# Display Red Channel
Red_Channel = img[:, :, 0]
print(img)
print('Original Image shape:', Red_Channel.shape)  # 3 Channel
print('Original Image dtype:', Red_Channel.dtype)  # Float type
print('Original Image type:', type(Red_Channel))   # Numpy ndarray
plt.subplot(131)
plt.imshow(Red_Channel)
plt.title("Red Channel")

# Display Green Channel
Green_Channel = img[:, :, 1]
plt.subplot(132)
plt.imshow(Green_Channel)
plt.title("Green Channel")

# Display Blue Channel
Blue_Channel = img[:, :, 2]
plt.subplot(133)
plt.imshow(Blue_Channel)
plt.title("Blue Channel")
plt.show()


# Now, with a luminosity (2D, no color) image, the default colormap (aka lookup table, LUT), is applied. The default is called viridis. There are plenty of others to choose from.
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
plt.title("cmap='hot'")
plt.show()

# Note that you can also change colormaps on existing plot objects using the set_cmap() method:
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.title("imgplot.set_cmap('nipy_spectral')")
plt.show()

# Color scale reference
# It's helpful to have an idea of what value a color represents. We can do that by adding a color bar to your figure:

imgplot = plt.imshow(lum_img)
plt.colorbar()
plt.title("Color scale reference")
plt.show()


# Examining a specific data range
# Sometimes you want to enhance the contrast in your image, or expand the contrast in a particular region while sacrificing the detail in colors that don't vary much, or don't matter.
# A good tool to find interesting regions is the histogram. To create a histogram of our image data, we use the hist() function.

plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
plt.title("Histogram plot")
plt.show()

plt.subplot(121)
plt.imshow(img)
plt.title("Original image")

# We don't effect our original image
img_copy = img.copy()
img_copy[img_copy < 0.4], img_copy[img_copy > 0.8] = 0.0, 1.0
print('Contrast image:', img_copy)  # 3 Channel
print('Min value :', np.min(img_copy))  # Float type
print('Max value :', np.max(img_copy))   # Numpy ndarray

plt.subplot(122)
plt.imshow(img_copy)
plt.title("Expand Contrast")
plt.show()

# Set Clim
'''
Most often, the "interesting" part of the image is around the peak, and you can get extra contrast by clipping the regions above and/or below the peak. 
In our histogram, it looks like there's not much useful information on the upper end of histogram (frequency of white pixel is less in the image as compair to medium gray). 
Let's adjust the upper limit, so that we effectively "zoom in on" part of the histogram. We do this by passing the clim argument to imshow.
'''

# Earlier our limit is 0.0 to 1.0
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(lum_img)
ax.set_title('Before')
plt.colorbar(orientation='horizontal')

ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
ax.set_title('After')
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
plt.show()

# Array Interpolation schemes

'''
Interpolation calculates what the color or value of a pixel "should" be, according to different mathematical schemes. One common place that this happens is when you resize an image. 
The number of pixels change, but you want the same information. Since pixels are discrete, there's missing space. 
Interpolation is how you fill that space. 
This is why your images sometimes come out looking pixelated when you blow them up. 
The effect is more pronounced when the difference between the original image and the expanded image is greater. Let's take our image and shrink it. We're effectively discarding pixels, only keeping a select few. Now when we plot it, that data gets blown up to the size on your screen. The old pixels aren't there anymore, and the computer has to draw in pixels to fill that space.

We'll use the Pillow library that we used to load the image also to resize the image.
'''


img = Image.open('../Images and Videos/stinkbug.png')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)
plt.title("Interpolation = 'bilinear' [Pixelated]")
plt.show()

'''
Here we have the default interpolation, bilinear, since we did not give imshow() any interpolation argument.

Let's try some others. Here's "nearest", which does no interpolation.
'''

imgplot = plt.imshow(img, interpolation="nearest")
plt.title("Interpolation = 'nearest'")
plt.show()


# Bicubic interpolation is often used when blowing up photos - people tend to prefer blurry over pixelated.
imgplot = plt.imshow(img, interpolation="bicubic")
plt.title("Interpolation = 'bicubic'")
plt.show()

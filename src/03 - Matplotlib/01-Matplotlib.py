'''
Output : Image will be displayed using matplotlib
'''
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np


# Convert RGB To Grayscale - Using luminace formula
def rgb2gray(rgb):
    # Each inner list represents a pixel. Here, with an RGB image, there are 3 values. Since it's a black and white image, R, G, and B are all similar.
    # Method 01 : We can also use this formula
    #   1. np.dot(rgb[..., :3], [0.333, 0.333, 0.333])
    # Method 02 : Luminance formula
    #   2. np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def main():

    # read an image
    # Matplotlib relies on the Pillow library to load image data.
    # Matplotlib read image in RGB Format, not in BGR format like cv2
    img = image.imread('../Images and Videos/car2.jpg')

    print('Original Image shape:', img.shape)  # 3 Channel
    print('Original Image dtype:', img.dtype)  # Integer type
    print('Original Image type:', type(img))   # Numpy ndarray

    # So, you have your data in a numpy array (either by importing it, or by generating it). Let's render it. In Matplotlib, this is performed using the imshow() function.
    # Default interpolations : bilinear
    plt.imshow(img, interpolation='bilinear')
    plt.title("RGB Image")
    plt.show()

    # Annotate image using matplotlib
    plt.imshow(img)
    plt.plot([250, 400], [250, 800], color="white", linewidth=10)
    plt.title("Annotated image")
    plt.show()

    gray = rgb2gray(img)
    plt.imshow(gray, cmap='gray', vmin=0, vmax=255)
    plt.title("Grayscale Image")
    plt.show()

    # If you want to display the inverse grayscale, switch the cmap to cmap='gray_r'.
    plt.imshow(gray, cmap='gray_r', vmin=0, vmax=255)
    plt.title("Inverse Grayscale Image")
    plt.show()


main()

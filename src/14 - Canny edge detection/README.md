

# Canny 

The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. It was developed by John F. Canny in 1986. Canny also produced a computational theory of edge detection explaining why the technique works. 

# Process of Canny edge detection algorithm

The Process of Canny edge detection algorithm can be broken down to 5 different steps: 
Apply Gaussian filter to smooth the image in order to remove the noise
Find the intensity gradients of the image
Apply non-maximum suppression to get rid of spurious response to edge detection
Apply double threshold to determine potential edges
Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.
# Gaussian filter
Since all edge detection results are easily affected by image noise, it is essential to filter out the noise to prevent false detection caused by noise. To smooth the image, a Gaussian filter is applied to convolve with the image. This step will slightly smooth the image to reduce the effects of obvious noise on the edge detector. 
The equation for a Gaussian filter kernel of size (2k+1)×(2k+1) is given by

![alt text](https://github.com/yoyoberenguer/Sobel-Feldman/blob/master/Assets/Graphics/Canny1.png)

Here is an example of a 5×5 Gaussian filter, used to create the adjacent image, with 
σ = 1.4. (The asterisk denotes a convolution operation.) 

![alt text](https://github.com/yoyoberenguer/Sobel-Feldman/blob/master/Assets/Graphics/Canny2.png)

It is important to understand that the selection of the size of the Gaussian kernel will affect the performance of the detector. The larger the size is, the lower the detector’s sensitivity to noise. Additionally, the localization error to detect the edge will slightly increase with the increase of the Gaussian filter kernel size. A 5×5 is a good size for most cases, but this will also vary depending on specific situations. 


![alt text](https://github.com/yoyoberenguer/Sobel-Feldman/blob/master/Canny.png)

## Reference 

* [https://github.com/yoyoberenguer/Sobel-Feldman](https://github.com/yoyoberenguer/Sobel-Feldman)

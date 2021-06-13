## **Digital Image Processing**

- Digital Image Processing denotes the process of digital images with
the use of digital computer.

- Digital images are contains various types of noises which are
reduces the quality of images. Noises can be removed by various
enhancement techniques.

- Noise is anything in the image that are unwanted or undesired
information. <br/>
    Examples:

    - Light fluctuations<br/>
    - Sensor noise<br/>
    - Transmission

## **Smoothing**

- Smoothing is often used to reduce noise within an image.
- Image smoothing is a key technology of image enhancement,
which can remove noise in images. So, it is a necessary
functional module in various image-processing software.
- Image smoothing is a method of improving the quality of
images.
- Smoothing is performed by spatial and frequency filters

## **Filtering**

Image filtering can be grouped in two depending on the effects:

- **Low pass filters (Removal of noise, Smoothing/Blurring the images)**

    Low pass filtering (aka smoothing), is employed to remove high spatial frequency noise from a digital image. The low-pass filters usually employ moving window operator which affects one pixel of the image at a time, changing its value by some function of a local region (window) of pixels. The operator moves over the image to affect all the pixels in the image.

    An image is smoothed by decreasing the disparity between pixel values by averaging nearby pixels.

    Using a low pass filter tends to retain the low frequency information within an image while reducing the high frequency information.

- **High pass filters (Edge Detection, Sharpening)**

    A high-pass filter can be used to make an image appear sharper. These filters emphasize fine details in the image - the opposite of the low-pass filter. High-pass filtering works in the same way as low-pass filtering; it just uses a different convolution kernel.

When filtering an image, each pixel is affected by its neighbors, and the net effect of filtering is moving information around the image.


## **Spatial filtering** 

- Spatial filtering term is the filtering operations that are
performed directly on the pixels of an image. The process
consists simply of moving the filter mask from point to point
in an image.

    - Smoothing spatial filters (Low pass filters)
    - Sharpening spatial filters (High pass filters)

## **Smoothing Spatial Filters** 

- Smoothing filters are used for noise reduction and blurring
operations.

- It takes into account the pixels surrounding it in order to make
a determination of a more accurate version of this pixel.

- By taking neighboring pixels into consideration, extreme
“noisy” pixels can be filtered out.

- Unfortunately, extreme pixels can also represent original fine
details, which can also be lost due to the smoothing process

## **What is an image filtering?** 

First of all, let’s introduce a concept of filtering. The filter is actually a small matrix that we will use to sharpen or blur our original image. In order to do that we need to perform an operation of convolution. As it is always the case with most important concepts let’s quickly refresh our knowledge of convolution.

As you can see at the GIF animation below (left), we have a matrix of `6×6` pixels that represents our image. Next, we perform a convolution operation with a `3×3` filter. The final product of this convolution process will be a `4×4` matrix. In order to calculate the first element (top left corner) of this `4×4` matrix, we take a `3×3` filter and place it at the top of the `3×3` region of the input image. Then, we take a product of each corresponding element and add them together as you can see in the formula below.

<p align="center"><img src="http://media5.datahacker.rs/2020/11/movie1-1-5.gif"/></p>

So, after evaluating the first expression we obtained the result of -5. This will be a pixel value at the top left corner in the output image. Then we move our filter across the overall image an create an output image . Notice that our filter is a matrix with the same height and width (3×3, 5×5, 9×9). There is a very good reason for that. We always use an odd number because we need a pixel at the center of this matrix.

**NOTE :** 

```
Input image size and output image size is different, the information on the borders of images are not preserved. To overcome these problems, we use padding.
```
if we not apply padding on the input image, then there will be 2 downside

- Shrinking outputs
- Loosing information on corners of the image

### **What is padding ?**

Padding is simply a process of adding layers of zeros to our input images so as to avoid the problems mentioned above.

<p align="center"><img src="https://media.geeksforgeeks.org/wp-content/uploads/20190721014439/Screenshot-2019-07-21-at-1.43.59-AM.png" width="300px"></p>

This increases the contribution of the pixels at the border of the original image by bringing them into the middle of the padded image. Thus, information on the borders is preserved as well as the information in the middle of the image.

**Example 01** : Input and output image size is preserved. 

<p align="center"><img src="https://miro.medium.com/max/790/1*1okwhewf5KCtIPaFib4XaA.gif"></p>


**Example 02** : Performing filtering operation on padded input image (ignore the kernel (aka filtering matrix) for now, which is laplacian kernel use for detecting edges, will discuss that later). 

<p align="center"><img src="http://www.michaelfxu.com/assets/gifs/neural_networks/cnn_convolve_with_padding.gif"></p>

**Example 03** : Performing filtering on RGB image 

<p align="center"><img src="https://predictiveprogrammer.com/wp-content/uploads/2018/06/convolve.gif"></p>


So, we have reminded ourselves how to apply a convolution on images. In a process of convolution we can use a variety of filters. By using different filter coefficients we perform blurring, sharpening and other image processing effects.

## **How to smooth an image in OpenCV?**

Let’s see how we can smooth or blur an image. Now, you may ask yourself “Why do I have to blur my image”? Well, while blurring may be undesirable in the pictures, it will be quite useful later when we start to work with more advanced OpenCV functions. For instance it is used in image thresholding and edge detection. In addition, these blurring techniques are commonly used to reduce noise, and we can also apply them to reduce the pixelated effect in 
low-resolution images.


Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. It actually removes high frequency content (eg: noise, edges) from the image. **`So edges are blurred a little bit in this operation (there are also blurring techniques which don't blur the edges).`** OpenCV provides four main types of blurring techniques.

OpenCV provides a large number of different types of blurring methods. So, let’s explore some of them.

## **2D Convolution ( Image Filtering )**

As in one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. LPF helps in removing noise, blurring images, etc. HPF filters help in finding edges in images.

OpenCV provides a function **`cv2.filter2D()`** to convolve a kernel with an image. As an example, we will try an averaging filter on an image. A 5x5 averaging filter kernel will look like the below:

<p align="center"><img src="https://i.stack.imgur.com/TRAtW.png"</p>

The operation works like this: keep this kernel above a pixel, add all the 25 pixels below this kernel, take the average, and replace the central pixel with the new average value. 

## **Averaging/Mean filter - Linear filter**

In the picture below we can see that the input image on the left is processed with the averaging filter (box filter). Here, all the coefficient values have the same value of 1/9. After we have applied convolution operator, we have generated our output image on the right. It is good to know that as a filter size increases our image will become more blurred.

<p align="center"><img src="http://media5.datahacker.rs/2019/05/96-1024x631.png"></p>

It simply takes the average of all the pixels under the kernel area and replaces the central element. This is done by the function **`cv2.blur()`** or **`cv2.boxFilter()`**. Check the docs for more details about the kernel. We should specify the width and height of the kernel. A 3x3 normalized box filter would look like the below:

<p align="center"><img src="https://hub.packtpub.com/wp-content/uploads/2018/04/image6-4.png"></p>


To perform averaging in OpenCV we use both **`cv2.blur()`** and **`cv2.boxFilter()`** functions. There are only two arguments required: an image that we want to blur and the size of the filter. We have chosen three different sizes for the filter to demonstrate that the output image will become more blurred as the filter size increases.

**Note**
```
If you don't want to use a normalized box filter, use cv.boxFilter(). Pass an argument normalize=False to the function.
```

**`Example 01`**

<p align="center"><img src="https://docs.opencv.org/master/filter.jpg"></p>

**`Example 02`**

<p align="center"><img src="http://media5.datahacker.rs/2020/05/download9-1024x341.png"></p>



As we can see our output images are quite blurred. However, there are some problems with that. When we want to smooth an image our goal is to remove noise, but we want to preserve smooth behavior of our edges in the image. However, we can see that the Averaging filter gives rather poor blurring result. This is due to the fact that all pixel within a filter matrix have the same coefficients. We will see that a better result will be obtained with the Gaussian filter where more emphasis is a given to the central area. On the other hand, the peripheral pixels have relatively smaller impact on the filtering with a Gaussian matrix.

## **Gaussian filter**

Apart from the averaging filter we can use several other common filters to perform image blurring. Now we are going to explore a slightly more complicated filter. It is the most commonly used kernel in image processing and it is called the Gaussian filter. For the creation of this filter we use the famous Gaussian function. This function represents the probability that events are centered around the mean value. Furthermore, the standard deviation (σ) of this function controls how wide this distribution would be. By sampling this function values we will get  coefficients for a Gaussian filter matrix. Effect of different (σ) values can be observed in the following image.

<p align="center"><img src="http://media5.datahacker.rs/2020/05/image5.png"></p>

In the image below we can see a 2D Gaussian distribution. Now, when you look at it in 3D, it becomes more obvious how the coefficient values are generated.

<p align="center"><img src="https://3.bp.blogspot.com/-cVNi7VZLB_A/V3WTNVSHSqI/AAAAAAAAAuY/J1SN00PpFGoYWgKLKo-Pa_UozqZXmDb4ACLcB/s1600/GaussianKernel.png"></p>


<p align="center"><img src="http://media5.datahacker.rs/2019/05/gaussian_2d-1-768x634.png"></p>


<p align="center"><img src="http://media5.datahacker.rs/2020/04/OIWce-768x576.png"></p>

Now, when we know what is a Gaussian distribution we can focus on our code. Here, we will use a function **`cv2.GaussianBlur()`**. Similarly to a averaging filter, we provide a tuple that represents our filter size. This is how our 3×3 filter looks like:

<p align="center"><img src="http://media5.datahacker.rs/2020/04/24-768x639.jpg"></p>

We should specify the **`width`** and **`height`** of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions i.e. **`σx – standard deviation`** (sigmaX) and **`σy – standard deviation`** (sigmaY) respectively. 

- If only sigmaX is specified, sigmaY is taken as the same as sigmaX. 
- If both are given as zeros, they are calculated from the kernel size. 

Gaussian blurring is highly effective in removing Gaussian noise from an image.

If you want, you can create a Gaussian kernel with the function, [cv.getGaussianKernel()](https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gac05a120c1ae92a6060dd0db190a61afa).

The above code can be modified for Gaussian blurring:

```py
blur = cv.GaussianBlur(img,(5,5),0)
```
<p align="center"><img src="http://media5.datahacker.rs/2019/05/Featured-Image-005-Averaging.png"></p>

## Reference 

- [Smoothing in Digital Image Processing - Pallavi Agarwal](https://www.slideshare.net/hiiampallavi15/smoothing-in-digital-image-processing)

- [](http://datahacker.rs/004-how-to-smooth-and-sharpen-an-image-in-opencv/)

- [](https://www.geeksforgeeks.org/cnn-introduction-to-padding/)

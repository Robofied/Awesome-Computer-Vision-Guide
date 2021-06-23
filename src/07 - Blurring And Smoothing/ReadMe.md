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
Input image size and output image size is different, the information on the borders of images are not preserved. 
To overcome these problems, we use padding.
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

## **Linear filtering**

The simplest filter is a point operator. Each pixel value is multiplied by a scalar value. This operation can be written as follows:

<p align="center"><img src="https://hub.packtpub.com/wp-content/uploads/2018/04/image19.png"></p>

Here:

- The input image is F and the value of pixel at (i,j) is denoted as f(i,j)
- The output image is G and the value of pixel at (i,j) is denoted as g(i,j)
- K is scalar constant

This type of operation on an image is what is known as a linear filter. In addition to multiplication by a scalar value, each pixel can also be increased or decreased by a constant value. So overall point operation can be written like this:

<p align="center"><img src="https://hub.packtpub.com/wp-content/uploads/2018/04/image15.png"></p>

This operation can be applied both to grayscale images and RGB images. For RGB images, each channel will be modified with this operation separately. The following is the result of varying both **`K`** and **`L`**. 

- The first image is input on the left. 
- In the second image, **`K=0.5`** and **`L=0.0`**, 
- while in the third image, **`K`** is set to **`1.0`** and **`L`** is **`10`**. 
- For the final image on the right, **`K=0.7`** and **`L=25`** . As you can see, varying K changes the brightness of the image and varying L changes the contrast of the image:

<p align="center"><img src="https://hub.packtpub.com/wp-content/uploads/2018/04/image5-4.png"></p>


## **2D Convolution ( Image Filtering )**

As in one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. LPF helps in removing noise, blurring images, etc. HPF filters help in finding edges in images.

OpenCV provides a function **`cv2.filter2D()`** to convolve a kernel with an image. As an example, we will try an averaging filter on an image. A 5x5 averaging filter kernel will look like the below:

<p align="center"><img src="https://i.stack.imgur.com/TRAtW.png"</p>

The operation works like this: keep this kernel above a pixel, add all the 25 pixels below this kernel, take the average, and replace the central pixel with the new average value. 

## **How to apply padding in image using OpenCV ?**

We learned to use convolution to operate on images. One problem that naturally arises is how to handle the boundaries. 

**`Important Question`** : How can we convolve them if the evaluated points are at the edge of the image?

For example, if you want to smooth an image using a **`Gaussian 3×3 filter`**, then, when processing the left-most pixels in each row, you need pixels to the left of them, that is, outside of the image. You can let these pixels be the same as the left-most image pixels ("replicated border" extrapolation method), or assume that all the non-existing pixels are zeros ("constant border" extrapolation method), and so on. OpenCV enables you to specify the extrapolation method. For details, see [BorderTypes](https://docs.opencv.org/master/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5)

What most of OpenCV functions do is to copy a given image onto another slightly larger image and then automatically pads the boundary. This way, the convolution can be performed over the needed pixels without problems (the extra padding is cut after the operation is done).

In this tutorial, we will briefly explore two ways of defining the extra padding (border) for an image:

- **`BORDER_CONSTANT`** : Pad the image with a constant value (i.e. black or 0)

- **`BORDER_REPLICATE`** : The row or column at the very edge of the original is replicated to the extra border. 

This will be seen more clearly in the Code section.
## **Averaging/Mean filter - Linear filter**

In the picture below we can see that the input image on the left is processed with the averaging filter (box filter). Here, all the coefficient values have the same value of 1/9. After we have applied convolution operator, we have generated our output image on the right. It is good to know that as a filter size increases our image will become more blurred.

<p align="center"><img src="http://media5.datahacker.rs/2019/05/96-1024x631.png"></p>

Now, as the filter **`H(u,v)`** is being moved around the image **`F(x,y)`**, the new image **`G(x,y)`** on the right is generated.

It simply takes the average of all the pixels under the kernel area and replaces the central element. This is done by the function **`cv2.blur()`** or **`cv2.boxFilter()`**. Check the docs for more details about the kernel. We should specify the width and height of the kernel. A 3x3 normalized box filter would look like the below:

<p align="center"><img src="https://hub.packtpub.com/wp-content/uploads/2018/04/image6-4.png"></p>

The idea of mean filtering is simply to replace each pixel value in an image with the **`mean(average)`** value of its neighbors, including itself. This has the effect of eliminating pixel values which are unrepresentative of their surroundings. Mean filtering is usually thought of as a **`convolution`** filter. Like other convolutions it is based around a kernel, which represents the shape and size of the neighborhood to be sampled when calculating the mean. Often a `3×3` square kernel is used, although larger kernels (e.g. `5×5` squares) can be used for more severe smoothing. 

**`NOTE`**

That a small kernel can be applied more than once in order to produce a similar but not identical effect as a single pass with a large kernel.

To perform averaging in OpenCV we use both **`cv2.blur()`** and **`cv2.boxFilter()`** functions. There are only two arguments required: an image that we want to blur and the size of the filter. We have chosen three different sizes for the filter to demonstrate that the output image will become more blurred as the filter size increases.

**Note**
```
If you don't want to use a normalized box filter, use cv2.boxFilter(). Pass an argument normalize=False to the function.
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

<p align="center"><img src="https://3.bp.blogspot.com/-cVNi7VZLB_A/V3WTNVSHSqI/AAAAAAAAAuY/J1SN00PpFGoYWgKLKo-Pa_UozqZXmDb4ACLcB/s1600/GaussianKernel.png" width="300px"></p>

where **`x`** and **`y`** are the respective distances to the horizontal and vertical center of the kernel and **`sigma`** is the standard deviation of the Gaussian kernel.


<p align="center"><img src="http://media5.datahacker.rs/2019/05/gaussian_2d-1-768x634.png" width="400px"></p>


<p align="center"><img src="http://media5.datahacker.rs/2020/04/OIWce-768x576.png" width="400px"></p>

```
Effect of gaussian on varying sigma 
```

<p align="center"><img src="https://i.ibb.co/HHLFQsf/gauss.jpg" alt="gauss" border="0" width="500px"></p>

Now, when we know what is a Gaussian distribution we can focus on our code. Here, we will use a function **`cv2.GaussianBlur()`**. Similarly to a averaging filter, we provide a tuple that represents our filter size. This is how our 3×3 filter looks like:

<p align="center"><img src="http://media5.datahacker.rs/2020/04/24-768x639.jpg" width="300px"></p>

We should specify the **`width`** and **`height`** of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions i.e. **`σx – standard deviation`** (sigmaX) and **`σy – standard deviation`** (sigmaY) respectively. 

- If only sigmaX is specified, sigmaY is taken as the same as sigmaX. 
- If both are given as zeros, they are calculated from the kernel size. 

Gaussian blurring is highly effective in removing Gaussian noise from an image.

If you want, you can create a Gaussian kernel with the function, [cv2.getGaussianKernel()](https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gac05a120c1ae92a6060dd0db190a61afa).

The above code can be modified for Gaussian blurring:

```py
blur = cv2.GaussianBlur(img,(5,5),0)
```
<p align="center"><img src="http://media5.datahacker.rs/2019/05/Featured-Image-005-Averaging.png" width="500px"></p>

<p align="center"><img src="http://media5.datahacker.rs/2020/05/download10-1024x341.png"></p>


As you can see our image filtered with Gaussian filter is less, but more naturally blurred. Why? Because all pixels in the kernel neighborhood of an averaging filter have equal weight. On the other hand, in Gaussian filter there are higher values at center pixels and the lower values in pixels moving away from the center. That is why with Gaussian filter we preserve edges which will appear sharper in our output image.

## **Median filter - Non linear filter**

Traditionally, the median blur method has been most effective when removing salt-and-pepper noise. This type of noise is exactly what it sounds like: imagine taking a photograph, putting it on your dining room table, and sprinkling salt and pepper on top of it. Using the median blur method, you could remove the salt and pepper from your image.

Median filtering is a **`nonlinear operation`** often used in image processing to reduce "salt and pepper" noise.

<p align="center"><img src="https://i.ibb.co/Jm1TJ5j/Salt-and-papper-noise.jpg" alt="Salt-and-papper-noise" border="0"></p>

Here, the function **`cv2.medianBlur()`** takes the median of all the pixels under the kernel area and the central element is replaced with this median value. This is highly effective against salt-and-pepper noise in an image. Interestingly, in the above filters, the central element is a newly calculated value which may be a pixel value in the image or a new value. But in median blurring, the central element is always replaced by some pixel value in the image. It reduces the noise effectively. Its kernel size should be a positive odd integer.

When applying a median blur, we first define our kernel size. Then, as in the averaging blurring method, we consider all pixels in the neighborhood of size **`K x K`** where K is an odd integer.

<p align="center"><img src="https://i.ibb.co/Hn0f6YL/Median-filter.jpg" alt="Median-filter" border="0"></p>

Notice how, unlike average blurring and Gaussian blurring where the kernel size could be rectangular ([Read in docs](https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1)), the kernel size for the median must be square. Furthermore (unlike the averaging method), instead of replacing the central pixel with the average of the neighborhood, we instead replace the central pixel with the median of the neighborhood.

<p align="center"><img src="http://1.bp.blogspot.com/--O0Fm6ggZqY/VYsc_mBsqnI/AAAAAAAAA38/mNTJ2kJRSyU/s1600/content_08.png"></p>

The reason median blurring is more effective at removing salt-and-pepper style noise from an image is that each central pixel is always replaced with a pixel intensity that exists in the image. And since the median is robust to outliers, the salt-and-pepper noise will be less influential to the median than another statistical method, such as the average.

Again, methods such as averaging and Gaussian compute means or weighted means for the neighborhood — this average pixel intensity may or may not be present in the neighborhood. But by definition, the median pixel must exist in our neighborhood. By replacing our central pixel with a median rather than an average, we can substantially reduce noise.

We use the function: [**`cv2.medianBlur (src, dst, ksize)`**](https://docs.opencv.org/3.4/dd/d6a/tutorial_js_filtering.html)

**NOTE**

The median filter uses [**`cv2.BORDER_REPLICATE`**](https://docs.opencv.org/3.4/d2/de8/group__core__array.html#gga209f2f4869e304c82d07739337eae7c5aa1de4cff95e3377d6d0cbe7569bd4e9f) internally to cope with border pixels.

The median blur is by no means a **`“natural blur”`** like Gaussian smoothing. However, for damaged images or photos captured under highly suboptimal conditions, a median blur can really help as a pre-processing step prior to passing the image along to other methods, such as thresholding and edge detection

## **Bilateral Filtering**

[**`cv2.bilateralFilter()`**](https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed) is highly effective in noise removal while keeping edges sharp. But the operation is slower compared to other filters. We already saw that gaussian filter takes the a neighbourhood around the pixel and find its gaussian weighted average. This gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. It doesn't consider whether pixels have almost same intensity. It doesn't consider whether pixel is an edge pixel or not. So it blurs the edges also, which we don't want to do.

<p align="center"><img src="https://i.ibb.co/0CszTRf/Screenshot-2751.png" alt="Screenshot-2751" border="0" width="700px"></p>

Bilateral filter also takes a gaussian filter in space, but one more gaussian filter which is a function of pixel difference. Gaussian function of space make sure only nearby pixels are considered for blurring while gaussian function of intensity difference make sure only those pixels with similar intensity to central pixel is considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.

We use the function: [**`cv2.bilateralFilter(src, dst, d, sigmaColor, sigmaSpace, borderType = cv.BORDER_DEFAULT)`**](https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#ga9d7064d478c95d60003cf839430737ed)

**`Sigma values`**: For simplicity, you can set the 2 sigma values to be the same. If they are small (< 10), the filter will not have much effect, whereas if they are large (> 150), they will have a very strong effect, making the image look "cartoonish".

**`Filter size`**: Large filters (d > 5) are very slow, so it is recommended to use d=5 for real-time applications, and perhaps d=9 for offline applications that need heavy noise filtering.

**Bilateral filtering example**

<p align="center"><img src="http://xidexia.github.io/Bilateral-Filtering/img/cat_compare.png" width="400px"></p>

<p align="center"><img src="https://i.ibb.co/CPNDPzB/bilateral-filter.png" alt="bilateral-filter" border="0"></p>

**`Figure 5 (c)`** shows the result of five iterations of bilateral filtering of the image in **`figure 5 (a)`**. While a single iteration produces a much cleaner image (**`figure 5 (b)`**) than the original, and is probably sufficient for most image processing needs, multiple iterations have the effect of flattening the colors in an image considerably, but without blurring edges. The resulting image has a much smaller color map, and the effects of bilateral filtering are easier to see when displayed on a printed page. Notice the cartoon-like appearance of **`figure 5 (c)`**. All shadows and edges are preserved, but most of the shading is gone, and no "new" colors are introduced by filtering.

## Reference 

- [Smoothing in Digital Image Processing - Pallavi Agarwal](https://www.slideshare.net/hiiampallavi15/smoothing-in-digital-image-processing)

- [How to smooth and sharpen an image in opencv - Datahacker](http://datahacker.rs/004-how-to-smooth-and-sharpen-an-image-in-opencv/)


- [C. Tomasi and R. Manduchi, "Bilateral Filtering for Gray and Color Images"](https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html)

- [Filtering tutorial - OpenCV Officially Documentation](https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html)

- [OpenCV smoothing and blurring - Pyimagesearch (Adrian Rosebrock)](https://www.pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring/)

- [Mean Filter - homepages.inf.ed.ac.uk](https://homepages.inf.ed.ac.uk/rbf/HIPR2/mean.htm)


- [Introduction to padding - geeksforgeeks](https://www.geeksforgeeks.org/cnn-introduction-to-padding/)

- [Matlab Tutorial Digital Image Processing Filter_Smoothing - bogotobogo](https://www.bogotobogo.com/Matlab/Matlab_Tutorial_Digital_Image_Processing_6_Filter_Smoothing_Low_Pass_fspecial_filter2.php)

- [Image Filtering - AI Stanford](https://ai.stanford.edu/~syyeung/cvweb/tutorial1.html)

- [image filtering techniques opencv - Hub Packtpub](https://hub.packtpub.com/image-filtering-techniques-opencv/)
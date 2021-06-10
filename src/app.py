# --------------------------#
# Author : Hritik Jaiswal
# Github : https://github.com/hritik5102
# Repository : https://github.com/Robofied/Awesome-Computer-Vision-Guide
# --------------------------#

# To save your changes, copy your custom theme into the clipboard and paste it into the[theme] section of your .streamlit/config.toml file.
# [theme]
# primaryColor="#f63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#f0f2f6"
# textColor="#262730"
# font="sans serif"


# Import package
import base64
import streamlit as st
import pandas as pd
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

st.set_page_config(
    layout="wide", page_title='Awesome Computer vision Repository')


def main():

    # list of folder name
    list_of_folder_name = [i for i in os.listdir('./')]

    # split folder names into num and names
    spliter = [i.split(" - ") for i in list_of_folder_name]
    nums, name = [], []

    # collect number is one list and name in others
    for i in range(len(spliter)):
        if len(spliter[i]) == 1:
            continue
        nums.append(spliter[i][0])
        name.append(spliter[i][1])

    # concatenate welcome in list of folders name
    list_of_folder_name = ["Welcome"] + list_of_folder_name

    st.sidebar.title("Content")
    selected_box = st.sidebar.selectbox(
        "Choose one of the following",
        list_of_folder_name[:-2]
    )

    if selected_box == list_of_folder_name[0]:
        welcome(nums, name)
    if selected_box == list_of_folder_name[1]:
        image_01()
    if selected_box == list_of_folder_name[2]:
        video_02()
    if selected_box == list_of_folder_name[3]:
        matplotlib_03()
    if selected_box == list_of_folder_name[4]:
        drawing_function_04()


def welcome(nums, name):
    st.image('Images and Videos/Robofied.png', use_column_width=True)
    st.markdown('''
    # Computer Vision Tutorials &nbsp; ![](https://img.shields.io/github/forks/Robofied/Awesome-Computer-Vision-Guide?style=social) ![](https://img.shields.io/github/stars/Robofied/Awesome-Computer-Vision-Guide?style=social) ![](https://img.shields.io/github/watchers/Robofied/Awesome-Computer-Vision-Guide?style=social)

    ![](https://img.shields.io/github/repo-size/Robofied/Awesome-Computer-Vision-Guide) ![](https://img.shields.io/github/license/Robofied/Awesome-Computer-Vision-Guide?color=red)    [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Robofied/Awesome-Computer-Vision-Guide)
    ![](https://img.shields.io/github/issues/Robofied/Awesome-Computer-Vision-Guide?color=green) ![](https://img.shields.io/github/issues-pr/Robofied/Awesome-Computer-Vision-Guide?color=green) ![](https://img.shields.io/github/downloads/Robofied/Awesome-Computer-Vision-Guide/total) ![](https://img.shields.io/github/last-commit/Robofied/Awesome-Computer-Vision-Guide) ![](https://img.shields.io/github/contributors/Robofied/Awesome-Computer-Vision-Guide)

    Computer Vision is one of the hottest topics in artificial intelligence. It is making tremendous advances in self-driving cars, robotics as well as in various photo correction apps. Steady progress in object detection is being made every day. GANs is also a thing researchers are putting their eyes on these days. Vision is showing us the future of technology and we can’t even imagine what will be the end of its possibilities.

    So do you want to take your first step in Computer Vision and participate in this latest movement? Welcome you are at the right place. From this article, we’re going to have a series of tutorials on the basics of image processing and object detection. This is the first part of OpenCV tutorial for beginners and the complete set of the series is as follows:

    # Clone git repository

    ```sh
        $ git clone "https://github.com/Robofied/Awesome-Computer-Vision-Guide"
    ```

    You can run and edit the algorithms or contribute to them using [Gitpod.io](https://www.gitpod.io/), a free online development environment, with a single click.

    [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](http://gitpod.io/#https://github.com/Robofied/Awesome-Computer-Vision-Guide)

    ''')

    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Content</h2>
    </div>
    <hr/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    code_link = ["[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/01%20-%20Image)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/02%20-%20Video)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/03%20-%20Matplotlib)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/04%20-%20Drawing%20Shapes)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/05%20-%20Masking)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/06%20-%20Trackbar)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/07%20-%20Blurring%20And%20Smoothing)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/08%20-%20Morphological_Transformation)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/09%20-%20Thresholding)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/10%20-%20Adaptive%20thresolding)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/11%20-%20Otsu%20thresolding)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/12%20-%20Transformation)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/13%20-%20Callbacks)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/14%20-%20Canny%20edge%20detection)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/15%20-%20Sobel%20and%20Laplacian%20Operation)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/16%20-%20Gradient)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/17%20-%20Histogram)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/18%20-%20Hough%20Line)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/19%20-%20Fourier%20transform)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/20%20-%20Contour)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/21%20-%203d%20map)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/22%20-%20Background-filter)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/23%20-%20Corner%20detection)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/24%20-%20Gamma%20Correction)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/25%20-%20Stereo_blend_2_Camera)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/26%20-%20Template%20Matching)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/27%20-%20Haar%20Cascade)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/28%20-%20Color%20tracking)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/29%20-%20Mouse%20Movement)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/30%20-%20Color%20Detection)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/31%20-%20Jack_in_the_box)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/32%20-%20Lane%20detection)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/33%20-%20Pillow%20Library)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/34%20-%20Digital%20Negative%20and%20Gray%20level%20slicing)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/35%20-%20Intensity%20transformation)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/36%20-%20Histogram%20Equalization)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/38%20-%20Image%20Registration%20Using%20Homography)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/39%20-%20Convert%20URL%20to%20image)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/40%20-%20OpenCV%20In%20Colab)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/41%20-%20Word%20Detection)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/42%20-%20Mixing%202%20Frames)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/43%20-%20Color_Slicing)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/44%20-%20Camera%20Calibration)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/45%20-%20Align_images)"
                 ]

    # code_link = [st.markdown(link) for link in code_link]
    print(len(code_link), len(name))
    left, center, right = st.beta_columns((1, 2, 1))

    with left:
        left.markdown('''**No.** ''', unsafe_allow_html=True)
        for i in nums:
            left.write(i)
    with center:
        center.markdown('''**Discription**''', unsafe_allow_html=True)
        for i in name:
            center.write(i)
    with right:
        right.markdown('''**Code**''', unsafe_allow_html=True)
        for link in code_link:
            right.markdown(link, unsafe_allow_html=True)

    st.markdown('''
        # License

    Licensed under the [MIT License](LICENSE)

    # Contributing to Awesome Computer Vision Guide

    All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

    A detailed overview on how to contribute can be found in the contributing guide. There is also an overview on GitHub.

    If you are simply looking to start working with the voicenet codebase, navigate to the GitHub "issues" tab and start looking through interesting issues. There are a number of issues listed under Docs and good first issue where you could start out.

    You can also triage issues which may include reproducing bug reports, or asking for vital information such as version numbers or reproduction instructions.

    Or maybe through using you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’. You can do something about it!

    Feel free to ask questions on the mailing list or on Slack.

    # Contributor
    ''')
    html_temp = """

    |                                                                                                                                                                                                                   <a href="https://hritik5102.github.io/"><img src="https://avatars.githubusercontent.com/hritik5102" width="150px" height="150px" /></a>                                                                                                                                                                                                                    |
    | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
    |                                                                                                                                                                                                                                                             **[Hritik Jaiswal](https://linktr.ee/hritikdj)**                                                                                                                                                                                                                                                              |
    | <a href="https://twitter.com/imhritik_dj"><img src="https://i.ibb.co/kmgQVyW/twitter.png" width="32px" height="32px"></a> <a href="https://github.com/hritik5102"><img src="https://cdn.iconscout.com/icon/free/png-256/github-108-438008.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/hritik.jaiswal.56808"><img src="https://i.ibb.co/zmYNW4p/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/hritik-jaiswal-22a136166/"><img src="https://i.ibb.co/Kx2GSrT/linkedin.png" width="32px" height="32px"></a> |
    """
    st.markdown(html_temp, unsafe_allow_html=True)



def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a style="background-color:#00C4EB;border-radius:5px;box-shadow: 0 5px 0 rgb(0, 116, 191);color: #FFFFFF;padding: 1em 1.5em;position: relative;text-decoration: none;font-weight:bold;cursor: pointer;" href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download  {file_label}  📃</a>'
    return href


def image_01():
    html_temp = """
    <div>
        <h2 style="text-align:center;font-weight:bold">Image processing using OpenCV and Python</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Reading an image</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    # st.header("Reading an image")

    # st.header("Files uploader")
    # image = st.file_uploader("Upload a file")
    # uploaded_file = st.file_uploader(
    #     "Choose an image...", type=['png', 'jpeg', 'jpg'])

    # if uploaded_file:
    #     file_details = {"FileName": uploaded_file.name,
    #                     "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    #     st.write(file_details)

    #     image = Image.open(uploaded_file)
    #     # Read an image
    #     img = cv2.imread(image)

    #     # Convert RGB to Grayscale
    #     gray = cv2.imread(image, 0)
    # else:
    #     st.error('Please upload a valid image file!!!')

    # Read an image
    img = cv2.imread('Images and Videos/dog.png')

    # Convert RGB to Grayscale
    gray = cv2.imread('Images and Videos/dog.png', 0)

    st.markdown('''
      When the image file is read with the OpenCV function ```imread()```, the order of colors is ```BGR (blue, green, red)```.
      On the other hand, in Pillow, the order of colors is assumed to be ```RGB (red, green, blue)```.

      When reading a color image file, OpenCV ```imread()``` reads as a NumPy array ndarray of row ```(height) x column (width) x color (3)```.
      The order of color is ```BGR (blue, green, red)```.
      ''', unsafe_allow_html=True)

    st.code('''img = cv2.imread('../Images and Videos/dog.png')''',
            language='javascript')

    st.markdown('''The OpenCV function ```imwrite()``` that saves an image assumes that the order of colors is BGR, so it is saved as a correct image.''', unsafe_allow_html=True)

    code = '''cv2.imwrite('Save_Dog.png', img)'''
    st.code(code, language='javascript')

    st.markdown('''Convert RGB to Grayscale(1 Channel)''',
                unsafe_allow_html=True)
    code = '''gray = cv2.imread('../Images and Videos/dog.png', 0)'''
    st.code(code, language='javascript')

    st.markdown(
        '''But when displaying the image, it show the image as RGB image instead BGR''', unsafe_allow_html=True)
    code = '''cv2.imshow('BGR_Image', img)'''
    st.code(code, language='javascript')

    if st.button('See Original Image'):
        original = Image.open('Images and Videos/dog.png')
        placeholder = st.image(original, use_column_width=True)
        if st.button("Hide original image"):
            placeholder.empty()

    left, center, right = st.beta_columns(3)

    with left:
        html_temp = """
        <h2 style="text-align:center;font-weight:bold">BGR Image</h2>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.image(img, width=500, use_column_width=True)

    with center:
        html_temp = """
        <h2 style="text-align:center;font-weight:bold">RGB Image</h2>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
                 width=500, use_column_width=True)

    with right:
        html_temp = """
        <h2 style="text-align:center;font-weight:bold">Grayscale Image</h2>
        """
        st.markdown(html_temp, unsafe_allow_html=True)

        st.image(gray, width=500, use_column_width=True)

    # parameters
    #   1. Shape - Height, Width, Color
    #   2. dtype - type

    st.success(f'Shape of the Original image: {img.shape}')
    st.success(f'Shape of the Grayscale image: {gray.shape}')
    st.success(f'dtype of the image: {img.dtype}')
    st.success(f'type of the image: {type(img)}')
    st.markdown('''---''')

    left, center, right = st.beta_columns(3)
    with left:
        left.markdown(get_binary_file_downloader_html(
            '01 - Image/01-image_Processing.py', 'python file - 01'), unsafe_allow_html=True)
    with center:
        center.markdown(get_binary_file_downloader_html(
            '01 - Image/02-image_Processing.py', 'python file - 02'), unsafe_allow_html=True)

# ffmpeg -i Original_frame.avi -vcodec libx264 flip_frame.mp4

def video_02():
    html_temp = """
    <div>
        <h2 style="text-align:center;font-weight:bold">Image processing using OpenCV and Python</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Capturing a video from a webcam or from video file</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header("Original frame")
    video_file = open('02 - Video/demo_output.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4', start_time=0)

    st.header("Hue saturation value - HSV")
    video_file = open('02 - Video/hsv.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4', start_time=0)

    st.header("Blue color detected")
    video_file = open('02 - Video/res.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4', start_time=0)

    st.header("Flip Operation")
    video_file = open('02 - Video/flip_frame.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, format='video/mp4', start_time=0)

def matplotlib_03():
    
    html_temp = """
    <div>
        <h2 style="text-align:center;font-weight:bold">Image processing using OpenCV and Python</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Exploring Image operation in Matplotlib</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    html_temp = """
                <h2 style="font-weight:bold">Display a sample image using Matplotlib</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_1.png', use_column_width=True)
    
    html_temp = """
                <h2 style="font-weight:bold">Annotate image using Matplotlib</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    # with st.beta_expander("🧙 Click here to view the image 🔮"):
    st.image('03 - Matplotlib/Figure_2.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Display a Grayscale image using Matplotlib</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_3.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Display a Digital negative image using Matplotlib</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_4.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Display an 24-bit RGB image</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_6.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Display individual 8bit (Red, Green, Blue) image</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_6.png', width=400, use_column_width=True)


    html_temp = """
                <h2 style="font-weight:bold">Display image when Colormap is set to "hot"</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_7.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Display image when Colormap is set to "nipy_spectral"</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_8.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Color scale reference</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_9.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Histogram plot - To Define the thresold</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_10.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Original image Vs Contrast enhanced image</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_11.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Expand contrast by cliping upper end of histogram</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_12.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Interpolation = "bilinear"[pixelated]</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_13.png', width=400, use_column_width=True)

    html_temp = """
                <h2 style="font-weight:bold">Interpolation = "nearest"</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.image('03 - Matplotlib/Figure_14.png', width=400, use_column_width=True)
    html_temp = """
                <h2 style="font-weight:bold">Interpolation = "bicubic"</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('03 - Matplotlib/Figure_15.png', width=400, use_column_width=True)


def drawing_function_04():
    html_temp = """
    <div>
        <h2 style="text-align:center;font-weight:bold">Image processing using OpenCV and Python</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:#02203c;padding:10px">
    <h2 style="color:white;text-align:center;font-weight:bold">Exploring Drawing function in OpenCV</h2>
    </div>
    <br/><br/>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    html_temp = """
                <h2 style="font-weight:bold">Draw a line</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_1.png', width=500)
    
    html_temp = """
                <h2 style="font-weight:bold">Draw a rectangle</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    # with st.beta_expander("🧙 Click here to view the image 🔮"):
    st.image('04 - Drawing Shapes/Figure_2.png', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Fill the rectangle</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_3.png', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Draw a circle</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_4.png', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Draw a ellipse</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_6.png', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Draw a polygon</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_6.png', width=500)


    html_temp = """
                <h2 style="font-weight:bold">Original image for testing</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('Images and Videos/image8.jpg', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Draw a line on an image</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_7.png', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Draw a Rectangle on an image</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_8.png', width=500)

    html_temp = """
                <h2 style="font-weight:bold">Put a text on an image</h2>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('04 - Drawing Shapes/Figure_9.png', width=500)


if __name__ == '__main__':
    main()

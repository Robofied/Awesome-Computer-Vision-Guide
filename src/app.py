# --------------------------#
# Author : Hritik Jaiswal
# Github : https://github.com/hritik5102
# --------------------------#


# Import package
import streamlit as st
import pandas as pd
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# st.set_page_config(layout="wide", page_title='Computer vision')

st.markdown(
    """ 
<style>
.reportview-container {
background: #4b6cb7;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #182848, #4b6cb7);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #182848, #4b6cb7); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

    color: rgb(255, 255, 255);
</style>
""",
    unsafe_allow_html=True,
)


def main():

    st.sidebar.title("Content")
    selected_box = st.sidebar.selectbox(
        "Choose one of the following",
        ["Welcome", "01 - image", "02-Video", "03- Matplotlib"]
    )

    if selected_box == "Welcome":
        welcome()


def welcome():
    st.image('Images and Videos/Robofied.png', use_column_width=True)
    st.markdown('''
    ## Computer Vision Tutorials &nbsp; ![](https://img.shields.io/github/forks/Robofied/Awesome-Computer-Vision-Guide?style=social) ![](https://img.shields.io/github/stars/Robofied/Awesome-Computer-Vision-Guide?style=social) ![](https://img.shields.io/github/watchers/Robofied/Awesome-Computer-Vision-Guide?style=social) 

![](https://img.shields.io/github/repo-size/Robofied/Awesome-Computer-Vision-Guide) ![](https://img.shields.io/github/license/Robofied/Awesome-Computer-Vision-Guide?color=red)    [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Robofied/Awesome-Computer-Vision-Guide)
![](https://img.shields.io/github/issues/Robofied/Awesome-Computer-Vision-Guide?color=green) ![](https://img.shields.io/github/issues-pr/Robofied/Awesome-Computer-Vision-Guide?color=green) ![](https://img.shields.io/github/downloads/Robofied/Awesome-Computer-Vision-Guide/total) ![](https://img.shields.io/github/last-commit/Robofied/Awesome-Computer-Vision-Guide) ![](https://img.shields.io/github/contributors/Robofied/Awesome-Computer-Vision-Guide)

  Computer Vision is one of the hottest topics in artificial intelligence. It is making tremendous advances in self-driving cars, robotics as well as in various photo correction apps. Steady progress in object detection is being made every day. GANs is also a thing researchers are putting their eyes on these days. Vision is showing us the future of technology and we can’t even imagine what will be the end of its possibilities.

 So do you want to take your first step in Computer Vision and participate in this latest movement? Welcome you are at the right place. From this article, we’re going to have a series of tutorials on the basics of image processing and object detection. This is the first part of OpenCV tutorial for beginners and the complete set of the series is as follows:

## Clone git repository

```sh
    $ git clone "https://github.com/Robofied/Awesome-Computer-Vision-Guide"
```

You can run and edit the algorithms or contribute to them using [Gitpod.io](https://www.gitpod.io/), a free online development environment, with a single click.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](http://gitpod.io/#https://github.com/Robofied/Awesome-Computer-Vision-Guide)

    ''')

    # Store the filename in the list (name)
    st.header("Content")
    res = [i.split(" - ") for i in os.listdir('./')]
    nums, name = [], []
    for i in range(len(res)):
        if len(res[i]) == 1:
            continue
        nums.append(res[i][0])
        name.append(res[i][1])

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
        left.header("No. ")
        for i in nums:
            left.write(i)
    with center:
        center.header("Discription")
        for i in name:
            center.write(i)
    with right:
        right.header("Code")
        for link in code_link:
            right.markdown(link, unsafe_allow_html=True)

    st.markdown('''
    ## License

Licensed under the [MIT License](LICENSE)

## Contributing to Awesome Computer Vision Guide

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

A detailed overview on how to contribute can be found in the contributing guide. There is also an overview on GitHub.

If you are simply looking to start working with the voicenet codebase, navigate to the GitHub "issues" tab and start looking through interesting issues. There are a number of issues listed under Docs and good first issue where you could start out.

You can also triage issues which may include reproducing bug reports, or asking for vital information such as version numbers or reproduction instructions.

Or maybe through using you have an idea of your own or are looking for something in the documentation and thinking ‘this can be improved’. You can do something about it!

Feel free to ask questions on the mailing list or on Slack.

## Contributor

[Hritik Jaiswal](https://hritik5102.github.io)

    ''')
    # dic = {
    #     # "No.": num,
    #     "Discription": name,
    #     "Code": code_link
    # }
    # data = pd.DataFrame.from_dict(dic)
    # data.index = data.index + 1
    # st.table(data)


if __name__ == '__main__':
    main()

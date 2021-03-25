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


def main():
    st.sidebar.title("Content ")
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
    name = []
    for i in range(len(res)):
        if len(res[i]) == 1:
            continue
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
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)",
                 "[![](https://img.shields.io/badge/Code-Python-blue)](https://github.com/Robofied/Awesome-Computer-Vision-Guide/tree/master/src/37%20-%20Cartoon_Effect)"
                 ]

    code_link = [st.markdown(link) for link in code_link]
    print(len(code_link), len(name))
    dic = {
        # "No.": num,
        "Discription": name,
        "Code": code_link
    }
    data = pd.DataFrame.from_dict(dic)
    data.index = data.index + 1
    st.table(data)
    # st.write(data)


if __name__ == '__main__':
    main()

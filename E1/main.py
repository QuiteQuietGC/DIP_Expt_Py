# -*- coding: utf-8 -*-
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 数字图像处理实验1-1
'''
    DIY均值滤波————模版运算,实现均值滤波.
'''
# python & OpenCV  ~> pip3 install opencv-python 🤔️
# 20230719 

import numpy as np
import cv2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 读图
img = cv2.imread('../SomeImg/lena.png',cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

rows,cols = img.shape
print('rows:',rows,'cols:',cols)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 模版
w = np.mat([[1/25,1/25,1/25,1/25,1/25],
            [1/25,1/25,1/25,1/25,1/25],
            [1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]])

w = w.astype(float)

n,n1 = w.shape;     r = (n-1)/2;    r = int(r);

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ data processing
imgInputGrayFloat = img.astype(float)
imgOutput = np.mat(np.zeros((rows,cols)))

# conv conv
for x in range(int(r),int(rows-r)):
    for y in range(int(r),int(cols-r)):
        for s in range(int(-r),int(r)+1):           # s = -2 -1 0 1 2
            for t in range(int(-r),int(r)+1):       # t = -2 -1 0 1 2
                imgOutput[x,y] = round(imgOutput[x,y]+w[s+r,t+r]*imgInputGrayFloat[x+s,y+t])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 输出结果
cv2.namedWindow('imageOutput', cv2.WINDOW_NORMAL)   # 可以调整窗口大小
imgOutput = imgOutput.astype(np.uint8)              # 💡💡🌟🌟 img data 2 uint8
cv2.imshow('imageOutput', imgOutput)                # 窗口会自动调整为图像大小

cv2.namedWindow('imageInput', cv2.WINDOW_NORMAL)    # 可以调整窗口大小
cv2.imshow('imageInput', img)                       # 窗口会自动调整为图像大小

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 实现在窗口上按任意键退出
cv2.waitKey(delay=0)        # 返回按键的ASCII码值
cv2.destroyAllWindows()



# P.s: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# img = cv2.imread('lena.png', cv2.IMREAD_COLOR)        # 透明度会被忽略(默认参数)。
# img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)    # L灰度
# img = cv2.imread('lena.png',cv2.IMREAD_UNCHANGED)     # 含 alpha 通道

# w = [1/9 1/9 1/9;1/9 1/9 1/9;1/9 1/9 1/9;]                <- matlab写法
# w = np.mat('1/9 1/9 1/9;1/9 1/9 1/9;1/9 1/9 1/9');        <- 错误 
# w = np.mat('1 2 3;1 2 3;3 2 1');                          <- 正确 👌

# w = np.mat([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])   <- 正确 👌


# imgOutput[x,y] = round(imgOutput[x,y]+w[s+r,t+r]*imgInputGrayFloat[x+s,y+t])
# == > 
# imgOutput[x,y] = round(imgOutput[x,y]+np.dot(w[s+r,t+r],imgInputGrayFloat[x+s,y+t]))

# img = cv2.resize(img, (256, 256))
# cv2.imwrite('lena.png', img)
# cv2.normalize(img,img,0,255,cv2.NORM_MINMAX)

'''
try: 
    rows,cols,ch = img.shape
    print('行:',rows,'列:',cols,'通道:',ch)
except BaseException as theErr: 
    print("err:",theErr)

try: 
    rows,cols = img.shape
    print('行:',rows,'列:',cols)
except BaseException as theErr: 
    print("err:",theErr)
'''
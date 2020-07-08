# -*- coding: utf-8 -*-

import cv2
import os


def cartoonise(picture_name):

    imgInput_FileName = picture_name
    #imgOutput_FileName = "E:\github\python_toolbox\Picture_turn_into_cartoon" + picture_name
    num_down = 2         #缩减像素采样的数目
    num_bilateral = 7    #定义双边滤波的数目
    img_rgb = cv2.imread(imgInput_FileName)     #读取图片
    #用高斯金字塔降低取样
    img_color = img_rgb
    for _ in range(num_down):
        img_color = cv2.pyrDown(img_color)
    #重复使用小的双边滤波代替一个大的滤波
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7)
    #升采样图片到原始大小
    for _ in range(num_down):
        img_color = cv2.pyrUp(img_color)
    #转换为灰度并且使其产生中等的模糊
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    #检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur,255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=9,
                                     C=2)
    #转换回彩色图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    # 让两张图片格式编程一致
    rows, cols = img_edge.shape[:2]
    img_color = cv2.resize(img_color, (cols, rows), interpolation=cv2.INTER_CUBIC)
    img_cartoon = cv2.bitwise_and(img_color, img_edge)

    cv2.imshow('img_color',img_color)
    cv2.imshow('img_edge',img_edge)
    cv2.imshow('None',img_cartoon)


# ImageList = []  #建立空的List
# #循环读取"D:\pythonpractice\Image"中的文件名
# for filename in os.listdir(r"E:\github\python_toolbox\Picture_turn_into_cartoon\imgs"):
#     ImageList.append(filename)      #将文件名添加到ImageList
# for i in ImageList:   #循环读取ImageList中的文件名，将其进行卡通化处理
#     print("正在卡通化" + i)
#     cartoonise(i)

def main():
    path = r"E:\github\python_toolbox\Picture_turn_into_cartoon\imgs\lzl.jpg"
    cartoonise(path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
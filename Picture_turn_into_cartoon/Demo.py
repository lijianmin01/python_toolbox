import cv2
import numpy as np
"""
    动漫化风格的特点
要想搞清楚怎么变成动漫化风格，首先就要明白动漫和普通照片的区别。主要的区别有三点：
（1）动漫中的细节相对少；
（2）动漫中的边缘轮廓更突出；
（3）动漫的色彩更鲜艳（相对于普通的、未经PS的照片）；
"""

# 将图片转成素描图片
def rgb_to_sketch(src_image):
    img_rgb = cv2.imread(src_image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
    img_blend = cv2.divide(img_gray, img_blur, scale=255)
    #cv2.imwrite(dst_image, img_blend)

    # # 转换回RGB三通道，方便与img_color进行与操作
    imgContour = cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)
    #cv2.imshow('None',imgContour)
    return imgContour


# 减少细节
def Begin_Cartton(path,picture_name=None):
    dowmsampleNum = 2 # 金字塔下采样的次数
    bilateralNum = 11 # 不断的双边滤波的次数
    img = cv2.imread(path)
    shape = tuple(list(((i//4)*4 for i in img.shape))[:2])[::-1]
    img = cv2.resize(img,dsize=shape)
    imgColor = img
    # 通过不断的双边滤波来降低色彩的数量
    for i in range(dowmsampleNum):
        # 进行金字塔采样降低分辨率
        imgColor = cv2.pyrDown(imgColor)
    for i in range(bilateralNum):
        # 利用较小的核不断进行双边滤波，减少图片样色
        imgColor = cv2.bilateralFilter(imgColor,d=9,sigmaColor=5,sigmaSpace=7)
    for i in range(dowmsampleNum):
        # 将图片进行上采样，到原始图片大小
        imgColor = cv2.pyrUp(imgColor)
    # cv2.imshow("imgColor",imgColor)
    return imgColor

def add_picture(path):
    one = rgb_to_sketch(path)
    two = Begin_Cartton(path)

    rows, cols = one.shape[:2]
    two = cv2.resize(two,(cols,rows),interpolation=cv2.INTER_CUBIC)

    # img_cartoon = cv2.bitwise_and(one,two)
    # cv2.imshow('none',img_cartoon)

    add_img = cv2.addWeighted(one, 0.64, two, 0.36, 0)  # 图像融合
    cv2.imshow('none',add_img)


def main():
    path = r"E:\github\python_toolbox\Picture_turn_into_cartoon\zyx.jpg"
    add_picture(path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
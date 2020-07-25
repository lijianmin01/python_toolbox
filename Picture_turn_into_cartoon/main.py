import cv2
import os
"""
色彩数量少，说明细节展示的不如色彩图片清晰
细节边缘比真实色彩图片清楚
"""

def Pic2Cartton(path,picture_name=None):
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
    cv2.imshow("imgColor",imgColor)

    imgBinary = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    imgMedianBlur = cv2.medianBlur(imgBinary,7) #中值滤波来取出噪声点
    cv2.imshow('imgMedianBlur',imgMedianBlur)

    # 采用自适应阈值将灰度图二值化，提取边缘
    imgContour = cv2.adaptiveThreshold(imgMedianBlur,255,
                                       cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY,blockSize=9,C=3)
    # cv2.imshow('imgContur',imgContour)
    # 转换回RGB三通道，方便与img_color进行与操作
    imgContour = cv2.cvtColor(imgContour,cv2.COLOR_GRAY2RGB)
    cv2.imshow('imgContour',imgContour)
    # 采用与操作，边缘保留黑色，其他位置保留img_color颜色
    img_cartoon = cv2.bitwise_and(imgColor,imgContour)
    filename ='{}'.format(picture_name)
    cv2.imshow('img_cartoon',img_cartoon)
    # cv2.imwrite(filename,img_cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return filename

if __name__ == '__main__':
    Pic2Cartton(r"E:\github\python_toolbox\Picture_turn_into_cartoon\timg.jpg")













import cv2
import os


base_path = "E:\\github\\python_toolbox\\Sql_questions"


# 寻找所处理的图片的路径
def find_img(path):
    # 处理的图片的数量
    img_num = 0

    for root, dirs, files in os.walk(path, topdown=True):
        # print(root)  # E:\github\python_toolbox\数据库原理试题整理\sources\test
        # # print(dirs)
        # print(files)
        """
        []
        
        ['Screenshot_2020-06-05-08-31-09-091_com.alibaba.an.jpg',
         'Screenshot_2020-06-05-08-32-52-331_com.alibaba.an.jpg', 
         'Screenshot_2020-06-05-08-33-53-874_com.alibaba.an.jpg', 
         'Screenshot_2020-06-05-08-35-05-585_com.alibaba.an.jpg']
        """
        for img_file in files:
            img_path=root+'\\'+img_file
            # print(img_path)
            img_num = deal_with_img(img_path,img_num)


# 裁剪图片
def deal_with_img(path,img_num):
    img = cv2.imread(path)
    cv2.namedWindow('original', 0)
    cv2.imshow('original', img)

    # # 可能有一些图片不清楚，重复了，删除
    # k = cv2.waitKey(0)
    # if k == 27:
    #     cv2.close()

    # 选在裁剪的位置
    # 选择ROI
    roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
    x, y, w, h = roi


    # 显示ROI并保存图片
    if roi != (0, 0, 0, 0):
        crop = img[y:y + h, x:x + w]
        save_path = './data/'
        #print(save_path)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_path = './data/' + str(img_num) + '.jpg'
        cv2.imwrite(save_path, crop)
        print(str(img_num)+'.jpg  ~~~~~  '+'Saved!')
        img_num+=1

    return img_num

def main():
    path = base_path+'\\sources\\yangben'

    find_img(path)


if __name__ == '__main__':
    main()
import cv2
import os


def find_img(path):
    # 处理的图片的数量
    img_num = 0
    for root, dirs, files in os.walk(path, topdown=True):
        for img_file in files:
            img_path = root + '\\' + img_file
            # print(img_path)
            chage_size(img_path, img_num)
            img_num += 1

def chage_size(path,cnt=0):
    img = cv2.imread(path)
    h,w = img.shape[0],img.shape[1]
    #print(w,h)
    new_h = int(h*1.0/w * 2000)
    img2 = cv2.resize(img,(2000,new_h),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("./data2/"+str(cnt)+'.jpg',img2)
    #print("img2",img2.shape)




def main():
    path = 'data'
    find_img(path)

if __name__ == '__main__':
    main()
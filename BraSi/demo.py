import cv2
import numpy as np


# 网络摄像头

frameWdith = 2000
frameHeight = 2000

cap = cv2.VideoCapture(0)
cap.set(3,frameWdith)
cap.set(4,frameHeight)
cap.set(10,150)

# 绿  橙  蓝
myColors = [[54,154,133,87,255,255],
            [0,186,221,87,255,255],
            [100,188,77,130,255,250]]

# BGR
myColorValues = [[139,255,61],
                 [0,102,255],
                 [255,26,0]]

myPoints = []  # [x , y , colorId]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lowser = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lowser, upper)
        x, y =getContours(mask)
        cv2.circle(imgResult,(x,y),2,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1

    return newPoints

# 找到画笔的轮廓
def getContours(img):
    # contours,hierarchy,_ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    binary, contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)

    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors)
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints)!=0 :
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



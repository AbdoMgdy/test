import numpy as np
import cv2
frameWidth = 640
frameHeight = 480

myColors = [[133, 0, 224, 179, 255, 255],
            [80, 67, 205, 106, 135, 255]]

myPoints = []


def findColor(img, myColors, imgResult):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, (255, 0, 0), cv2.FILLED)
    return x


def getContours(img):
    contours, hierachy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


def get_coordinates(video):
    cap = cv2.VideoCapture(video)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    res = []
    while True:
        fn = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        success, img = cap.read()
        try:
            imgResult = img.copy()
            x = findColor(img, myColors, imgResult)
            t = round(fn/30, 1)
            res.append([x, t])
        except:
            print('Video Ended')
            break
    return res

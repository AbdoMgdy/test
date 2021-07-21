import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from time import sleep
font = cv2.FONT_HERSHEY_SIMPLEX

# fontScale
fontScale = 0.5

# Blue color in BGR
red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
orange = (0, 69, 255)
# Line thickness of 2 px
thickness = 1
cap = cv2.VideoCapture('Gate_1.mp4')
#cap = cv2.VideoCapture(r'Gate_2.mp4')
#frame_height = int(cap.get(4))
#frame_width = int(cap.get(3))
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('outgate2.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
while True:
    ret, img = cap.read()

    edges = img.copy()
    imgo = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    imgo = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    imgo = clahe.apply(imgo)
    imgo = cv2.medianBlur(imgo, 7)
    imgo = cv2.GaussianBlur(imgo, (5, 5), 2, 2)
    imgo = clahe.apply(imgo)

    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)
    imgo = clahe.apply(imgo)

    imgo = cv2.erode(imgo, kernel, iterations=1)
    imgo = cv2.dilate(imgo, kernel, iterations=1)
    imgo = cv2.erode(imgo, kernel, iterations=1)
    imgo = cv2.dilate(imgo, kernel2, iterations=1)

    ret, imgo = cv2.threshold(imgo, 235, 255, 0)
    mask = cv2.dilate(imgo, kernel, iterations=1)
    masked = cv2.bitwise_and(edges, edges, mask=mask)
    imgray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hier = cv2.findContours(thresh, 1, 2)
    if contours:
        for c in contours:
            area = int(cv2.contourArea(c))
            if area >> 12:
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(edges, [box], 0, orange, 2)
                x = int(rect[0][0])
                y = int(rect[0][1])
                c_number = cv2.putText(edges, 'Orange Gate', (x, y), font, fontScale, orange, thickness, cv2.LINE_AA)
    cv2.imshow('f', edges)
    sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

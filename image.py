import cv2
import numpy as np
from time import sleep
font = cv2.FONT_HERSHEY_SIMPLEX

# fontScale
fontScale = 0.5


def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [0, 0, 255], 3)
    except:
        pass


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))

orange = (0, 69, 255)


def draw_contours(img, contours, threshold):
    for c in contours:
        area = int(cv2.contourArea(c))
        if area < threshold['h'] and area > threshold['l']:
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(img, [box], 0, orange, 2)
            x = int(rect[0][0])
            y = int(rect[0][1])
            cv2.putText(img, 'Orange Gate', (x, y), font, fontScale, orange, 2, cv2.LINE_AA)


# Blue color in BGR
red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cap = cv2.VideoCapture('Gate_1.mp4')
frame_height = int(cap.get(4))
frame_width = int(cap.get(3))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outgate_2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
while True:
    blank_img = np.ones((300, 300, 1), np.uint8)*255
    ret, img = cap.read()
    frame = cv2.GaussianBlur(img, (5, 5), 0)
    imgo = cv2.erode(frame, kernel, iterations=1)
    imgo = cv2.dilate(imgo, kernel, iterations=1)
    imgo = cv2.erode(imgo, kernel, iterations=1)
    imgo = cv2.dilate(imgo, kernel2, iterations=1)
    hsv_frame = cv2.cvtColor(imgo, cv2.COLOR_BGR2HSV)
# high (99,225,212)
# low (83,0,174)
    low_color = np.array([80, 0, 160])
    up_color = np.array([100, 225, 230])
    mask = cv2.inRange(hsv_frame, low_color, up_color)
    edges = cv2.Canny(mask, 20, 40)
    imgo = cv2.GaussianBlur(edges, (5, 5), 2, 2)
    imgo = clahe.apply(imgo)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 10, 20, 5)
    # draw_lines(img, lines)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    draw_contours(img, contours, {'h': 1500, 'l': 1300})
    output = cv2.bitwise_and(frame, hsv_frame, mask=mask)
    sleep(0.05)
    # cv2.imshow('f', blank_img)
    cv2.imshow('i', output)
    # if ret == True:
    #     out.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

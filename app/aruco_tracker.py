

import numpy as np
import cv2
import cv2.aruco as aruco
import glob
import time


def calibrate():
    # ---------------------- CALIBRATION ---------------------------
    # termination criteria for the iterative algorithm
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    # checkerboard of size (7 x 6) is used
    objp = np.zeros((6*7, 3), np.float32)
    objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

    # arrays to store object points and image points from all the images.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    # iterating through all calibration images
    # in the folder
    images = glob.glob('calib_images/checkerboard/*.jpg')
    print(images)
    first_img = cv2.imread(images[0])
    gray = cv2.cvtColor(first_img, cv2.COLOR_BGR2GRAY)
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # find the chess board (calibration pattern) corners
        ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

        # if calibration pattern is found, add object points,
        # image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            # Refine the corners of the detected corners
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (7, 6), corners2, ret)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    return mtx, dist


c = calibrate()


def get_cords(video):

    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(video)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    res = []
    start = time.time()
    while (True):
        try:
            ret, frame = cap.read()

            # operations on the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # set dictionary size depending on the aruco marker selected
            aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

            # detector parameters can be set here (List of detection parameters[3])
            parameters = aruco.DetectorParameters_create()
            parameters.adaptiveThreshConstant = 10

            # lists of ids and the corners belonging to each id
            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

            # font for displaying text (below)
            font = cv2.FONT_HERSHEY_SIMPLEX

            # check if the ids list is not empty
            # if no check is added the code will crash
            if np.all(ids != None):

                # estimate pose of each marker and return the values
                # rvet and tvec-different from camera coefficients
                rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, c[0], c[1])

                # (rvec-tvec).any() # get rid of that nasty numpy value array error
                # print(rvec, tvec)

                for i in range(0, ids.size):
                    # draw axis for the aruco markers

                    aruco.drawAxis(frame, c[0], c[1], rvec[i], tvec[i], 0.1)
                    x = corners[0][0][0][0]
                    y = corners[0][0][0][1]

                    print("x = ", x)
                    print("y = ", y)
                    stop = time.time()
                    t = stop-start
                    print("x = ", x)

                    res.append([x, t])
                # draw a square around the markers
                aruco.drawDetectedMarkers(frame, corners)

                # code to show ids of the marker found
                strg = ''
                for i in range(0, ids.size):
                    strg += str(ids[i][0])+', '

                cv2.putText(frame, "Id: " + strg, (0, 64), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

            else:
                # code to show 'No Ids' when no markers are found
                cv2.putText(frame, "No Ids", (0, 64), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        except:
            print('Video Ended')
            break
        # display the resulting frame
        # cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return res


def get_all(d):
    varr = []
    for i in range(len(d)):
        try:
            first = d[i]
            second = d[i+1]
            t = second[1]
            dx = second[0] - first[0]
            dt = second[1] - first[1]
            v = dx/dt
            a = v/dt
            # print(f'dx:{dx} dt:{dt} v:{v} a:{a}')
            varr.append([second[0], v, a, t])
        except:
            break
    return varr


def getRes(v):
    d_list = get_cords(v)
    all_list = get_all(d_list)

    return all_list


print(getRes("30.mp4"))

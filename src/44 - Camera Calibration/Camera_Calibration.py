# import package
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import sys
# Reference : 'https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_calibration/py_calibration.html#calibration'
# Reference : OpenCv and Camera Calibration on a Raspberry Pi 3 (https://www.youtube.com/watch?v=QV1a1G4lL3U)


'''
Camera Calibration algorithm undistort the selected distorted image present in the set of images.
'''

def camera_calibration(image_dir, nRows, nCols, dimension):
    """
        Parameters:
            image_dir (str): path to folder contains chessboard images
            nx (int): width of chessboard (number of squares) = 9
            ny (int): height of chessboard (number of squares) = 6

        Class that calibrate camera using chessboard images.
            Attributes:

            dist (np.array): Distortion coefficients
            Distortion coefficient : (k1 k2 p1 p2 p3)

            k1 and k2 = Radial distortion coefficient
            p1, p2 and p3 = Radial distortion coefficient

            In addition to this, we need to find a few more information, like intrinsic and extrinsic parameters of a camera. Intrinsic parameters are specific to a camera.                        
            mtx (np.array): Camera matrix 
            Camera matrix : [fx  0   cx]
                            [0   fy  cy]
                            [0    0   1]
            fx and fy = focal length
            cx and cy = optical centers 
    """
    # Get on all images
    images = glob.glob('{}/*'.format(image_dir))

    if len(images) < 9:
        print("Not enough images were found: at least 9 shall be provided!!!")
        sys.exit()


    # terminal criteria
    criteria = (cv2.TERM_CRITERIA_EPS +
                cv2.TERM_CRITERIA_MAX_ITER, dimension, 0.001)

    # 3D points are called object points and 2D image points are called image points.
    objpoints = []  # 3d point in real world space
    imgpoints = []  # 2d points in image plane.

    # Coordinates of chessboard's corners in 3D
    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((nRows*nCols, 3), np.float32)
    objp[:, :2] = np.mgrid[0:nRows, 0:nCols].T.reshape(-1, 2)
    print(objp.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(objp)):
        xs = objp[i][0]
        ys = objp[i][1]
        zs = objp[i][2]
        ax.scatter(xs, ys, zs)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

    # Check for correct pattern obtained so far
    nPatternFound = 0

    # Iterate over all images
    for image in images:

        # Input image
        img = cv2.imread(image)

        # Convert to grayscale image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # find the chessboard corners
        # It returns the corner points and ret which will be True if pattern is obtained
        ret, corners = cv2.findChessboardCorners(img, (nRows, nCols))

        if ret:

            # --- Sometimes, Harris cornes fails with crappy pictures, so
            corners2 = cv2.cornerSubPix(
                gray, corners, (11, 11), (-1, -1), criteria)

            # Draw and display the corners
            cv2.drawChessboardCorners(img, (nRows, nCols), corners2, ret)
            cv2.putText(img,"Press [ESC] => to reject | Press [Any Keyboard] => to accept",(10,30),\
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), thickness=3)
            cv2.imshow('img', img)

            k = cv2.waitKey(0) & 0xFF
            if k == 27:  # -- ESC Button
                print("Image Skipped")
                imgNotGood = image
                continue

            print("Image accepted")
            nPatternFound += 1
            objpoints.append(objp)
            imgpoints.append(corners2)

        # shape = (frame.shape[1],frame.shape[0])
        # ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, shape, None, None)

    cv2.destroyAllWindows()

    if (nPatternFound > 1):
        print("Found %d good images" % (nPatternFound))

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
            objpoints, imgpoints, gray.shape[::-1], None, None)

        if not ret:
            raise Exception("Unable to calibrate camera")
            sys.exit()

        # Undistort an image
        img = cv2.imread(imgNotGood)
        h,  w = img.shape[:2]
        print("Image to undistort: ", imgNotGood)
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
            mtx, dist, (w, h), 1, (w, h))

        # undistort
        mapx, mapy = cv2.initUndistortRectifyMap(
            mtx, dist, None, newcameramtx, (w, h), 5)
        dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        print("ROI: ", x, y, w, h)

        os.makedirs("./assets", exist_ok=True)

        cv2.imwrite("assets/calibresult.png", dst)
        print("Calibrated picture saved as calibresult.png")
        print("Calibration Matrix: ")
        print(mtx)
        print("Disortion: ", dist)

        # --------- Save result
        filename = "assets/cameraMatrix.txt"
        np.savetxt(filename, mtx, delimiter=',')
        filename = "assets/cameraDistortion.txt"
        np.savetxt(filename, dist, delimiter=',')

        mean_error = 0
        for i in range(len(objpoints)):
            imgpoints2, _ = cv2.projectPoints(
                objpoints[i], rvecs[i], tvecs[i], mtx, dist)
            error = cv2.norm(imgpoints[i], imgpoints2,
                             cv2.NORM_L2)/len(imgpoints2)
            mean_error += error

        print("total error: ", mean_error/len(objpoints))

    else:
        print("In order to calibrate you need at least 9 good pictures... try again")

    return mtx, dist


if __name__ == '__main__':
    camera_calibration(image_dir = '../Images and Videos/camera_calibration_images',nRows=9, nCols = 6, dimension = 25)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

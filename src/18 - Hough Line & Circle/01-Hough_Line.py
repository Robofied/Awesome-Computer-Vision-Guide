import cv2
import math
import numpy as np

# Original frame 
frame = cv2.imread('../Images and Videos/road.jpg')

# Grayscale image
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 150, None, 10, 10)
    
if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(gray, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

# cv2.imwrite('houghlines5.jpg',gray)
cv2.imshow('Detected lines',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

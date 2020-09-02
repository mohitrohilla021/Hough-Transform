import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Cany_edge_parameters- (image, initial_threshold, final_threshold,apertureSize)
edges = cv2.Canny(gray,50,150,apertureSize=3)
cv2.imshow('canny image',edges)

# the HoughLines(image,rho,theta,threshold)...
lines = cv2.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    # this conversion is important bcz, we need to convert...
    # the polar coordinates into cartesian for the "line" method.
    x0 = a * rho
    y0 = b * rho
    # x1 has the value, (rho*cos(theta) - 1000*sin(theta))
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    # all the lines we try to plot in this loop.
cv2.imshow('Hough',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

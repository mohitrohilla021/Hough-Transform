# In this method instead of taking all the points, it takes some...
# random points that are sufficient to draw a line.
import cv2
import numpy as np

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150,apertureSize=3)
cv2.imshow("Edges",edges)

# here, we have minLineLength, i.e. lines shorter than this will be rejected...
# the next argument is maxLineGap, this is maximum allowed gap btw line segments to treat that as a single line.
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("Probabilistic Hough",img)
cv2.waitKey()
cv2.destroyAllWindows()
